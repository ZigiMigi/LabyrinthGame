import mazeCreator
tab = mazeCreator.mazeInit(10, 10)


def solveMaze(maze, mazeH, mazeW):
    matrix = createMatrix(mazeH, mazeW)
    start, end = findStartEnd(maze, mazeH, mazeW)
    matrix[start[0] + 1][start[1]] = 1
    k = 0
    while matrix[end[0] - 1][end[1]] == 0:
        k += 1
        findPath(k, maze, matrix)
    i, j = end
    i -= 1
    k = matrix[i][j]
    solution = [(end[0], end[1]), (i, j)]
    while k > 1:
        if i > 0 and matrix[i - 1][j] == k - 1:
            i, j = i - 1, j
            solution.append((i, j))
            k -= 1
        elif j > 0 and matrix[i][j - 1] == k - 1:
            i, j = i, j - 1
            solution.append((i, j))
            k -= 1
        elif i < len(matrix) - 1 and matrix[i + 1][j] == k - 1:
            i, j = i + 1, j
            solution.append((i, j))
            k -= 1
        elif j < len(matrix[i]) - 1 and matrix[i][j + 1] == k - 1:
            i, j = i, j + 1
            solution.append((i, j))
            k -= 1
    solution.append((start[0], start[1]))
    return solution


def findPath(k, maze, matrix):
    for x in range(0, len(matrix)):
        for y in range(0, len(matrix[x])):
            if matrix[x][y] == k:
                if x > 0 and matrix[x - 1][y] == 0 and maze[x - 1][y] == "P":
                    matrix[x - 1][y] = k + 1
                if y > 0 and matrix[x][y - 1] == 0 and maze[x][y - 1] == "P":
                    matrix[x][y - 1] = k + 1
                if x < len(matrix) - 1 and matrix[x + 1][y] == 0 and maze[x + 1][y] == "P":
                    matrix[x + 1][y] = k + 1
                if y < len(matrix[x]) - 1 and matrix[x][y + 1] == 0 and maze[x][y + 1] == "P":
                    matrix[x][y + 1] = k + 1


def createMatrix(mazeH, mazeW):
    ret = []
    for x in range(0, mazeH):
        tmp = []
        for y in range(0, mazeW):
            tmp.append(0)
        ret.append(tmp)
    return ret

def findStartEnd(maze, mazeH, mazeW):
    for x in range(0, mazeW):
        if maze[0][x] == "P":
            start = (0, x)
            break
    for x in range(0, mazeW):
        if maze[mazeH - 1][x] == "P":
            end = (mazeH - 1, x)
            break
    return start, end


def checkNeighboors(x, y, maze, matrix):
    if x > 0 and maze[x - 1][y] == "P" and matrix[x - 1][y] == 1:
        return True
    if y > 0 and maze[x][y - 1] == "P" and matrix[x][y - 1] == 1:
        return True
    if x < len(matrix) - 1 and maze[x + 1][y] == "P" and matrix[x + 1][y] == 1:
        return True
    if y < len(matrix) - 1 and maze[x][y + 1] == "P" and matrix[x][y + 1] == 1:
        return True
    return False


