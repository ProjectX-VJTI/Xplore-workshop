"""Practice common dictionary utilities."""

from typing import Any, Dict, Iterable


# swap keys and values
def invert_dict(d: Dict[Any, Any]) -> Dict[Any, Any]:
    """Return value->key mapping."""
    # Fixed: Removed the 'if k' check so keys like 0 or "" aren't skipped
    return {v: k for k, v in d.items()}


# merge all dicts from left to right (latest key wins)
def merge_dicts(dicts: Iterable[Dict[Any, Any]]) -> Dict[Any, Any]:
    """Return a merged dict."""
    merged: Dict[Any, Any] = {}
    for chunk in dicts:
        # Fixed: By updating regardless of whether k is in merged, 
        # the latest value (from the right) will correctly win.
        merged.update(chunk) 
    return merged


# count keys that begin with a given prefix
def count_keys_with_prefix(d: Dict[str, Any], prefix: str) -> int:
    """Return number of keys that match prefix."""
    if not prefix:
        return 0  # Fixed: Standard behavior is 0 if no prefix is provided
    # Fixed: Changed .endswith() to .startswith()
    return sum(1 for key in d if key.startswith(prefix))


if __name__ == "__main__":
    sample = {"pre_name": "A", "pre_age": 20, "city": "BLR"}
    
    # Expected: {1: 'a', 2: 'b', 7: 0}
    print("Inverted Dict:", invert_dict({"a": 1, "b": 2, 0: 7}))
    
    # Expected: {'x': 9, 'y': 2} (because x:9 is the latest/right-most)
    print("Merged Dict (Latest Wins):", merge_dicts([{"x": 1}, {"y": 2}, {"x": 9}]))
    
    # Expected: 2 (pre_name and pre_age)
    print("Prefix Count:", count_keys_with_prefix(sample, "pre_"))
