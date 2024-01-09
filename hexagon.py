import pygame
import math


class Hexagon:
    def __init__(self, x, y, color, is_colored=False):
        """
        Initializes a Hexagon object.

        Parameters:
        - x (float): The x-coordinate of the hexagon.
        - y (float): The y-coordinate of the hexagon.
        - color (tuple): The color of the hexagon.
        - is_colored (bool, optional): A flag indicating whether the hexagon is colored. Defaults to False.
        """
        self.x = x
        self.y = y
        self.color = color
        self.is_colored = is_colored

    def __lt__(self, other):
        """
        Compares this hexagon with another hexagon.

        Parameters:
        - other (Hexagon): The other hexagon to compare with.

        Returns:
        - bool: True if this hexagon is less than the other hexagon, False otherwise.
        """
        return self.x < other.x or (self.x == other.x and self.y < other.y)

    def __hash__(self):
        """
        Returns the hash value of the hexagon.

        Returns:
        - int: The hash value of the hexagon.
        """
        return hash((self.x, self.y, self.color, self.is_colored))

    def __eq__(self, other):
        """
        Checks if this hexagon is equal to another hexagon.

        Parameters:
        - other (Hexagon): The other hexagon to compare with.

        Returns:
        - bool: True if this hexagon is equal to the other hexagon, False otherwise.
        """
        if isinstance(other, Hexagon):
            return self.x == other.x and self.y == other.y and self.color == other.color and self.is_colored == other.is_colored
        return False


def draw_hexagon(surface, x, y, size, color, border_color, border_width):
    """
    Draws a hexagon on a pygame surface.

    Parameters:
    - surface (pygame.Surface): The surface to draw on.
    - x (float): The x-coordinate of the hexagon.
    - y (float): The y-coordinate of the hexagon.
    - size (float): The size of the hexagon.
    - color (tuple): The color of the hexagon.
    - border_color (tuple): The color of the hexagon's border.
    - border_width (int): The width of the hexagon's border.

    Returns:
    - None
    """
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
