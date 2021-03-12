from typing import List, TypeVar

T = TypeVar("T", int, float)


def n_digit_numbers(numbers: List[T], n: int) -> List[int]:
    if n < 1:
        raise ValueError("n must be greater than 0")

    result = []
    for number in numbers:
        if number >= 0:
            str_len = n
        else:
            str_len = n + 1

        num_string = str(number).replace(".", "").ljust(str_len, "0")[:str_len]
        result.append(int(num_string))

    return result
