from typing import List

from common.color_type_enum import ColourType
from common.move_enum import Move
from cube.cube import Cube


def layer_two(cube: Cube):
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
                        cube.movement_parser(
                            [Move.left_prime, Move.up_prime, Move.front_prime, Move.up, Move.left, Move.front_prime,
                             Move.down, Move.front])
                        moves_played += " l' u' f' u l f' d f"
                    else:
                        cube.movement_parser(
                            [Move.right, Move.up, Move.front_prime, Move.up_prime, Move.front_prime, Move.right_prime,
                             Move.front])
                        moves_played += " r u f' u' f' r' f"
                else:
                    if cube.sides[1][3] == cube.sides[1][4] and cube.sides[0][5] == cube.sides[0][4]:
                        cube.movement_parser(
                            [Move.right, Move.up, Move.front, Move.up_prime, Move.right_prime, Move.front,
                             Move.down_prime, Move.front_prime])
                        moves_played += " r u f u' r' f d' f'"
                    else:
                        cube.movement_parser(
                            [Move.left_prime, Move.up_prime, Move.front, Move.up, Move.front, Move.left,
                             Move.front_prime])
                        moves_played += " l' u' f u f l f'"

        for i in range(2):
            if (cube.sides[0][5] != cube.sides[0][4] or cube.sides[1][4] != cube.sides[1][3]) and \
                    (cube.sides[0][5] in color_lst and cube.sides[1][3] in color_lst):
                cube.movement_parser(
                    [Move.right_prime, Move.down_prime, Move.right, Move.down, Move.front, Move.down, Move.front_prime])
                moves_played += " r' d' r d f d f'"
            if (cube.sides[0][3] != cube.sides[0][4] or cube.sides[3][5] != cube.sides[3][4]) and \
                    (cube.sides[0][3] in color_lst and cube.sides[3][5] in color_lst):
                cube.movement_parser(
                    [Move.left, Move.down, Move.left_prime, Move.down_prime, Move.front_prime, Move.down_prime,
                     Move.front])
                moves_played += " l d l' d' f' d' f"
            cube.turn_left(2)
            moves_played += " y' y'"


