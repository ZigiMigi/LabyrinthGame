"""
Binary tree algorithm for creating mazes
Walls are marked with "W", Paths with "P" and unwalked cells are marked with "?"
"""
import random


def binaryTreeInit(mazeHeight, mazeWidth):
    # init maze with all walls
    maze = []
    for i in range(0, mazeHeight):
        row = []
        for j in range(0, mazeWidth):
            row.append('W')
        maze.append(row)

    for i in range(1, mazeHeight - 1, 2):
        for j in range(1, mazeWidth - 1, 2):
            if i == mazeWidth - 2 and j == mazeHeight - 2:
                direction = 0
            elif j == mazeWidth - 2:
                direction = -1
            elif i == mazeHeight - 2:
                direction = 1
            else:
                direction = random.choice([-1, 1])

            # check where to go
            if direction == -1:
                # vertical
                for k in range(3):
                    maze[i][j + k] = "P"
            elif direction == 1:
                # horizontal
                for k in range(3):
                    maze[i + k][j] = "P"


    for x in maze:
        print(x)

binaryTreeInit(10, 10)
