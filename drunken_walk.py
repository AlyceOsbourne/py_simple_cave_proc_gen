import numpy as np


def drunken_walk(
        grid: np.array,
        start: tuple[int, int],
        max_step: int,
        passable_values: list[int],
        max_distance_from_start: int
):
    directions = {
        0: (0, 1),
        1: (0, -1),
        2: (1, 0),
        3: (-1, 0)
    }
    current_step = 0
    current_position = start
    path = [current_position]
    while current_step < max_step:
        direction = np.random.randint(0, 4)
        new_position = (current_position[0] + directions[direction][0], current_position[1] + directions[direction][1])
        if new_position[0] < 0 or new_position[0] >= grid.shape[0] or new_position[1] < 0 or new_position[1] >= \
                grid.shape[1]:
            continue
        if max_distance_from_start is not None and abs(new_position[0] - start[0]) + abs(
                new_position[1] - start[1]) > max_distance_from_start:
            continue
        if grid[new_position[0], new_position[1]] in passable_values:
            current_position = new_position
            path.append(current_position)
            current_step += 1
    return path
