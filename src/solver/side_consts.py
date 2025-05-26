from typing import List

from common.color_type_enum import ColourType
from solver.side_data import SideData

side_order: List[SideData] = [
    SideData(ColourType.blue,
             front_cross_index=5,
             side_front_middle_index=3,
             side_index=1,
             turns_from_top=1,
             left_bottom_corner=[(2, 2), (1, 2), (5, 0)],
             left_top_corner=[(0, 2), (1, 0), (2, 8)]),
    SideData(ColourType.orange, 1, 7, 2, 0, [(2, 0), (3, 0), (5, 2)], [(0, 0), (2, 6), (3, 2)]),
    SideData(ColourType.green, 3, 5, 3, 3, [(3, 6), (4, 6), (5, 8)], [(0, 6), (3, 8), (4, 0)]),
    SideData(ColourType.red, 7, 1, 4, 2, [(4, 8), (1, 8), (5, 6)], [(0, 8), (4, 2), (1, 6)])]

none_side_data = SideData(ColourType.black, -1, -1, -1, -1, [(-1, -1)], [(-1, -1)])
