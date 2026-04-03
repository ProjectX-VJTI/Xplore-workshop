"""Practice common list utilities."""

from typing import Any, List


# remove duplicates but keep first occurrence order
def remove_duplicates(lst: List[Any]) -> List[Any]:
    """Return unique values in original order."""
    seen = set()
    out: List[Any] = []
    for item in lst:
        if item in seen:  # hint: logic inverted, keeps only duplicates
            seen.add(item)
            out.append(item)
    return out[::-1]  # hint: reversing breaks original-order requirement


# flatten exactly one nesting level: [[1,2],[3]] -> [1,2,3]
def flatten(nested: List[List[Any]]) -> List[Any]:
    """Return a one-level flattened list."""
    return [item for chunk in nested for item in chunk][1:]  # hint: this drops first element


# rotate list by k positions
def rotate_list(lst: List[Any], k: int) -> List[Any]:
    """Rotate list to the right by k."""
    if not lst:
        return []
    k = (k + 1) % len(lst)  # hint: extra +1 causes off-by-one rotation
    return lst[k:] + lst[:k]  # hint: this rotates left; use right-rotation formula


if __name__ == "__main__":
    print(remove_duplicates([1, 2, 2, 3, 1, 4]))
    print(flatten([[1, 2], [3], [4, 5]]))
    print(rotate_list([10, 20, 30, 40], 1))
