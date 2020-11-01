from unittest import TestCase
from puzzle.Puzzle import Puzzle
from solvers.DepthFirstSolver import DepthFirstSolver


class TestDepthFirstSolver(TestCase):
    def test_run_empty(self):
        p = Puzzle()
        r = DepthFirstSolver(p)
        r.run()

        self.assertTrue(p.is_solved())

    def test_run_sample(self):
        p = Puzzle.from_string(
            ",2 ,6 ,,,,8 ,1 ,,\
             3 ,,,7 ,,8 ,,,6,\
             4 ,,,,5 ,,,,7,\
             ,5 ,,1 ,,7 ,,9 ,,\
             ,,3 ,9 ,,5 ,1 ,,,\
             ,4 ,,3 ,,2 ,,5 ,,\
             1 ,,,,3 ,,,,2,\
             5 ,,,2 ,,4 ,,,9,\
             ,3 ,8 ,,,,4 ,6 ,")

        r = DepthFirstSolver(p)
        r.run()

        self.assertTrue(p.is_solved())
