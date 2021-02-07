from decimal import Decimal, ROUND_HALF_UP


def round_decimal(value: Decimal, decimals: int = 2, rounding=ROUND_HALF_UP) -> Decimal:
    decimal_places = Decimal(10) ** (decimals * -1)

    return value.quantize(decimal_places, rounding=rounding)


def round_up(num):
    weirdos = find_weird_conversions()
    d = float(round(Decimal(str(num)), 2))
    f = round(num, 2)
    return round(num, 2)


def find_weird_conversions(max_value: float = 3):
    num = Decimal(0)
    weirdos = []
    while num < max_value:
        num += Decimal("0.001")
        d1 = float(round(Decimal(str(num)), 2))
        d2 = float(num.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP))
        if d1 != d2:
            print("oh shit!")
        f = round(float(str(num)), 2)
        if f != d2:
            weirdos.append(num)

    return weirdos