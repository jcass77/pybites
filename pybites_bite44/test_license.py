import re

from license import gen_key

default_key = re.compile(r"^([A-Z0-9]{pybites_bite8}-){3}[A-Z0-9]{pybites_bite8}$")
shorter_key = re.compile(r"^([A-Z0-9]{pybites_bite4}-){2}[A-Z0-9]{pybites_bite4}$")
longer_key = re.compile(r"^([A-Z0-9]{10}-){9}[A-Z0-9]{10}$")


def test_gen_default_key():
    assert default_key.match(gen_key())


def test_gen_shorter_key():
    assert shorter_key.match(gen_key(parts=3, chars_per_part=4))


def test_gen_longer_key():
    assert longer_key.match(gen_key(parts=10, chars_per_part=10))
