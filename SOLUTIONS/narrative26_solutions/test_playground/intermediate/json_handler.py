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
        raise FileNotFoundError(p)
    return json.loads(p.read_text(encoding="utf-8"))


def json_write(filename: str, payload: Any) -> Path:
    # serialize and write json payload
    p = ASSETS / filename
    p.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    return p


def json_update_key(filename: str, key_path: str, value: Any) -> bool:
    # create/update value at dotted key path
    data = json_read(filename)
    keys = key_path.split(".") if key_path else []
    if not keys:
        return False
    cur = data
    for k in keys[:-1]:
        if k in cur and not isinstance(cur[k], dict):
            return False
        cur = cur.setdefault(k, {})
    cur[keys[-1]] = value
    json_write(filename, data)
    return True


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
    return False


if __name__ == "__main__":
    sample = {"a": {"b": 1}, "list": [1, 2, 3]}
    json_write("demo.json", sample)
    print(json_read("demo.json"))