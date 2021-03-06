from functools import wraps
from typing import Callable


def make_strong(func: Callable):
    @wraps(func)
    def func_wrapper(*args, **kwargs):
        return f"<strong>{func(*args, **kwargs)}</strong>"

    return func_wrapper


def make_html(elem: str):  # Decorator factory
    def func_decorator(func: Callable):
        @wraps(func)
        def func_wrapper(*args, **kwargs):
            return f"<{elem}>{func(*args, **kwargs)}</{elem}>"

        return func_wrapper

    return func_decorator
