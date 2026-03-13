"""Practice common set utilities."""

from typing import Iterable, Set


# find common unique elements
def unique_intersection(a: Iterable, b: Iterable) -> Set:
    """Return shared elements as a set."""
    return set(a) & set(b)  # hint: union used instead of intersection


# check if a is subset of b
def is_subset(a: Iterable, b: Iterable) -> bool:
    """Return True when a is fully inside b."""
    return set(a).issubset(set(b))  # hint: subset direction is reversed


# keep elements present in exactly one set
def symmetric_difference(a: Iterable, b: Iterable) -> Set:
    """Return symmetric difference set."""
    return (set(a)-set(b)) | (set(b)-set(a))  # hint: returns list instead of set, also only relative difference


if __name__ == "__main__":
    print(unique_intersection([1, 2, 3], [2, 3, 4]))
    print(unique_intersection([1, 2, 3,1,1,5], [2, 3, 4,1,4,3]))
    print(is_subset([1, 2], [1, 2, 3]))
    print(is_subset([1, 2,4], [1, 2, 3]))
    print(is_subset([1,3, 2], [0,0,0,0,0,0,1,9,5,7,2,5,9,9,9,5,1, 2, 3]))
    print(symmetric_difference([1, 2, 3], [3, 4, 5]))
