def round_to_next(number: int, multiple: int):
    quotient, remainder = divmod(number, multiple)

    result = quotient * multiple
    if remainder:
        result += multiple

    return result
