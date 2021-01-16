import itertools
import string


def sequence_generator():
    seq = ((d, c) for d, c in enumerate(string.ascii_uppercase, start=1))
    return itertools.cycle(itertools.chain.from_iterable(seq))
