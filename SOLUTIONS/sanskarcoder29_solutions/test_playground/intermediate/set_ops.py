"""Practice set utilities."""

from typing import Iterable, Set

def unique_intersection(a: Iterable, b: Iterable) -> Set:

    return set(a) & set(b)


def is_subset(a: Iterable, b: Iterable) -> bool:

    return set(a).issubset(set(b))


def symmetric_difference(a: Iterable, b: Iterable) -> Set:

    return set(a) ^ set(b)