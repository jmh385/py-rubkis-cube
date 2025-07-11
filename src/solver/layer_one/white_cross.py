from typing import List, Optional

from common.color_type_enum import ColourType
from common.move_enum import Move
from cube.cube import Cube
from cube.cube_exception import CubeException
from cube.edge_consts import edge_mappings, sides_to_bottom_middle, sides_and_bottom_middle_to_side_5, \
    edges_with_white
from solver.layer_one.utils import generate_most_matching, is_colour_is_aligned, does_side_data_match_side_index
from solver.side_consts import side_order
from solver.side_data import SideData


def is_edge_with_white_not_on_back(cube: Cube, side_data: SideData) -> bool:
    return any(
        ((cube.sides[edge_face_1_side][edge_face_1_index] == ColourType.white
          and cube.sides[edge_face_2_side][edge_face_2_index] == side_data.colour_type)

         or (cube.sides[edge_face_1_side][edge_face_1_index] == side_data.colour_type
             and cube.sides[edge_face_2_side][edge_face_2_index] == ColourType.white))

        for (edge_face_1_side, edge_face_1_index), (edge_face_2_side, edge_face_2_index) in edge_mappings.items()
        if edge_face_1_side != 5 and edge_face_2_side != 5 and edge_face_1_side != 0 and edge_face_2_side != 0)


def is_edge_backwards(cube: Cube, side_data: SideData) -> bool:
    return any((cube.sides[side][bottom_middle] == ColourType.white
                and cube.sides[5][sides_and_bottom_middle_to_side_5[(side, bottom_middle)]] == side_data.colour_type)
               for side, bottom_middle in sides_to_bottom_middle)


def is_edge_correct_oriented(cube: Cube, side_data: SideData) -> bool:
    return any((cube.sides[side][bottom_middle] == side_data.colour_type
                and cube.sides[5][sides_and_bottom_middle_to_side_5[(side, bottom_middle)]] == ColourType.white)
               for side, bottom_middle in sides_to_bottom_middle)


def detect_backwards_edge(cube: Cube, side_data: SideData) -> Optional[SideData]:
    for side_index, bottom_middle in sides_to_bottom_middle:
        if (cube.sides[side_index][bottom_middle] == ColourType.white
                and cube.sides[5][
                    sides_and_bottom_middle_to_side_5[(side_index, bottom_middle)]] == side_data.colour_type):
            return [side for side in side_order if does_side_data_match_side_index(side, side_index)][0]
    return None


def backwards_edge_solve(cube: Cube, side_data: SideData) -> List[Move]:
    moves: List[Move] = []
    moves.extend(cube.turn_z(side_data.turns_from_top))
    backwards_piece_side = detect_backwards_edge(cube, side_data)
    if backwards_piece_side:
        moves.extend(cube.back(backwards_piece_side.turns_from_top))

        if cube.sides[2][1] != ColourType.white or cube.sides[5][1] != side_data.colour_type:
            raise CubeException(cube, "Failed to align back correctly")

        moves.extend(cube.movement_parser([Move.up, Move.front, Move.right_prime, Move.front_prime]))
    moves.extend(cube.turn_z_prime(side_data.turns_from_top))
    return moves


def detect_correct_oriented_edge(cube: Cube, side_data: SideData) -> Optional[SideData]:
    for side_index, bottom_middle in sides_to_bottom_middle:
        if (cube.sides[side_index][bottom_middle] == side_data.colour_type
                and cube.sides[5][
                    sides_and_bottom_middle_to_side_5[(side_index, bottom_middle)]] == ColourType.white):
            return [side for side in side_order if does_side_data_match_side_index(side, side_index)][0]
    return None


def correct_oriented_edge_solve(cube: Cube, side_data: SideData) -> List[Move]:
    moves: List[Move] = []
    moves.extend(cube.turn_z(side_data.turns_from_top))
    correct_oriented_edge_side = detect_correct_oriented_edge(cube, side_data)
    if correct_oriented_edge_side:
        moves.extend(cube.back(correct_oriented_edge_side.turns_from_top))

        if cube.sides[5][1] != ColourType.white or cube.sides[2][1] != side_data.colour_type:
            raise CubeException(cube, "Failed to align back correctly")

        moves.extend(cube.up(2))
    moves.extend(cube.turn_z_prime(side_data.turns_from_top))
    return moves


