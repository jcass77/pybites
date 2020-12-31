import secrets
import string


def gen_key(parts: int = 4, chars_per_part: int = 8):
    choices = string.ascii_uppercase + string.digits

    secret_parts = []

    for part in range(parts):
        secret_parts.append(
            "".join(secrets.choice(choices) for _ in range(chars_per_part))
        )

    return "-".join(["{}"] * parts).format(*secret_parts)
