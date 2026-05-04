"""Tuple utilities."""

from typing import Any, List, Tuple

def tuple_to_list(t: Tuple[Any, ...]) -> List[Any]:

    return list(t)


def swap_first_last(t: Tuple[Any, ...]) -> Tuple[Any, ...]:

    if len(t) <= 1:
        return t

    return (t[-1],) + t[1:-1] + (t[0],)


def count_in_tuple(t: Tuple[Any, ...], value: Any) -> int:

    return t.count(value)