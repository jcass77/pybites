import collections


def get_index_different_char(chars: list):
    is_alnum = [str(c).isalnum() for c in chars]
    most_common = collections.Counter(is_alnum).most_common(1)[0][0]

    return is_alnum.index(not most_common)
