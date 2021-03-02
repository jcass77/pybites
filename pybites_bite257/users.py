import re


def get_users(passwd: str) -> dict:
    """Split password output by newline,
    extract user and name (1st and 5th columns),
    strip trailing commas from name,
    replace multiple commas in name with a single space
    return dict of keys = user, values = name.
    """
    result = {}
    for line in passwd.strip().splitlines():
        elements = line.split(":")
        uname = elements[0]
        name = re.sub(r",+", r" ", elements[4].rstrip(",") or "unknown")

        result[uname] = name

    return result

