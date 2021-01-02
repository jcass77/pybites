import re
from typing import List

IGNORE_CHAR = "b"
QUIT_CHAR = "q"
MAX_NAMES = 5


def filter_names(names: List[str]):
    result = []
    ignore_or_digit = re.compile(f"^[{IGNORE_CHAR}]|[0-9]+", flags=re.IGNORECASE)

    for i, name in enumerate(
        (name for name in names if not ignore_or_digit.search(name))
    ):
        if i == MAX_NAMES or name.startswith(QUIT_CHAR):
            break

        result.append(name)

    return result
