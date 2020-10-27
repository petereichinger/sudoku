from typing import Optional
from . import Types


class PositionError(Exception):
    def __init__(self, cell: Types.Position):
        self.cell = cell

    def __str__(self):
        return "Cell: {}".format(self.cell)


class InvalidValueError(Exception):
    def __init__(self, cell: Types.Position, value: Optional[int]):
        self.cell = cell
        self.value = value

    def __str__(self):
        return "Cell: {} Value {}".format(self.cell, self.value)
