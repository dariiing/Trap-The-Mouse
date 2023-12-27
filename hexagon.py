import pygame
import math


class Hexagon:
    def __init__(self, x, y, color, is_colored=False):
        self.x = x
        self.y = y
        self.color = color
        self.is_colored = is_colored


def draw_hexagon(surface, x, y, size, color, border_color, border_width):
    h = size * math.sqrt(3) / 2
    # hexagon color
    pygame.draw.polygon(surface, color, [(x, y),
                                         (x + size, y),
                                         (x + size + size / 2, y + h),
                                         (x + size, y + 2 * h),
                                         (x, y + 2 * h),
                                         (x - size / 2, y + h)])

    # hexagon border
    pygame.draw.polygon(surface, border_color, [(x, y),
                                                (x + size, y),
                                                (x + size + size / 2, y + h),
                                                (x + size, y + 2 * h),
                                                (x, y + 2 * h),
                                                (x - size / 2, y + h)], border_width)