def writeToFile(maze):
    file = open(r"C:\Users\zigak\ResumeProject\MAZE.txt", "w")
    for x in maze:
        line = ""
        for y in x:
            line += y + " "
        file.write(line)
        file.write("\n")
    file.close()


def writeSolution(solution, mazeHeight, mazeWidth):
    matrix = createMatrix(mazeHeight, mazeWidth)
    for x in solution:
        i, j = x
        matrix[i][j] = 1
    file = open(r"C:\Users\zigak\ResumeProject\SOLUTION.txt", "w")
    for x in matrix:
        line = ""
        for y in x:
            line += str(y) + " "
        file.write(line)
        file.write("\n")
    file.close()


def createMatrix(mazeH, mazeW):
    ret = []
    for x in range(0, mazeH):
        tmp = []
        for y in range(0, mazeW):
            tmp.append(0)
        ret.append(tmp)
    return ret

def readMaze(fileName):
    ret = []
    file = open(fileName, "r")
    for row in file:
        line = row.split(" ")
        del line[-1]
        ret.append(line)
    return ret

