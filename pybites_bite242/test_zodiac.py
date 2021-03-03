from datetime import datetime
import json
import os
from pathlib import Path
from urllib.request import urlretrieve

import pytest

from zodiac import (
    get_signs,
    get_sign_with_most_famous_people,
    signs_are_mutually_compatible,
    get_sign_by_date,
)

# original source: https://zodiacal.herokuapp.com/api
URL = "https://bites-data.s3.us-east-2.amazonaws.com/zodiac.json"
TMP = os.getenv("TMP", "/tmp")
PATH = Path(TMP, "zodiac.json")


@pytest.fixture(scope="module")
def signs():
    if not PATH.exists():
        urlretrieve(URL, PATH)
    with open(PATH) as f:
        data = json.loads(f.read())
    return get_signs(data)


def test_sign_class_name_does_not_change(signs):
    assert signs[0].__class__.__name__ == "Sign"


def test_get_sign_with_most_famous_people(signs):
    top_signs = ("Scorpio", 35), ("Capricorn", 35)
    assert get_sign_with_most_famous_people(signs) in top_signs


@pytest.mark.parametrize(
    "sign1, sign2, expected",
    [
        ("Aries", "Taurus", False),
        ("Aries", "Gemini", True),
        ("Taurus", "Gemini", False),
        ("Taurus", "Cancer", True),
        ("Taurus", "Leo", False),
        ("Gemini", "Cancer", False),
        ("Gemini", "Libra", True),
        ("Cancer", "Leo", False),
        ("Cancer", "Scorpio", True),
        ("Taurus", "Pisces", True),
        ("Pisces", "Taurus", True),
    ],
)
def test_signs_are_mutually_compatible(sign1, sign2, expected, signs):
    assert signs_are_mutually_compatible(signs, sign1, sign2) == expected
    assert signs_are_mutually_compatible(signs, sign2, sign1) == expected


@pytest.mark.parametrize(
    "month, day, expected",
    [
        (3, 21, "Aries"),
        (4, 19, "Aries"),
        (4, 20, "Taurus"),
        (5, 1, "Taurus"),
        (5, 20, "Taurus"),
        (5, 21, "Gemini"),
        (6, 20, "Gemini"),
        (6, 21, "Cancer"),
        (7, 1, "Cancer"),
        (7, 22, "Cancer"),
        (8, 22, "Leo"),
        (8, 23, "Virgo"),
        (9, 1, "Virgo"),
        (9, 22, "Virgo"),
        (9, 23, "Libra"),
        (10, 22, "Libra"),
        (10, 23, "Scorpio"),
        (11, 21, "Scorpio"),
        (11, 22, "Sagittarius"),
        (12, 1, "Sagittarius"),
        (12, 21, "Sagittarius"),
        (12, 22, "Capricorn"),
        (1, 19, "Capricorn"),
        (1, 20, "Aquarius"),
        (2, 18, "Aquarius"),
        (2, 19, "Pisces"),
        (3, 1, "Pisces"),
        (3, 20, "Pisces"),
    ],
)
def test_get_sign_by_date(signs, month, day, expected):
    actual = get_sign_by_date(signs, datetime(year=2019, month=month, day=day))
    assert actual == expected
