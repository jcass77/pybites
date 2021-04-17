from functools import wraps
from numbers import Integral


def int_args(func):
    @wraps(func)
    def func_wrapper(*args, **kwargs):
        for arg in args:
            if not isinstance(arg, Integral):
                raise TypeError("Arguments must be integers")

            if arg < 0:
                raise ValueError("Arguments must be positive numbers")

        return func(*args, **kwargs)

    return func_wrapper
