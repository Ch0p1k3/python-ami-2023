import functools
from datetime import datetime


def time_it(func):
    @functools.wraps(func)
    def wrap(*args, **kwargs):
        start = datetime.now()
        answer = func(*args, **kwargs)
        wrap.last_time_taken = (datetime.now() - start).total_seconds()
        return answer

    wrap.last_time_taken = 0.
    return wrap

