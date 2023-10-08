def chain(*iterables):
    for it in iterables:
        for element in it:
            yield element


def count(start=0, step=1):
    n = start
    while True:
        yield n
        n += step


def cycle(iterable):
    result = []
    for element in iterable:
        yield element
        result.append(element)
    while result:
        for element in result:
              yield element


def repeat(obj, times=None):
    if times is None:
        while True:
            yield obj
    else:
        for _ in range(times):
            yield obj
