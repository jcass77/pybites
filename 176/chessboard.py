from collections import deque

WHITE, BLACK = " ", "#"


def create_chessboard(size=8):
    """Create a chessboard with of the size passed in.
    Don't return anything, print the output to stdout"""
    if size % 2 != 0:
        raise ValueError("Chessboard size has to be a multiple of 2!")

    row = deque("# " * int(size / 2))

    for _ in range(size):
        row.rotate(1)
        print("".join(row))
