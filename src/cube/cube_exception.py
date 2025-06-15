from cube.cube import Cube

default_message = "some cube operation went wrong"

class CubeException(Exception):
    def __init__(self, cube: Cube, message = default_message):
        self.message = message
        self.cube = cube
        super().__init__(f"{self.message}\ncube:\n{self.cube}")