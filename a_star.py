import heapq
import math

from constants import *
from map import get_neighbors


def heuristic(a, b):
    """
    Calculates the heuristic value for A* search algorithm.

    Parameters:
    a (Hexagon): The starting hexagon.
    b (Hexagon): The goal hexagon.

    Returns:
    int: The maximum of the absolute differences in the x and y coordinates of the two hexagons.
    """
    dx = abs(b.x - a.x)
    dy = abs(b.y - a.y)
    return max(dx, dy)


def a_star_search(hexagons, start, goal, hex_size):
    """
    Performs the A* search algorithm on a grid of hexagons.

    Parameters:
    hexagons (list): The list of all hexagons.
    start (Hexagon): The starting hexagon.
    goal (Hexagon): The goal hexagon.
    hex_size (int): The size of the hexagons.

    Returns:
    dict: A dictionary mapping each hexagon to the hexagon that came before it in the path.
    dict: A dictionary mapping each hexagon to the cost of the path from the start hexagon to it.
    """
    frontier = []
    heapq.heappush(frontier, (0, start))
    came_from = {start: None}
    cost_so_far = {start: 0}

    while frontier:
        _, current = heapq.heappop(frontier)

        if current == goal:
            break

        neighbors = get_neighbors(hexagons, current, hex_size)
        for next_hex in neighbors:
            new_cost = cost_so_far[current] + (1 if next_hex.color == RED else 0)
            if next_hex not in cost_so_far or new_cost < cost_so_far[next_hex]:
                cost_so_far[next_hex] = new_cost
                priority = new_cost + heuristic(goal, next_hex)
                heapq.heappush(frontier, (priority, next_hex))
                came_from[next_hex] = current

    return came_from, cost_so_far


def shortest_path_to_edge(hexagons, start, hex_size, start_x, start_y, total_width, total_height):
    """
    Finds the shortest path from a starting hexagon to the edge of the grid.

    Parameters:
    hexagons (list): The list of all hexagons.
    start (Hexagon): The starting hexagon.
    hex_size (int): The size of the hexagons.
    start_x (int): The x-coordinate of the top left corner of the grid.
    start_y (int): The y-coordinate of the top left corner of the grid.
    total_width (int): The total width of the grid.
    total_height (int): The total height of the grid.

    Returns:
    list: The shortest path from the starting hexagon to the edge of the grid.
    """
    goals = [hexs for hexs in hexagons if is_edge_hex(hexs, hex_size, start_x, start_y, total_width, total_height)]
    shortest_path = None
    shortest_path_cost = float('inf')

    for goal in goals:
        came_from, cost_so_far = a_star_search(hexagons, start, goal, hex_size)
        if goal in cost_so_far and cost_so_far[goal] < shortest_path_cost:
            shortest_path = reconstruct_path(came_from, start, goal)
            shortest_path_cost = cost_so_far[goal]

    return shortest_path


def reconstruct_path(came_from, start, goal):
    """
    Reconstructs the path from the start hexagon to the goal hexagon.

    Parameters:
    came_from (dict): A dictionary mapping each hexagon to the hexagon that came before it in the path.
    start (Hexagon): The starting hexagon.
    goal (Hexagon): The goal hexagon.

    Returns:
    list: The path from the start hexagon to the goal hexagon.
    """
    current = goal
    path = [current]

    while current != start:
        current = came_from[current]
        path.append(current)

    return path[::-1]


def is_edge_hex(hexagon, hex_size, start_x, start_y, total_width, total_height):
    """
    Checks if a hexagon is on the edge of the grid.

    Parameters:
    hexagon (Hexagon): The hexagon to check.
    hex_size (int): The size of the hexagons.
    start_x (int): The x-coordinate of the top left corner of the grid.
    start_y (int): The y-coordinate of the top left corner of the grid.
    total_width (int): The total width of the grid.
    total_height (int): The total height of the grid.

    Returns:
    bool: True if the hexagon is on the edge of the grid, False otherwise.
    """
    return (
            hexagon.x <= start_x
            or hexagon.x + 3 * hex_size / 2 >= start_x + total_width
            or hexagon.y <= start_y
            or hexagon.y + math.sqrt(3) * hex_size >= start_y + total_height
    )

