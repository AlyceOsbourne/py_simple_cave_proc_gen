# we use drunken walk to create rooms, then use a* + drunken walk to connect them
import random
from typing import Literal

import numpy as np

from a_star import a_star
from drunken_walk import drunken_walk
from itertools import permutations


def make_caves(
        *,
        size: tuple[int, int],
        num_rooms: int,
        num_corridors: int,
        room_min_steps: int,
        room_max_steps: int,
        room_iterations: int,
        room_max_distance_from_start: int|None,
        corridor_min_steps: int,
        corridor_max_staps: int,
        corridor_max_distance_from_start: int,
        border_padding: int,
        carvable_values: list[int],
        passable_values: list[int],
        carve_value: int,
        heuristic_methods: list[Literal["manhattan", "euclidean", "octile", "chebyshev"]],
        max_attempts: int,
        min_room_distance: int
):

    if num_corridors < num_rooms - 1:
        raise ValueError("Not enough corridors to connect all the rooms")
    if (min_room_distance + border_padding) / 2 > min(size):
        raise ValueError("Min room distance and border padding are too close together")

    grid = np.zeros(size, dtype=np.int8)
    grid[0, :] = 1
    grid[-1, :] = 1
    grid[:, 0] = 1
    grid[:, -1] = 1
    room_centers = []
    while len(room_centers) < num_rooms:
        room = (
            np.random.randint(border_padding, size[0] - border_padding),
            np.random.randint(border_padding, size[1] - border_padding)
        )
        if grid[room] == carve_value or any(
                map(lambda x: np.linalg.norm(np.array(room) - np.array(x)) < min_room_distance, room_centers)):
            continue
        room_centers.append(room)

    for room_center in room_centers:
        for _ in range(room_iterations):
            room_path = drunken_walk(
                grid=grid,
                start=room_center,
                max_step=np.random.randint(room_min_steps, room_max_steps),
                passable_values=carvable_values,
                max_distance_from_start=room_max_distance_from_start
            )
            for position in room_path:
                grid[position[0], position[1]] = carve_value

    corridors = 0

    while corridors < num_corridors:
        start = room_centers[np.random.randint(0, len(room_centers))]
        end = room_centers[np.random.randint(0, len(room_centers))]
        while grid[start[0], start[1]] not in carvable_values:
            start = room_centers[np.random.randint(0, len(room_centers))]
        while grid[end[0], end[1]] not in carvable_values or start == end:
            end = room_centers[np.random.randint(0, len(room_centers))]
        path = a_star(grid=grid, start=start, goal=end, passable_values=carvable_values,
                      method=random.choice(heuristic_methods))
        if path is None:
            continue
        for step in path:
            for position in drunken_walk(
                    grid,
                    step,
                    np.random.randint(corridor_min_steps, corridor_max_staps),
                    carvable_values,
                    max_distance_from_start=corridor_max_distance_from_start
            ):
                grid[position[0], position[1]] = carve_value
        corridors += 1

    for a, b in permutations(room_centers, 2):
        if a_star(grid=grid, start=a, goal=b, passable_values=passable_values,
                  method=random.choice(heuristic_methods)) is None:
            if max_attempts == 0:
                return None
            print("Failed to connect rooms, retrying")
            return make_caves(
                size=size,
                num_rooms=num_rooms,
                num_corridors=num_corridors,
                room_min_steps=room_min_steps,
                room_max_steps=room_max_steps,
                room_iterations=room_iterations,
                room_max_distance_from_start=room_max_distance_from_start,
                corridor_min_steps=corridor_min_steps,
                corridor_max_staps=corridor_max_staps,
                corridor_max_distance_from_start=corridor_max_distance_from_start,
                border_padding=border_padding,
                carvable_values=carvable_values,
                passable_values=passable_values,
                carve_value=carve_value,
                heuristic_methods=heuristic_methods,
                max_attempts=max_attempts - 1,
                min_room_distance=min_room_distance
            )

    return grid


def main():
    colours = {
        0: "\033[0;30m",
        1: "\033[0;37m",
    }
    cave = make_caves(
        size=(120, 120),
        num_rooms=7,
        num_corridors=6,
        room_min_steps=10,
        room_max_steps=40,
        room_iterations=100,
        room_max_distance_from_start=40,
        corridor_min_steps=3,
        corridor_max_staps=5,
        corridor_max_distance_from_start=6,
        border_padding=20,
        carvable_values=[0, 1],
        passable_values=[1],
        carve_value=1,
        heuristic_methods=['euclidean', 'octile', 'manhattan', 'chebyshev'],
        max_attempts=100
    )
    if cave is None:
        print("Failed to generate cave")
        return
    for row in cave:
        for cell in row:
            print(f"{colours[cell]}██", end="")
        print()


if __name__ == '__main__':
    main()
