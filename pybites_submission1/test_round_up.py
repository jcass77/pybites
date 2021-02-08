import pytest

from round_up import round_up


@pytest.mark.parametrize(
    "arg, expected",
    [
        (0.005, 0.01),
        (0.015, 0.02),
        (0.025, 0.03),
        (0.035, 0.04),
        (0.045, 0.05),
    ],
)
def test_round_up(arg, expected):
    assert round_up(arg) == expected