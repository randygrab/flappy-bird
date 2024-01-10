import sys
import pygame
from game_variables import game_active, pipe_list, score, bird_movement, gravity
from game_functions import Pipe, draw_score, main_menu

def game_loop(screen, clock, bg_surface, main_menu_bg, start_game_button, start_game_button_rect, retry_button, retry_button_rect, main_menu_button, main_menu_button_rect, bird_surface, bird_rect, pipe_surface, game_font):
    global game_active, bird_movement, pipe_list, score

    # Create a timer event to generate new pipes
    SPAWNPIPE = pygame.USEREVENT
    pygame.time.set_timer(SPAWNPIPE, 1200)

    # Display the main menu
    main_menu(screen, clock, main_menu_bg, start_game_button, start_game_button_rect)

    # Game Loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and game_active:
                    bird_movement = 0
                    bird_movement -= 6
                if event.key == pygame.K_SPACE and not game_active:
                    game_active = True
                    bird_rect.center = (50, 256)
                    bird_movement = 0
                    pipe_list.clear()
                    score = 0
            if event.type == pygame.MOUSEBUTTONDOWN:
                if retry_button_rect.collidepoint(event.pos) and not game_active:
                    game_active = True
                    bird_rect.center = (50, 256)
                    bird_movement = 0
                    pipe_list.clear()
                    score = 0
                if main_menu_button_rect.collidepoint(event.pos) and not game_active:
                    main_menu(screen, clock, main_menu_bg, start_game_button, start_game_button_rect)
            if event.type == SPAWNPIPE:
                pipe_list.append(Pipe(pipe_surface))

        screen.blit(bg_surface, (0, 0))  # Display the background

        if game_active:
            bird_movement += gravity
            bird_rect.centery += bird_movement
            screen.blit(bird_surface, bird_rect)

            for pipe in pipe_list:
                pipe.move()
                pipe.draw(screen)

                if pipe.collide(bird_rect):
                    game_active = False
                if not pipe.scored and pipe.bottom_pipe.centerx < bird_rect.centerx:
                    pipe.scored = True
                    score += 1

            if bird_rect.top <= -100 or bird_rect.bottom >= 457:
                game_active = False

            draw_score(score, game_font, screen)
        else:
            screen.blit(retry_button, retry_button_rect)
            screen.blit(main_menu_button, main_menu_button_rect)

        pygame.display.update()
        clock.tick(120)