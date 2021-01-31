import itertools


def sort_words_case_insensitively(words):
    """Sort the provided word list ignoring case, and numbers last
    (1995, 19ab = numbers / Happy, happy4you = strings, hence for
     numbers you only need to check the first char of the word)
    """
    data = sorted(words, key=str.lower)

    sorted_words = []
    for k, g in itertools.groupby(data, key=lambda x: x[0].isdigit()):
        if k:
            # Starts with digit, add to end
            sorted_words += list(g)
        else:
            sorted_words = list(g) + sorted_words

    return sorted_words
