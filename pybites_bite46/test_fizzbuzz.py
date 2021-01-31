import random

from fizzbuzz import fizzbuzz

# tests are hidden for this Bite


def test_fizzbuzz_not_divisible_returns_numer_as_is():
    for x in (random.randint(0, 1_000) for _ in range(100)):
        if x % 3 == 0 and x % 5 == 0:
            assert fizzbuzz(x) == "Fizz Buzz"
        elif x % 3 == 0:
            assert fizzbuzz(x) == "Fizz"
        elif x % 5 == 0:
            assert fizzbuzz(x) == "Buzz"
        else:
            assert fizzbuzz(x) == x
