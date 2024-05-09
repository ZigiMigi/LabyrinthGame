"""
Naive algorithm for creating mazes
Walls are marked with "W", Paths with "P" and unwalked cells are marked with "?"
"""
import random


def naiveRandInit(mazeHeight, mazeWidth):
    # Initialize the maze with walls
    maze = [['W' for _ in range(mazeHeight)] for _ in range(mazeWidth)]

    # random start
    width = random.randint(1, mazeWidth - 2)
    height = 0
    maze[height][width] = 'P'

    while height < mazeWidth - 1:
        # can move only left, right and down
        randPath = random.choice(['left', 'right', 'down'])
        if canMove(randPath, (height, width), maze):
            if randPath == 'left':
                width -= 1
            elif randPath == 'right':
                width += 1
            else:
                height += 1
        else:
            if randPath == 'left':
                randPath = random.choice(['right', 'down'])
            else:
                randPath = random.choice(['left', 'down'])

            if canMove(randPath, (height, width), maze):
                if randPath == 'left':
                    width -= 1
                elif randPath == 'right':
                    width += 1
                else:
                    height += 1
            else:
                height += 1
        maze[height][width] = 'P'

    return fillRandom(maze, mazeHeight, mazeWidth)


def canMove(path, currentPosition, maze):
    # cant move left/right if it is in the first row
    # cant move left/right if it is at the border
    # cant move left/right if diagonal is already a path
    curHeight, curWidth = currentPosition
    if path == 'left':
        if curWidth - 1 < 1 or curHeight == 0:
            return False
        # check diagonal
        if curHeight >= 1 and maze[curHeight - 1][curWidth - 1] == 'P':
            return False
        if curHeight <= len(maze) - 2 and maze[curHeight + 1][curWidth - 1] == 'P':
            return False

    elif path == 'right':
        if curWidth + 1 > len(maze) - 2 or curHeight == 0:
            return False
        # check diagonal
        if curHeight >= 1 and maze[curHeight - 1][curWidth + 1] == 'P':
            return False
        if curHeight <= len(maze) - 2 and maze[curHeight + 1][curWidth + 1] == 'P':
            return False
    return True


def fillRandom(maze, mazeHeight, mazeWidth):
    for _ in range(int(mazeHeight * mazeWidth / 2)):
        randWidth, randHeight = random.randint(1, mazeWidth - 2), random.randint(1, mazeHeight - 2)
        maze[randWidth][randHeight] = 'P'
    return maze
