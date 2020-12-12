"some function for misc"


from typing import Any, Callable, Iterable


def every(iterable: Iterable, func: Callable[[Any], bool] = None) -> bool:
    """like all(iterable), can accept an test function"""
    if func is None:
        return all(iterable)

    for it in iterable:
        if not func(it):
            return False

    return True


def some(iterable: Iterable, func: Callable[[Any], bool] = None) -> bool:
    """like any(iterable), can accept an test function"""
    if func is None:
        return any(iterable)

    for it in iterable:
        if func(it):
            return True

    return False
