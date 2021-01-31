from secrets import choice
from string import ascii_uppercase, digits

ALPHABET = ascii_uppercase + digits
DASH = "-"


def gen_key(parts=4, chars_per_part=8):
    return DASH.join(
        "".join(choice(ALPHABET) for _ in range(chars_per_part)) for _ in range(parts)
    )
