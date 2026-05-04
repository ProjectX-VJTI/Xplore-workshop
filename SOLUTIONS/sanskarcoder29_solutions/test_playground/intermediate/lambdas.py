"""Practice lambdas."""

from typing import Any, Callable, List

def sort_by_lastname(names: List[str]) -> List[str]:

    return sorted(names, key=lambda full: full.split()[-1])


def apply_transform(lst: List[Any], func: Callable[[Any], Any]) -> List[Any]:

    return [func(x) for x in lst]


def filter_even_squares(nums: List[int]) -> List[int]:

    return list(map(lambda x: x * x, filter(lambda x: x % 2 == 0, nums)))