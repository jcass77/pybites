from collections import deque


def rotate(string, n):
    """Rotate characters in a string.
       Expects string and n (int) for number of characters to move.
    """
    deq = deque(string)
    deq.rotate(-n)

    return "".join(deq)