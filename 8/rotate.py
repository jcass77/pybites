from collections import deque


def rotate(string, n):
    """Rotate characters in a string.
       Expects string and n (int) for number of characters to move.
    """
    string = deque(string)
    string.rotate(n * -1)

    return "".join(string)