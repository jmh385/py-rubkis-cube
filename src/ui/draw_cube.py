import pygame

from common.colours_const import colours
from common.color_type_enum import ColourType

from cube.cube import Cube


def draw(display_size, display_height, display_length, side, diff_x, diff_y, x, y):
    for index, colour in enumerate(side):
        if index < 3:
            pygame.draw.rect(display_size, colours[colour],
                             (display_length // 2 - diff_x + index * x, display_height // 2 - diff_y,
                              x, y))
            pygame.draw.rect(display_size, colours[ColourType.black],
                             (display_length // 2 - diff_x + index * x, display_height // 2 - diff_y,
                              x, y), 5)
        elif index < 6:
            pygame.draw.rect(display_size, colours[colour],
                             (display_length // 2 - diff_x + (index - 3) * x, display_height // 2 - diff_y + y,
                              x, y))
            pygame.draw.rect(display_size, colours[ColourType.black],
                             (display_length // 2 - diff_x + (index - 3) * x, display_height // 2 - diff_y + y,
                              x, y), 5)
        else:
            pygame.draw.rect(display_size, colours[colour],
                             (display_length // 2 - diff_x + (index - 6) * x, display_height // 2 - diff_y + y * 2,
                              x, y))
            pygame.draw.rect(display_size, colours[ColourType.black],
                             (display_length // 2 - diff_x + (index - 6) * x, display_height // 2 - diff_y + y * 2,
                              x, y), 5)

def draw_cube(display_size, display_height, display_length, cube: Cube):
    draw(display_size, display_height, display_length, cube.sides[0], 112, 112, 75, 75)
    draw(display_size, display_height, display_length, cube.sides[1], -188, 75, 50, 50)
    draw(display_size, display_height, display_length, cube.sides[2], 75, 337, 50, 50)
    draw(display_size, display_height, display_length, cube.sides[3], 337, 75, 50, 50)
    draw(display_size, display_height, display_length, cube.sides[4], 75, -188, 50, 50)