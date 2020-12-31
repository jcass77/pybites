import random

from fizzbuzz import fizzbuzz

# tests are hidden for this Bite


def test_fizzbuzz_div_3_returns_fizz():
    for x in [random.randrange(0, 1_000, 3) for _ in range(100)]:
        assert fizzbuzz(x) == "fizz"


def test_fizzbuzz_div_5_returns_buzz():
    for x in [random.randrange(0, 1_000, 5) for _ in range(100)]:
        if x % 3 == 0:
            continue

        assert fizzbuzz(x) == "buzz"


def test_fizzbuzz_not_divisible_returns_numer_as_is():
    for x in [x for x in range(100) if x % 3 != 0 and x % 5 != 0]:
        assert fizzbuzz(x) == x
