import unittest
from typing import Optional
from unittest import TestSuite

from anyio import sleep_forever

from common.color_type_enum import ColourType
from cube.cube import Cube
from solver.layer_one.layer_one import layer_one
from solver.side_consts import side_order


class TestLayerOne(unittest.TestCase):

    # def test_edge_with_white_not_on_back_solve(self):
    #
    #     # test_count = 100
    #     # cube: Optional[Cube] = None
    #     # for i in range(test_count):
    #     #     cube = Cube()
    #     #     cube.randomise()
    #     #     white_side_up(cube)
    #     #     align_sides(cube)
    #     #     side_data = side_order[0]
    #     #     if not is_edge_with_white_not_on_back(cube, side_data):
    #     #         i -= 1
    #     #         continue
    #     #
    #     #     print(f"before\n{cube.sides}")
    #     #     edge_with_white_not_on_back_solve(cube, side_data)
    #     #     print(f"after\n{cube.sides}")
    #     #     print(f"backwards: {is_edge_backwards(cube, side_data)} correct: {is_edge_correct_oriented(cube, side_data)}")
    #     #     self.assertTrue(is_edge_backwards(cube, side_data) or is_edge_correct_oriented(cube, side_data) )
    # def test_white_on_top_with_side_colour_mismatched_solve(self):
    #     test_count = 100
    #     cube: Optional[Cube] = None
    #     for i in range(test_count):
    #         cube = Cube()
    #         cube.randomise()
    #         white_side_up(cube)
    #         align_sides(cube)
    #         side_data = side_order[0]
    #         if not is_white_on_top_with_side_colour_mismatched(cube, side_data):
    #             i -= 1
    #             continue
    #
    #         print(f"before\n{cube.sides}")
    #         white_on_top_with_side_colour_mismatched_solve(cube, side_data)
    #         print(f"after\n{cube.sides}")
    #         print(f"backwards: {is_edge_backwards(cube, side_data)} correct: {is_edge_correct_oriented(cube, side_data)}")
    #         self.assertTrue(is_edge_backwards(cube, side_data) or is_edge_correct_oriented(cube, side_data) )

    # def test_white_on_side_with_colour_on_top_solve(self):
    #     test_count = 100
    #     cube: Optional[Cube] = None
    #     for i in range(test_count):
    #         cube = Cube()
    #         cube.randomise()
    #         white_side_up(cube)
    #         align_sides(cube)
    #         side_data = side_order[0]
    #         if not is_white_on_side_with_colour_on_top(cube, side_data):
    #             i -= 1
    #             continue
    #
    #         print(f"before\n{cube.sides}")
    #         white_on_side_with_colour_on_top_solve(cube, side_data)
    #         print(f"after\n{cube.sides}")
    #         print(f"backwards: {is_edge_backwards(cube, side_data)} correct: {is_edge_correct_oriented(cube, side_data)}")
    #         self.assertTrue(is_edge_backwards(cube, side_data) or is_edge_correct_oriented(cube, side_data) )

    # def test_white_corner_on_back(self):
    #     test_count = 10
    #     for i in range(test_count):
    #         cube = Cube()
    #         cube.randomise()
    #         layer_one(cube, True)
    #         for side_data in side_order:
    #             if not is_corner_aligned(cube, side_data) and is_corner_on_top_but_mismatched(cube, side_data):
    #                 print(f"before\n{cube.sides}")
    #                 save_corner_on_top_but_mismatched(cube, side_data)
    #                 print(f"after\n{cube.sides}")
    #                 self.assertTrue(is_corner_with_white_on_side(cube, side_data), "corner was not aligned")

    # def test_white_cross(self):
    #     test_count = 100
    #     for i in range(test_count):
    #         cube = Cube()
    #         cube.randomise()
    #         white_side_up(cube)
    #         align_sides(cube)
    #         print(f"before\n{cube.sides}")
    #         white_cross(cube)
    #         print(f"after\n{cube.sides}")
    #         self.assertEqual(cube.sides[0][4], ColourType.white)
    #         print(i)
    #         for side_data in side_order:
    #             self.assertTrue(cube.sides[side_data.side_index][4] == side_data.colour_type and cube.sides[side_data.side_index][side_data.side_front_middle_index])
    #             self.assertTrue(cube.sides[0][side_data.front_cross_index] == ColourType.white)

    def test_layer_one(self):
        test_count = 100
        for i in range(test_count):
            cube = Cube()
            cube.randomise()
            print(f"before:\n{cube.sides}")
            layer_one(cube, True)
            print(f"after: \n{cube.sides}")
            self.assertTrue(all(colour == ColourType.white for colour in cube.sides[0]))
            self.assertTrue(all(colour == ColourType.blue for colour in cube.sides[1][0:7:3]))
            self.assertTrue(all(colour == ColourType.orange for colour in cube.sides[2][6:9]))
            self.assertTrue(all(colour == ColourType.green for colour in cube.sides[3][2:9:3]))
            self.assertTrue(all(colour == ColourType.red for colour in cube.sides[4][0:3]))



unittest.main()




