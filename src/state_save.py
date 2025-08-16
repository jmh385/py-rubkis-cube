from typing import List

from common.color_type_enum import ColourType

state_save: List[List[ColourType]] = [
    [ColourType.red, ColourType.red, ColourType.red, ColourType.red, ColourType.red, ColourType.red, ColourType.green,
     ColourType.yellow, ColourType.green],
    [ColourType.blue, ColourType.blue, ColourType.blue, ColourType.blue, ColourType.blue, ColourType.blue,
     ColourType.red, ColourType.blue, ColourType.red],
    [ColourType.white, ColourType.white, ColourType.white, ColourType.white, ColourType.white, ColourType.white,
     ColourType.white, ColourType.white, ColourType.white],
    [ColourType.green, ColourType.green, ColourType.green, ColourType.green, ColourType.green, ColourType.green,
     ColourType.orange, ColourType.red, ColourType.orange],
    [ColourType.yellow, ColourType.green, ColourType.yellow, ColourType.yellow, ColourType.yellow, ColourType.yellow,
     ColourType.yellow, ColourType.orange, ColourType.yellow],
    [ColourType.orange, ColourType.orange, ColourType.orange, ColourType.orange, ColourType.orange, ColourType.orange,
     ColourType.blue, ColourType.yellow, ColourType.blue]]
