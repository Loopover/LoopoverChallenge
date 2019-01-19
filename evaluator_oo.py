"""
Loopover self._bd simulator that evaluates moves in Programmer Notation

This file is a more object-oriented version of evaluator.py.

Author: spdskatr
License: MIT
"""

class LoopoverBoard:
    def __init__(self, size : int):
        self._size = size
        self._pad_size = len(str(size * size))
        self._bd = [[size*i+j+1 for j in range(self._size)] for i in range(self._size)]
        self._total_moves = 0

    def size(self) -> int:
        """
        Returns an integer representing the dimensions of the loopover self._bd.
        """
        return self._size
    
    def total_moves(self) -> int:
        """
        Returns the number of moves made so far
        """
        return self._total_moves

    def eval_move(self, x : str) -> int:
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
                rn = self._size - int(x[p+1:-1]) - 1
            else:
                rn = int(x[p+1:])
            for _ in range(abs(move)):
                self.do_move(True, rn, bool(move//abs(move) + 1))

        elif x[p] == "C":
            move = int(x[:p])
            cn = 0
            if x[-1] == "'":
                cn = self._size - int(x[p+1:-1]) - 1
            else:
                cn = int(x[p+1:])
            for _ in range(abs(move)):
                self.do_move(False, cn, bool(move//abs(move) + 1))

        else:
            raise ValueError("Invalid move character %s in move %s" % (x[p], x));

    def do_move(self, row : bool, ind : int, forward : bool):
        global total_moves
        if row:
            temp = list(self._bd[ind])
            if forward:
                for i in range(self._size):
                    self._bd[ind][i] = temp[i-1]
            else:
                for i in range(self._size):
                    self._bd[ind][i-1] = temp[i]
        else:
            temp = [self._bd[i][ind] for i in range(self._size)]
            if forward:
                for i in range(self._size):
                    self._bd[i-1][ind] = temp[i]
            else:
                for i in range(self._size):
                    self._bd[i][ind] = temp[i-1]
        self._total_moves += 1

    def print_board_state(self):
        print("Board state:")
        print("\n".join([" ".join([("%%%dd" % self._pad_size) % i for i in l]) for l in self._bd]))

if __name__ == "__main__":
    board = LoopoverBoard(20)
    while True:
        print()
        board.print_board_state()
        print("%d moves so far" % board.total_moves())
        m = input("Move: ")
        board.eval_move(m)
