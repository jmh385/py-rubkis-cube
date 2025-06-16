from common.color_type_enum import ColourType
from cube.cube import Cube


def verify_layer_one_is_solved(cube: Cube) -> bool:
    all_side_2_is_white = all(colour == ColourType.white for colour in cube.sides[2])
    all_sides_are_fulfilled = all(all(cube.sides[side_index][face_index] == cube.sides[side_index][4]
                                       for face_index in range(3))
                                   for side_index in [0, 1, 3, 5])
    return all_side_2_is_white and all_sides_are_fulfilled
