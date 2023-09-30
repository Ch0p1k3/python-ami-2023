import functools


def catch(exceptions, logger):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                func(*args, **kwargs)
            except exceptions as exception:
                logger.exception(exception)

        return wrapper

    return decorator
