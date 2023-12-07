import math
from hexagon import Hexagon


def generate_hexagon_map(rows, cols, hex_size, screen_width, screen_height):
    hexagons = []
    total_width = cols * 3 * hex_size / 2
    total_height = rows * math.sqrt(3) * hex_size

    start_x = (screen_width - total_width) / 2
    start_y = (screen_height - total_height) / 2

    for row in range(rows):
        for col in range(cols):
            x = start_x + col * (3 / 2) * hex_size
            y = start_y + row * math.sqrt(3) * hex_size

            if col % 2 == 1:
                y += hex_size * math.sqrt(3) / 2

            hexagons.append(Hexagon(x, y, (255, 255, 255)))
    return hexagons
