from puzzle import Puzzle, block_generator

if __name__ == "__main__":
    test_puzzle = Puzzle("1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9")
    # test_puzzle.set((1, 1), 9)

    for pos in block_generator((3, 1)):
        print(pos)
    print(test_puzzle)
