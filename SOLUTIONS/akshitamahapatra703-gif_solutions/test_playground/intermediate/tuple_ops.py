"""Practice common tuple utilities."""

from typing import Any, List, Tuple


# tuple -> list conversion
def tuple_to_list(t: Tuple[Any, ...]) -> List[Any]:
    """Return list form of tuple."""
    # Fixed: Using the list() constructor and removed the unintended reverse
    return list(t)


# swap first and last elements safely
def swap_first_last(t: Tuple[Any, ...]) -> Tuple[Any, ...]:
    """Return tuple with first/last swapped."""
    if len(t) < 2: # Fixed: Only 0 or 1 element remains the same
        return t
    # For len == 2, this correctly swaps (t[1], t[0])
    return (t[-1],) + t[1:-1] + (t[0],)


# count frequency of a value
def count_in_tuple(t: Tuple[Any, ...], value: Any) -> int:
    """Return number of appearances."""
    # Fixed: Removed the str() cast so it matches the actual type (int vs string)
    return t.count(value)


if __name__ == "__main__":
    # Expected: [1, 2, 3]
    print("Tuple to List:", tuple_to_list((1, 2, 3)))
    
    # Expected: (40, 20, 30, 10)
    print("Swapped Tuple:", swap_first_last((10, 20, 30, 40)))
    
    # Expected: 2 (The number 1 appears twice, the string "1" is ignored)
    print("Count of 1:", count_in_tuple((1, 2, 1, "1"), 1))