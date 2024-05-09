"""
Recursive division algorithm for creating mazes
Walls are marked with "W", Paths with "P" and unwalked cells are marked with "?"
"""
import random


def recursiveDivisionInit(mazeWidth, mazeHeight):
    def divide(x, y, w, h):
        if w < 5 or h < 5:
            return

        # Calculate the difference in available space for both directions
        vertical_space = h - 4
        horizontal_space = w - 4

        # Choose the direction based on available space
        if vertical_space > horizontal_space:
            direction = 'vertical'
        elif horizontal_space > vertical_space:
            direction = 'horizontal'
        else:
            direction = random.choice(['horizontal', 'vertical'])

        if direction == 'vertical':
            newWall = y + random.randint(2, h - 3) // 2 * 2
            newHole = x + random.randint(1, w - 2) // 2 * 2 + 1

            if newWall < mazeHeight and x + w - 1 < mazeWidth:
                for i in range(x, x + w - 1):
                    maze[newWall][i] = "W"

                maze[newWall][newHole] = "P"

                newH = newWall - y + 1
                newW = w
                pairX = x
                pairY = newWall
                pairH = y + h - newWall
                pairW = w

        elif direction == 'horizontal':
            newWall = x + random.randint(2, w - 3) // 2 * 2
            newHole = y + random.randint(1, h - 2) // 2 * 2 + 1

            if newWall < mazeWidth and y + h - 1 < mazeHeight:
                for i in range(y, y + h - 1):
                    maze[i][newWall] = "W"

                maze[newHole][newWall] = "P"
                generation.append((newHole, newWall))

                newH = h
                newW = newWall - x + 1
                pairX = newWall
                pairY = y
                pairH = h
                pairW = x + w - newWall

        divide(x, y, newW, newH)
        divide(pairX, pairY, pairW, pairH)

    maze = []
    generation = []

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

    divide(0, 0, mazeWidth, mazeHeight)

    for i in range(0, mazeWidth):
        if maze[1][i] == "P":
            maze[0][i] = "P"
            break
    for i in range(mazeWidth - 1, 0, -1):
        if maze[mazeHeight - 2][i] == "P":
            maze[mazeHeight - 1][i] = "P"
            break

    return maze, generation
