"""Practice list utilities."""

from typing import Any, List


def remove_duplicates(lst: List[Any]) -> List[Any]:

    seen = set()
    out = []

    for item in lst:
        if item not in seen:
            seen.add(item)
            out.append(item)

    return out


def flatten(nested: List[List[Any]]) -> List[Any]:

    return [item for chunk in nested for item in chunk]


def rotate_list(lst: List[Any], k: int) -> List[Any]:

    if not lst:
        return []

    k = k % len(lst)

    if k == 0:
        return lst

    return lst[-k:] + lst[:-k]