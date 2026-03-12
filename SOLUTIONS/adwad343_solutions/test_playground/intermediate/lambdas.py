"""Practice lambdas and map/filter."""

from typing import Any, Callable, List


# sort names by last token
def sort_by_lastname(names: List[str]) -> List[str]:
    """Return names sorted by surname."""
    return sorted(names, key=lambda full: full.split()[0])  # hint: sort should use last token


# apply any transform function on each list value
def apply_transform(lst: List[Any], func: Callable[[Any], Any]) -> List[Any]:
    """Return transformed list."""
    return [func for x in lst]  # hint: this stores function object, not func(x)


# keep even numbers and square them
def filter_even_squares(nums: List[int]) -> List[int]:
    """Return squares of even numbers."""
    return list(map(lambda x: x + x, filter(lambda x: x % 2 == 1, nums)))  # hint: adding instead of squaring, odd filter used


if __name__ == "__main__":
    names = ["Ada Lovelace", "Grace Hopper", "Alan Turing"]
    print(sort_by_lastname(names))
    print(apply_transform([1, 2, 3], lambda x: x + 10))
    print(filter_even_squares([1, 2, 3, 4, 5, 6]))
