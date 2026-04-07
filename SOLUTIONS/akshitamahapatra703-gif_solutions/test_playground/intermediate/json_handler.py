"""Practice JSON file CRUD helpers."""

from pathlib import Path
import json
from typing import Any

ASSETS = Path(__file__).resolve().parent.parent / "assets"
ASSETS.mkdir(parents=True, exist_ok=True)


def json_read(filename: str) -> Any:
    """Load JSON data from file."""
    p = ASSETS / filename
    if not p.exists():

        raise FileNotFoundError(f"No such file: {p}")
    return json.loads(p.read_text(encoding="utf-8"))


def json_write(filename: str, payload: Any) -> Path:
    """Serialize and write JSON payload with pretty formatting."""
    p = ASSETS / filename
    
    p.write_text(json.dumps(payload, indent=4), encoding="utf-8")
    return p


def json_update_key(filename: str, key_path: str, value: Any) -> bool:
    """Update nested key path (e.g., 'a.b.c')."""
    if not key_path:
        return False
        
    try:
        data = json_read(filename)
    except FileNotFoundError:
        data = {}

    keys = key_path.split(".")
    cur = data
    for k in keys[:-1]:
        if k not in cur or not isinstance(cur[k], dict):
            cur[k] = {}
        cur = cur[k]
        
    cur[keys[-1]] = value
    json_write(filename, data)
    return True 


def json_delete_key(filename: str, key_path: str) -> bool:
    """Delete key at dotted path if present."""
    if not key_path:
        return False

    try:
        data = json_read(filename)
    except FileNotFoundError:
        return False

    keys = key_path.split(".")
    cur = data
    for k in keys[:-1]:
        if isinstance(cur, dict) and k in cur:
            cur = cur[k]
        else:
            return False 

    if isinstance(cur, dict) and keys[-1] in cur:
        del cur[keys[-1]]
        json_write(filename, data)
        return True
    return False 


if __name__ == "__main__":
    sample = {"a": {"b": 1}, "list": [1, 2, 3]}
    json_write("demo.json", sample)
    
    json_update_key("demo.json", "a.c", 10)
    
    json_update_key("demo.json", "players.Virat.runs", 10000)
    
    print("Updated JSON Content:")
    print(json.dumps(json_read("demo.json"), indent=4))
