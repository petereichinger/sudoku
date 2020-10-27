from typing import Dict, Optional, Union, Tuple
from . import PuzzleErrors
from . import Types

PuzzleDict = Dict[Types.Position, Optional[int]]


def row_generator(row: int):
    if row not in range(1, 10):
        raise ValueError(row)
    for col in range(1, 10):
        yield col, row


def col_generator(col: int):
    if col not in range(1, 10):
        raise ValueError(col)
    for row in range(1, 10):
        yield col, row


def block_generator(block: Types.Block):
    bx, by = block
    if bx not in range(1, 4) or by not in range(1, 4):
        raise ValueError((bx, by))

    for y in range(1, 4):
        for x in range(1, 4):
            yield (bx - 1) * 3 + x, (by - 1) * 3 + y


class Puzzle:
    def __init__(self, values: Union[str, PuzzleDict]):

        if isinstance(values, str):
            self.values = self._parse(values)
        else:
            self.values = values
        self._validate()

    def set(self, position: Types.Position, value: int):
        self._validate_entry((position, value))
        self.values[position] = value

    # def check(self) -> bool:

    @staticmethod
    def _parse(text: str):
        index = 0
        values = {}
        for val in text.split(','):
            if val.strip():
                values[(index // 9 + 1, index % 9 + 1)] = int(val)
            index += 1
        return values

    def _validate(self):
        for entry in self.values.items():
            self._validate_entry(entry)

    @staticmethod
    def _validate_entry(entry: Tuple[Tuple[int, int], Optional[int]]):
        (x, y), val = entry
        if x not in range(1, 10) or y not in range(1, 10):
            raise PuzzleErrors.PositionError((x, y))
        if val not in range(1, 10):
            raise PuzzleErrors.InvalidValueError((x, y), val)

    def __str__(self):
        str_list = [str(self.values[(x, y)]) if (x, y) in self.values else "_" for x in range(1, 10) for y in
                    range(1, 10)]
        return '\n'.join([''.join(str_list[i * 9:(i + 1) * 9]) for i in range(0, 10)])
