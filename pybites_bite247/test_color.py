from unittest.mock import patch

import pytest

import color


@pytest.fixture(scope="module")
def gen():
    return color.gen_hex_color()


@pytest.mark.parametrize(
    "rgb, expected",
    (
        ((0, 0, 0), "#000000"),
        ((1, 2, 3), "#010203"),
        ((170, 187, 204), "#AABBCC"),
    ),
)
def test_gen_hex_color_returns_correct_hex_value(gen, rgb, expected):
    with patch("color.sample", return_value=rgb):
        assert next(gen) == expected


def test_gen_hex_color_called_with_valid_hex_values(gen):
    with patch("color.sample", return_value=(0, 0, 0)) as sample_mock:
        next(gen)
        sample_mock.assert_called_once_with(range(0, 256), 3)