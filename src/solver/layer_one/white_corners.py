import operator
from typing import List, Tuple, Optional

from common.color_type_enum import ColourType
from common.move_enum import Move
from cube.cube import Cube
from cube.cube_exception import CubeException
from solver.layer_one.corner_consts import magic_corner_bottom, white_corner_triples, magic_corner_top, \
    yellow_corner_triples
from solver.layer_one.utils import get_side_data_by_side_index, movement_until_corner_aligns, get_corner_colours, \
    get_face_color
from solver.side_consts import side_order
from solver.side_data import SideData


def is_corner_aligned(cube: Cube, side_data: SideData) -> bool:
    left_side_index = side_data.side_index % 4 + 1
    corner = side_data.left_top_corner
    white_on_top_flag = any(side_index == 0 and cube.sides[side_index][face_index] == ColourType.white
                            for side_index, face_index in corner)
    side_data_appears_flag = any(
        cube.sides[side_index][face_index] == side_data.colour_type for side_index, face_index in corner)
    left_side_index_appears_flag = any(
        cube.sides[side_index][face_index] == get_side_data_by_side_index(left_side_index).colour_type
        for side_index, face_index in corner)
    return white_on_top_flag and side_data_appears_flag and left_side_index_appears_flag


def is_corner_with_white_on_side(cube: Cube, side_data: SideData) -> bool:
    left_side_index = side_data.side_index % 4 + 1

    possible_corners = [corner for corner in yellow_corner_triples
                        if ColourType.white in get_corner_colours(cube, corner)
                        and side_data.colour_type in get_corner_colours(cube, corner)
                        and get_side_data_by_side_index(left_side_index).colour_type
                        in get_corner_colours(cube, corner)]

    if len(possible_corners) == 0:
        return False

    possible_corner = possible_corners[0]

    for side_index, face_index in possible_corner:
        if side_index != 5 and cube.sides[side_index][face_index] == ColourType.white:
            return True
    return False


def detect_corner_with_white_on_side(cube: Cube, side_data: SideData) -> Optional[List[Tuple[int, int]]]:
    left_side_index = side_data.side_index % 4 + 1

    possible_corners = [corner for corner in yellow_corner_triples
                        if ColourType.white in get_corner_colours(cube, corner)
                        and side_data.colour_type in get_corner_colours(cube, corner)
                        and get_side_data_by_side_index(left_side_index).colour_type
                        in get_corner_colours(cube, corner)]

    return possible_corners[0]


def save_corner_with_white_on_side(cube: Cube, side_data: SideData) -> List[Move]:
    moves: List[Move] = []
    limit = 5
    while not is_corner_correctly_aligned_for_solving(cube, side_data) and limit > 0:
        moves.extend(cube.back())
        limit -= 1

    if limit == 0:
        raise CubeException(cube, "could not get corner piece aligned correctly")

    return moves


def is_corner_correctly_aligned_for_solving(cube: Cube, side_data: SideData) -> bool:
    left_side_index = side_data.side_index % 4 + 1
    possible_corners = [corner for corner in yellow_corner_triples
                        if ColourType.white in get_corner_colours(cube, corner)
                        and side_data.colour_type in get_corner_colours(cube, corner)
                        and get_side_data_by_side_index(left_side_index).colour_type
                        in get_corner_colours(cube, corner)]

    if len(possible_corners) == 0:
        return False

    possible_corner = possible_corners[0]
    side_data_index_face = [face for face in possible_corner
                            if cube.sides[face[0]][face[1]] == side_data.colour_type][0]
    left_side_index_face = [face for face in possible_corner
                            if cube.sides[face[0]][face[1]] == get_side_data_by_side_index(
            left_side_index).colour_type][0]

    return operator.xor(side_data_index_face[0] == side_data.side_index,
                        left_side_index_face[0] == get_side_data_by_side_index(
                            left_side_index).side_index)


def detect_corner_correctly_aligned(cube: Cube, side_data: SideData) -> Optional[List[Tuple[int, int]]]:
    left_side_index = side_data.side_index % 4 + 1

    possible_corners = [corner for corner in yellow_corner_triples
                        if ColourType.white in get_corner_colours(cube, corner)
                        and side_data.colour_type in get_corner_colours(cube, corner)
                        and get_side_data_by_side_index(left_side_index).colour_type
                        in get_corner_colours(cube, corner)]

    return possible_corners[0]


def solve_corner_correctly_aligned(cube: Cube, side_data: SideData) -> List[Move]:
    moves: List[Move] = []
    corner = detect_corner_correctly_aligned(cube, side_data)
    if not corner:
        raise CubeException(cube, "if_correctly_aligned miss fired")

    moves.extend(cube.turn_z(side_data.turns_from_top))
    white_side_corner_face = [face for face in magic_corner_bottom
                              if cube.sides[face[0]][face[1]] == ColourType.white][0]
    [side_index, _] = white_side_corner_face
    if side_index == 2:
        moves.extend(cube.movement_parser([Move.back_prime, Move.left_prime, Move.back, Move.left]))
    else:
        moves.extend(cube.movement_parser([Move.left_prime, Move.back_prime, Move.left]))
    moves.extend(cube.turn_z_prime(side_data.turns_from_top))

    return moves


