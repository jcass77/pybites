import collections


def freq_digit(num: int) -> int:
    return int(collections.Counter(str(num)).most_common()[0][0])
