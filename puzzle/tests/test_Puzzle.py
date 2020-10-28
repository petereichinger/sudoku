from unittest import TestCase
from puzzle.Puzzle import Puzzle
import puzzle.PuzzleErrors

positions = [(x, y) for x in range(1, 10) for y in range(1, 10)]
values = [val for val in range(1, 10)]


class TestPuzzle(TestCase):

    def test_from_string_empty(self):
        p = Puzzle.from_string("")
        self.assertFalse(p.values)

    def test_from_dict_empty(self):
        p = Puzzle.from_dict({})
        self.assertFalse(p.values)

    def test_from_string_single_value(self):
        p = Puzzle.from_string("1")
        self.assertEqual(p.values[(1, 1)], 1)

    def test_from_string_two_values(self):
        p = Puzzle.from_string("2,3")
        self.assertEqual(p.values[(1, 1)], 2)
        self.assertEqual(p.values[(2, 1)], 3)

    def test_from_string_two_values_with_empty(self):
        p = Puzzle.from_string("2,,3")
        self.assertEqual(p.values[(1, 1)], 2)
        self.assertTrue((2, 1) not in p.values)
        self.assertEqual(p.values[(3, 1)], 3)

    def test_from_dict_single_value(self):
        for pos in positions:
            for val in values:
                with self.subTest(msg=str(pos) + " " + str(val), p1=pos, p2=val):
                    p = Puzzle.from_dict({pos: val})
                    self.assertEqual(p.values[pos], val)
        for pos in positions:
            with self.subTest(msg=str(pos) + " " + str(val), p1=pos, p2=10):
                with self.assertRaises(puzzle.PuzzleErrors.InvalidValueError):
                    Puzzle.from_dict({pos: 10})

    def test_from_string_invalid_value(self):
        with self.assertRaises(puzzle.PuzzleErrors.InvalidValueError):
            Puzzle.from_string("10")
