from puzzle.Puzzle import Puzzle
from solvers.RandomSolver import RandomSolver
import time

if __name__ == "__main__":

    times = []
    for x in range(0, 100):
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

        r = RandomSolver(p)

        t = time.process_time()
        r.run()
        elapsed_time = time.process_time() - t

        times.append(elapsed_time)

    print(sum(times) / len(times))
