"""Practice CSV file CRUD helpers."""

from pathlib import Path
import csv
from typing import Any, Dict, List

ASSETS = Path(__file__).resolve().parent.parent / "assets"
ASSETS.mkdir(parents=True, exist_ok=True)


def csv_create(filename: str, headers: List[str], rows: List[List[Any]]) -> Path:
    """Create CSV with headers and rows."""
    p = ASSETS / filename
    with p.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(headers)  
        writer.writerows(rows)
    return p


def csv_read(filename: str) -> List[Dict[str, str]]:
    """Read CSV rows as dictionaries."""
    p = ASSETS / filename
    if not p.exists():
        return []
    with p.open("r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return list(reader)


def csv_append(filename: str, row: List[Any]) -> Path:
    """Append one data row."""
    p = ASSETS / filename
    with p.open("a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(row)
    return p


def csv_update_row_by_index(filename: str, index: int, new_row: List[Any]) -> bool:
    """Update row by index (where index 1 is the first data row after header)."""
    p = ASSETS / filename
    if not p.exists():
        return False

    with p.open("r", newline="", encoding="utf-8") as f:
        rows = list(csv.reader(f))

    if index < 1 or index >= len(rows):
        return False

    rows[index] = new_row  

    with p.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows(rows)
    return True


def csv_delete(filename: str) -> bool:
    """Delete CSV file if it exists."""
    p = ASSETS / filename
    if p.exists():
        p.unlink()
        return True  
    return False  #


if __name__ == "__main__":
    headers = ["name", "age", "grade"]
    rows = [["Akshita", 18, "A"], ["Virat", 19, "B"]]
    
    csv_create("students_demo.csv", headers, rows)
    
    
    csv_append("students_demo.csv", ["Rohit", 20, "A"])
    csv_update_row_by_index("students_demo.csv", 1, ["Akshita", 19, "O"]) 
    
    print("CSV Content as Dicts:")
    print(csv_read("students_demo.csv"))
