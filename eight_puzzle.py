
# Python Program to Represent the State of 8-Puzzle

puzzle = [
    [1, 2, 3],
    [4, 0, 5],
    [6, 7, 8]
]

def display_puzzle(state):
    print("8-Puzzle State:")

    for row in state:
        for tile in row:
            if tile == 0:
                print("_", end=" ")
            else:
                print(tile, end=" ")
        print()

display_puzzle(puzzle)
