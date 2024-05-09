import time
import saveMaze
import pygame
import sys
import mazeSolver
import binaryTreeAlgorithm


WIDTH = 800
HEIGHT = 800
MAZE_WIDTH = MAZE_HEIGHT = 25
WALL_THICKNESS = WIDTH // MAZE_WIDTH


pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Labrynth solver")
game = binaryTreeAlgorithm.binaryTreeInit(MAZE_WIDTH, MAZE_HEIGHT)
matrix = mazeSolver.createMatrix(MAZE_HEIGHT, MAZE_WIDTH)
start, end = mazeSolver.findStartEnd(game, MAZE_HEIGHT, MAZE_WIDTH)
matrix[start[0]][start[1]] = 1


y = 0
for row in game:
    x = 0
    for element in row:
        if element == "P":
            pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(x, y, WALL_THICKNESS, WALL_THICKNESS))
        elif element == "W":
            pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(x, y, WALL_THICKNESS, WALL_THICKNESS))
        x += WALL_THICKNESS
    y += WALL_THICKNESS
pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(start[1] * WALL_THICKNESS, start[0] * WALL_THICKNESS, WALL_THICKNESS, WALL_THICKNESS))
pygame.display.update()
gameStart = time.time()
cellX = 0
cellY = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if pygame.mouse.get_pressed()[0]:
            x, y = pygame.mouse.get_pos()
            cellX = x // WALL_THICKNESS
            cellY = y // WALL_THICKNESS

    if matrix[end[0]][end[1]] == 1:
        total_secs = round(time.time() - gameStart)
        minute = total_secs // 60
        seconds = total_secs % 60
        print("YOU HAVE COMPLETED THE MAZE!!!")
        print("YOUR TOTAL TIME WAS: " + str(minute) + " minutes and " + str(seconds) + " seconds.")
        pygame.quit()
        sys.exit()

    if game[cellY][cellX] == "P" and mazeSolver.checkNeighboors(cellY, cellX, game, matrix):
        matrix[cellY][cellX] = 1
        pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(
            cellX * WALL_THICKNESS, cellY * WALL_THICKNESS, WALL_THICKNESS, WALL_THICKNESS))
        pygame.display.update()


