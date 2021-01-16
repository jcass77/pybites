from itertools import chain, cycle
from string import ascii_uppercase


def sequence_generator():
    return cycle(chain.from_iterable(enumerate(ascii_uppercase, start=1)))
