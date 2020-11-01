from .Grid import Coordinate


class DuplicateError(Exception):
    def __init__(self, first: Coordinate, second: Coordinate, value: int):
        self.first = first
        self.second = second
        self.value = value

    def __str__(self):
        return "Same value {} for {} and {}".format(self.value, self.first, self.second)


class InvalidSetError(Exception):
    def __init__(self, set_pos: Coordinate, invalid_pos: Coordinate, value: int):
        self.set_pos = set_pos
        self.invalid_pos = invalid_pos
        self.value = value

    def __str__(self):
        return "Setting {} to {} removes all possibilities from {}".format(self.set_pos, self.value, self.invalid_pos)


class UnsolvableError(Exception):
    def __str__(self):
        return "Puzzle is unsolvable"
