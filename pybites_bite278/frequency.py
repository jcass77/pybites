from collections import Counter


def major_n_minor(numbers):
    """
    Input: an array with integer numbers
    Output: the majority and minority number
    """
    counts = Counter(numbers).most_common()
    return counts[0][0], counts[-1][0]
