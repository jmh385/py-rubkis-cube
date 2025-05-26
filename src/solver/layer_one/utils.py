from typing import List, Tuple

from common.color_type_enum import ColourType
from common.move_enum import Move
from cube.cube import Cube
from cube.cube_exception import CubeException
from solver.layer_one.white_cross import does_side_data_match_side_index
from solver.side_consts import side_order, none_side_data
from solver.side_data import SideData


def get_face_color(cube: Cube, face: Tuple[int, int]) -> ColourType:
    return cube.sides[face[0]][face[1]]


def white_side_up(cube: Cube) -> List[Move]:
    moves = []
    if cube.sides[0][4] == ColourType.white:
        return moves
    for i in range(4):
        cube.turn_left()
        moves.append(Move.turn_left)
        if cube.sides[0][4] == ColourType.white:
            return moves
    for i in range(4):
        cube.turn_down()
        moves.append(Move.turn_down)
        if cube.sides[0][4] == ColourType.white:
            return moves
    raise CubeException(cube, "White side could not be found")


def check_alignment(cube: Cube) -> bool:
    return any(cube.sides[index][4] == sideData.colour_type for index, sideData in enumerate(side_order, 1))


def align_sides(cube: Cube) -> List[Move]:
    moves: List[Move] = []
    if cube.sides[0][4] != ColourType.white:
        raise CubeException(cube, "White side is not on top")

    if check_alignment(cube):
        return moves

    for i in range(4):
        cube.turn_front()
        moves.append(Move.turn_front)
        if check_alignment(cube):
            return moves
    raise CubeException(cube, "could not align sides")


def generate_most_matching(cube: Cube) -> List[Move]:
    moves: List[Move] = []
    best_turn = 0
    best_count = 0
    for i in range(4):
        moves.extend(cube.front())
        count = sum(1 for index, side_data in enumerate(side_order, 1) if
                    cube.sides[0][side_data.front_cross_index] == ColourType.white
                    and cube.sides[index][side_data.side_front_middle_index] == side_data.colour_type)
        if count > best_count:
            best_turn = i + 1
            best_count = count
    moves.extend(cube.front(best_turn))
    return moves

def get_corner_colours(cube: Cube, corner: List[Tuple[int, int]]) -> Tuple[ColourType, ColourType, ColourType]:
    side_index_1, face_index_1 = corner[0]
    side_index_2, face_index_2 = corner[1]
    side_index_3, face_index_3 = corner[2]

    return cube.sides[side_index_1][face_index_1], cube.sides[side_index_2][face_index_2], cube.sides[side_index_3][
        face_index_3]

def get_side_data_by_side_index(side_index: int) -> SideData:
    for side_data in side_order:
        if does_side_data_match_side_index(side_data, side_index):
            return side_data

    return none_side_data


def movement_until_corner_aligns(cube: Cube,
                                 movement_sequence: List[Move],
                                 corner: List[Tuple[int, int]],
                                 expected_colours: List[ColourType],
                                 limit=4) -> List[Move]:
    def compare_colours(colours_1: List[ColourType], colours_2: List[ColourType]) -> bool:
        return sorted(colours_1) == sorted(colours_2)

    moves: List[Move] = []
    while limit > 0 and not compare_colours(list(get_corner_colours(cube, corner)), expected_colours):
        moves.extend(cube.movement_parser(movement_sequence))
        limit -= 1
    return moves

def is_colour_is_aligned(cube: Cube, side_data: SideData) -> bool:
    return (cube.sides[0][side_data.front_cross_index] == ColourType.white
            and cube.sides[side_data.side_index][side_data.side_front_middle_index] == side_data.colour_type)
