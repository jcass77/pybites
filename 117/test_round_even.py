import pytest

from round_even import round_even


@pytest.mark.parametrize(
    "arg, expected",
    [
        (0.45, 0.4),  # nearest even 10e-1
        (0.55, 0.6),
        (0.65, 0.6),  # nearest even 10e-1
        (1.45, 1.4),  # nearest even 10e-1
        (1.55, 1.6),
        (1.65, 1.6),  # nearest even 10e-1
        (2.55, 2.6),  # nearest even 10e-1
    ],
)
def test_round_even(arg, expected):
    assert round_even(arg) == expected
