import time
from copy import deepcopy
from typing import List

import pygame

from common.move_enum import Move
from cube.cube import Cube
from setup import setup_sides
from solver.layer_one import layer_one
from solver.layer_three.layer_three import layer_three
from solver.layer_two.layer_two import layer_two
from ui.draw_cube import draw_cube
from ui.square import Square

square_lst: List[Square] = []
pygame.init()
refresh_rate = 60
White = (255, 255, 255)
display_height = 700
display_length = 1066
display_size = pygame.display.set_mode((display_length, display_height))
display_size.fill(White)
cube = Cube()
start_time = time.time()
elapsed = 0
flag = False

square_lst.append(Square([display_length // 2 - 180, display_height // 2 - 65], [60, 30], display_size, Move.up))
square_lst.append(
    Square([display_length // 2 - 180, display_height // 2 + 38], [60, 30], display_size, Move.down_prime))
square_lst.append(Square([display_length // 2 + 121, display_height // 2 - 65], [60, 30], display_size, Move.up_prime))
square_lst.append(Square([display_length // 2 + 121, display_height // 2 + 38], [60, 30], display_size, Move.down))
square_lst.append(Square([display_length // 2 + 40, display_height // 2 - 180], [30, 60], display_size, Move.right))
square_lst.append(
    Square([display_length // 2 - 65, display_height // 2 - 180], [30, 60], display_size, Move.left_prime))
square_lst.append(
    Square([display_length // 2 + 40, display_height // 2 + 120], [30, 60], display_size, Move.right_prime))
square_lst.append(Square([display_length // 2 - 65, display_height // 2 + 120], [30, 60], display_size, Move.left))
square_lst.append(Square([0, 0], [30, 60], display_size, Move.front))
square_lst.append(Square([0, 400], [30, 60], display_size, Move.turn_z))
square_lst.append(Square([1000, 400], [30, 60], display_size, Move.turn_z_prime))

square_lst.append(Square([0, 500], [30, 60], display_size, Move.back))
square_lst.append(Square([50, display_height // 2 - 30], [60, 60], display_size, Move.turn_y_prime))
square_lst.append(Square([956, display_height // 2 - 30], [60, 60], display_size, Move.turn_y))
square_lst.append(Square([625, 50], [60, 60], display_size, Move.turn_x))
square_lst.append(Square([380, 590], [60, 60], display_size, Move.turn_x_prime))

TIME_BETWEEN_MOVES_SECONDS = 0
move_timestamp = time.time()
moves = []
current_move = -1

while True:
    if -1 < current_move < len(moves) and time.time() - move_timestamp > TIME_BETWEEN_MOVES_SECONDS:
        cube.movement_parser(moves[current_move])
        current_move += 1
        move_timestamp = time.time()
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            [mouse_pos_x, mouse_pos_y] = pygame.mouse.get_pos()
            for square in square_lst:
                [corner_x, corner_y] = square.corner
                [width, height] = square.dimensions
                if (corner_x + width >= mouse_pos_x >= corner_x) and (
                        corner_y + height >= mouse_pos_y >= corner_y):
                    cube.movement_parser(square.letter)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_TAB:
                cube.randomise()
                current_move = -1
            elif event.key == pygame.K_SPACE:
                moves = layer_one.layer_one(cube, True)
                current_move = 0
            elif event.key == pygame.K_RALT:
                layer_two(cube, True)
            elif event.key == pygame.K_w:
                layer_three(cube, True)
            elif event.key == pygame.K_LALT:
                cube.sides = deepcopy(setup_sides)
    elapsed = round(time.time() - start_time, 3)
    for square in square_lst:
        square.draw()

    draw_cube(display_size, display_height, display_length, cube)
    pygame.display.update()
    clock = pygame.time.Clock()
    clock.tick(refresh_rate)
