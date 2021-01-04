import collections
import string

ALPHA_NUMERIC = string.ascii_letters + string.digits


def get_index_different_char(chars: list):
    is_alpha = [c and str(c) in ALPHA_NUMERIC for c in chars]
    most_common = collections.Counter(is_alpha).most_common(1)[0][0]

    return is_alpha.index(not most_common)
