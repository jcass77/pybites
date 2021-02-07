from decimal import ROUND_CEILING, Decimal, ROUND_FLOOR


def round_up_or_down(transactions, up=True):
    """Round the list of transactions passed in.
    If up=True (default) round up, else round down.
    Return a new list of rounded values
    """
    r = ROUND_CEILING if up else ROUND_FLOOR
    return [Decimal(f).quantize(1, rounding=r) for f in transactions]
