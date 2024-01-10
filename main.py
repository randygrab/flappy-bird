import pygame
from game_loop import game_loop
from game_variables import *

# Game Initialization
pygame.init()

# Create the game screen
game_screen = pygame.display.set_mode(game_screen_size)

# Game clock
game_clock = pygame.time.Clock()

# Background surface
background_surface = pygame.image.load('assets/background.png').convert_alpha()

# Main menu background surface
main_menu_bg_surface = pygame.image.load('assets/main_menu_bg.png').convert_alpha()
main_menu_bg_surface = pygame.transform.scale(main_menu_bg_surface, main_menu_bg_size)

# Start game button surface, scaled and positioned
start_button_surface = pygame.image.load('assets/start_game.png').convert_alpha()
start_button_surface = pygame.transform.scale(start_button_surface, start_game_button_size)
start_button_rect = start_button_surface.get_rect(center = start_button_position)

# Retry button surface, positioned
retry_button_surface = pygame.image.load('assets/retry.png').convert_alpha()
retry_button_surface = pygame.transform.scale(retry_button_surface, retry_button_size)
retry_button_rect = retry_button_surface.get_rect(center = retry_button_position)

# Main menu button surface, positioned
main_menu_button_surface = pygame.image.load('assets/main_menu.png').convert_alpha()
main_menu_button_surface = pygame.transform.scale(main_menu_button_surface, main_menu_button_size)
main_menu_button_rect = main_menu_button_surface.get_rect(center = main_menu_button_position)

# Bird sprite surface, scaled
bird_sprite = pygame.image.load('assets/bluebird-midflap.png').convert_alpha()
bird_sprite = pygame.transform.scale(bird_sprite, bird_size)
bird_rect = bird_sprite.get_rect(center = bird_position)

# Pipe sprite surface, scaled
pipe_sprite = pygame.image.load('assets/pipe.png').convert_alpha()
pipe_sprite = pygame.transform.scale(pipe_sprite, pipe_size)

# Game font
game_font = pygame.font.Font(None, font_size)

# Start game loop
game_loop(game_screen, game_clock, background_surface, main_menu_bg_surface,
         start_button_surface, start_button_rect, retry_button_surface,
         retry_button_rect, main_menu_button_surface, main_menu_button_rect,
         bird_sprite, bird_rect, pipe_sprite, game_font)