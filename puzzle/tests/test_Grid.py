from unittest import TestCase
from puzzle.Grid import Grid, Coordinate


class TestGrid(TestCase):

    def test_init(self):
        with self.assertRaises(ValueError):
            Grid(0, 0)
        with self.assertRaises(ValueError):
            Grid(1, 0)
        with self.assertRaises(ValueError):
            Grid(0, 1)

    def test_set(self):
        g = Grid(1, 1)
        g.set(Coordinate(1, 1), "Test")
        with self.assertRaises(ValueError):
            g.set(Coordinate(0, 0), "Test")

        with self.assertRaises(ValueError):
            g.set(Coordinate(1, 0), "Test")

        with self.assertRaises(ValueError):
            g.set(Coordinate(0, 1), "Test")

        with self.assertRaises(ValueError):
            g.set(Coordinate(2, 1), "Test")

    def test_get(self):
        g = Grid(9, 9)

        for x in range(1, 10):
            for y in range(1, 10):
                g.set(Coordinate(x, y), (x - 1) * 9 + y)
                self.assertEqual(g.get(Coordinate(x, y)), (x - 1) * 9 + y)

    def test_clear(self):
        g = Grid(1, 1)

        g.set(Coordinate(1, 1), 1)

        g.clear(Coordinate(1, 1))

        self.assertIsNone(g.get(Coordinate(1, 1)))

    def test_clear_all(self):

        g = Grid(2, 2)

        g.set(Coordinate(1, 1), 1)
        g.set(Coordinate(2, 2), 1)

        g.clear_all()

        self.assertIsNone(g.get(Coordinate(1, 1)))
        self.assertIsNone(g.get(Coordinate(2, 2)))
