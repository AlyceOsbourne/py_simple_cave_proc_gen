import math
from functools import total_ordering
from typing import Literal

import numpy as np


@total_ordering
class Node:
    def __init__(self, x, y, parent=None):
        self.x = x
        self.y = y
        self.parent = parent
        self.f = 0
        self.g = 0
        self.h = 0

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return f"({self.x}, {self.y})"

    def __hash__(self):
        return hash((self.x, self.y))

    def __lt__(self, other):
        return self.f < other.f


def heuristic(node, goal, method="euclidean"):
    match method:
        case "euclidean":
            return math.sqrt((node.x - goal.x) ** 2 + (node.y - goal.y) ** 2)
        case "manhattan":
            return abs(node.x - goal.x) + abs(node.y - goal.y)
        case "octile":
            return max(abs(node.x - goal.x), abs(node.y - goal.y))
        case "chebyshev":
            return max(abs(node.x - goal.x), abs(node.y - goal.y))
        case _:
            raise ValueError(f"Unknown heuristic method: {method}")


def neighbors(node, grid):
    n = []
    if node.x < grid.shape[0] - 1:
        n.append(Node(node.x + 1, node.y, node))
    if node.x > 0:
        n.append(Node(node.x - 1, node.y, node))
    if node.y < grid.shape[1] - 1:
        n.append(Node(node.x, node.y + 1, node))
    if node.y > 0:
        n.append(Node(node.x, node.y - 1, node))
    return n


def a_star(*, grid: np.array, start: tuple[int, int], goal: tuple[int, int], passable_values: list[int], method: Literal["euclidean", "manhattan", "octile", "chebyshev"]):
    start_node = Node(start[0], start[1])
    goal_node = Node(goal[0], goal[1])
    open_list = {
        start_node
    }
    closed_list = set()
    while open_list:
        current_node = min(open_list)
        open_list.remove(current_node)
        closed_list.add(current_node)
        path = []
        if current_node == goal_node:
            while current_node is not None:
                path.append((current_node.x, current_node.y))
                current_node = current_node.parent
            return path[::-1]
        for neighbor in neighbors(current_node, grid):
            if grid[neighbor.x, neighbor.y] not in passable_values:
                continue
            if neighbor in closed_list:
                continue
            neighbor.g = current_node.g + 1
            neighbor.h = heuristic(neighbor, goal_node, method)
            neighbor.f = neighbor.g + neighbor.h
            if neighbor in open_list:
                continue
            open_list.add(neighbor)
    return []
