from dataclasses import dataclass

from common.color_type_enum import ColourType


@dataclass
class SideData:
    colour_type: ColourType
    front_cross_index: int
    side_front_middle_index: int
    side_index: int
    turns_from_top: int
