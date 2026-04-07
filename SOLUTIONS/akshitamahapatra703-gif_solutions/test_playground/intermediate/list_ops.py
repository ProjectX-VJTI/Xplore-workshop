"""Practice common list utilities."""

from typing import Any, List

# remove duplicates but keep first occurrence order
def remove_duplicates(lst: List[Any]) -> List[Any]:
    """Return unique values in original order."""
    seen = set()
    out: List[Any] = []
    for item in lst:
        # If we HAVEN'T seen it yet, add it to our result
        if item not in seen:
            seen.add(item)
            out.append(item)
    return out # No need to reverse!

# flatten exactly one nesting level: [[1,2],[3]] -> [1,2,3]
def flatten(nested: List[List[Any]]) -> List[Any]:
    """Return a one-level flattened list using list comprehension."""
    # The original had [1:] which was cutting off the first element
    return [item for chunk in nested for item in chunk]

# rotate list by k positions to the RIGHT
def rotate_list(lst: List[Any], k: int) -> List[Any]:
    """Rotate list to the right by k."""
    if not lst:
        return []
   
    k = k % len(lst)
    # Right rotation formula: take the last k elements and put them at the front
    return lst[-k:] + lst[:-k]

if __name__ == "__main__":
    # Expected: [1, 2, 3, 4]
    print("Unique List:", remove_duplicates([1, 2, 2, 3, 1, 4]))
    
    # Expected: [1, 2, 3, 4, 5]
    print("Flattened List:", flatten([[1, 2], [3], [4, 5]]))
    
    # Expected: [40, 10, 20, 30] (Rotating [10,20,30,40] right by 1)
    print("Rotated List (Right by 1):", rotate_list([10, 20, 30, 40], 1))
