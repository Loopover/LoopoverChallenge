"""
Loopover board simulator that evaluates moves in Programmer Notation

This version is more suited for running standalone or as a module.

Author: spdskatr
License: MIT
"""

SIZE = 20
PAD_SIZE = len(str(SIZE * SIZE))

board = [[SIZE*i+j+1 for j in range(SIZE)] for i in range(SIZE)]
total_moves = 0

def eval_move(x : str) -> int:
    """
    Evaluates a single move in programmer notation.

    # Programmer Notation
    0-indexed
      1R0 - Move the top row (row 0) to the right one square
      -1R0 - Move the top row (row 0) to the left one square
      2R0 - Move the top row to the right twice
      -1C2 - Move column 2 (third from the left) downwards one square
      1R1' Move row 1 from the bottom (second from the bottom) to the right one square

    """
    p = 0
    while p < len(x):
        if x[p].isalpha():
            break
        p += 1

    if p == len(x):
        raise ValueError("No move character in move %s" % x)

    if x[p] == "R":
        move = int(x[:p])
        rn = 0
        if x[-1] == "'":
            rn = SIZE - int(x[p+1:-1]) - 1
        else:
            rn = int(x[p+1:])
        for _ in range(abs(move)):
            do_move(True, rn, bool(move//abs(move) + 1))

    elif x[p] == "C":
        move = int(x[:p])
        cn = 0
        if x[-1] == "'":
            cn = SIZE - int(x[p+1:-1]) - 1
        else:
            cn = int(x[p+1:])
        for _ in range(abs(move)):
            do_move(False, cn, bool(move//abs(move) + 1))

    else:
        raise ValueError("Invalid move character %s in move %s" % (x[p], x));


def do_move(row : bool, ind : int, forward : bool):
    global total_moves
    if row:
        temp = list(board[ind]) 
        if forward:
            for i in range(SIZE):
                board[ind][i] = temp[i-1]
        else:
            for i in range(SIZE):
                board[ind][i-1] = temp[i]
    else:
        temp = [board[i][ind] for i in range(SIZE)]
        if forward:
            for i in range(SIZE):
                board[i-1][ind] = temp[i]
        else:
            for i in range(SIZE):
                board[i][ind] = temp[i-1]
    total_moves += 1

def print_board_state():
    print("Board state:")
    print("\n".join([" ".join([("%%%dd" % PAD_SIZE) % i for i in l]) for l in board]))

if __name__ == "__main__":
    while True:
        print()
        print_board_state()
        print("%d moves so far" % total_moves)
        m = input("Move: ")
        eval_move(m)

