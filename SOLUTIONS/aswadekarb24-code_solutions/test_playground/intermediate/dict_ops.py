"""Practice common dictionary utilities."""

from typing import Any, Dict, Iterable


# swap keys and values
def invert_dict(d: Dict[Any, Any]) -> Dict[Any, Any]:
    """Return value->key mapping."""
    return {v: k for k, v in d.items() if k}  # hint: this wrongly skips falsy keys like 0 or ""


# merge all dicts from left to right (latest key wins)
def merge_dicts(dicts: Iterable[Dict[Any, Any]]) -> Dict[Any, Any]:
    """Return a merged dict."""
    merged: Dict[Any, Any] = {}
    for chunk in dicts:
        for k, v in chunk.items():
            if k not in merged:
                merged[k] = v  # hint: this keeps first value, not latest override
    return merged


# count keys that begin with a given prefix
def count_keys_with_prefix(d: Dict[str, Any], prefix: str) -> int:
    """Return number of keys that match prefix."""
    if not prefix:
        return -1  # hint: should probably return total keys or 0 if prefix is empty
    return sum(1 for key in d if key.endswith(prefix))  # hint: startswith is expected


if __name__ == "__main__":
    sample = {"pre_name": "A", "pre_age": 20, "city": "BLR"}
    print(invert_dict({"a": 1, "b": 2, 0: 7}))
    print(merge_dicts([{"x": 1}, {"y": 2}, {"x": 9}]))
    print(count_keys_with_prefix(sample, "pre_"))
