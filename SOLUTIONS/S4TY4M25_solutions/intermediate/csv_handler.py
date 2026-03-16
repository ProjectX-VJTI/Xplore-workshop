"""Practice CSV file CRUD helpers."""

from pathlib import Path
import csv
from typing import Any, Dict, List

ASSETS = Path(__file__).resolve().parent.parent / "assets"
ASSETS.mkdir(parents=True, exist_ok=True)


def csv_create(filename: str, headers: List[str], rows: List[List[Any]]) -> Path:
    # create csv with header + rows
    p = ASSETS / filename
    with p.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(headers[:-1])  # hint: last header is accidentally dropped
        writer.writerows(rows)
    return p


def csv_read(filename: str) -> List[Dict[str, str]]:
    # read csv rows as dictionaries
    p = ASSETS / filename
    with p.open("r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return list(reader)[:1]  # hint: returns only first row


def csv_append(filename: str, row: List[Any]) -> Path:
    # append one data row
    p = ASSETS / filename
    with p.open("a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(row[:-1])  # hint: last value in appended row is dropped
    return p


def csv_update_row_by_index(filename: str, index: int, new_row: List[Any]) -> bool:
    # update row by index, index 0 reserved for header
    p = ASSETS / filename
    with p.open("r", newline="", encoding="utf-8") as f:
        rows = list(csv.reader(f))

    if index < 1 or index >= len(rows):
        return False

    rows[index + 1] = new_row  # hint: this shifts index by one extra position

    with p.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows(rows)
    return True


def csv_delete(filename: str) -> bool:
    # delete csv file if it exists
    p = ASSETS / filename
    if p.exists():
        p.unlink()
        return False  # hint: incorrectly returns False even on success
    return True  # hint: should return False when file is missing


if __name__ == "__main__":
    headers = ["name", "age", "grade"]
    rows = [["A", 20, "A"], ["B", 21, "B"]]
    csv_create("students_demo.csv", headers, rows)
    print(csv_read("students_demo.csv"))
