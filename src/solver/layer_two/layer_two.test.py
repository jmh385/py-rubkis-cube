import unittest

from common.color_type_enum import ColourType
from cube.cube import Cube
from solver.layer_one.layer_one import layer_one
from solver.layer_two.layer_two import layer_two


def is_layer_two_solved(cube: Cube):
    all_white = all(colour == ColourType.white for colour in cube.sides[2])
    all_sides = all(all(colour == cube.sides[side_index][4]
                        for colour in cube.sides[side_index][0:6]) for side_index in [0, 1, 3, 5])

    return all_sides and all_white


class TestLayerTwo(unittest.TestCase):
    def test_layer_two(self):
        cube = Cube()
        for i in range(1000):
            cube.randomise()
            layer_one(cube, True)
            print(f"cube before:\n{cube.sides}")
            layer_two(cube, True)

            print(f"cube after:\n{cube.sides}")
            print(i)
            self.assertTrue(is_layer_two_solved(cube))


unittest.main()
