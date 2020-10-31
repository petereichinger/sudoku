from collections import namedtuple
from typing import Optional, Set
Coordinate = namedtuple("Coordinate", ["x", "y"])


class Grid:

    def __init__(self, width: int, height: int):
        if width <= 0:
            raise ValueError("width must be larger than 0")
        if height <= 0:
            raise ValueError("height must be larger than 0")
        self.width = width
        self.height = height
        self.values = {}

    def verify_position(self, position: Coordinate):
        if not (0 < position.x <= self.width and 0 < position.y <= self.height):
            raise ValueError("{} is out of range of grid coordinates {} {}".format(position, self.width, self.height))

    def get(self, position: Coordinate) -> Optional[Set[int]]:
        self.verify_position(position)
        return self.values[position] if position in self.values else None

    def set(self, position: Coordinate, value):
        self.verify_position(position)
        self.values[position] = value

    def clear(self, position: Coordinate):
        self.verify_position(position)
        if position in self.values:
            del self.values[position]

    def clear_all(self):
        self.values.clear()
