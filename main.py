import pygame
import random

pygame.init()


WINDOW_WIDTH = 800
WINDOW_HEIGHT = 400



display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Catch the Clown!")





game_running = True
while game_running:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            game_running = False

        

    pygame.display.update()

pygame.quit()