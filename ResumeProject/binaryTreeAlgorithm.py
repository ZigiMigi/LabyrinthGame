"""
Binary tree algorithm for creating mazes
Walls are marked with "W", Paths with "P" and unwalked cells are marked with "?"
"""
import random


def binaryTreeInit(mazeHeight, mazeWidth):
    # Initialize the maze with walls
    maze = [['W' for _ in range(mazeHeight)] for _ in range(mazeWidth)]
    generation = []

    # Carve passages
    for row in range(1, mazeWidth - 2, 2):
        for col in range(1, mazeHeight - 2, 2):
            if random.choice([True, False]):
                for k in range(3):
                    if k + col < mazeHeight:
                        maze[row][col + k] = 'P'
                        generation.append((row, col + k))
            else:
                for k in range(3):
                    if k + row < mazeWidth:
                        maze[row + k][col] = 'P'
                        generation.append((row, col + k))

    for x in range(1, mazeWidth - 1):
        maze[x][mazeWidth - 2] = 'P'
        generation.append((x, mazeWidth - 2))
    for x in range(1, mazeHeight - 1):
        maze[mazeHeight - 2][x] = 'P'
        generation.append((mazeHeight - 2, x))

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
