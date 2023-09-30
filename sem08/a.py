import functools


class DeprecatedError(RuntimeError):
    pass


def deprecated(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        raise DeprecatedError(f'{func.__name__} is deprecated!')
    return wrapper
