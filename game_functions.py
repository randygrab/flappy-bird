import pygame
import sys
from game_variables import pipe_list, score

class Pipe:
    def __init__(self, pipe_surface):
        self.top_pipe_surface = pygame.transform.flip(pipe_surface, False, True)
        self.bottom_pipe_surface = pipe_surface
        self.top_pipe = self.top_pipe_surface.get_rect(midbottom = (700, 150))  # Adjust this value
        self.bottom_pipe = self.bottom_pipe_surface.get_rect(midtop = (700, 350))  # Adjust this value
        self.scored = False

    def move(self):
        self.top_pipe.centerx -= 5
        self.bottom_pipe.centerx -= 5

    def draw(self, screen):
        screen.blit(self.top_pipe_surface, self.top_pipe)
        screen.blit(self.bottom_pipe_surface, self.bottom_pipe)

    def collide(self, bird_rect):
        return bird_rect.colliderect(self.top_pipe) or bird_rect.colliderect(self.bottom_pipe)

    def collide(self, bird_rect):
        return bird_rect.colliderect(self.top_pipe) or bird_rect.colliderect(self.bottom_pipe)

def draw_score(score, game_font, screen):
    score_surface = game_font.render(str(int(score)), True, (255, 255, 255))
    score_rect = score_surface.get_rect(center = (304, 50))
    screen.blit(score_surface, score_rect)

def main_menu(screen, clock, main_menu_bg, start_game_button, start_game_button_rect):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_game_button_rect.collidepoint(event.pos):
                    return

        screen.blit(main_menu_bg, (0, 0))
        screen.blit(start_game_button, start_game_button_rect)
        pygame.display.update()
        clock.tick(120)