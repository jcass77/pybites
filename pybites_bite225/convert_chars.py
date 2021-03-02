PYBITES = "pybites"
SWAPPED_CASE = PYBITES.swapcase()

TRANS = str.maketrans(PYBITES + SWAPPED_CASE, SWAPPED_CASE + PYBITES)


def convert_pybites_chars(text: str):
    """Swap case all characters in the word pybites for the given text.
    Return the resulting string."""
    return text.translate(TRANS)
