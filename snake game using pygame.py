import pygame
import sys
import time
import random

score = 0

def level1():
    difficulty = 10

    # Window size
    window_x = 720
    window_y = 480
    width = int(window_x / 1.6)

    # Checks for errors encountered
    check_errors = pygame.init()

    # Initialise game window
    pygame.display.set_caption('Snake Game')
    game_window = pygame.display.set_mode((window_x, window_y))

    # game_window.pygame.image.load('background image.png')

    black = pygame.Color(0, 0, 0)
    white = pygame.Color(255, 255, 255)
    red = pygame.Color(255, 0, 0)
    green = pygame.Color(0, 255, 0)
    
    # FPS (frames per second)
    fps_controller = pygame.time.Clock()


    # Game variables
    snake_pos = [100, 50]
    snake_body = [[100, 50], [90, 50], [80, 50], [70, 50], [60, 50], [50, 50]]

    food_pos = [random.randrange(1, (window_x//10)) * 10, random.randrange(1, (window_y//10)) * 10]
    food_spawn = True

    pygame.display.update()

    direction = 'RIGHT'
    change_to = direction

    score = 0

    barriers = pygame.draw.rect(
            game_window,
            (255, 255, 255),
            (window_x / 2, 100, 10,200)
        )
    pygame.mixer.music.load("music.mp3")
    pygame.mixer.music.play()

    # Game Over function
    def game_over():
        my_font = pygame.font.SysFont('times new roman', 90)
        game_over_surface = my_font.render('YOU DIED', True, red)
        game_over_rect = game_over_surface.get_rect()
        game_over_rect.midtop = (window_x/2, window_y/4)
        game_window.fill(black)
        game_window.blit(game_over_surface, game_over_rect)
        show_score(0, red, 'times', 20)
        pygame.display.flip()
        time.sleep(3)
        pygame.quit()
        sys.exit()

