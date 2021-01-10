import re
from typing import List

IGNORE_CHAR = "b"
QUIT_CHAR = "q"
MAX_NAMES = 5


def filter_names(names: List[str]):
    matches = re.compile(f"^[{IGNORE_CHAR}]|[0-9]+", flags=re.IGNORECASE)
    names = (name for name in names if matches.search(name) is None)

    for count, name in enumerate(names):
        if count == MAX_NAMES or name.startswith(QUIT_CHAR):
            break

        yield name
