import itertools
from collections import deque

WHITE, BLACK = " ", "#"


def create_chessboard(size=8):
    """Create a chessboard with of the size passed in.
    Don't return anything, print the output to stdout"""
    pattern = itertools.cycle((WHITE, BLACK))
    row = deque((next(pattern) for _ in range(size - 1)), maxlen=size)

    for _ in range(size):
        row.append(next(pattern))
        print("".join(row))
