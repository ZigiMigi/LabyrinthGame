import json
import mimetypes
import pickle
import socket
from os.path import isdir
from urllib.parse import unquote_plus

# Pickle file for storing data
PICKLE_DB = "db.pkl"

# Directory containing www data
WWW_DATA = "www-data"

# Header template for a successful HTTP request
HEADER_RESPONSE_200 = """HTTP/1.1 200 OK\r
content-type: %s\r
content-length: %d\r
connection: Close\r
\r
"""

# Represents a table row that holds user data
TABLE_ROW = """
<tr>
    <td>%d</td>
    <td>%s</td>
    <td>%s</td>
</tr>
"""

RESPONSE_301 = """HTTP/1.1 301 Redirect\r
location: %s\r
"""

RESPONSE_400 = """HTTP/1.1 400 Bad request\r
Content-Type: text/html; charset=utf-8\r
content-length: 59\r
connection: Close\r
\r
<!doctype html>
<h1>400 Bad request</h1>
<p>Bad request</p>
"""

# Template for a 404 (Not found) error
RESPONSE_404 = """HTTP/1.1 404 Not found\r
Content-Type: text/html; charset=utf-8\r
content-length: 71\r
Connection: Close\r
\r
<!doctype html>
<h1>404 Page not found</h1>
<p>Page cannot be found</p>
"""

RESPONSE_405 = """HTTP/1.1 405 Method not allowed\r
Content-Type: text/html; charset=utf-8\r
content-length: 73\r
connection: Close\r
\r
<!doctype html>
<h1>405 Method not allowed</h1>
<p>Method not allowed</p>
"""

def save_to_db(first, last):
    """Create a new user with given first and last name and store it into
    file-based database.

    For instance, save_to_db("Mick", "Jagger"), will create a new user
    "Mick Jagger" and also assign him a unique number.

    Do not modify this method."""

    existing = read_from_db()
    existing.append({
        "number": 1 if len(existing) == 0 else existing[-1]["number"] + 1,
        "first": first,
        "last": last
    })
    with open(PICKLE_DB, "wb") as handle:
        pickle.dump(existing, handle)


def read_from_db(criteria=None):
    """Read entries from the file-based DB subject to provided criteria

    Use this method to get users from the DB. The criteria parameters should
    either be omitted (returns all users) or be a dict that represents a query
    filter. For instance:
    - read_from_db({"number": 1}) will return a list of users with number 1
    - read_from_db({"first": "bob"}) will return a list of users whose first
    name is "bob".

    Do not modify this method."""
    if criteria is None:
        criteria = {}
    else:
        # remove empty criteria values
        for key in ("number", "first", "last"):
            if key in criteria and criteria[key] == "":
                del criteria[key]

        # cast number to int
        if "number" in criteria:
            criteria["number"] = int(criteria["number"])

    try:
        with open(PICKLE_DB, "rb") as handle:
            data = pickle.load(handle)

        filtered = []
        for entry in data:
            predicate = True

            for key, val in criteria.items():
                if val != entry[key]:
                    predicate = False

            if predicate:
                filtered.append(entry)

        return filtered
    except (IOError, EOFError):
        return []


def parse_headers(client):
    headers = dict()
    while True:
        line = client.readline().decode("utf-8").strip()
        if not line:
            return headers
        key, value = line.split(":", 1)
        headers[key.strip()] = value.strip()


def process_request(connection, address):
    client = connection.makefile("wrb")
    line = client.readline().decode("utf-8").strip()
    try:
        method, uri, version = line.split()
        typ = mimetypes.MimeTypes().guess_type(uri)[0]
        if typ is None:
            typ = "application/octet-stream"
        headers = parse_headers(client)
        assert method == "GET" or method == "POST", "Invalid request method"
        assert len(uri) > 0 and uri[0] == "/", "Invalid request URI"
        assert version == "HTTP/1.1", "Invalid HTTP version"
        assert "Host" in headers.keys(), "Invalid request headers"
        if method == "POST":
            assert "Content-Length" in headers.keys(), "Invalid request headers"
        if uri[-1] == "/":
            uri = "/index.html"
            head = RESPONSE_301 % (
                "http://" + headers["Host"] + uri
            )
            client.write(head.encode("utf-8"))
        if uri == "/app-add":
            assert method == "POST", "Invalid request method"
            pom = client.read(int(headers["Content-Length"]))
            first, last = pom.decode("utf-8").split("&")
            fname, fvalue = first.split("=")
            lname, lvalue = last.split("=")
            assert fname == "first" and lname == "last", "Invalid request values"
            save_to_db(fvalue, lvalue)
            uri = "/app_add.html"
        if "/app-index" in uri:
            assert method == "GET", "Invalid request method"
            pomo = unquote_plus(uri)
            if "?" not in pomo:
                tab = read_from_db()
            else:
                _, pom = pomo.split("?")
                tmp = dict()
                if "&" in pom:
                    number, first, last = pom.split("&")
                    if number != "number=":
                        _, x = number.split("=")
                        tmp["number"] = x
                    elif first != "first=":
                        _, x = first.split("=")
                        tmp["first"] = x
                    elif last != "last=":
                        _, x = last.split("=")
                        tmp["last"] = x
                else:
                    name, val = pom.split("=")
                    tmp[name] = val
                tab = read_from_db(tmp)
            uri = "/app_list.html"
            zapis = ""
            for x in tab:
                if x != "":
                    zapis += TABLE_ROW % (
                        x["number"],
                        x["first"],
                        x["last"]
                    )
            with open(WWW_DATA + uri, "r") as handle:
                body = handle.read()
            body = body.replace("{{students}}", zapis)
            body = body.encode("utf-8")
            head = HEADER_RESPONSE_200 % (
                typ,
                len(body)
            )
            client.write(head.encode("utf-8"))
            client.write(body)
            return
        if "/app-json" in uri:
            assert method == "GET", "Invalid request method"
            pomo = unquote_plus(uri)
            assert "?" not in pomo, "Invalid request json"
            head = HEADER_RESPONSE_200 % (
                "application/json",
                len(str(json.dumps(read_from_db())))
            )
            client.write(head.encode("utf-8"))
            client.write(json.dumps(read_from_db()).encode("utf-8"))
        with open(WWW_DATA + uri, "rb") as handle:
            body = handle.read()
        head = HEADER_RESPONSE_200 % (
            typ,
            len(body)
        )
        client.write(head.encode("utf-8"))
        client.write(body)
    except (ValueError, AssertionError) as e:
        if e.args[0] == "Invalid request method":
            client.write(RESPONSE_405.encode("utf-8"))
        else:
            client.write(RESPONSE_400.encode("utf-8"))
    except IOError:
        client.write(RESPONSE_404.encode("utf-8"))
    finally:
        client.close()



def main(port):
    """Starts the server and waits for connections."""

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(("", port))
    server.listen(1)

    print("Listening on %d" % port)

    while True:
        connection, address = server.accept()
        print("[%s:%d] CONNECTED" % address)
        process_request(connection, address)
        connection.close()
        print("[%s:%d] DISCONNECTED" % address)


if __name__ == "__main__":
    main(8080)
