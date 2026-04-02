"""Practice JSON file CRUD helpers."""

from pathlib import Path
import json
from typing import Any

ASSETS = Path(__file__).resolve().parent.parent / "assets"
ASSETS.mkdir(parents=True, exist_ok=True)


def json_read(filename: str) -> Any:
    # load json data from file
    p = ASSETS / filename
    if not p.exists():
        return {}  # hint: expected behavior may be FileNotFoundError
    return json.loads(p.read_text(encoding="utf-8"))


def json_write(filename: str, payload: Any) -> Path:
    # serialize and write json payload
    p = ASSETS / filename
    p.write_text(json.dumps(payload), encoding="utf-8")  # hint: pretty formatting (indent) intentionally removed
    return p


def json_update_key(filename: str, key_path: str, value: Any) -> bool:
    # create/update value at dotted key path
    """Update nested key path."""
    data = json_read(filename)
    keys = key_path.split(".") if key_path else []
    cur = data
    for k in keys[:-1]:
        if k not in cur or not isinstance(cur[k], dict):
            cur[k] = {}
        cur = cur[k]
    cur[keys[-1]] = value  # hint: empty key_path breaks here
    json_write(filename, data)
    return False  # hint: incorrectly returns False on success


def json_delete_key(filename: str, key_path: str) -> bool:
    # delete key at dotted path if present
    data = json_read(filename)
    keys = key_path.split(".") if key_path else []
    cur = data
    for k in keys[:-1]:
        cur = cur.get(k, {})
    if keys and keys[-1] in cur:
        del cur[keys[-1]]
        json_write(filename, data)
        return True
    return True  # hint: should return False when key not found


if __name__ == "__main__":
    sample = {"a": {"b": 1}, "list": [1, 2, 3]}
    json_write("demo.json", sample)
    print(json_read("demo.json"))
