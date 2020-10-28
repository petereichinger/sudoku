from typing import Dict, Optional, Union, Tuple, Iterable
from . import PuzzleErrors
from . import Types
from itertools import chain

PuzzleDict = Dict[Types.Position, Optional[int]]


def _check_range(min_val, max_val, x: Union[int, Tuple[int, int]]):
    if isinstance(x, int):
        return min_val <= x <= max_val
    else:
        return _check_range(min_val, max_val, x[0]) and _check_range(min_val, max_val, x[1])


def row_generator(row: int):
    if not _check_range(1, 9, row):
        raise ValueError(row)
    for col in range(1, 10):
        yield col, row


def col_generator(col: int):
    if not _check_range(1, 9, col):
        raise ValueError(col)
    for row in range(1, 10):
        yield col, row


def block_generator(block: Types.Block):
    if not _check_range(1, 3, block):
        raise ValueError(block)

    bx, by = block
    for y in range(1, 4):
        for x in range(1, 4):
            yield (bx - 1) * 3 + x, (by - 1) * 3 + y


class Puzzle:
    @classmethod
    def from_string(cls, text: str):
        if not isinstance(text, str):
            raise TypeError(text)
        return Puzzle(cls.__parse(text))

    @classmethod
    def from_dict(cls, puzzle_dict: PuzzleDict):
        return Puzzle(puzzle_dict)

    def __init__(self, values: PuzzleDict):
        self.values = values
        self.__validate()

    def set(self, position: Types.Position, value: int):
        self.__validate_entry((position, value))
        self.values[position] = value

    def check(self) -> bool:
        return all(chain(
            (self.__check_pos_range(col_generator(col)) for col in range(1, 10)),
            (self.__check_pos_range(row_generator(row)) for row in range(1, 10)),
            (self.__check_pos_range(block_generator((x, y))) for x in range(1, 4) for y in range(1, 4))
        ))

    def __check_pos_range(self, pos_range: Iterable):
        items = [self.values[pos] for pos in pos_range if pos in self.values]
        value_set = set(items)
        return len(items) == len(value_set)

    @staticmethod
    def __parse(text: str) -> PuzzleDict:
        index = 0
        values = {}
        for val in text.split(','):
            if val.strip():
                values[(index % 9 + 1, index // 9 + 1)] = int(val)
            index += 1
        return values

    def __validate(self):
        for entry in self.values.items():
            self.__validate_entry(entry)

    @staticmethod
    def __validate_entry(entry: Tuple[Tuple[int, int], Optional[int]]):
        (x, y), val = entry
        if not _check_range(1, 9, (x, y)):
            raise PuzzleErrors.PositionError((x, y))
        if not _check_range(1, 9, val):
            raise PuzzleErrors.InvalidValueError((x, y), val)

    def __str__(self):
        str_list = [str(self.values[(x, y)]) if (x, y) in self.values else "_" for y in
                    range(1, 10) for x in range(1, 10)]
        return '\n'.join([''.join(str_list[i * 9:(i + 1) * 9]) for i in range(0, 10)])
