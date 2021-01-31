import decimal


def round_even(number):
    """Takes a number and returns it rounded even"""
    d = decimal.Decimal(str(number))
    return d.quantize("0.01", rounding=decimal.ROUND_HALF_EVEN)