def is_white_face_of_corner_on_back_side(cube: Cube, side_data: SideData) -> bool:
    left_side_index = side_data.side_index % 4 + 1

    for corner in yellow_corner_triples:
        face_index_at_side_index_5 = [face_index for side_index, face_index in corner if side_index == 5][0]
        side_data_appears_flag = any(
            cube.sides[side_index][face_index] == side_data.colour_type for side_index, face_index in corner)
        left_side_index_appears_flag = any(
            cube.sides[side_index][face_index] == get_side_data_by_side_index(left_side_index).colour_type
            for side_index, face_index in corner)

        if left_side_index_appears_flag and side_data_appears_flag and cube.sides[5][
            face_index_at_side_index_5] == ColourType.white:
            return True
    return False


def detect_white_face_of_corner_on_back_side(cube: Cube, side_data: SideData) -> List[Tuple[int, int]]:
    left_side_index = side_data.side_index % 4 + 1

    for corner in yellow_corner_triples:
        face_index_at_side_index_5 = [face_index for side_index, face_index in corner if side_index == 5][0]
        side_data_appears_flag = any(
            cube.sides[side_index][face_index] == side_data.colour_type for side_index, face_index in corner)
        left_side_index_appears_flag = any(
            cube.sides[side_index][face_index] == get_side_data_by_side_index(left_side_index).colour_type
            for side_index, face_index in corner)

        if left_side_index_appears_flag and side_data_appears_flag and cube.sides[5][
            face_index_at_side_index_5] == ColourType.white:
            return corner
    raise CubeException(cube, "is_white_face_of_corner_on_back_side miss fired")


def save_white_face_of_corner_on_back_side(cube: Cube, side_data: SideData) -> List[Move]:
    moves: List[Move] = []
    corner = detect_white_face_of_corner_on_back_side(cube, side_data)
    moves.extend(movement_until_corner_aligns(cube,
                                              [Move.back],
                                              side_data.left_bottom_corner,
                                              list(get_corner_colours(cube, corner))))

    moves.extend(cube.turn_z(side_data.turns_from_top))
    moves.extend(cube.movement_parser([Move.left_prime, Move.back, Move.left]))
    moves.extend(cube.turn_z_prime(side_data.turns_from_top))

    return moves


def is_corner_on_top_but_mismatched(cube, side_data: SideData) -> bool:
    left_side_index = side_data.side_index % 4 + 1

    for corner in white_corner_triples:
        side_data_appears_flag = any(
            cube.sides[side_index][face_index] == side_data.colour_type for side_index, face_index in corner)
        left_side_index_appears_flag = any(
            cube.sides[side_index][face_index] == get_side_data_by_side_index(left_side_index).colour_type
            for side_index, face_index in corner)
        white_appears_flag = any(
            cube.sides[side_index][face_index] == ColourType.white
            for side_index, face_index in corner)
        if side_data_appears_flag and left_side_index_appears_flag and white_appears_flag:
            return True
    return False


def detect_corner_on_top_but_mismatched(cube, side_data: SideData) -> List[Tuple[int, int]]:
    left_side_index = side_data.side_index % 4 + 1

    for corner in white_corner_triples:
        side_data_appears_flag = any(
            cube.sides[side_index][face_index] == side_data.colour_type for side_index, face_index in corner)
        left_side_index_appears_flag = any(
            cube.sides[side_index][face_index] == get_side_data_by_side_index(left_side_index).colour_type
            for side_index, face_index in corner)
        white_appears_flag = any(
            cube.sides[side_index][face_index] == ColourType.white
            for side_index, face_index in corner)
        if side_data_appears_flag and left_side_index_appears_flag and white_appears_flag:
            return corner
    raise CubeException(cube, "is_corner_on_top_but_mismatched miss fired")


def save_corner_on_top_but_mismatched(cube, side_data: SideData) -> List[Move]:
    moves: List[Move] = []
    corner = detect_corner_on_top_but_mismatched(cube, side_data)
    moves_to_align_corner = movement_until_corner_aligns(cube,
                                                         [Move.turn_z],
                                                         magic_corner_top,
                                                         list(get_corner_colours(cube, corner)))
    moves.extend(moves_to_align_corner)
    top_side_face_magic_corner = [face for face in magic_corner_top if face[0] == 0][0]
    front_side_face_magic_corner = [face for face in magic_corner_top if face[0] == 2][0]
    side_side_face_magic_corner = [face for face in magic_corner_top if face[0] == 3][0]

    if get_face_color(cube, top_side_face_magic_corner) == ColourType.white:
        moves.extend(cube.movement_parser([Move.left_prime, Move.back_prime, Move.left]))
    elif get_face_color(cube, side_side_face_magic_corner) == ColourType.white:
        moves.extend(cube.movement_parser([Move.left_prime, Move.back, Move.back, Move.left]))
    elif get_face_color(cube, front_side_face_magic_corner) == ColourType.white:
        moves.extend(cube.movement_parser([Move.up, Move.back, Move.up_prime]))

    moves.extend(cube.turn_z_prime(len(moves_to_align_corner)))
    return moves


def white_corners(cube: Cube) -> List[Move]:
    moves: List[Move] = []
    for side_data in side_order:
        if is_corner_aligned(cube, side_data):
            continue
        else:
            if is_corner_on_top_but_mismatched(cube, side_data):
                moves.extend(save_corner_on_top_but_mismatched(cube, side_data))
            if is_white_face_of_corner_on_back_side(cube, side_data):
                moves.extend(save_white_face_of_corner_on_back_side(cube, side_data))
            if is_corner_with_white_on_side(cube, side_data):
                moves.extend(save_corner_with_white_on_side(cube, side_data))
            if is_corner_correctly_aligned_for_solving(cube, side_data):
                moves.extend(solve_corner_correctly_aligned(cube, side_data))

    return moves
