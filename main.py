import pygame
from game_loop import game_loop

# Game Initialization
pygame.init()

# Create the screen with the dimensions of the background image
screen = pygame.display.set_mode((608, 457))  # Set the size of the screen to match your background image
clock = pygame.time.Clock()

# Load the background image and get its dimensions
bg_surface = pygame.image.load('assets/background.png').convert_alpha()

# Load the main menu background and scale it to fit the screen
main_menu_bg = pygame.image.load('assets/main_menu_bg.png').convert_alpha()
main_menu_bg = pygame.transform.scale(main_menu_bg, (608, 457))

# Load the start game button image, scale it, and get its rect
start_game_button = pygame.image.load('assets/start_game.png').convert_alpha()
start_game_button = pygame.transform.scale(start_game_button, (177, 52))
start_game_button_rect = start_game_button.get_rect(center = (304, 228))

# Load the retry button image and get its rect
retry_button = pygame.image.load('assets/retry.png').convert_alpha()
retry_button_rect = retry_button.get_rect(center = (304, 228))

# Load the main menu button image and get its rect
main_menu_button = pygame.image.load('assets/main_menu.png').convert_alpha()
main_menu_button_rect = main_menu_button.get_rect(center = (304, 300))

# Game Sprites
bird_surface = pygame.image.load('assets/bluebird-midflap.png').convert_alpha()
bird_surface = pygame.transform.scale(bird_surface, (50, 50))
bird_rect = bird_surface.get_rect(center = (50, 256))

pipe_surface = pygame.image.load('assets/pipe.png').convert_alpha()
pipe_surface = pygame.transform.scale(pipe_surface, (80, 250))  # Resize the pipe image

# Define game font
game_font = pygame.font.Font(None, 50)

# Start the game loop
game_loop(screen, clock, bg_surface, main_menu_bg, start_game_button, start_game_button_rect, retry_button, retry_button_rect, main_menu_button, main_menu_button_rect, bird_surface, bird_rect, pipe_surface, game_font)