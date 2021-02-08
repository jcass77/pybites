FORMATS = {"cm": 2.54, "in": 1/2.54}


def convert(value: float, fmt: str) -> float:
    """Converts the value to the designated format.

    :param value: The value to be converted must be numeric or raise a TypeError
    :param fmt: String indicating format to convert to
    :return: Float rounded to 4 decimal places after conversion
    """
    fmt = fmt.lower()

    if fmt not in FORMATS.keys():
        raise ValueError(f"Expected 'fmt' to be either 'cm' or 'in'!")

    try:
        return round(value * FORMATS[fmt], 4)
    except TypeError:
        raise TypeError(f"Expected '{value}' to be either a float or an int!")
