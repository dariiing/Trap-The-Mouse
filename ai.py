import math


def distance_to_edge(hexagon, start_x, total_width, start_y, total_height, hex_size):
    left_distance = hexagon.x - start_x
    right_distance = (start_x + total_width) - (hexagon.x + 3 * hex_size / 2)
    top_distance = hexagon.y - start_y
    bottom_distance = (start_y + total_height) - (hexagon.y + math.sqrt(3) * hex_size)
    return min(left_distance, right_distance, top_distance, bottom_distance)