"""
Random Kruskal's algorithm for creating mazes
Walls are marked with "W", Paths with "P" and unwalked cells are marked with "?"
"""
import random


def kuskalInit(mazeHeight, mazeWidth):
    def replace(oldValue, newValue):
        for i in range(1, mazeHeight - 1, 2):
            for j in range(1, mazeWidth - 1, 2):
                if sets[i][j] == oldValue:
                    sets[i][j] = newValue
    maze = []
    elements = []
    sets = []
    cnt = 1

    # fill maze with all walls and mark every element
    for i in range(0, mazeHeight):
        row = []
        setRow = []
        for j in range(0, mazeWidth):
            row.append('W')
            setRow.append(0)
        maze.append(row)
        sets.append(setRow)

    for i in range(1, mazeHeight - 1, 2):
        for j in range(1, mazeWidth - 1, 2):

            # append every coordinate to an array with random direction (1 meaning vertical, -1 horizontal)
            if i + 2 < mazeHeight - 1:
                elements.append((i, j, 1))
            if j + 2 < mazeWidth - 1:
                elements.append((i, j, - 1))
            sets[i][j] = cnt
            cnt += 1

    # shuffle all elements
    random.shuffle(elements)

    # loop through every element till you run out
    while elements:
        currentElement = elements.pop()
        if currentElement[2] == 1:
            # vertical
            if sets[currentElement[0] + 2][currentElement[1]] != sets[currentElement[0]][currentElement[1]]:
                replace(sets[currentElement[0] + 2][currentElement[1]], sets[currentElement[0]][currentElement[1]])
                # place path
                for i in range(3):
                    maze[currentElement[0] + i][currentElement[1]] = "P"
        elif currentElement[2] == -1:
            # horizontal
            if sets[currentElement[0]][currentElement[1] + 2] != sets[currentElement[0]][currentElement[1]]:
                replace(sets[currentElement[0]][currentElement[1] + 2], sets[currentElement[0]][currentElement[1]])
                # place path
                for i in range(3):
                    maze[currentElement[0]][currentElement[1] + i] = "P"

    # create a start and exit
    for i in range(0, mazeWidth):
        if maze[1][i] == "P":
            maze[0][i] = "P"
            break
    for i in range(mazeWidth - 1, 0, -1):
        if maze[mazeHeight - 2][i] == "P":
            maze[mazeHeight - 1][i] = "P"
            break
    return maze

