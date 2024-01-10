import pygame
from game_loop import game_loop

# Game Initialization
pygame.init()

# Create the game screen
game_screen = pygame.display.set_mode((608, 457))

# Game clock
game_clock = pygame.time.Clock()

# Background surface
background_surface = pygame.image.load('assets/background.png').convert_alpha()

# Main menu background surface
main_menu_bg_surface = pygame.image.load('assets/main_menu_bg.png').convert_alpha()
main_menu_bg_surface = pygame.transform.scale(main_menu_bg_surface, (608, 457))

# Start game button surface, scaled and positioned
start_button_surface = pygame.image.load('assets/start_game.png').convert_alpha()
start_button_surface = pygame.transform.scale(start_button_surface, (177, 52))
start_button_rect = start_button_surface.get_rect(center = (304, 228))

# Retry button surface, positioned
retry_button_surface = pygame.image.load('assets/retry.png').convert_alpha()
retry_button_rect = retry_button_surface.get_rect(center = (304, 228))

# Main menu button surface, positioned
main_menu_button_surface = pygame.image.load('assets/main_menu.png').convert_alpha()
main_menu_button_rect = main_menu_button_surface.get_rect(center = (304, 300))

# Bird sprite surface, scaled
bird_sprite = pygame.image.load('assets/bluebird-midflap.png').convert_alpha()
bird_sprite = pygame.transform.scale(bird_sprite, (50, 50))
bird_rect = bird_sprite.get_rect(center = (50, 256))

# Pipe sprite surface, scaled
pipe_sprite = pygame.image.load('assets/pipe.png').convert_alpha()
pipe_sprite = pygame.transform.scale(pipe_sprite, (80, 250))

# Game font
game_font = pygame.font.Font(None, 50)

# Start game loop
game_loop(game_screen, game_clock, background_surface, main_menu_bg_surface,
         start_button_surface, start_button_rect, retry_button_surface,
         retry_button_rect, main_menu_button_surface, main_menu_button_rect,
         bird_sprite, bird_rect, pipe_sprite, game_font)
