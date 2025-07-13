from typing import List, Dict, Callable, Union

import random

from common.color_type_enum import ColourType
from common.move_enum import Move


class Cube:
    def __init__(self, n=0):
        self.sides: List[List[ColourType]] = [[ColourType.white for _ in range(9)],
                                              [ColourType.blue for _ in range(9)],
                                              [ColourType.orange for _ in range(9)],
                                              [ColourType.green for _ in range(9)],
                                              [ColourType.red for _ in range(9)],
                                              [ColourType.yellow for _ in range(9)]]
        self.functions: Dict[Move, Callable] = {Move.up: self.up, Move.up_prime: self.up_prime,
                                                Move.down: self.down, Move.down_prime: self.down_prime,
                                                Move.right: self.right, Move.right_prime: self.right_prime,
                                                Move.left: self.left, Move.left_prime: self.left_prime,
                                                Move.back: self.back, Move.back_prime: self.back_prime,
                                                Move.front: self.front, Move.front_prime: self.front_prime,
                                                Move.turn_x: self.turn_x, Move.turn_x_prime: self.turn_x_prime,
                                                Move.turn_y: self.turn_y, Move.turn_y_prime: self.turn_y_prime,
                                                Move.turn_z: self.turn_z,
                                                Move.turn_z_prime: self.turn_z_prime}

    def up(self, times: int = 1) -> List[Move]:
        for i in range(times):
            ret_lst = []
            ret_lst[0:3] = self.sides[2][6::-3]
            ret_lst[3:6] = self.sides[2][7::-3]
            ret_lst[6:] = self.sides[2][8:1:-3]
            self.sides[2] = ret_lst[:]
            dump = self.sides[0][:3]
            self.sides[0][:3] = self.sides[1][:3]
            self.sides[1][:3] = self.sides[5][:3]
            self.sides[5][:3] = self.sides[3][:3]
            self.sides[3][:3] = dump[:]
        return [Move.up] * times

    def up_prime(self, times: int =1) -> List[Move]:
        self.up(3 * times)
        return [Move.up_prime] * times

    def front(self, times: int = 1) -> List[Move]:
        for i in range(times):
            ret_lst = []
            ret_lst[0:3] = self.sides[0][6::-3]
            ret_lst[3:6] = self.sides[0][7::-3]
            ret_lst[6:] = self.sides[0][8:1:-3]
            self.sides[0] = ret_lst[:]
            dump = self.sides[1][6::-3]
            self.sides[1][:7:3] = self.sides[2][6:]
            self.sides[2][6:] = self.sides[3][8:1:-3]
            self.sides[3][8:1:-3] = self.sides[4][2::-1]
            self.sides[4][:3] = dump[:]
        return  [Move.front] * times

    def front_prime(self, times: int = 1) -> List[Move]:
        self.front(3 * times)
        return [Move.front_prime] * times

    def left(self, times: int = 1) -> List[Move]:
        for i in range(times):
            ret_lst = []
            ret_lst[0:3] = self.sides[3][6::-3]
            ret_lst[3:6] = self.sides[3][7::-3]
            ret_lst[6:] = self.sides[3][8:1:-3]
            self.sides[3] = ret_lst[:]
            dump = self.sides[2][::3]
            self.sides[2][::3] = self.sides[5][8:1:-3]
            self.sides[5][8:1:-3] = self.sides[4][::3]
            self.sides[4][::3] = self.sides[0][::3]
            self.sides[0][::3] = dump[:]
        return [Move.left] * times

    def left_prime(self, times: int = 1) -> List[Move]:
        self.left(3 * times)
        return [Move.left_prime] * times


    def right(self, times: int = 1) -> List[Move]:
        for i in range(times):
            ret_lst = []
            ret_lst[0:3] = self.sides[1][6::-3]
            ret_lst[3:6] = self.sides[1][7::-3]
            ret_lst[6:] = self.sides[1][8:1:-3]
            self.sides[1] = ret_lst[:]
            dump = self.sides[4][2::3]
            self.sides[4][2::3] = self.sides[5][6::-3]
            self.sides[5][6::-3] = self.sides[2][2::3]
            self.sides[2][2::3] = self.sides[0][2::3]
            self.sides[0][2::3] = dump[:]
        return [Move.right] * times

    def right_prime(self, times: int = 1) -> List[Move]:
        self.right(3 * times)
        return [Move.right_prime] * times

    def down(self, times: int = 1) -> List[Move]:
        for i in range(times):
            ret_lst = []
            ret_lst[0:3] = self.sides[4][6::-3]
            ret_lst[3:6] = self.sides[4][7::-3]
            ret_lst[6:] = self.sides[4][8:1:-3]
            self.sides[4] = ret_lst[:]
            dump = self.sides[3][6:]
            self.sides[3][6:] = self.sides[5][6:]
            self.sides[5][6:] = self.sides[1][6:]
            self.sides[1][6:] = self.sides[0][6:]
            self.sides[0][6:] = dump[:]
        return [Move.down] * times


    def down_prime(self, times: int = 1) -> List[Move]:
        self.down(3 * times)
        return [Move.down_prime] * times

    def back(self, times: int = 1) -> List[Move]:
        for i in range(times):
            ret_lst = []
            ret_lst[0:3] = self.sides[5][6::-3]
            ret_lst[3:6] = self.sides[5][7::-3]
            ret_lst[6:] = self.sides[5][8:1:-3]
            self.sides[5] = ret_lst[:]
            dump = self.sides[1][8::-3]
            self.sides[1][8::-3] = self.sides[4][6:]
            self.sides[4][6:] = self.sides[3][0:7:3]
            self.sides[3][0:7:3] = self.sides[2][2::-1]
            self.sides[2][2::-1] = dump[:]
        return [Move.back] * times

    def back_prime(self, times: int = 1) -> List[Move]:
        self.back(3 * times)
        return [Move.back_prime] * times

    def turn_y(self, times: int = 1) -> List[Move]:
        for i in range(times):
            dump = self.sides[1][:]
            self.sides[1] = self.sides[5]
            self.sides[5] = self.sides[3]
            self.sides[3] = self.sides[0]
            self.sides[0] = dump[:]
            ret_lst = []
            ret_lst[0:3] = self.sides[2][2::3]
            ret_lst[3:6] = self.sides[2][1:8:3]
            ret_lst[6:] = self.sides[2][0:7:3]
            self.sides[2] = list(reversed(ret_lst))
            ret_lst = []
            ret_lst[0:3] = self.sides[4][2::3]
            ret_lst[3:6] = self.sides[4][1:8:3]
            ret_lst[6:] = self.sides[4][0:7:3]
            self.sides[4] = ret_lst[:]
        return [Move.turn_y] * times

    def turn_y_prime(self, times: int = 1) -> List[Move]:
        self.turn_y(3 * times)
        return [Move.turn_y_prime] * times

    def turn_x(self, times: int = 1) -> List[Move]:
        self.turn_x_prime(3 * times)
        return [Move.turn_x] * times

    def turn_x_prime(self, times: int = 1) -> List[Move]:
        for i in range(times):
            dump = self.sides[2][:]
            self.sides[2] = list(reversed(self.sides[5]))
            self.sides[5] = list(reversed(self.sides[4]))
            self.sides[4] = self.sides[0]
            self.sides[0] = dump[:]
            ret_lst = []
            ret_lst[0:3] = self.sides[1][2::3]
            ret_lst[3:6] = self.sides[1][1:8:3]
            ret_lst[6:] = self.sides[1][0:7:3]
            self.sides[1] = ret_lst[:]
            ret_lst = []
            ret_lst[0:3] = self.sides[3][2::3]
            ret_lst[3:6] = self.sides[3][1:8:3]
            ret_lst[6:] = self.sides[3][0:7:3]
            self.sides[3] = list(reversed(ret_lst))
        return [Move.turn_x_prime] * times

    def turn_z_prime(self, times: int = 1) -> List[Move]:
        for i in range(times):
            self.turn_x_prime()
            self.turn_y_prime()
            self.turn_x()
        return  [Move.turn_z_prime] * times

    def turn_z(self, times: int = 1) -> List[Move]:
        self.turn_z_prime(3 * times)
        return [Move.turn_z] * times

    def movement_parser(self, moves: Union[List[Move], Move]) -> List[Move]:
        if type(moves) == Move:
            self.functions[moves]()
            return  [moves]
        for move in moves:
            self.functions[move]()
        return moves

    def randomise(self) -> List[Move]:
        moves: List[Move] = []
        for i in range(20):
            move: Move = list(self.functions.keys())[random.randint(0, len(self.functions) - 7)]
            moves.append(move)
            self.functions[move]()
        return moves

    def count_corners(self) -> int:
        count_corners = 0
        for side in self.sides[0], self.sides[1], self.sides[3], self.sides[5]:
            if side[0] == side[2] and side[0] != side[1]:
                count_corners += 1
        return count_corners

    def randomise_for_study(self):
        count = 0
        while self.sides[1].count(self.sides[1][4]) != 9 or \
                self.sides[0].count(self.sides[0][4]) != 9 or \
                self.sides[5].count(self.sides[5][4]) != 9 or \
                self.sides[2].count(self.sides[2][4]) != 9 or \
                self.sides[3].count(self.sides[3][4]) != 9:
            letter = list(self.functions.keys())[random.randint(0, len(self.functions) - 7)]
            self.functions[letter]()
            count += 1

    def __str__(self) -> str:
        ret = ""
        for side in self.sides:
            for colour in side:
                ret += str(colour) + ", "
            ret += "\b\b\n"
        return ret
