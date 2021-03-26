"""A palindrome is a word, phrase, number, or other sequence of characters
which reads the same backward as forward"""
import os
import re
import string
import urllib.request
from typing import Iterable

DICTIONARY = os.path.join("/tmp", "dictionary_m_words.txt")
urllib.request.urlretrieve("http://bit.ly/2Cbj6zn", DICTIONARY)


def load_dictionary():
    """Load dictionary (sample) and return as generator (done)"""
    with open(DICTIONARY) as f:
        return (word.lower().strip() for word in f.readlines())


def is_palindrome(word: str) -> bool:
    word = re.subn(rf"[^{string.ascii_lowercase}]", "", word, flags=re.IGNORECASE)[
        0
    ].lower()
    return word == word[::-1]


def get_longest_palindrome(words: Iterable[str] = None) -> str:
    words = words or load_dictionary()

    longest_words = list(words)
    longest_words.sort(key=len, reverse=True)

    longest_word = ""
    for word in longest_words:
        if is_palindrome(word):
            if len(word) <= len(longest_word):
                # No chance of sorted list producing longer palindromes
                break
            else:
                longest_word = word

    return longest_word
