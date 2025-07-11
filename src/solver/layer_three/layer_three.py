from copy import deepcopy
from typing import List

from common.color_type_enum import ColourType
from common.move_enum import Move
from cube.cube import Cube
from cube.cube_exception import CubeException
from solver.layer_three.verify_layer_two_is_solved import verify_layer_two_is_solved


def yellow_side_up(cube: Cube) -> List[Move]:
    moves = []
    if cube.sides[2][4] == ColourType.yellow:
        return moves
    for i in range(4):
        cube.turn_y()
        moves.append(Move.turn_y_prime)
        if cube.sides[2][4] == ColourType.yellow:
            return moves
    for i in range(4):
        cube.turn_x_prime()
        moves.append(Move.turn_x_prime)
        if cube.sides[2][4] == ColourType.yellow:
            return moves
    raise CubeException(cube, "Yellow side could not be found")


def phase_one_algorithm(cube: Cube) -> List[Move]:
    return cube.movement_parser([
        Move.front,
        Move.up,
        Move.right,
        Move.up_prime,
        Move.right_prime,
        Move.front_prime
    ])


def phase_two_algorithm(cube: Cube) -> List[Move]:
    return cube.movement_parser(
        [Move.right, Move.up, Move.right_prime, Move.up, Move.right, Move.up, Move.up, Move.right_prime]
    )


def phase_three_algorithm(cube: Cube) -> List[Move]:
    return cube.movement_parser(
        [Move.left_prime, Move.up, Move.right, Move.up_prime, Move.left, Move.up, Move.up, Move.right_prime,
         Move.up, Move.right, Move.up, Move.up, Move.right_prime]
    )


def misaligned_sides_shift_right_algorithm(cube: Cube) -> List[Move]:
    return cube.movement_parser(
        [Move.front, Move.front, Move.up_prime, Move.right_prime, Move.left, Move.front, Move.front,
         Move.left_prime, Move.right, Move.up_prime, Move.front, Move.front]
    )


def misaligned_sides_shift_left_algorithm(cube: Cube) -> List[Move]:
    return cube.movement_parser(
        [Move.front, Move.front, Move.up, Move.right_prime, Move.left, Move.front, Move.front,
         Move.left_prime, Move.right, Move.up, Move.front, Move.front]
    )


def is_phase_one(cube: Cube) -> bool:
    return not all(face == ColourType.yellow for face in cube.sides[2][1:8:2])


def align_phase_one(cube: Cube) -> List[Move]:
    moves: List[Move] = []
    if all(face != ColourType.yellow for face in cube.sides[2][1:8:2]) or (
            cube.sides[2][1] == ColourType.yellow and cube.sides[2][7] == ColourType.yellow):
        return moves
    elif cube.sides[2][3] == ColourType.yellow and cube.sides[2][5] == ColourType.yellow:
        moves.extend(cube.up())
    else:
        i = 0
        while i < 5 and not (cube.sides[2][3] == ColourType.yellow and cube.sides[2][1] == ColourType.yellow):
            moves.extend(cube.up())
            i += 1
        if i == 5:
            raise CubeException(cube, "Could not align L in phase one")
    return moves


def is_phase_two(cube: Cube) -> bool:
    return not is_phase_one(cube) and not all(face == ColourType.yellow for face in cube.sides[2][0:9:2])


def align_phase_two(cube: Cube) -> List[Move]:
    moves: List[Move] = []
    fulfilled_corners = [1 for face in cube.sides[2][0:9:2] if face == ColourType.yellow]
    if len(fulfilled_corners) == 2:
        i = 0
        while i < 5 and not cube.sides[2][6] == ColourType.yellow:
            moves.extend(cube.up())
            i += 1
        if i == 5:
            raise CubeException(cube, "Could not position fish eye in phase two")
    else:
        i = 0
        while i < 5 and not cube.sides[3][2] == ColourType.yellow:
            moves.extend(cube.up())
            i += 1
        if i == 5:
            raise CubeException(cube, "Could not position side yellow in phase two")
    return moves


def is_phase_three(cube: Cube) -> bool:
    return all(face == ColourType.yellow for face in cube.sides[2])


def is_phase_three_side_colour_undefined(cube: Cube) -> bool:
    return is_phase_three(cube) and all(cube.sides[side_index][0] != cube.sides[side_index][2]
                                        for side_index in [0, 1, 3, 5])


def is_single_matched_side(cube: Cube) -> bool:
    sides_mathing_status = [cube.sides[side_index][0] == cube.sides[side_index][2]
                            for side_index in [0, 1, 3, 5]]
    return is_phase_three(cube) and sides_mathing_status.count(True) == 1


