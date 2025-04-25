from typing import Tuple, Dict

from common.color_type_enum import ColourType

colours: Dict[ColourType, Tuple[int, int, int]] = {ColourType.red: (255, 0, 0),
                                                   ColourType.white: (255, 255, 255),
                                                   ColourType.green: (0, 255, 0),
                                                   ColourType.blue: (0, 0, 255),
                                                   ColourType.orange: (255, 137, 0),
                                                   ColourType.yellow: (255, 255, 0),
                                                   ColourType.black: (0, 0, 0)}
