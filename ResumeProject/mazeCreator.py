'''
Random Prim's algoritm for creating mazes
Walls are marked with "W", Paths with "P" and unwalked cells are marked with "?"
'''
import random


def mazeInit(mazeHeight, mazeWidth):
    #fill array with unwalked cells

    maze = []
    walls = []
    for i in range(0, mazeHeight):
        row = []
        for j in range(0, mazeWidth):
            row.append('?')
        maze.append(row)
    #find random position in the maze, mark it with a path and surround it with walls

    randStartH = random.randint(1, mazeHeight - 2)
    randStartW = random.randint(1, mazeWidth - 2)
    maze[randStartH][randStartW] = "P"
    walls.extend(([randStartH - 1, randStartW], [randStartH + 1, randStartW],
                  [randStartH, randStartW - 1], [randStartH, randStartW + 1]))
    maze[randStartH - 1][randStartW] = maze[randStartH + 1][randStartW] = \
        maze[randStartH][randStartW - 1] = maze[randStartH][randStartW + 1] = "W"

    while walls:
        randWall = walls[int(random.random()*len(walls))-1]
        #left wall
        if randWall[1] != 0:
            if maze[randWall[0]][randWall[1] - 1] == "?" and maze[randWall[0]][randWall[1] + 1] == "P":
                if checkSurroundings(randWall, maze) < 2:
                    maze[randWall[0]][randWall[1]] = "P"

                    if randWall[0] != 0:
                        if maze[randWall[0] - 1][randWall[1]] != "P":
                            maze[randWall[0] - 1][randWall[1]] = "W"
                        if [randWall[0] - 1, randWall[1]] not in walls:
                            walls.append([randWall[0] - 1, randWall[1]])
                    if randWall[0] != mazeHeight - 1:
                        if maze[randWall[0] + 1][randWall[1]] != "P":
                            maze[randWall[0] + 1][randWall[1]] = "W"
                        if [randWall[0] + 1, randWall[1]] not in walls:
                            walls.append([randWall[0] + 1, randWall[1]])
                    if randWall[1] != 0:
                        if maze[randWall[0]][randWall[1] - 1] != "P":
                            maze[randWall[0]][randWall[1] - 1] = "W"
                        if [randWall[0], randWall[1] - 1] not in walls:
                            walls.append([randWall[0], randWall[1] - 1])

                for i in walls:
                    if i[0] == randWall[0] and i[1] == randWall[1]:
                        walls.remove(i)
                continue

        #upper wall
        if randWall[0] != 0:
            if maze[randWall[0] - 1][randWall[1]] == "?" and maze[randWall[0] + 1][randWall[1]] == "P":
                if checkSurroundings(randWall, maze) < 2:
                    maze[randWall[0]][randWall[1]] = "P"

                    if randWall[0] != 0:
                        if maze[randWall[0] - 1][randWall[1]] != "P":
                            maze[randWall[0] - 1][randWall[1]] = "W"
                        if [randWall[0] - 1, randWall[1]] not in walls:
                            walls.append([randWall[0] - 1, randWall[1]])
                    if randWall[1] != 0:
                        if maze[randWall[0]][randWall[1] - 1] != "P":
                            maze[randWall[0]][randWall[1] - 1] = "W"
                        if [randWall[0], randWall[1] - 1] not in walls:
                            walls.append([randWall[0], randWall[1] - 1])
                    if randWall[1] != mazeWidth - 1:
                        if maze[randWall[0]][randWall[1] + 1] != "P":
                            maze[randWall[0]][randWall[1] + 1] = "W"
                        if [randWall[0], randWall[1] + 1] not in walls:
                            walls.append([randWall[0], randWall[1] + 1])

                for i in walls:
                    if i[0] == randWall[0] and i[1] == randWall[1]:
                        walls.remove(i)
                continue

        #bottom wall
        if randWall[0] != mazeHeight - 1:
            if maze[randWall[0] + 1][randWall[1]] == "?" and maze[randWall[0] - 1][randWall[1]] == "P":
                if checkSurroundings(randWall, maze) < 2:
                    maze[randWall[0]][randWall[1]] = "P"

                    if randWall[0] != mazeHeight - 1:
                        if maze[randWall[0] + 1][randWall[1]] != "P":
                            maze[randWall[0] + 1][randWall[1]] = "W"
                        if [randWall[0] + 1, randWall[1]] not in walls:
                            walls.append([randWall[0] + 1, randWall[1]])
                    if randWall[1] != 0:
                        if maze[randWall[0]][randWall[1] - 1] != "P":
                            maze[randWall[0]][randWall[1] - 1] = "W"
                        if [randWall[0], randWall[1] - 1] not in walls:
                            walls.append([randWall[0], randWall[1] - 1])
                    if randWall[1] != mazeWidth - 1:
                        if maze[randWall[0]][randWall[1] + 1] != "P":
                            maze[randWall[0]][randWall[1] + 1] = "W"
                        if [randWall[0], randWall[1] + 1] not in walls:
                            walls.append([randWall[0], randWall[1] + 1])

                for i in walls:
                    if i[0] == randWall[0] and i[1] == randWall[1]:
                        walls.remove(i)
                continue

        #right wall
        if randWall[1] != mazeWidth - 1:
            if maze[randWall[0]][randWall[1] + 1] == "?" and maze[randWall[0]][randWall[1] - 1] == "P":
                if checkSurroundings(randWall, maze) < 2:
                    maze[randWall[0]][randWall[1]] = "P"

                    if randWall[1] != mazeWidth - 1:
                        if maze[randWall[0]][randWall[1] + 1] != "P":
                            maze[randWall[0]][randWall[1] + 1] = "W"
                        if [randWall[0], randWall[1] + 1] not in walls:
                            walls.append([randWall[0], randWall[1] + 1])
                    if randWall[0] != mazeHeight - 1:
                        if maze[randWall[0] + 1][randWall[1]] != "P":
                            maze[randWall[0] + 1][randWall[1]] = "W"
                        if [randWall[0] + 1, randWall[1]] not in walls:
                            walls.append([randWall[0] + 1, randWall[1]])
                    if randWall[0] != 0:
                        if maze[randWall[0] - 1][randWall[1]] != "P":
                            maze[randWall[0] - 1][randWall[1]] = "W"
                        if [randWall[0] - 1, randWall[1]] not in walls:
                            walls.append([randWall[0] - 1, randWall[1]])

                for i in walls:
                    if i[0] == randWall[0] and i[1] == randWall[1]:
                        walls.remove(i)
                continue
        for i in walls:
            if i[0] == randWall[0] and i[1] == randWall[1]:
                walls.remove(i)
    #set walls to left unmarked cells
    for i in range(0, mazeHeight):
        for j in range(0, mazeWidth):
            if maze[i][j] == "?":
                maze[i][j] = "W"

    #create a start and exit
    for i in range(0, mazeWidth):
        if maze[1][i] == "P":
            maze[0][i] = "P"
            break
    for i in range(mazeWidth - 1, 0, -1):
        if maze[mazeHeight - 2][i] == "P":
            maze[mazeHeight - 1][i] = "P"
            break
    return maze


def checkSurroundings(randWall, maze):
    count = 0
    if maze[randWall[0] - 1][randWall[1]] == "P":
        count += 1
    if maze[randWall[0] + 1][randWall[1]] == "P":
        count += 1
    if maze[randWall[0]][randWall[1] - 1] == "P":
        count += 1
    if maze[randWall[0]][randWall[1] + 1] == "P":
        count += 1
    return count


def printMaze(maze):
    for i in range(0, len(maze)):
        print(maze[i])





