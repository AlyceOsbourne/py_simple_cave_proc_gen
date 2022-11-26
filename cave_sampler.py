# takes a numpy array of ints and draps thew map as a png file using pygame, drawing each value as a square
import pygame;

pygame.init()
from cave_carver import make_caves


def main():
    tile_size = 4
    size = (120, 120)
    for i in range(5):
        caves = make_caves(
            size=size,
            num_rooms=7,
            num_corridors=9,
            room_min_steps=30,
            room_max_steps=70,
            room_iterations=30,
            room_max_distance_from_start=None,
            corridor_min_steps=3,
            corridor_max_staps=5,
            corridor_max_distance_from_start=6,
            border_padding=20,
            carvable_values=[0, 1],
            passable_values=[1],
            carve_value=1,
            heuristic_methods=['euclidean', 'octile', 'manhattan', 'chebyshev'],
            max_attempts=100,
            min_room_distance=15
        )
        if caves is None:
            print("Failed to generate cave")
            exit()
        surface = pygame.Surface((size[0] * tile_size, size[1] * tile_size))
        for y, row in enumerate(caves):
            for x, cell in enumerate(row):
                pygame.draw.rect(surface, (cell * 255, cell * 255, cell * 255),
                                 (x * tile_size, y * tile_size, tile_size, tile_size))
        pygame.image.save(surface, f"examples/cave_{i}.png")
    pygame.quit()


if __name__ == '__main__':
    main()
