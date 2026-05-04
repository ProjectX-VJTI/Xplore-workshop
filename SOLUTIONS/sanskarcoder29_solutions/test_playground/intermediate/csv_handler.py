"""Practice CSV file CRUD helpers."""

from pathlib import Path
import csv
from typing import Any, Dict, List

ASSETS = Path(__file__).resolve().parent.parent / "assets"
ASSETS.mkdir(parents=True, exist_ok=True)


def csv_create(filename: str, headers: List[str], rows: List[List[Any]]) -> Path:

    p = ASSETS / filename
    with p.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(rows)

    return p


def csv_read(filename: str) -> List[Dict[str, str]]:

    p = ASSETS / filename
    with p.open("r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return list(reader)


def csv_append(filename: str, row: List[Any]) -> Path:

    p = ASSETS / filename
    with p.open("a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(row)

    return p