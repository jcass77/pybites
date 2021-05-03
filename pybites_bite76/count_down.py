import collections
import numbers
from functools import singledispatch


@singledispatch
def count_down(obj):
    raise ValueError(f"Unsupported type: {type(obj)}!")


@count_down.register(str)
def _str(text):
    for i in range(len(text), 0, -1):
        print(text[:i])


@count_down.register(numbers.Complex)
def _num(text):
    count_down(str(text))


@count_down.register(collections.Collection)
def _itr(itr):
    text = "".join((str(element) for element in itr))
    count_down(text)
