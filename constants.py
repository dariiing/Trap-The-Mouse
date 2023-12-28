import pygame

WIDTH, HEIGHT = 1000, 900
WHITE = (255, 255, 255)
PINK = (255, 182, 193)
LIGHT_PINK = (255, 200, 210)
RED = (255, 140, 150)
BLACK = (50, 50, 50)

EXIT_BUTTON = {"x": WIDTH - 350, "y": HEIGHT - 80, "width": 300, "height": 60}
RETURN_BUTTON = {"x": 50, "y": HEIGHT - 80, "width": 300, "height": 60}

win = pygame.display.set_mode((WIDTH, HEIGHT))
