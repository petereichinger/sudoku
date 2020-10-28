from puzzle import Puzzle, row_generator, col_generator

if __name__ == "__main__":
    test_puzzle = Puzzle("1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9")
    # test_puzzle.set((1, 1), 9)

    print(test_puzzle.check())
