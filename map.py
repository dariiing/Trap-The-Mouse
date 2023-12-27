import math
import random
from hexagon import Hexagon


def generate_hexagon_map(rows, cols, hex_size, screen_width, screen_height, colored_percentage=0.05):
    hexagons = []
    total_width = cols * 3 * hex_size / 2
    total_height = rows * math.sqrt(3) * hex_size

    start_x = (screen_width - total_width) / 2
    start_y = (screen_height - total_height) / 2

    center_x = start_x + total_width / 2
    center_y = start_y + total_height / 2

    closest_distance = float('inf')
    mouse = None

    for row in range(rows):
        for col in range(cols):
            x = start_x + col * (3 / 2) * hex_size
            y = start_y + row * math.sqrt(3) * hex_size

            if col % 2 == 1:
                y += hex_size * math.sqrt(3) / 2

            distance_to_center = math.sqrt((center_x - x) ** 2 + (center_y - y) ** 2)

            # check position for mouse
            if distance_to_center < closest_distance:
                closest_distance = distance_to_center
                mouse = Hexagon(x, y, (255, 255, 255), False)

            # percentage to be changed according to the level of the game(easy,medium,hard)
            is_colored = random.random() < colored_percentage
            color = (255, 0, 0) if is_colored else (255, 255, 255)

            hexagons.append(Hexagon(x, y, color, is_colored))

    # added mouse to map
    if mouse:
        mouse.color = (0, 0, 0)
        hexagons.append(mouse)

    return hexagons


def get_neighbors(hexagons, target_hexagon, hex_size):
    neighbors = []
    for hexagon in hexagons:
        if hexagon != target_hexagon:
            distance = math.sqrt((hexagon.x - target_hexagon.x) ** 2 + (hexagon.y - target_hexagon.y) ** 2)
            if distance <= hex_size * 2:
                neighbors.append(hexagon)
    return neighbors
