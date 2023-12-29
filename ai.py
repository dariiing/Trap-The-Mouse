import math
import random

from constants import *


def distance_to_edge(hexagon, start_x, total_width, start_y, total_height, hex_size, difficulty):
    left_distance = hexagon.x - start_x
    right_distance = (start_x + total_width) - (hexagon.x + 3 * hex_size / 2)
    top_distance = hexagon.y - start_y
    bottom_distance = (start_y + total_height) - (hexagon.y + math.sqrt(3) * hex_size)

    if difficulty == "medium":
        weight_left = 1 + random.uniform(-0.2, 0.2)
        weight_right = 1 + random.uniform(-0.2, 0.2)
        weight_top = 1 + random.uniform(-0.2, 0.2)
        weight_bottom = 1 + random.uniform(-0.2, 0.2)
    elif difficulty == "hard":
        weight_left = 3 + random.uniform(-0.5, 0.5)
        weight_right = 3 + random.uniform(-0.5, 0.5)
        weight_top = 3 + random.uniform(-0.5, 0.5)
        weight_bottom = 3 + random.uniform(-0.5, 0.5)
    else:
        raise ValueError("Invalid difficulty level")

    weighted_distance = (
        weight_left * left_distance +
        weight_right * right_distance +
        weight_top * top_distance +
        weight_bottom * bottom_distance
    )

    return weighted_distance

