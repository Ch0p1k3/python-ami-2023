import functools


def cache(max_size):
    def wrapper(func):
        if max_size == 0:
            @functools.wraps(func)
            def first_wraps(*args, **kwargs):
                return func(args, kwargs)
            return first_wraps

        used = dict()
        obj = object()

        @functools.wraps(func)
        def second_wraps(*args, **kwargs):
            key = args + (obj, )
            for item in kwargs.items():
                key += item

            hash_key = hash(key)

            if hash_key in used:
                result = used[hash_key]
                del used[hash_key]
                used[hash_key] = result
                return result

            if len(used) == max_size:
                _ = used.popitem(last=False)

            result = func(*args, **kwargs)
            used[hash_key] = result

            return result

        return second_wraps

    return wrapper

