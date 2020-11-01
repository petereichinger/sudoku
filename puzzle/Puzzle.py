from typing import Dict, Union, Generator, Set

from .Grid import Grid, Coordinate
from .PuzzleErrors import *


class Puzzle:

    @staticmethod
    def __get_block_index(value):
        return (value - 1) // 3 + 1

    @staticmethod
    def __conflicting_cells(position: Coordinate) -> Generator[Coordinate, None, None]:
        block = Puzzle.__get_block_index(position.x), Puzzle.__get_block_index(position.y)
        for col in range(1, 10):
            col_block = Puzzle.__get_block_index(col)

            if col_block == block[0]:
                if col == position.x:
                    for y in (y for y in range(1, 10) if y != position.y):
                        yield Coordinate(col, y)
                else:
                    for y in range(1, 4):
                        yield Coordinate(col, y + (block[1] - 1) * 3)
            else:
                yield Coordinate(col, position.y)

    @staticmethod
    def __all_cells_generator():
        return (Coordinate(x, y) for x in range(1, 10) for y in range(1, 10))

    def get_solved_positions(self):
        return self.__get_solves(self.__all_cells_generator())

    def get_unsolved_positions(self):
        return self.__get_possibilities(self.__all_cells_generator())

    def is_solved(self):
        return all(isinstance(self.get(Coordinate(x, y)), int) for x in range(1, 10) for y in range(1, 10))

    def valid_solve(self):
        return sum(self.get(pos) for pos in self.__all_cells_generator()) == 405

    def __get_solves(self, pos_iter):
        return ((pos, solves) for (pos, solves) in ((pos, self.grid.get(pos)) for pos in pos_iter) if
                isinstance(solves, int))

    def __get_possibilities(self, pos_iter):
        return ((pos, possibilities) for (pos, possibilities) in ((pos, self.grid.get(pos)) for pos in pos_iter) if
                isinstance(possibilities, set))

    @classmethod
    def from_string(cls, text: str):
        index = 0
        p = Puzzle()
        for val in str(text).strip("[] ").split(','):
            if val.strip():
                p.set(Coordinate(index % 9 + 1, index // 9 + 1), int(val))
            index += 1

        return p

    @classmethod
    def from_dict(cls, values: Dict[Coordinate, int]):
        p = Puzzle()
        for pos, value in values:
            p.set(pos, value)

        return p

    def __init__(self):
        self.grid = Grid(9, 9)
        for x in range(1, 10):
            for y in range(1, 10):
                self.grid.set(Coordinate(x, y), set(range(1, 10)))

    def set(self, position, value: int):
        if isinstance(self.get(position), int):
            self.unset(position)

        if not (0 < value < 10):
            raise ValueError("Cannot set {} to {}".format(position, value))

        self.__update_puzzle(position, value)

    def unset(self, position: Coordinate):
        new_valid_values = set(range(1, 10)).difference(
            val for pos, val in self.__get_solves(self.__conflicting_cells(position)))

        self.grid.set(position, new_valid_values)

        for other_pos in self.__conflicting_cells(position):
            if not isinstance(self.get(other_pos), int):
                self.grid.set(other_pos,
                              set(range(1, 10)).difference(
                                  val for pos, val in self.__get_solves(self.__conflicting_cells(other_pos))))

    def get(self, position) -> Union[int, Set[int]]:
        return self.grid.get(position)

    def __update_puzzle(self, position, value):

        for pos, val in self.__get_solves(self.__conflicting_cells(position)):
            if val == value:
                raise DuplicateError(position, pos, value)

        for pos, val in self.__get_possibilities(self.__conflicting_cells(position)):
            new_vals = self.grid.get(pos).difference({value})
            if len(new_vals) == 0:
                raise InvalidSetError(position, pos, value)
            self.grid.set(pos, new_vals)

        self.grid.set(position, value)

    def __get_str(self, position: Coordinate):
        val = self.grid.get(position)

        if val is None or not isinstance(val, int):
            return "_"

        return str(val)

    def __str__(self):
        return '\n'.join(''.join(self.__get_str(Coordinate(x, y)) for x in range(1, 10)) for y in range(1, 10))
