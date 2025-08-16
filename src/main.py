import sys, os

import argparse
import time
from copy import deepcopy
from typing import List

import pygame

from common.color_type_enum import ColourType
from cube.cube import Cube
from solver.solve_cube import solve_cube
from state_save import state_save
from ui.draw_cube import draw_cube
from ui.square import Square, Direction

def resource_path(relative_path):
    """Get absolute path to resource, works for dev and for PyInstaller bundle"""
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

img_path = resource_path("assets\save-image.jpg")


parser = argparse.ArgumentParser()
parser.add_argument("--move_wait_time", help="time between solution moves in seconds")

args = parser.parse_args()

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

save_icon = pygame.image.load(img_path).convert_alpha()


square_lst.append(
    Square([display_length // 2 - 180, display_height // 2 + 38], [60, 30], display_size, lambda: cube.down_prime(),
           Direction.right))
square_lst.append(
    Square([display_length // 2 - 180, display_height // 2 - 65], [60, 30], display_size, lambda: cube.up(),
           Direction.right))
square_lst.append(
    Square([50, display_height // 2 - 30], [60, 60], display_size, lambda: cube.turn_y_prime(), Direction.right))

square_lst.append(
    Square([display_length // 2 + 121, display_height // 2 - 65], [60, 30], display_size, lambda: cube.up_prime(),
           Direction.left))
square_lst.append(
    Square([display_length // 2 + 121, display_height // 2 + 38], [60, 30], display_size, lambda: cube.down(),
           Direction.left))
square_lst.append(
    Square([956, display_height // 2 - 30], [60, 60], display_size, lambda: cube.turn_y(), Direction.left))
square_lst.append(
    Square([display_length // 2 - 65, display_height // 2 - 180], [30, 60], display_size, lambda: cube.left_prime(),
           Direction.up))
square_lst.append(
    Square([display_length // 2 + 40, display_height // 2 - 180], [30, 60], display_size, lambda: cube.right(),
           Direction.up))
square_lst.append(Square([625, 50], [60, 60], display_size, lambda: cube.turn_x(), Direction.up))
square_lst.append(
    Square([display_length // 2 + 40, display_height // 2 + 120], [30, 60], display_size, lambda: cube.right_prime(),
           Direction.down))
square_lst.append(
    Square([display_length // 2 - 65, display_height // 2 + 120], [30, 60], display_size, lambda: cube.left(),
           Direction.down))
square_lst.append(
    Square([display_length // 2 + 200, display_height // 2 + 85], [30, 60], display_size, lambda: cube.front(),
           Direction.down))
square_lst.append(
    Square([display_length // 2 - 225, display_height // 2 + 85], [30, 60], display_size, lambda: cube.front_prime(),
           Direction.down))
square_lst.append(
    Square([display_length // 2 + 300, display_height // 2 + 85], [30, 60], display_size, lambda: cube.back_prime(),
           Direction.down))
square_lst.append(
    Square([display_length // 2 - 325, display_height // 2 + 85], [30, 60], display_size, lambda: cube.back(),
           Direction.down))
square_lst.append(Square([380, 590], [60, 60], display_size, lambda: cube.turn_x_prime(), Direction.down))

square_lst.append(
    Square([display_length // 2 + 235, display_height // 2 - 150], [60, 60], display_size, lambda: cube.turn_z(),
           Direction.up))
square_lst.append(
    Square([display_length // 2 - 290, display_height // 2 - 150], [60, 60], display_size, lambda: cube.turn_z_prime(),
           Direction.up))


def set_state_save(state: List[List[ColourType]], new_state: List[List[ColourType]]):
    state.clear()
    state.extend(new_state)


square_lst.append(Square([display_length - 120, 50], [60, 60], display_size,
                         lambda: set_state_save(state_save, deepcopy(cube.sides)), image=save_icon))


TIME_BETWEEN_MOVES_SECONDS = float(args.move_wait_time) if args.move_wait_time else 0.1
move_timestamp = time.time()
moves = []
current_move = -1

while True:
    if -1 < current_move < len(moves) and time.time() - move_timestamp > TIME_BETWEEN_MOVES_SECONDS:
        cube.movement_parser(moves[current_move])
        current_move += 1
        print(current_move, len(moves))
        move_timestamp = time.time()
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            [mouse_pos_x, mouse_pos_y] = pygame.mouse.get_pos()
            for square in square_lst:
                [corner_x, corner_y] = square.corner
                [width, height] = square.dimensions
                if (corner_x + width >= mouse_pos_x >= corner_x) and (
                        corner_y + height >= mouse_pos_y >= corner_y):
                    square.function()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_TAB:
                cube.randomise()
                current_move = -1
            elif event.key == pygame.K_w:
                moves = deepcopy(solve_cube(cube, False))
                current_move = 0
            elif event.key == pygame.K_LALT:
                cube.sides = deepcopy(state_save)
    elapsed = round(time.time() - start_time, 3)
    for square in square_lst:
        square.draw()

    draw_cube(display_size, display_height, display_length, cube)
    pygame.display.update()
    clock = pygame.time.Clock()
    clock.tick(refresh_rate)
