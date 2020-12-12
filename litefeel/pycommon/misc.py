"some function for misc"


from typing import Any, Callable, Iterable

_all = all
_any = any


def all(iterable: Iterable, func: Callable[[Any], bool] = None) -> bool:
    """like buildin all(iterable), can accept an test function"""
    if func is None:
        return _all(iterable)

    for it in iterable:
        if not func(it):
            return False

    return True


def any(iterable: Iterable, func: Callable[[Any], bool] = None) -> bool:
    """like buildin any(iterable), can accept an test function"""
    if func is None:
        return _any(iterable)

    for it in iterable:
        if func(it):
            return True

    return False
