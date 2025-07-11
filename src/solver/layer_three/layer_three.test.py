import unittest

from cube.cube import Cube
from solver.layer_one.layer_one import layer_one
from solver.layer_three.layer_three import layer_three
from solver.layer_two.layer_two import layer_two


def cube_is_solved(cube: Cube):
    all_sides = all(all(colour == cube.sides[side_index][4]
                        for colour in cube.sides[side_index]) for side_index in range(6))

    return all_sides


class TestLayerTwo(unittest.TestCase):
    def test_layer_two(self):
        cube = Cube()
        for i in range(1000):
            cube.randomise()
            layer_one(cube, True)
            layer_two(cube, True)
            print(f"cube before:\n{cube.sides}")
            layer_three(cube, True)
            print(f"cube after:\n{cube}")
            print(i)
            self.assertTrue(cube_is_solved(cube))


unittest.main()
