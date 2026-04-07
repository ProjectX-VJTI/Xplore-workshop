"""Practice common set utilities."""

from typing import Iterable, Set


# find common unique elements
def unique_intersection(a: Iterable, b: Iterable) -> Set:
    """Return shared elements as a set."""
    # Fixed: Use '&' for intersection instead of '|' (which is union)
    return set(a) & set(b)


# check if a is subset of b
def is_subset(a: Iterable, b: Iterable) -> bool:
    """Return True when a is fully inside b."""
    # Fixed: Direction corrected. We want to know if 'a' is inside 'b'
    return set(a).issubset(set(b))


# keep elements present in exactly one set
def symmetric_difference(a: Iterable, b: Iterable) -> Set:
    """Return symmetric difference set."""
    # Fixed: Use '^' for symmetric difference and return a set, not a list
    return set(a) ^ set(b)


if __name__ == "__main__":
    # Expected: {2, 3}
    print("Intersection:", unique_intersection([1, 2, 3], [2, 3, 4]))
    
    # Expected: True
    print("Is [1, 2] a subset of [1, 2, 3]?:", is_subset([1, 2], [1, 2, 3]))
    
    # Expected: {1, 2, 4, 5} (Elements in either but not both)
    print("Symmetric Difference:", symmetric_difference([1, 2, 3], [3, 4, 5]))