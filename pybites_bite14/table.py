import random
from typing import Generator

names = "Julian Bob PyBites Dante Martin Rodolfo".split()
aliases = "Pythonista Nerd Coder".split() * 2
points = random.sample(range(81, 101), 6)
awake = [True, False] * 3
SEPARATOR = " | "


def generate_table(*columns) -> Generator[str, None, None]:
    for row in zip(*columns):
        yield SEPARATOR.join(str(column) for column in row)
