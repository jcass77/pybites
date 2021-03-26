import random

BITES = {
    6: "PyBites Die Hard",
    7: "Parsing dates from logs",
    9: "Palindromes",
    10: "Practice exceptions",
    11: "Enrich a class with dunder methods",
    12: "Write a user validation function",
    13: "Convert dict in namedtuple/json",
    14: "Generate a table of n sequences",
    15: "Enumerate 2 sequences",
    16: "Special PyBites date generator",
    17: "Form teams from a group of friends",
    18: "Find the most common word",
    19: "Write a simple property",
    20: "Write a context manager",
    21: "Query a nested data structure",
}
BITES_DONE = {6, 10, 16, 18, 21}


class NoBitesAvailable(Exception):
    pass


class Promo:
    def __init__(self):
        self.all_bites = BITES.copy()
        self.bites_done = BITES_DONE.copy()

    def _pick_random_bite(self) -> str:
        remaining_bites = self.all_bites.keys() - self.bites_done
        if not remaining_bites:
            raise NoBitesAvailable()

        return random.sample(remaining_bites, 1)[0]

    def new_bite(self):
        bite_no = self._pick_random_bite()
        self.bites_done.add(bite_no)
        return bite_no
