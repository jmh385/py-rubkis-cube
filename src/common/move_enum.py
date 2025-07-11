from enum import Enum


class Move(Enum):
    left = 'l'
    left_prime = 'L'

    right = 'r'
    right_prime = 'R'

    up = 'u'
    up_prime = 'U'

    down = 'd'
    down_prime = 'D'

    front = 'f'
    front_prime = 'F'

    back = 'b'
    back_prime = 'B'

    turn_x = 'x'
    turn_x_prime = 'X'

    turn_y = 'y'
    turn_y_prime = 'Y'

    turn_z = 'z'
    turn_z_prime = 'Z'
