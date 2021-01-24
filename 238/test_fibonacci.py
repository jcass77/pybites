import random

import pytest

from fibonacci import fib


def test_fib_negative_value_raises_error():
    with pytest.raises(ValueError):
        fib(-1)


def test_fib_less_than_two_returns_input_parameter_as_is():
    assert all(fib(i) == i for i in [0, 1])


@pytest.mark.parametrize("n", (random.randint(2, 20) for _ in range(5)))
def test_fib_calculates_correct_sequence(n):
    assert fib(n) == fib(n-1) + fib(n-2)
