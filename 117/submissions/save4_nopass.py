from decimal import Decimal, ROUND_HALF_EVEN


def round_even(number):
    """Takes a number and returns it rounded even"""
    d = Decimal(str(number))
    return d.quantize(Decimal("0.1"), rounding=ROUND_HALF_EVEN)
