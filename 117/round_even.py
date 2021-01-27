from decimal import Decimal, ROUND_HALF_EVEN


def round_even(number):
    return float(round(Decimal(str(number)), 1))
    # return float(round(number, 1))
    # return float(Decimal(number).quantize(Decimal("0.1")))
    # d = Decimal(str(number))
    # return float(d.quantize(Decimal("0.1"), rounding=ROUND_HALF_EVEN))
