import pygame
import math


class Hexagon:
    def __init__(self, x, y, color, is_colored=False):
        self.x = x
        self.y = y
        self.color = color
        self.is_colored = is_colored

    def __lt__(self, other):
        return self.x < other.x or (self.x == other.x and self.y < other.y)

    def __hash__(self):
        return hash((self.x, self.y, self.color, self.is_colored))

    def __eq__(self, other):
        if isinstance(other, Hexagon):
            return self.x == other.x and self.y == other.y and self.color == other.color and self.is_colored == other.is_colored
        return False


def draw_hexagon(surface, x, y, size, color, border_color, border_width):
    h = size * math.sqrt(3) / 2
    points = [(x, y),
              (x + size, y),
              (x + size + size / 2, y + h),
              (x + size, y + 2 * h),
              (x, y + 2 * h),
              (x - size / 2, y + h)]
    # hexagon color
    pygame.draw.polygon(surface, color, points)

    # hexagon border
    pygame.draw.polygon(surface, border_color, points, border_width)
