"""
Recursive backtracking algorithm for creating mazes
Walls are marked with "W", Paths with "P" and unwalked cells are marked with "?"
"""
import random


def recursiveBacktrackingInit(mazeWidth, mazeHeight):
    def backtrack(x, y):
        direction = ["up", "down", "left", "right"]
        random.shuffle(direction)

        # iterate through every drection
        for i in direction:
            if i == "up":
                if y > 2 and maze[y - 2][x] == "W":
                    for j in range(3):
                        maze[y - 2 + j][x] = "P"
                        generation.append((y - 2 + j, x))
                    backtrack(x, y - 2)
            elif i == "down":
                if y + 2 < mazeHeight - 1 and maze[y + 2][x] == "W":
                    for j in range(3):
                        maze[y + j][x] = "P"
                        generation.append((y + j, x))
                    backtrack(x, y + 2)
            elif i == "left":
                if x > 2 and maze[y][x - 2] == "W":
                    for j in range(3):
                        maze[y][x - 2 + j] = "P"
                        generation.append((y, x - 2 + j))
                    backtrack(x - 2, y)
            else:
                if x + 2 < mazeWidth - 1 and maze[y][x + 2] == "W":
                    for j in range(3):
                        maze[y][x + j] = "P"
                        generation.append((y, x + j))
                    backtrack(x + 2, y)

    # init maze with all walls
    maze = []
    generation = []
    for i in range(0, mazeHeight):
        row = []
        for j in range(0, mazeWidth):
            row.append('W')
        maze.append(row)

    # random starting point
    startX = random.randint(1, mazeWidth - 2) // 2 * 2 + 1
    startY = random.randint(1, mazeHeight - 2) // 2 * 2 + 1

    # start run
    backtrack(startX, startY)

    # create a start and exit
    for i in range(0, mazeWidth):
        if maze[1][i] == "P":
            maze[0][i] = "P"
            generation.append((0, i))
            break
    for i in range(mazeWidth - 1, 0, -1):
        if maze[mazeHeight - 2][i] == "P":
            maze[mazeHeight - 1][i] = "P"
            generation.append((mazeHeight - 1, i))
            break

    return maze, generation
