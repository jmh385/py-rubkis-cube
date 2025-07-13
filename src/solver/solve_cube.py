from copy import deepcopy
from typing import List

from common.move_enum import Move
from cube.cube import Cube
from solver.layer_one.layer_one import layer_one
from solver.layer_three.layer_three import layer_three
from solver.layer_two.layer_two import layer_two


def solve_cube(real_cube: Cube, debug=False) -> List[Move]:
    cube: Cube = deepcopy(real_cube) if not debug else real_cube
    moves: List[Move] = []
    moves.extend(layer_one(cube, True))
    moves.extend(layer_two(cube, True))
    moves.extend(layer_three(cube, True))
    return moves