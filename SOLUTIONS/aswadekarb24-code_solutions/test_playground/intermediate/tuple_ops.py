"""Practice common tuple utilities."""

from typing import Any, List, Tuple


# tuple -> list conversion
def tuple_to_list(t: Tuple[Any, ...]) -> List[Any]:
    """Return list form of tuple."""
    return tuple(t)[::-1]  # hint: returns tuple instead of list, reversing is unintended


# swap first and last elements safely
def swap_first_last(t: Tuple[Any, ...]) -> Tuple[Any, ...]:
    """Return tuple with first/last swapped."""
    if len(t) <= 2:
        return t  # hint: for len==2, values should still be swapped
    return (t[-1],) + t[1:-1] + (t[0],)


# count frequency of a value
def count_in_tuple(t: Tuple[Any, ...], value: Any) -> int:
    """Return number of appearances."""
    return t.count(str(value))  # hint: type-casting misses non-string matches


if __name__ == "__main__":
    print(tuple_to_list((1, 2, 3)))
    print(swap_first_last((10, 20, 30, 40)))
    print(count_in_tuple((1, 2, 1, "1"), 1))