def solve(cube: Cube, watch=False):
    color = 0
    while cube.sides[1].count(cube.sides[1][4]) != 9 or \
            cube.sides[0].count(cube.sides[0][4]) != 9 or \
            cube.sides[5].count(cube.sides[5][4]) != 9 or \
            cube.sides[2].count(cube.sides[2][4]) != 9 or \
            cube.sides[3].count(cube.sides[3][4]) != 9:

        cube.turn_down(2)
        while cube.sides[2].count(cube.sides[2][4]) != 9:
            #  creates cross - tested OK
            while not (
                    cube.sides[2][1] == cube.sides[2][4] == cube.sides[2][3] ==
                    cube.sides[2][5] == cube.sides[2][7]):
                if cube.sides[2][1] != ColourType.yellow and cube.sides[2][3] != ColourType.yellow and \
                        cube.sides[2][5] != ColourType.yellow and cube.sides[2][7] != ColourType.yellow:
                    cube.movement_parser(
                        [Move.front, Move.up, Move.right, Move.up_prime, Move.right_prime, Move.front_prime])

                if (cube.sides[2][5] == ColourType.yellow and cube.sides[2][3] == ColourType.yellow) or \
                        (cube.sides[2][1] == ColourType.yellow and cube.sides[2][7] == ColourType.yellow):
                    while cube.sides[2][7] != ColourType.yellow:
                        cube.up()
                    cube.movement_parser(
                        [Move.front, Move.up, Move.right, Move.up_prime, Move.right_prime, Move.front_prime])

                if (cube.sides[2][1] == ColourType.yellow and cube.sides[2][3] == ColourType.yellow) or \
                        (cube.sides[2][1] == ColourType.yellow and cube.sides[2][5] == ColourType.yellow) or \
                        (cube.sides[2][5] == ColourType.yellow and cube.sides[2][7] == ColourType.yellow) or \
                        (cube.sides[2][3] == ColourType.yellow and cube.sides[2][7] == ColourType.yellow):
                    while cube.sides[2][1] != ColourType.yellow or cube.sides[2][3] != ColourType.yellow:
                        cube.up()
                    cube.movement_parser(
                        [Move.front, Move.up, Move.right, Move.up_prime, Move.right_prime, Move.front_prime])
            #  end of cross section
            #  start of filling yellow - not tested - doesnt work
            print(cube.sides[2])
            while cube.sides[2].count(cube.sides[2][4]) != 6:
                while cube.sides[3][2] != ColourType.yellow:
                    print(cube)
                    cube.up()
                cube.movement_parser(
                    [Move.right, Move.up, Move.right_prime, Move.up, Move.right, Move.up, Move.up, Move.right_prime])
            while cube.sides[2].count(cube.sides[2][4]) == 6:
                while cube.sides[2][6] != ColourType.yellow:
                    cube.up()
                cube.movement_parser(
                    [Move.right, Move.up, Move.right_prime, Move.up, Move.right, Move.up, Move.up, Move.right_prime])
            #  end of filling stage
        print(cube)
        print(cube.count_corners())
        while cube.sides[1].count(cube.sides[1][4]) != 9 or \
                cube.sides[0].count(cube.sides[0][4]) != 9 or \
                cube.sides[5].count(cube.sides[5][4]) != 9 or \
                cube.sides[2].count(cube.sides[2][4]) != 9 or \
                cube.sides[3].count(cube.sides[3][4]) != 9:
            count_corners = cube.count_corners()
            if count_corners == 0 or count_corners == 1:
                if count_corners == 0:
                    for side in cube.sides[0], cube.sides[1], cube.sides[3], cube.sides[5]:
                        if side.count(side[4]) == 9:
                            while not (cube.sides[3][0] == cube.sides[3][2] == cube.sides[3][1]):
                                cube.turn_left()
                if count_corners == 1:
                    for side in cube.sides[0], cube.sides[1], cube.sides[3], cube.sides[5]:
                        if side[0] == side[2] and side[0] != side[1]:
                            color = side[0]
                    for side in cube.sides[0], cube.sides[1], cube.sides[3], cube.sides[5]:
                        if side[4] == color:
                            true_side = side
                    while true_side[4] != true_side[0] or true_side[4] != true_side[2]:
                        print(color)
                        cube.up()
                    while cube.sides[3][0] != cube.sides[3][2]:
                        cube.turn_left()
                        print(cube)
                cube.movement_parser(
                    [Move.left_prime, Move.up, Move.right, Move.up_prime, Move.left, Move.up, Move.up, Move.right_prime,
                     Move.up, Move.right, Move.up, Move.up, Move.right_prime])
                count_corners = cube.count_corners()
            '''print(cube)
            count_corners = cube.count_corners()
            print(count_corners)'''
            if count_corners == 4:
                if cube.sides[0][2] == cube.sides[1][4]:
                    cube.movement_parser(
                        [Move.front, Move.front, Move.up_prime, Move.right_prime, Move.left, Move.front, Move.front,
                         Move.left_prime, Move.right_prime, Move.up_prime, Move.front, Move.front])
                else:
                    cube.movement_parser(
                        [Move.front, Move.front, Move.up, Move.right_prime, Move.left, Move.front, Move.front,
                         Move.left_prime, Move.right, Move.up, Move.front, Move.front])
                count_corners = cube.count_corners()
            if count_corners == 3:
                while cube.sides[5].count(cube.sides[5][4]) != 9:
                    cube.turn_left()
                if cube.sides[0][2] == cube.sides[1][4]:
                    cube.movement_parser(
                        [Move.front, Move.front, Move.up_prime, Move.right_prime, Move.left, Move.front, Move.front,
                         Move.left_prime, Move.right_prime, Move.up_prime, Move.front, Move.front])
                else:
                    cube.movement_parser(
                        [Move.front, Move.front, Move.up, Move.right_prime, Move.left, Move.front, Move.front,
                         Move.left_prime, Move.right, Move.up, Move.front, Move.front])

        """side_piece_key = {1: 0, 3: 3, 5: 1, 7: 5}
        w_side_piece_key = {1: 5, 3: 3, 5: 1, 7: 0}
        i = 0
        while cube.sides[2][4] != "white" and i < 4:
            cube.turn_right()
            i += 1
        i = 0
        while cube.sides[2][4] != "white" and i < 4:
            cube.turn_up()
            i += 1
        whites = []
        for index, side in enumerate(cube.sides):
            for jdex, colour in enumerate(side):
                if colour == "white":
                    whites.append([index, jdex])
        white = [-1, -1]
        i = 0
        while i < 9 and (white[0] != 2 or white[1] % 2 != 0):
            white = whites[i]
            i += 1
        if white[0] == 2 and white[1] % 2 != 0:
            while cube.sides[w_side_piece_key[white[1]]][1] != cube.sides[w_side_piece_key[white[1]]][4]:
                cube.up()
        white_bottom = []
        for coordinate in whites:
            if coordinate[0] == 4 and coordinate[1] % 2 != 0:
                white_bottom.append(coordinate[1])
        if white_bottom:
            for index in white_bottom:
                if cube.sides[side_piece_key[index]][7] == cube.sides[side_piece_key[index]][4]:
                    cube.front(2)
                else:
                    while cube.sides[side_piece_key[index]][7] != cube.sides[side_piece_key[index]][4]:
                        cube.down()
        else:
            whites = []
            for index, side in enumerate(cube.sides):
                for jdex, colour in enumerate(side):
                    if colour == "white":
                        whites.append([index, jdex])
            wrong_whites = []
            for white1 in whites:
                if white1[0] != 2 and white1[1] % 2 != 0:
                    wrong_whites.append(white1)
            print(wrong_whites)
            for white in wrong_whites:
                pass"""
