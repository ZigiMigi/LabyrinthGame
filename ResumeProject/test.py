import pygame
import sys
import kruskalsAlgorithm
import primsAlgorithm
import binaryTreeAlgorithm
import recursiveBacktrackingAlgorithm
import recursiveDivisionAlgorithm
import naiveBranchAlgorithm

# Initialize Pygame
pygame.init()

# Set up the screen dimensions
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Menu")

# Load background image
background_image = pygame.image.load("background.png").convert_alpha()
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (150, 150, 150)
GREEN = (100, 200, 100)

MAZE_WIDTH = MAZE_HEIGHT = 50
WALL_THICKNESS = 800 // MAZE_WIDTH

# Fonts
font = pygame.font.SysFont(None, 50)


# Function to create buttons
def draw_button(screen, text, x, y, width, height, color):
    pygame.draw.rect(screen, color, (x, y, width, height), border_radius=10)
    font_surface = font.render(text, True, BLACK)
    font_rect = font_surface.get_rect(center=(x + width / 2, y + height / 2))
    screen.blit(font_surface, font_rect)


# Main menu
def main_menu():
    screen.blit(background_image, (0, 0))
    pygame.draw.rect(screen, BLACK, (0, 0, WIDTH, HEIGHT), 10)
    draw_button(screen, "Play", 300, 200, 200, 100, GRAY)
    draw_button(screen, "Learn", 300, 350, 200, 100, GRAY)
    pygame.display.update()


# Learn menu
def learn_menu():
    screen.blit(background_image, (0, 0))
    pygame.draw.rect(screen, BLACK, (0, 0, WIDTH, HEIGHT), 10)
    draw_button(screen, "Kruskal", 150, 100, 220, 55, GRAY)
    draw_button(screen, "Prim", 150, 200, 220, 55, GRAY)
    draw_button(screen, "Binary Tree", 150, 300, 220, 55, GRAY)
    draw_button(screen, "Division", 150, 400, 220, 55, GRAY)
    draw_button(screen, "Backtracking", 150, 500, 220, 55, GRAY)
    draw_button(screen, "Choosing", 450, 100, 220, 55, GRAY)
    draw_button(screen, "Branching", 450, 200, 220, 55, GRAY)
    pygame.display.update()


def play_screen():
    screen.fill(GREEN)  # Fill the screen with green color
    pygame.draw.rect(screen, BLACK, (0, 0, WIDTH, HEIGHT), 10)
    font = pygame.font.SysFont(None, 100)  # Choose font and size
    text_surface = font.render(str(7.48) + '!', True, BLACK)  # Render the number
    text_rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2))  # Position the number in the center
    screen.blit(text_surface, text_rect)  # Blit the number onto the screen
    pygame.display.update()  # Update the display


# Function to display algorithm window
def algorithm_window(imageName, generation):
    global current_screen
    screen.blit(background_image, (0, 0))
    pygame.draw.rect(screen, BLACK, (0, 0, WIDTH, HEIGHT), 10)

    # Right section for black square
    pygame.draw.rect(screen, BLACK, (350, 100, 400, 400))

    # Load and blit image
    algorithm_image = pygame.image.load(imageName)
    algorithm_image = pygame.transform.scale(algorithm_image, (250, 400))  # Adjust size as needed
    screen.blit(algorithm_image, (70, 100))  # Adjust position as needed

    # Buttons
    draw_button(screen, "-", 200, 525, 150, 50, GRAY)  # Adjust position and size as needed
    draw_button(screen, "+", 400, 525, 150, 50, GRAY)  # Adjust position and size as needed

    pygame.display.update()

    for x, y in generation:
        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(
            x * WALL_THICKNESS + 350, y * WALL_THICKNESS + 100, WALL_THICKNESS, WALL_THICKNESS))
        pygame.display.update()
        pygame.time.wait(20)

    # Freeze window until 'b' is pressed
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_b:
                    running = False
                    current_screen = "learn"
            '''
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if 150 <= mouse_x <= 350 and 550 <= mouse_y <= 600:  # Check if "Naive Choosing" button clicked
                    _, generation = kruskalsAlgorithm.kuskalInit(25, 25)
                    redraw_algorithm_window(imageName, generation)
                elif 400 <= mouse_x <= 600 and 550 <= mouse_y <= 600:  # Check if "Naive Branching" button clicked
                    _, generation = kruskalsAlgorithm.kuskalInit(51, 51)
                    redraw_algorithm_window(imageName, generation)
'''


