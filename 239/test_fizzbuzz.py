import pytest

from fizzbuzz import fizzbuzz


# write one or more pytest functions below, they need to start with test_
@pytest.mark.parametrize(
    "num, expected",
    [
        (0, "Fizz Buzz"),  # Zero case
        (1, 1),  # Not divisible
        (3, "Fizz"),
        (-3, "Fizz"),  # Negative number
        (5, "Buzz"),
        (15, "Fizz Buzz"),  # Divisible by both
    ],
)
def test_fizzbuzz_returns_correct_value(num, expected):
    assert fizzbuzz(num) == expected
