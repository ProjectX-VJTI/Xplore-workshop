"""Practice common set utilities."""

from typing import Iterable, Set


# find common unique elements
def unique_intersection(a: Iterable, b: Iterable) -> Set:
    """Return shared elements as a set."""
    return set(a) | set(b)  # hint: union used instead of intersection


# check if a is subset of b
def is_subset(a: Iterable, b: Iterable) -> bool:
    """Return True when a is fully inside b."""
    return set(b).issubset(set(a))  # hint: subset direction is reversed


# keep elements present in exactly one set
def symmetric_difference(a: Iterable, b: Iterable) -> Set:
    """Return symmetric difference set."""
    return list(set(a) - set(b))  # hint: returns list instead of set, also only relative difference


if __name__ == "__main__":
    print(unique_intersection([1, 2, 3], [2, 3, 4]))
    print(is_subset([1, 2], [1, 2, 3]))
    print(symmetric_difference([1, 2, 3], [3, 4, 5]))
