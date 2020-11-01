from unittest import TestCase
from puzzle.Grid import Coordinate
from puzzle.Puzzle import Puzzle
from puzzle.PuzzleErrors import DuplicateError
from random import Random


class TestPuzzle(TestCase):

    def setUp(self):
        self.positions = [Coordinate(x, y) for x in range(1, 10) for y in range(1, 10)]
        self.values = [val for val in range(1, 10)]
        self.invalidValues = [0, 10]
        r = Random(666)
        r.shuffle(self.positions)
        r.shuffle(self.values)

    def test_from_string_empty(self):
        p = Puzzle.from_string("")
        self.assertIsInstance(p, Puzzle)

    def test_from_dict_empty(self):
        p = Puzzle.from_dict({})
        self.assertIsInstance(p, Puzzle)

    def test_valid_possibilities(self):
        p = Puzzle.from_string("1,2,3,4,5,6,7,8,9")
        for x in range(1, 10):
            self.assertEqual(x, p.get(Coordinate(x, 1)))
        for x in range(1, 4):
            self.assertEqual({4, 5, 6, 7, 8, 9}, p.get(Coordinate(x, 2)))

        for x in range(4, 7):
            self.assertEqual({1, 2, 3, 7, 8, 9}, p.get(Coordinate(x, 2)))

        for x in range(7, 10):
            self.assertEqual({1, 2, 3, 4, 5, 6}, p.get(Coordinate(x, 2)))

    def test_set_invalid(self):
        p = Puzzle()
        p.set(Coordinate(1, 1), 1)
        with self.assertRaises(DuplicateError):
            p.set(Coordinate(1, 2), 1)

    def test_unset(self):
        p = Puzzle()

        for pos in self.positions[0:20]:
            with self.subTest("Test unset", pos=pos):
                p.set(pos, 1)
                p.unset(pos)

                self.assertEqual(p.get(pos), set(range(1, 10)))

    def test_set_twice(self):

        p = Puzzle()

        pos = Coordinate(1, 1)
        nextpos = Coordinate(2, 1)
        p.set(pos, 1)

        self.assertEqual(set(range(2, 10)), p.get(nextpos))

        p.set(pos, 9)

        self.assertEqual(set(range(1, 9)), p.get(nextpos))

    def test_invalid_values(self):
        p = Puzzle()
        for pos in self.positions[0:20]:
            for val in self.invalidValues:
                with self.subTest("Set invalid value", pos=pos, val=val):
                    with self.assertRaises(ValueError):
                        p.set(pos, val)

    def test_valid_puzzle(self):

        sudoku = "7,2,6,4,9,3,8,1,5,\
                                3,1,5,7,2,8,9,4,6,\
                                4,8,9,6,5,1,2,3,7,\
                                8,5,2,1,4,7,6,9,3,\
                                6,7,3,9,8,5,1,2,4,\
                                9,4,1,3,6,2,7,5,8,\
                                1,9,4,8,3,6,5,7,2,\
                                5,6,7,2,1,4,3,8,9,\
                                2,3,8,5,7,9,4,6,1"
        p = Puzzle.from_string(sudoku)

        values = [int(str_val) for str_val in sudoku.split(",")]
        index = 0
        for y in range(1, 10):
            for x in range(1, 10):
                coordinate = Coordinate(x, y)
                with self.subTest("Check Pos", pos=coordinate):
                    self.assertIsInstance(p.get(coordinate), int)
                    self.assertEqual(values[index], p.get(coordinate))
                    index += 1
