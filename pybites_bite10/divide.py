def positive_divide(numerator, denominator):
    try:
        result = numerator / denominator
        if result < 0:
            raise ValueError("Result cannot be negative!")
        return result
    except ZeroDivisionError:
        return 0
