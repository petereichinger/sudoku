from .Grid import Coordinate


class LogicError(Exception):
    def __init__(self, first: Coordinate, second: Coordinate, value: int):
        self.first = first
        self.second = second
        self.value = value

    def __str__(self):
        return "Same value {} for {} and {}".format(self.value, self.first, self.second)
