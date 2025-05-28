from typing import List

from common.color_type_enum import ColourType
from common.move_enum import Move
from cube.cube import Cube


def layer_two(cube: Cube) -> List[Move]:
    moves_played: List[Move] = []
    true_side = 0
    while cube.sides[0][:6].count(cube.sides[0][4]) != 6 or \
            cube.sides[1][:6].count(cube.sides[1][4]) != 6 or \
            cube.sides[3][:6].count(cube.sides[3][4]) != 6 or \
            cube.sides[5][:6].count(cube.sides[5][4]) != 6:
        side_key = {0: 1, 1: 5, 5: 7, 3: 3}
        color_lst = [ColourType.green, ColourType.blue, ColourType.red, ColourType.orange]
        i = 0
        side_lst = [cube.sides[0], cube.sides[1], cube.sides[3], cube.sides[5]]
        for side in side_lst:
            if side[7] != ColourType.yellow and cube.sides[4][side_key[i]] != ColourType.yellow:
                color = side[7]
                for side1 in side_lst:
                    if side1[4] == color:
                        true_side = side1
                while true_side[7] != color:
                    cube.down()
                while cube.sides[0][4] != color:
                    cube.turn_left()
                if cube.sides[4][1] == cube.sides[1][4]:
                    if cube.sides[3][5] == cube.sides[3][4] and cube.sides[0][3] == cube.sides[0][4]:
                        moves_played.extend(cube.movement_parser(
                            [Move.left_prime, Move.up_prime, Move.front_prime, Move.up, Move.left, Move.front_prime,
                             Move.down, Move.front]))
                    else:
                        moves_played.extend(cube.movement_parser(
                            [Move.right, Move.up, Move.front_prime, Move.up_prime, Move.front_prime, Move.right_prime,
                             Move.front]))
                else:
                    if cube.sides[1][3] == cube.sides[1][4] and cube.sides[0][5] == cube.sides[0][4]:
                        moves_played.extend(cube.movement_parser(
                            [Move.right, Move.up, Move.front, Move.up_prime, Move.right_prime, Move.front,
                             Move.down_prime, Move.front_prime]))
                    else:
                        moves_played.extend(cube.movement_parser(
                            [Move.left_prime, Move.up_prime, Move.front, Move.up, Move.front, Move.left,
                             Move.front_prime]))

        for i in range(2):
            if (cube.sides[0][5] != cube.sides[0][4] or cube.sides[1][4] != cube.sides[1][3]) and \
                    (cube.sides[0][5] in color_lst and cube.sides[1][3] in color_lst):
                moves_played.extend(cube.movement_parser(
                    [Move.right_prime, Move.down_prime, Move.right, Move.down, Move.front, Move.down, Move.front_prime]))
            if (cube.sides[0][3] != cube.sides[0][4] or cube.sides[3][5] != cube.sides[3][4]) and \
                    (cube.sides[0][3] in color_lst and cube.sides[3][5] in color_lst):
                moves_played.extend(cube.movement_parser(
                    [Move.left, Move.down, Move.left_prime, Move.down_prime, Move.front_prime, Move.down_prime,
                     Move.front]))
            moves_played.extend(cube.turn_left(2))

    return moves_played