"""Practice lambdas and map/filter."""

from typing import Any, Callable, List


# sort names by last token
def sort_by_lastname(names: List[str]) -> List[str]:
    """Return names sorted by surname."""
    # Fixed: We split the name and take the last part [-1] as the sort key
    return sorted(names, key=lambda full: full.split()[-1])


# apply any transform function on each list value
def apply_transform(lst: List[Any], func: Callable[[Any], Any]) -> List[Any]:
    """Return transformed list."""
    # Fixed: Actually CALLING the function on each element x
    return [func(x) for x in lst]


# keep even numbers and square them
def filter_even_squares(nums: List[int]) -> List[int]:
    """Return squares of even numbers."""
    # Fixed: Changed filter to check for evens (x % 2 == 0)
    # Fixed: Changed map to square (x * x) instead of add (x + x)
    return list(map(lambda x: x * x, filter(lambda x: x % 2 == 0, nums)))


if __name__ == "__main__":
    names = ["Ada Lovelace", "Grace Hopper", "Alan Turing"]
    # Expected: ['Grace Hopper', 'Ada Lovelace', 'Alan Turing'] (H, L, T)
    print("Sorted by Surname:", sort_by_lastname(names))
    
    # Expected: [11, 12, 13]
    print("Transformed List:", apply_transform([1, 2, 3], lambda x: x + 10))
    
    # Expected: [4, 16, 36] (2^2, 4^2, 6^2)
    print("Even Squares:", filter_even_squares([1, 2, 3, 4, 5, 6]))