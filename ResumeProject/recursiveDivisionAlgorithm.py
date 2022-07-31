"""
Recursive division algorithm for creating mazes
Walls are marked with "W", Paths with "P" and unwalked cells are marked with "?"
"""
import random


def recursiveDivisionInit(mazeWidth, mazeHeight):
    def divide(x, y, w, h):
        if w < h:
            direction = -1
        elif h < w:
            direction = 1
        else:
            direction = random.choice([1, -1])

        # firstly check if the direction is vertical
        if direction == 1:
            # direction is vertical
            if h < 5:
                return

            # new wall is always even, while the hole is always odd
            newWall = y + random.randint(2, h - 3) // 2 * 2
            newHole = x + random.randint(1, h - 2) // 2 * 2 + 1

            # walls
            for i in range(x, x + w - 1):
                maze[newWall][i] = "W"

            # hole
            maze[newWall][newHole] = "P"

            # prepare for new run
            newH = newWall - y + 1
            newW = w
            pairX = x
            pairY = newWall
            pairH = y + h - newWall
            pairW = w

        elif direction == -1:
            # direction is horizontal

            if w < 5:
                return

            # new wall is always even, while the hole is always odd
            newWall = x + random.randint(2, h - 3) // 2 * 2
            newHole = y + random.randint(1, h - 2) // 2 * 2 + 1

            # walls
            for i in range(y, y + h - 1):
                maze[i][newWall] = "W"

            # hole
            maze[newHole][newWall] = "P"

            # prepare for new run
            newH = h
            newW = newWall - x + 1
            pairX = newWall
            pairY = y
            pairH = h
            pairW = x + w - newWall

        # do next runs
        divide(x, y, newW, newH)
        divide(pairX, pairY, pairW, pairH)

    maze = []

    # fill center of the maze with all paths
    for i in range(mazeHeight):
        row = []
        for j in range(mazeWidth):
            if i == 0 or i == mazeHeight - 1:
                row.append("W")
            else:
                if j == 0 or j == mazeWidth - 1:
                    row.append("W")
                else:
                    row.append("P")
        maze.append(row)

    # start run
    divide(0, 0, mazeWidth, mazeHeight)

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
