from puzzle.Puzzle import Puzzle, Coordinate

if __name__ == "__main__":
    p = Puzzle()

    p.set(Coordinate(1, 1), 1)
    p.set(Coordinate(1, 2), 2)

    print(p)
