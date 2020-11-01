from puzzle.Puzzle import Puzzle, Coordinate
from puzzle.PuzzleErrors import UnsolvableError, InvalidSetError, DuplicateError

from typing import Tuple


class DepthFirstSolver:
    def __init__(self, p: Puzzle):
        self.puzzle = p

    def __unpack_possibility(self, possibility: Tuple[Coordinate, set]):
        coord, values = possibility

        return coord, list(values)

    def run(self):
        positions_to_solve = ((pos, values) for pos, values in self.puzzle.get_unsolved_positions())
        stack = [self.__unpack_possibility(next(positions_to_solve))]
        while len(stack) > 0:
            possibilities = stack[-1]
            pos = possibilities[0]

            if len(possibilities[1]) > 0:
                try:
                    value = possibilities[1].pop()
                    self.puzzle.set(pos, value)
                    next_unsolved = self.puzzle.get_next_unsolved(pos)
                    if next_unsolved:
                        stack.append(self.__unpack_possibility(next_unsolved))

                except (InvalidSetError, DuplicateError):
                    continue

                if self.puzzle.is_solved():
                    break
            else:
                self.puzzle.unset(pos)
                stack.pop()

        if not self.puzzle.is_solved():
            raise UnsolvableError()
