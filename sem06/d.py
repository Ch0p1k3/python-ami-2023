import typing as tp


def flat_it(sequence: tp.Iterable[tp.Any]) -> tp.Generator[tp.Any, None, None]:
    for el in sequence:
        try:
            iter(el)
        except TypeError:
            yield el
        else:
            if isinstance(el, str) and len(el) == 1:
                yield el
            else:
                yield from flat_it(el)
