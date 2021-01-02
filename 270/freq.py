import collections
from operator import itemgetter


def freq_digit(num: int) -> int:
    counts = sorted(
        collections.Counter(str(num)).items(), key=itemgetter(1), reverse=True
    )
    return int(counts[0][0])
