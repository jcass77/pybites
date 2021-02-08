def convert(value: float, fmt: str) -> float:
    """Converts the value to the designated format.

    :param value: The value to be converted must be numeric or raise a TypeError
    :param fmt: String indicating format to convert to
    :return: Float rounded to 4 decimal places after conversion
    """
    if type(value) not in [float, int]:
        raise TypeError(f"Expected 'value' to be either a float or an int!")

    fmt = fmt.lower()
    if fmt not in ["cm", "in"]:
        raise ValueError(f"Expected 'fmt' to be either 'cm' or 'in'!")

    if fmt == "cm":
        return round(value * 2.54, 4)

    return round(value * 0.3937008, 4)
