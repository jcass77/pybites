from typing import List


def minimum_number(digits: List[int]) -> int:
    digits = digits or [0]  # Default is zero
    unique_digits = set(digits)
    if len(unique_digits) == 1:
        # List containing a single digit does not require further
        # processing.
        return unique_digits.pop()

    return int("".join(str(digit) for digit in sorted(unique_digits)))