def align_single_matched_side(cube: Cube) -> List[Move]:
    moves: List[Move] = []
    i = 0
    while i < 5 and not cube.sides[3][0] == cube.sides[3][2]:
        moves.extend(cube.up())
        i += 1
    if i == 5:
        raise CubeException(cube, "Could not align matched side")
    return moves


def is_fully_matched_sides(cube: Cube) -> bool:
    return is_phase_three(cube) and all(cube.sides[side_index][0] == cube.sides[side_index][2]
                                        for side_index in [0, 1, 3, 5])


def is_no_side_fully_matched(cube: Cube) -> bool:
    return is_fully_matched_sides(cube) and not any(cube.sides[side_index][0] == cube.sides[side_index][2]
                                                    and cube.sides[side_index][1] == cube.sides[side_index][2]
                                                    for side_index in [0, 1, 3, 5])


def align_single_fully_matched_side(cube: Cube) -> List[Move]:
    moves: List[Move] = []
    i = 0
    while i < 5 and not (cube.sides[3][0] == cube.sides[3][2]
    ):
        moves.extend(cube.up())
        i += 1
    if i == 5:
        raise CubeException(cube, "Could not turn coloured side till aligned")
    return moves


def align_fully_matched_sides(cube: Cube) -> List[Move]:
    moves: List[Move] = []
    i = 0
    while i < 5 and not all(cube.sides[side_index][0] == cube.sides[side_index][2]
                            and cube.sides[side_index][2] == cube.sides[side_index][4]
                            for side_index in [0, 1, 3, 5]):
        moves.extend(cube.up())
        i += 1
    if i == 5:
        raise CubeException(cube, "Could not turn all sides till aligned")
    i = 0
    while i < 5 and not (cube.sides[5][0] == cube.sides[5][2]
                         and cube.sides[5][1] == cube.sides[5][2]
                         and cube.sides[5][4] == cube.sides[5][2]
    ):
        moves.extend(cube.turn_y())
        i += 1
    if i == 5:
        raise CubeException(cube, "Could not turn cube to align fully coloured to back")
    return moves


def is_left_shifted(cube: Cube) -> bool:
    return cube.sides[0][1] == cube.sides[3][4]


def is_final_turns(cube: Cube) -> bool:
    return all(cube.sides[side_index][0] == cube.sides[side_index][2]
               and cube.sides[side_index][1] == cube.sides[side_index][2]
               for side_index in [0, 1, 3, 5])


def solve_final_turns(cube: Cube) -> List[Move]:
    moves: List[Move] = []
    i = 0
    while i < 5 and not is_phase_three_complete(cube):
        moves.extend(cube.up())
        i += 1
    if i == 5:
        raise CubeException(cube, "Could not solve cube")
    return moves


def is_phase_three_complete(cube: Cube) -> bool:
    return is_phase_three(cube) and all(all(cube.sides[side_index][face_index] == cube.sides[side_index][4]
                                            for face_index in range(3))
                                        for side_index in [0, 1, 3, 5])


def solve_cube_yellow_side(cube: Cube) -> List[Move]:
    moves: List[Move] = []
    if is_phase_one(cube):
        i = 0
        while i < 5 and not (is_phase_two(cube) or is_phase_three(cube)):
            moves.extend(align_phase_one(cube))
            moves.extend(phase_one_algorithm(cube))
            i += 1
        if i == 5:
            raise CubeException(cube, "could not solve phase one")
    if is_phase_two(cube):
        i = 0
        while i < 10 and not is_phase_three(cube):
            moves.extend(align_phase_two(cube))
            moves.extend(phase_two_algorithm(cube))
            i += 1
        if i == 10:
            raise CubeException(cube, "could not solve phase two")
    if is_phase_three(cube):
        if is_phase_three_side_colour_undefined(cube):
            moves.extend(phase_three_algorithm(cube))
        if is_single_matched_side(cube):
            moves.extend(align_single_fully_matched_side(cube))
            moves.extend(phase_three_algorithm(cube))
        if is_fully_matched_sides(cube) and not is_final_turns(cube):
            if is_no_side_fully_matched(cube):
                moves.extend(misaligned_sides_shift_left_algorithm(cube))
            moves.extend(align_fully_matched_sides(cube))
            if is_left_shifted(cube):
                moves.extend(misaligned_sides_shift_left_algorithm(cube))
            else:
                moves.extend(misaligned_sides_shift_right_algorithm(cube))
        if is_final_turns(cube):
            moves.extend(solve_final_turns(cube))
    return moves


def  layer_three(real_cube: Cube, debug: bool = False) -> List[Move]:
    cube: Cube = deepcopy(real_cube) if not debug else real_cube
    moves: List[Move] = []
    moves.extend(yellow_side_up(cube))
    if not verify_layer_two_is_solved(cube):
        raise CubeException(cube, "tried to invoke third layer solve but second layer was not solved")
    moves.extend(solve_cube_yellow_side(cube))
    return moves
