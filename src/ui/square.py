from enum import StrEnum
from typing import List, Optional, Callable

import pygame
from pygame import Surface

from common.color_type_enum import ColourType
from common.colours_const import colours


class Direction(StrEnum):
    up = "up"
    down = "down"
    left = "left"
    right = "right"


IMAGE_REDUCING_FACTOR = 20

class Square:
    def __init__(self,
                 corner: List[int],
                 dimensions: List[int],
                 display_size: Surface,
                 function: Callable,
                 direction: Optional[Direction] = None,
                 image: Optional[Surface] = None):
        self.corner = corner[:]
        self.dimensions = dimensions[:]
        self.display_size = display_size
        self.function = function
        self.direction = direction
        self.rect = [self.corner, self.dimensions]
        self.image = image

    def draw(self):
        [corner_x, corner_y] = self.corner
        [width, height] = self.dimensions
        pygame.draw.rect(self.display_size, colours[ColourType.black], self.rect, 5)
        if self.direction == Direction.down:
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
        if self.direction == Direction.left:
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
        if self.direction == Direction.right:
            pygame.draw.polygon(self.display_size, colours[ColourType.black],
                                ((corner_x + width, corner_y + height // 4),
                                 (corner_x + width, corner_y + height * 3 // 4),
                                 (corner_x + width // 3,
                                  corner_y + height * 3 // 4),
                                 (corner_x + width // 3, corner_y + height),
                                 (corner_x, corner_y + height // 2),
                                 (corner_x + width // 3, corner_y),
                                 (corner_x + width // 3, corner_y + height // 4)))
        if self.direction == Direction.up:
            pygame.draw.polygon(self.display_size, colours[ColourType.black],
                                ((corner_x + width // 4, corner_y + height),
                                 (corner_x + width * 3 // 4, corner_y + height),
                                 (corner_x + width * 3 // 4,
                                  corner_y + height // 3),
                                 (corner_x + width, corner_y + height // 3),
                                 (corner_x + width // 2, corner_y),
                                 (corner_x, corner_y + height // 3),
                                 (corner_x + width // 4, corner_y + height // 3)))
        if self.image:
            scaled_image = pygame.transform.scale(self.image, [dimension - IMAGE_REDUCING_FACTOR for dimension in self.dimensions])
            self.display_size.blit(scaled_image, [corner + IMAGE_REDUCING_FACTOR // 2 for corner in self.corner])