from typing import List

from common.color_type_enum import ColourType

setup_sides: List[List[ColourType]] = [
    [ColourType.red, ColourType.green, ColourType.orange, ColourType.white, ColourType.white, ColourType.blue,
     ColourType.orange, ColourType.white, ColourType.yellow],
    [ColourType.green, ColourType.blue, ColourType.blue, ColourType.red, ColourType.blue, ColourType.orange,
     ColourType.green, ColourType.red, ColourType.red],
    [ColourType.green, ColourType.orange, ColourType.orange, ColourType.orange, ColourType.orange, ColourType.yellow,
     ColourType.yellow, ColourType.white, ColourType.white],
    [ColourType.white, ColourType.blue, ColourType.blue, ColourType.red, ColourType.green, ColourType.blue,
     ColourType.green, ColourType.yellow, ColourType.white],
    [ColourType.blue, ColourType.red, ColourType.red, ColourType.green, ColourType.red, ColourType.yellow,
     ColourType.yellow, ColourType.yellow, ColourType.blue],
    [ColourType.yellow, ColourType.white, ColourType.red, ColourType.green, ColourType.yellow, ColourType.green,
     ColourType.white, ColourType.orange, ColourType.orange]]
