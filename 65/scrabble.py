import itertools
import os
import urllib.request

# PREWORK
import bisect
from typing import List

TMP = os.getenv("TMP", "/tmp")
DICT = "dictionary.txt"
DICTIONARY = os.path.join(TMP, DICT)
urllib.request.urlretrieve(
    f"https://bites-data.s3.us-east-2.amazonaws.com/{DICT}", DICTIONARY
)

with open(DICTIONARY) as f:
    dictionary = sorted(set([word.strip().lower() for word in f.read().split()]))


def is_word(perm: str, sorted_dictionary: List[str]):
    i = bisect.bisect_left(sorted_dictionary, perm)
    if i != len(dictionary) and sorted_dictionary[i] == perm:
        return True
    return False


def get_possible_dict_words(draw):
    return (perm for perm in _get_permutations_draw(draw) if is_word(perm, dictionary))


def _get_permutations_draw(draw):
    for i in range(len(draw)):
        for perm in itertools.permutations(draw, r=i):
            yield "".join(perm).lower()
