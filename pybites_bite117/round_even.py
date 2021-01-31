from decimal import Decimal, ROUND_HALF_UP


def round_even(number):
    precise_number = Decimal(str(number))
    return float(precise_number.quantize(Decimal("0.1"), rounding=ROUND_HALF_UP))
    # return round(number)
    # return float(Decimal(number).quantize(Decimal("0.pybites_bite1")))
    # d = Decimal(str(number))
    # return float(d.quantize(Decimal("0.pybites_bite1"), rounding=ROUND_HALF_EVEN))