def detect_edge_with_white_not_on_back(cube: Cube, side_data: SideData) -> Optional[SideData]:
    possible_edges = list(
        ((edge_face_1_side, edge_face_1_index), (edge_face_2_side, edge_face_2_index))
        for (edge_face_1_side, edge_face_1_index), (edge_face_2_side, edge_face_2_index) in edge_mappings.items()
        if (edge_face_1_side != 5 and edge_face_2_side != 5 and edge_face_1_side != 0 and edge_face_2_side != 0)
        and ((cube.sides[edge_face_1_side][edge_face_1_index] == ColourType.white
              and cube.sides[edge_face_2_side][edge_face_2_index] == side_data.colour_type)

             or (cube.sides[edge_face_2_side][edge_face_2_index] == ColourType.white
                 and cube.sides[edge_face_1_side][edge_face_1_index] == side_data.colour_type)))
    print(possible_edges)
    res = None
    for i in range(4):
        for possible_edge in possible_edges:
            white_edge = [edge for edge in edges_with_white if
                          edge[0][0] == possible_edge[1][0]]  # find the white side of the edge
            # print(f"white edge: {white_edge}")
            if len(white_edge) > 0 and cube.sides[0][white_edge[0][1][1]] != ColourType.white:
                chosen_side_index, index_on_side = possible_edge[0]
                res = [side for side in side_order if does_side_data_match_side_index(side, chosen_side_index)][0]
        cube.front()
    return res


def edge_with_white_not_on_back_solve(cube: Cube, side_data: SideData) -> List[Move]:
    moves: List[Move] = []
    not_on_back_side = detect_edge_with_white_not_on_back(cube, side_data)
    print(f"bad side: {not_on_back_side}")
    # print(cube.sides[2][4])
    moves.extend(cube.turn_z(not_on_back_side.turns_from_top))
    freeing_moves = turn_front_until_free_over_top(cube)
    moves.extend(freeing_moves)
    if any(
            cube.sides[side_index_1][edge_index_1] == ColourType.white
            and cube.sides[side_index_2][edge_index_2] == side_data.colour_type
            for (side_index_1, edge_index_1), (side_index_2, edge_index_2)
            in [((2, 3), (3, 1)), ((3, 1), (2, 3))]):
        moves.extend(cube.up())
    elif any(cube.sides[side_index_1][edge_index_1] == ColourType.white
             and cube.sides[side_index_2][edge_index_2] == side_data.colour_type
             for (side_index_1, edge_index_1), (side_index_2, edge_index_2)
             in [((2, 5), (1, 1)), ((1, 1), (2, 5))]):
        moves.extend(cube.up_prime())
    else:
        raise CubeException(cube, "Could not find right side")
    moves.extend(cube.front_prime(len(freeing_moves)))
    moves.extend(cube.turn_z_prime(not_on_back_side.turns_from_top))
    return moves


def is_top_side_mistake(cube: Cube, side_data: SideData) -> bool:
    return (
            is_white_on_side_with_colour_on_top(cube, side_data)
            or is_white_on_top_with_side_colour_mismatched(cube, side_data)
    )


def is_white_on_top_with_side_colour_mismatched(cube: Cube, side_data: SideData) -> bool:
    return any(
        cube.sides[edge_face_1_side][edge_face_1_index] == side_data.colour_type
        and cube.sides[edge_face_1_side][4] != side_data.colour_type
        and cube.sides[edge_face_2_side][edge_face_2_index] == ColourType.white

        for (edge_face_1_side, edge_face_1_index), (edge_face_2_side, edge_face_2_index) in
        edge_mappings.items()
        if edge_face_2_side == 0
    )


def is_white_on_side_with_colour_on_top(cube: Cube, side_data: SideData) -> bool:
    return any(
        cube.sides[edge_face_1_side][edge_face_1_index] == ColourType.white
        and cube.sides[edge_face_2_side][edge_face_2_index] == side_data.colour_type
        for (edge_face_1_side, edge_face_1_index), (edge_face_2_side, edge_face_2_index) in edge_mappings.items()
        if edge_face_2_side == 0
    )


