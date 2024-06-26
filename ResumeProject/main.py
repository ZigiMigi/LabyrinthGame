import sys
import time
import tracemalloc

import pygame
import primsAlgorithm
import mazeSolver
import saveMaze
import kruskalsAlgorithm
import binaryTreeAlgorithm
import recursiveBacktrackingAlgorithm
import recursiveDivisionAlgorithm
import naiveRandomAlgorithm
import naiveBranchAlgorithm


WIDTH = 600
HEIGHT = 600
MAZE_WIDTH = MAZE_HEIGHT = 50
WALL_THICKNESS = WIDTH // MAZE_WIDTH


pygame.init()
clock = pygame.time.Clock()
sys.setrecursionlimit(5000)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Labrynth solver")
# game = recursiveBacktrackingAlgorithm.recursiveBacktrackingInit(MAZE_WIDTH, MAZE_HEIGHT)

all_times = 0
all_space = 0
all_peaks = 0
for x in range(10):
    print(f"Iteration: {x}")
    start_time = time.time()
    tracemalloc.start()
    game = naiveBranchAlgorithm.naiveBranchInit(
        MAZE_WIDTH, MAZE_HEIGHT
    )
    current, peak = tracemalloc.get_traced_memory()
    end_time = time.time()
    all_times += (end_time - start_time) * 1000
    all_space += current
    all_peaks += peak

print(f"Average elapsed time: {all_times/10:.2f} ms")
print(f"Average memory usage: {(all_space/10) / 10 ** 6} MB")
print(f"Average peak memory usage: {(all_peaks/10) / 10 ** 6} MB")
'''
game = naiveBranchAlgorithm.naiveBranchInit(
        MAZE_WIDTH, MAZE_HEIGHT
    )

bfs_total = 0
dfs_total = 0
for x in range(10):
    start_time = time.time()
    solutionDFS = mazeSolver.solveMazeDFS(game, MAZE_HEIGHT, MAZE_WIDTH)
    end_time = time.time()
    dfs_total += (end_time - start_time) * 1000

    start_time = time.time()
    solutionBFS = mazeSolver.solveMazeBFS(game, MAZE_HEIGHT, MAZE_WIDTH)
    end_time = time.time()
    bfs_total += (end_time - start_time) * 1000

print(f"Average elapsed time for DFS: {dfs_total/10:.2f} ms")
print(f"Average elapsed time for BFS: {bfs_total/10:.2f} ms")
#saveMaze.writeToFile(game)
'''
solution = mazeSolver.solveMazeBFS(game, MAZE_HEIGHT, MAZE_WIDTH)
saveMaze.writeSolution(solution, MAZE_HEIGHT, MAZE_WIDTH)




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

    if not solutionDrawn:
        solutionDrawn = True
        for coordinates in solution:
            y, x = coordinates
            pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(
                x * WALL_THICKNESS, y * WALL_THICKNESS, WALL_THICKNESS, WALL_THICKNESS))
            pygame.display.update()
            pygame.time.wait(25)


