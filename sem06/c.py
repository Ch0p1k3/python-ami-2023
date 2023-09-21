import functools
import sys


def trace(dest = sys.stderr):
    def wraps(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print(
                f'{func.__name__} called with args {args}, {kwargs}!',
                file=dest
            )
            return func(*args, **kwargs)
        return wrapper
    return wraps
