import sys
import pygame
import primsAlgorithm
import mazeSolver
import saveMaze
import kruskalsAlgorithm


WIDTH = 600
HEIGHT = 600
MAZE_WIDTH = MAZE_HEIGHT = 25
WALL_THICKNESS = WIDTH // MAZE_WIDTH


pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Labrynth solver")
game = kruskalsAlgorithm.kuskalInit(MAZE_WIDTH, MAZE_HEIGHT)
#solution = mazeSolver.solveMaze(game, MAZE_HEIGHT, MAZE_WIDTH)
saveMaze.writeToFile(game)
#saveMaze.writeSolution(solution, MAZE_HEIGHT, MAZE_WIDTH)


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
pygame.display.update()
solutionDrawn = True
#solution.reverse()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    """
    if not solutionDrawn:
        solutionDrawn = True
        for coordinates in solution:
            y, x = coordinates
            pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(
                x * WALL_THICKNESS, y * WALL_THICKNESS, WALL_THICKNESS, WALL_THICKNESS))
            pygame.display.update()
            pygame.time.wait(25)
    """

