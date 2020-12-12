"some function for misc"


from typing import Callable, Iterable


def every(iterable: Iterable, call: Callable = None) -> bool:
    if call is None:
        return all(iterable)

    for it in iterable:
        if not call(it):
            return False

    return True


def some(iterable: Iterable, call: Callable = None) -> bool:
    if call is None:
        return any(iterable)

    for it in iterable:
        if call(it):
            return True

    return False
