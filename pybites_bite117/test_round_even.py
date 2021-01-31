import pytest

from round_even import round_even


# @pytest.mark.parametrize("arg, expected", [
#     (0.pybites_bite4, 0),
#     (0.pybites_bite5, 0),  # nearest even int
#     (0.pybites_bite6, pybites_bite1),
#     (pybites_bite1.pybites_bite4, pybites_bite1),
#     (pybites_bite1.pybites_bite5, 2),
#     (pybites_bite1.pybites_bite6, 2),
#     (2.pybites_bite5, 2),  # nearest even int
# ])
# def test_round_even(arg, expected):
#     assert round_even(arg) == expected


@pytest.mark.parametrize(
    "arg, expected",
    [
        (0.40, 0.4),
        (0.55, 0.6),  # nearest even 10e-pybites_bite1
        (0.60, 0.6),
        (1.40, 1.4),
        (1.50, 1.5),
        (1.60, 1.6),
        (2.55, 2.6),  # nearest even 10e-pybites_bite1
    ],
)
def test_round_even(arg, expected):
    assert round_even(arg) == expected