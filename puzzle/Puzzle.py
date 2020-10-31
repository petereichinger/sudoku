from typing import Dict, Union, Tuple, Generator, Set

from .Grid import Grid, Coordinate
from .PuzzleErrors import LogicError


def _check_val_range(min_val: int, max_val: int, x: Union[int, Tuple]):
    if isinstance(x, tuple):
        return all(_check_val_range(min_val, max_val, tuple_entry) for tuple_entry in x)

    return min_val <= x <= max_val


def row_generator(row: int):
    if not _check_val_range(1, 9, row):
        raise ValueError(row)
    for col in range(1, 10):
        yield col, row


def col_generator(col: int):
    if not _check_val_range(1, 9, col):
        raise ValueError(col)
    for row in range(1, 10):
        yield col, row


def block_generator(block):
    if not _check_val_range(1, 3, block):
        raise ValueError(block)

    bx, by = block
    for y in range(1, 4):
        for x in range(1, 4):
            yield (bx - 1) * 3 + x, (by - 1) * 3 + y


def get_block_index(value):
    return (value - 1) // 3 + 1


def overlap_generator(position: Coordinate) -> Generator[Coordinate, None, None]:
    block = get_block_index(position.x), get_block_index(position.y)
    for col in range(1, 10):
        col_block = get_block_index(col)

        if col_block == block[0]:
            if col == position.x:
                for y in (y for y in range(1, 10) if y != position.y):
                    yield Coordinate(col, y)
            else:
                for y in range(1, 4):
                    yield Coordinate(col, y + (block[1] - 1) * 3)
        else:
            yield Coordinate(col, position.y)


class Puzzle:
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
        if len(self.grid.get(position)) == 1:
            self.unset(position)

        if not (0 < value < 10):
            raise ValueError("Cannot set {} to {}".format(position, value))

        self.__update_puzzle(position, value)

    def unset(self, position: Coordinate):
        if len(self.grid.get(position)) > 1:
            return

        new_valid_values = set(range(1, 10)).difference(self.get_values_in_iter(overlap_generator(position)))

        self.grid.set(position, new_valid_values)

        for other_pos in overlap_generator(position):
            self.grid.set(other_pos,
                          set(range(1, 10)).difference(self.get_values_in_iter(overlap_generator(other_pos))))

    def get_values_in_iter(self, pos_iter):

        for pos in pos_iter:
            values = self.grid.get(pos)

            if len(values) == 1:
                yield next(iter(values))

    def get(self, position) -> Set[int]:
        return self.grid.get(position)

    def __update_puzzle(self, position, value):
        value_set = {value}
        for check_pos in overlap_generator(position):
            check_value = self.grid.get(check_pos)

            if check_value == value_set:
                raise LogicError(position, check_pos, value)

        for check_pos in overlap_generator(position):
            self.grid.get(check_pos).difference_update(value_set)

        self.grid.set(position, value_set)

    def __can_set(self, position: Coordinate, value) -> bool:
        return all(val is None or val != {value} for val in (self.grid.get(pos) for pos in overlap_generator(position)))

    def __get_str(self, position: Coordinate):
        val = self.grid.get(position)

        if val is None or len(val) > 1:
            return "_"

        return str(next(iter(val)))

    def __str__(self):
        return '\n'.join(''.join(self.__get_str(Coordinate(x, y)) for x in range(1, 10)) for y in range(1, 10))
