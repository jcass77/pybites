from decimal import Decimal, ROUND_HALF_EVEN


def round_even(number):
    return float(round(Decimal(str(number)), 1))
    # return round(number)
    # return float(Decimal(number).quantize(Decimal("0.pybites_bite1")))
    # d = Decimal(str(number))
    # return float(d.quantize(Decimal("0.pybites_bite1"), rounding=ROUND_HALF_EVEN))
