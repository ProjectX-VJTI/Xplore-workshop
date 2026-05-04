"""Practice dictionary utilities."""

from typing import Any, Dict, Iterable

def invert_dict(d: Dict[Any, Any]) -> Dict[Any, Any]:
    return {v: k for k, v in d.items()}

def merge_dicts(dicts: Iterable[Dict[Any, Any]]) -> Dict[Any, Any]:

    merged = {}
    for chunk in dicts:
        for k, v in chunk.items():
            merged[k] = v

    return merged

def count_keys_with_prefix(d: Dict[str, Any], prefix: str) -> int:

    if not prefix:
        return len(d)

    return sum(1 for key in d if key.startswith(prefix))