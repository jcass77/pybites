import functools
import operator


def sum_numbers(numbers=None):
    if numbers is None:
        numbers = range(1, 101)

    return functools.reduce(operator.add, numbers, 0)
