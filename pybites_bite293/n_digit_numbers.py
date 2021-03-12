from decimal import Decimal
from typing import List, TypeVar

T = TypeVar("T", int, float)


def n_digit_numbers(numbers: List[T], n: int) -> List[int]:
    if n < 1:
        raise ValueError("n must be greater than 0")

    result = []
    for number in numbers:
        sign, digits, _ = Decimal(number).normalize().as_tuple()
        sign = "-" if sign else ""
        digits = ''.join(str(d) for d in digits)
        exponent = n - len(digits)

        d = Decimal(f"{sign}{digits}e{exponent}")
        result.append(int(d))

    return result
