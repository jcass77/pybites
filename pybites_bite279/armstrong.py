import math


def is_armstrong(n: int) -> bool:
    digits = str(n)
    length = len(digits)
    if length == 1:
        return True

    return sum(math.pow(int(digit), length) for digit in digits) == n
