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
        raise FileNotFoundError(f"{filename} not found in assets")  ## DONE -> # hint: expected behavior may be FileNotFoundError
    return json.loads(p.read_text(encoding="utf-8"))


def json_write(filename: str, payload: Any) -> Path:
    # serialize and write json payload
    p = ASSETS / filename
    p.write_text(json.dumps(payload , indent=4), encoding="utf-8") ## DONE-> # hint: pretty formatting (indent) intentionally removed
    return p


def json_update_key(filename: str, key_path: str, value: Any) -> bool:
    # create/update value at dotted key path
    """Update nested key path."""
    if not key_path:
        json_write(filename, value)
        return True

    data = json_read(filename)
    keys = key_path.split(".") if key_path else []
    cur = data
    for k in keys[:-1]:
        if k not in cur or not isinstance(cur[k], dict):
            cur[k] = {}
        cur = cur[k]
    cur[keys[-1]] = value ## DONE-> # hint: empty key_path breaks here
    json_write(filename, data)
    return True ## DONE-> # hint: incorrectly returns False on success


def json_delete_key(filename: str, key_path: str) -> bool:
    # delete key at dotted path if present
    data = json_read(filename)
    
    if not key_path: ## FIX
        return False 

    keys = key_path.split(".") if key_path else []
    cur = data
    for k in keys[:-1]:
        if not isinstance(cur, dict) or k not in cur:
            return False
        cur = cur[k]

    if isinstance(cur, dict) and keys[-1] in cur:
        del cur[keys[-1]]
        json_write(filename, data)
        return True

    return False  ## DONE-> # hint: should return False when key not found


if __name__ == "__main__":
    sample = {"a": {"b": 1}, "list": [1, 2, 3]}
    json_write("demo.json", sample)
    print(json_read("demo.json"))
