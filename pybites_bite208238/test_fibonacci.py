import pytest

from fibonacci import fib


EXPECTED = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]


def test_fib_negative_value_raises_error():
    with pytest.raises(ValueError):
        fib(-1)


def test_fib_less_than_two_returns_input_parameter_as_is():
    assert fib(0) == 0
    assert fib(1) == 1


@pytest.mark.parametrize("x, y", list(enumerate(EXPECTED)))
def test_fib_calculates_correct_sequence(x, y):
    assert fib(x) == y


# Run at least one test with n >= 10 to keep MutPy happy :(
def test_fib_calculates_correct_sequence_10():
    assert fib(10) == 55
