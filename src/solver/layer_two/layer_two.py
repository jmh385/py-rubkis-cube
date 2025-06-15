from copy import deepcopy
from typing import List, Tuple

from common.color_type_enum import ColourType
from common.move_enum import Move
from cube.cube import Cube
from cube.cube_exception import CubeException
from cube.edge_consts import edge_mappings

non_first_layer_edges: List[Tuple[Tuple[int, int], Tuple[int, int]]] = [edge
                                                                        for edge
                                                                        in edge_mappings.items()
                                                                        if edge[0][0] != 2 and edge[1][0] != 2]
edge_combos: List[Tuple[ColourType, ColourType]] = [(ColourType.orange, ColourType.blue),
                                                    (ColourType.orange, ColourType.green),
                                                    (ColourType.red, ColourType.green),
                                                    (ColourType.red, ColourType.blue)]


def solve_left_destroy_right(cube: Cube) -> List[Move]:
    return cube.movement_parser([Move.left_prime,
                                 Move.up_prime,
                                 Move.front,
                                 Move.up,
                                 Move.front,
                                 Move.left,
                                 Move.front_prime])


def solve_left_save_right(cube: Cube) -> List[Move]:
    return cube.movement_parser([Move.right,
                                 Move.up,
                                 Move.front,
                                 Move.up_prime,
                                 Move.right_prime,
                                 Move.front,
                                 Move.down_prime,
                                 Move.front_prime])


def solve_right_destroy_left(cube: Cube) -> List[Move]:
    return cube.movement_parser([Move.right,
                                 Move.up,
                                 Move.front_prime,
                                 Move.up_prime,
                                 Move.front_prime,
                                 Move.right_prime,
                                 Move.front])


def solve_right_save_left(cube: Cube) -> List[Move]:
    return cube.movement_parser([Move.left_prime,
                                 Move.up_prime,
                                 Move.front_prime,
                                 Move.up,
                                 Move.left,
                                 Move.front_prime,
                                 Move.down,
                                 Move.front])


def extract_left(cube: Cube) -> List[Move]:
    return cube.movement_parser([
        Move.left,
        Move.down,
        Move.left_prime,
        Move.down_prime,
        Move.front_prime,
        Move.down_prime,
        Move.front
    ])


def extract_right(cube: Cube) -> List[Move]:
    return cube.movement_parser([
        Move.right_prime,
        Move.down_prime,
        Move.right,
        Move.down,
        Move.front,
        Move.down,
        Move.front_prime
    ])


def colours_on_side(cube: Cube) -> List[Move]:
    moves = []
    if cube.sides[2][4] == ColourType.white and cube.sides[4][4] == ColourType.yellow:
        return moves
    for i in range(4):
        cube.turn_x()
        if cube.sides[2][4] == ColourType.white and cube.sides[4][4] == ColourType.yellow:
            return moves
    for i in range(4):
        cube.turn_y_prime()
        if cube.sides[2][4] == ColourType.white and cube.sides[4][4] == ColourType.yellow:
            return moves
    raise CubeException(cube, "could not align colours to the main band")


def is_left_aligned(cube: Cube) -> bool:
    # the side we are checking is always at 0
    return (cube.sides[0][4] == cube.sides[0][3]
            and cube.sides[3][4] == cube.sides[3][5])


def is_right_aligned(cube: Cube) -> bool:
    # the side we are checking is always at 0
    return (cube.sides[0][4] == cube.sides[0][5]
            and cube.sides[1][4] == cube.sides[1][3])


def is_combo_solved(cube: Cube, edge_combo: Tuple[ColourType, ColourType]) -> bool:
    is_solved = False
    for _ in range(4):
        are_colours_correct = all(colour in edge_combo for colour in [cube.sides[0][4],
                                                                      cube.sides[0][3],
                                                                      cube.sides[3][4],
                                                                      cube.sides[3][5]])
        are_edges_matching = (cube.sides[0][4] == cube.sides[0][3]
                              and cube.sides[3][4] == cube.sides[3][5])
        if are_colours_correct and are_edges_matching:
            is_solved = True
        cube.turn_y()
    return is_solved


def is_left_edge_backwards(cube: Cube, edge_combo: Tuple[ColourType, ColourType]) -> bool:
    are_colours_matching = all(side_colour in edge_combo for side_colour in [cube.sides[0][3], cube.sides[3][5]])
    are_sides_not_aligned = cube.sides[0][4] != cube.sides[0][3] or cube.sides[3][4] != cube.sides[3][5]
    return are_colours_matching and are_sides_not_aligned


def is_right_edge_backwards(cube: Cube, edge_combo: Tuple[ColourType, ColourType]) -> bool:
    are_colours_matching = all(side_colour in edge_combo for side_colour in [cube.sides[0][5], cube.sides[1][3]])
    are_sides_not_aligned = cube.sides[0][4] != cube.sides[0][5] or cube.sides[1][4] != cube.sides[1][3]
    return are_colours_matching and are_sides_not_aligned


def align_bottom_edge(cube: Cube, edge_combo: Tuple[ColourType, ColourType]) -> List[Move]:
    moves: List[Move] = []
    colour_1, colour_2 = edge_combo
    for _ in range(4):
        if (cube.sides[0][7] == colour_1 and cube.sides[4][1] == colour_2)\
                or (cube.sides[0][7] == colour_2 and cube.sides[4][1] == colour_1):
            return moves
        moves.extend(cube.down())
    raise CubeException(cube, "Something went horribly wrong")


def extract_edge(cube: Cube,
                 edge_combo: Tuple[ColourType, ColourType]) -> List[Move]:
    moves: List[Move] = []
    for _ in range(4):
        if is_right_edge_backwards(cube, edge_combo):
            moves.extend(extract_right(cube))
            return moves
        if is_left_edge_backwards(cube, edge_combo):
            moves.extend(extract_left(cube))
            return moves
        moves.extend(cube.turn_y())

    return moves


def solve_side_edges(cube: Cube) -> List[Move]:
    moves: List[Move] = []
    for edge_combo in edge_combos:
        if is_combo_solved(cube, edge_combo):
            continue
        moves.extend(extract_edge(cube, edge_combo))
        moves.extend(align_bottom_edge(cube, edge_combo))
        for _ in range(4):
            main_colour = cube.sides[0][4]
            if main_colour in edge_combo and main_colour == cube.sides[0][7]:
                if cube.sides[4][1] == cube.sides[1][4] and cube.sides[1][4] in edge_combo:
                    if is_left_aligned(cube):
                        moves.extend(solve_right_save_left(cube))
                    else:
                        moves.extend(solve_right_destroy_left(cube))
                if cube.sides[4][1] == cube.sides[3][4] and cube.sides[3][4] in edge_combo:
                    if is_right_aligned(cube):
                        moves.extend(solve_left_save_right(cube))
                    else:
                        moves.extend(solve_left_destroy_right(cube))
            moves.extend(cube.turn_y())
            moves.extend(cube.down())

    return moves


def layer_two(real_cube: Cube, debug: bool = False) -> List[Move]:
    cube: Cube = deepcopy(real_cube) if not debug else real_cube
    moves: List[Move] = []
    moves.extend(colours_on_side(cube))
    moves.extend(solve_side_edges(cube))
    return moves
