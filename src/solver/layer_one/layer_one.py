from copy import deepcopy
from typing import List

from common.move_enum import Move
from cube.cube import Cube
from solver.layer_one.utils import white_side_up, align_sides
from solver.layer_one.white_corners import white_corners
from solver.layer_one.white_cross import white_cross


def layer_one(real_cube: Cube, debug: bool = False) -> List[Move]:
    cube: Cube = deepcopy(real_cube) if not debug else real_cube
    moves: List[Move] = []
    moves.extend(white_side_up(cube))
    moves.extend(align_sides(cube))
    moves.extend(white_cross(cube))
    moves.extend(white_corners(cube))
    return moves
