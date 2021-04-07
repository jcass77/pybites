import re
import string

PUNCTUATION_CHARS = list(string.punctuation)

used_passwords = set("PassWord@1 PyBit$s9".split())


def validate_password(password: str) -> bool:
    invalid = (
        password in used_passwords
        or not re.search(r"(?=.*\d+)(?=.*[a-z]{2,})(?=.*[A-Z]).{6,12}", password)
        or not any(c in password for c in PUNCTUATION_CHARS)
    )

    if invalid:
        return False

    used_passwords.add(password)
    return True
