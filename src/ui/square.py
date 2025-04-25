from typing import List

import pygame
from pygame import Surface

from common.colours_const import colours
from common.color_type_enum import ColourType
from common.move_enum import Move


class Square:
    def __init__(self, corner: List[int], dimensions: List[int], display_size: Surface, letter: Move):
        self.corner = corner[:]
        self.dimensions = dimensions[:]
        self.display_size = display_size
        self.letter = letter

    def draw(self):
        [corner_x, corner_y] = self.corner
        [width, height] = self.dimensions
        pygame.draw.rect(self.display_size, colours[ColourType.black], [self.corner, self.dimensions], 5)
        if self.letter == Move.right_prime or self.letter == Move.left or self.letter == Move.turn_down:
            pygame.draw.polygon(self.display_size, colours[ColourType.black],
                                ((corner_x + width // 4, corner_y),
                                 (corner_x + width * 3 // 4, corner_y),
                                 (corner_x + width * 3 // 4,
                                  corner_y + height * 2 // 3),
                                 (corner_x + width, corner_y + height * 2 // 3),
                                 (corner_x + width // 2, corner_y + height),
                                 (corner_x, corner_y + height * 2 // 3),
                                 (corner_x + width // 4,
                                  corner_y + height * 2 // 3)))
        if self.letter == Move.up_prime or self.letter == Move.down or self.letter == Move.turn_right:
            pygame.draw.polygon(self.display_size, colours[ColourType.black],
                                ((corner_x, corner_y + height // 4),
                                 (corner_x, corner_y + height * 3 // 4),
                                 (corner_x + width * 2 // 3,
                                  corner_y + height * 3 // 4),
                                 (corner_x + width * 2 // 3, corner_y + height),
                                 (corner_x + width, corner_y + height // 2),
                                 (corner_x + width * 2 // 3, corner_y),
                                 (corner_x + width * 2 // 3,
                                  corner_y + height // 4)))
        if self.letter == Move.up or self.letter == Move.down_prime or self.letter == Move.turn_left:
            pygame.draw.polygon(self.display_size, colours[ColourType.black],
                                ((corner_x + width, corner_y + height // 4),
                                 (corner_x + width, corner_y + height * 3 // 4),
                                 (corner_x + width // 3,
                                  corner_y + height * 3 // 4),
                                 (corner_x + width // 3, corner_y + height),
                                 (corner_x, corner_y + height // 2),
                                 (corner_x + width // 3, corner_y),
                                 (corner_x + width // 3, corner_y + height // 4)))
        if self.letter == Move.right or self.letter == Move.left_prime or self.letter == Move.turn_up:
            pygame.draw.polygon(self.display_size, colours[ColourType.black],
                                ((corner_x + width // 4, corner_y + height),
                                 (corner_x + width * 3 // 4, corner_y + height),
                                 (corner_x + width * 3 // 4,
                                  corner_y + height // 3),
                                 (corner_x + width, corner_y + height // 3),
                                 (corner_x + width // 2, corner_y),
                                 (corner_x, corner_y + height // 3),
                                 (corner_x + width // 4, corner_y + height // 3)))