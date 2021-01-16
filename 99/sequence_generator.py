from itertools import chain, cycle
from string import ascii_uppercase


def sequence_generator():
    seq = ((d, c) for d, c in enumerate(ascii_uppercase, start=1))
    return cycle(chain.from_iterable(seq))
