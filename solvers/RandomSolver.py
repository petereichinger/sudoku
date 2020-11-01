from puzzle.Puzzle import Puzzle, Coordinate
from random import Random
from puzzle.PuzzleErrors import InvalidSetError
import datetime


class RandomSolver:

    def __init__(self, p: Puzzle, seed=None):
        self.puzzle = p
        self.random = Random(seed)

    def run(self):
        already_set_positions = set(coord for coord, value in self.puzzle.get_solved_positions())

        while not self.puzzle.is_solved():
            pos, values = self.random.choice(list(self.puzzle.get_unsolved_positions()))
            value = self.random.choice(list(values))

            try:
                self.puzzle.set(pos, value)
            except InvalidSetError as e:
                possible_resets = set(pos for pos, value in self.puzzle.get_solved_positions())
                possible_resets.difference_update(already_set_positions)
                if len(possible_resets) > 0:
                    unset_entry = self.random.sample(possible_resets, 1)
                    self.puzzle.unset(unset_entry[0])
