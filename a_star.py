import heapq
import math

from constants import *
from map import get_neighbors


def heuristic(a, b):
    dx = abs(b.x - a.x)
    dy = abs(b.y - a.y)
    return max(dx, dy)


def a_star_search(hexagons, start, goal, hex_size):
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
            if next_hex.color != WHITE:
                continue
            new_cost = cost_so_far[current] + (1 if next_hex.color == RED else 0)
            if next_hex not in cost_so_far or new_cost < cost_so_far[next_hex]:
                cost_so_far[next_hex] = new_cost
                priority = new_cost + heuristic(goal, next_hex)
                heapq.heappush(frontier, (priority, next_hex))
                came_from[next_hex] = current

    return came_from, cost_so_far


def shortest_path_to_edge(hexagons, start, hex_size, start_x, start_y, total_width, total_height):
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
    current = goal
    path = [current]

    while current != start:
        current = came_from[current]
        path.append(current)

    return path[::-1]


def is_edge_hex(hexagon, hex_size, start_x, start_y, total_width, total_height):
    return (
            hexagon.x <= start_x
            or hexagon.x + 3 * hex_size / 2 >= start_x + total_width
            or hexagon.y <= start_y
            or hexagon.y + math.sqrt(3) * hex_size >= start_y + total_height
    )