def detect_white_on_side_with_colour_on_top(cube: Cube, side_data: SideData) -> Optional[SideData]:
    possible_edges = list(
        ((edge_face_1_side, edge_face_1_index), (edge_face_2_side, edge_face_2_index))
        for (edge_face_1_side, edge_face_1_index), (edge_face_2_side, edge_face_2_index) in edge_mappings.items()
        if edge_face_2_side == 0
        and cube.sides[edge_face_1_side][edge_face_1_index] == ColourType.white  # side is white
        and cube.sides[edge_face_2_side][edge_face_2_index] == side_data.colour_type  # top is a colour
    )
    if len(possible_edges) > 0:
        ((incorrect_white_side, _), _) = possible_edges[0]
        return [side for side in side_order if does_side_data_match_side_index(side, incorrect_white_side)][0]
    return None


def detect_white_on_top_with_side_colour_mismatched(cube: Cube, side_data: SideData) -> Optional[SideData]:
    possible_edges = list(
        ((edge_face_1_side, edge_face_1_index), (edge_face_2_side, edge_face_2_index))
        for (edge_face_1_side, edge_face_1_index), (edge_face_2_side, edge_face_2_index) in edge_mappings.items()
        if edge_face_2_side == 0
        and cube.sides[edge_face_1_side][edge_face_1_index] == side_data.colour_type
        and cube.sides[edge_face_1_side][4] != side_data.colour_type  # side colour is not matched with expected colour
        and cube.sides[edge_face_2_side][edge_face_2_index] == ColourType.white  # top is white
    )
    if len(possible_edges) > 0:
        ((incorrect_white_side, _), _) = possible_edges[0]
        return [side for side in side_order if does_side_data_match_side_index(side, incorrect_white_side)][0]
    return None


def white_on_top_with_side_colour_mismatched_solve(cube: Cube, side_data: SideData) -> List[Move]:
    moves: List[Move] = []
    white_on_top_with_side_colour_mismatched = detect_white_on_top_with_side_colour_mismatched(cube, side_data)
    moves.extend(cube.turn_z(white_on_top_with_side_colour_mismatched.turns_from_top))
    moves.extend(cube.up(2))  # 2 turns to make it solvable
    moves.extend(cube.turn_z_prime(white_on_top_with_side_colour_mismatched.turns_from_top))
    return moves


def white_on_side_with_colour_on_top_solve(cube: Cube, side_data: SideData) -> List[Move]:
    moves: List[Move] = []
    white_on_side_with_colour_on_top = detect_white_on_side_with_colour_on_top(cube, side_data)
    moves.extend(cube.turn_z(white_on_side_with_colour_on_top.turns_from_top))
    moves.extend(cube.up(2))  # 2 turns to make it solvable
    moves.extend(cube.turn_z_prime(white_on_side_with_colour_on_top.turns_from_top))
    return moves


def turn_front_until_free_over_top(cube: Cube) -> List[Move]:
    moves: List[Move] = []
    for i in range(4):
        if cube.sides[0][1] != ColourType.white:
            return moves
        moves.extend(cube.front())
    return moves


def white_cross(cube: Cube) -> List[Move]:
    moves: List[Move] = []
    if sum(1 for i in range(1, 8, 2) if cube.sides[0][i] == ColourType.white) > 0:
        moves.extend(generate_most_matching(cube))
    for side_data in side_order:
        if is_colour_is_aligned(cube, side_data):
            print(f"color {side_data} is aligned")
            continue
        else:
            # white side edges
            if is_white_on_top_with_side_colour_mismatched(cube, side_data):
                moves.extend(white_on_top_with_side_colour_mismatched_solve(cube, side_data))
            if is_white_on_side_with_colour_on_top(cube, side_data):
                moves.extend(white_on_side_with_colour_on_top_solve(cube, side_data))
            # colour side edges
            if is_edge_with_white_not_on_back(cube, side_data):
                moves.extend(edge_with_white_not_on_back_solve(cube, side_data))
            # yellow side edges
            if is_edge_backwards(cube, side_data):
                moves.extend(backwards_edge_solve(cube, side_data))
            if is_edge_correct_oriented(cube, side_data):
                moves.extend(correct_oriented_edge_solve(cube, side_data))
    return moves
