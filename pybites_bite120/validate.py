from functools import wraps


def int_args(func):
    @wraps(func)
    def func_wrapper(*args, **kwargs):
        for arg in args:
            if type(arg) is not int:
                raise TypeError("Arguments must be integers")

            if arg < 0:
                raise ValueError("Arguments must be positive numbers")

        return func(*args, **kwargs)

    return func_wrapper
