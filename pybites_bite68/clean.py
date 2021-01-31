import re
import string


def remove_punctuation(input_string):
    """Return a str with punctuation chars stripped out"""
    return re.sub(f"[{re.escape(string.punctuation)}]", "", input_string)
