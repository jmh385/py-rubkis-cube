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

    turn_up = 'x'
    turn_down = 'X'

    turn_right = 'y'
    turn_left = 'Y'

    turn_front = 'z'
    turn_front_prime = 'Z'
