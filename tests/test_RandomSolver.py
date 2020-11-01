from unittest import TestCase
from puzzle.Puzzle import Puzzle
from solvers.RandomSolver import RandomSolver


class TestRandomSolver(TestCase):
    def test_run_empty(self):
        p = Puzzle()
        r = RandomSolver(p, 666)
        r.run()

        self.assertTrue(p.is_solved() and p.valid_solve())

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

        r = RandomSolver(p, 666)
        r.run()

        self.assertTrue(p.is_solved() and p.valid_solve())