def redraw_algorithm_window(imageName, generation):
    screen.blit(background_image, (0, 0))
    pygame.draw.rect(screen, BLACK, (0, 0, WIDTH, HEIGHT), 10)

    # Right section for black square
    pygame.draw.rect(screen, BLACK, (350, 100, 400, 400))

    # Load and blit image
    algorithm_image = pygame.image.load(imageName)
    algorithm_image = pygame.transform.scale(algorithm_image, (250, 400))  # Adjust size as needed
    screen.blit(algorithm_image, (70, 100))  # Adjust position as needed

    # Buttons
    draw_button(screen, "-", 200, 525, 150, 50, GRAY)  # Adjust position and size as needed
    draw_button(screen, "+", 400, 525, 150, 50, GRAY)  # Adjust position and size as needed

    WALL_THICKNESS = 800 // 102

    for x, y in generation:
        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(
            x * WALL_THICKNESS + 350, y * WALL_THICKNESS + 100, WALL_THICKNESS, WALL_THICKNESS))
        pygame.display.update()
        pygame.time.wait(20)

    pygame.display.update()


# Main loop
running = True
current_screen = "main_menu"
drawn = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_b:
                if current_screen != "main_menu":
                    current_screen = "main_menu"
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if current_screen == "main_menu":
                if 300 <= event.pos[0] <= 500 and 200 <= event.pos[1] <= 300:
                    current_screen = "play"
                elif 300 <= event.pos[0] <= 500 and 350 <= event.pos[1] <= 450:
                    current_screen = "learn"
            elif current_screen == "learn":
                if 150 <= event.pos[0] <= 370:
                    if 100 <= event.pos[1] <= 155:
                        current_screen = "kruskal"
                    elif 200 <= event.pos[1] <= 255:
                        current_screen = "prim"
                    elif 300 <= event.pos[1] <= 355:
                        current_screen = "binary_tree"
                    elif 400 <= event.pos[1] <= 455:
                        current_screen = "division"
                    elif 500 <= event.pos[1] <= 555:
                        current_screen = "backtracking"
                elif 450 <= event.pos[0] <= 670:
                    if 100 <= event.pos[1] <= 155:
                        current_screen = "choosing"
                    elif 200 <= event.pos[1] <= 255:
                        current_screen = "branching"

    if current_screen == "main_menu":
        main_menu()
    elif current_screen == "learn":
        learn_menu()
    elif current_screen == "kruskal":
        _, process = kruskalsAlgorithm.kuskalInit(25, 25)
        algorithm_window('kruskalProcess.png', process)
    elif current_screen == "prim":
        _, process = primsAlgorithm.primInit(25, 25)
        algorithm_window('primProcess.png', process)
    elif current_screen == "binary_tree":
        _, process = binaryTreeAlgorithm.binaryTreeInit(25, 25)
        algorithm_window('kruskalProcess.png', process)
    elif current_screen == "division":
        _, process = recursiveDivisionAlgorithm.recursiveDivisionInit(25, 25)
        algorithm_window('backtrackingProcess.png', process)
    elif current_screen == "backtracking":
        _, process = recursiveBacktrackingAlgorithm.recursiveBacktrackingInit(25, 25)
        algorithm_window('backtrackingProcess.png', process)
    elif current_screen == "branching":
        _, process = naiveBranchAlgorithm.naiveBranchInit(25, 25)
        algorithm_window('branchingProcess.png', process)
    elif current_screen == "play":
        play_screen()

# Quit Pygame
pygame.quit()
sys.exit()
