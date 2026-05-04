"""Practice CSV file CRUD helpers."""
#I HAVE MODIFIED THE FUNCTION 'CSV_READ' FOR EXPLORATORY PURPOSES TO IMPLEMENT A FUNCTION THAT 
# returns a given number of rows (if not specified)
from pathlib import Path
import csv
from typing import Any, Dict, List, Optional

ASSETS = Path(__file__).resolve().parent.parent / "assets"
ASSETS.mkdir(parents=True, exist_ok=True)


def csv_create(filename: str, headers: List[str], rows: List[List[Any]]) -> Path:
    # create csv with header + rows
    p = ASSETS / filename #combines the folder 'assets' with filename
    with p.open("w", newline="", encoding="utf-8") as f: #file has been opened in write mode
        writer = csv.writer(f)
        writer.writerow(headers)  # hint: last header is accidentally dropped
        writer.writerows(rows)
    return p


def csv_read(filename: str, max: Optional[int]=5) -> List[Dict[str, str]]:
    # read csv rows as dictionaries
    p = ASSETS / filename
    with p.open("r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f) #reader is of the type dict
        if max is None:
            return list(reader)
        rows=[]
        for i, row in enumerate(reader): 
            if i>=max: 
                break
            rows.append(row)
        return list(rows)  # hint: returns only first row


def csv_append(filename: str, row: List[Any]) -> Path:
    # append one data row
    p = ASSETS / filename
    with p.open("a", newline="", encoding="utf-8") as f: #'a' means append mode which starts writing from the end
        writer = csv.writer(f)
        writer.writerow(row)  # hint: last value in appended row is dropped
    return p


def csv_update_row_by_index(filename: str, index: int, new_row: List[Any]) -> bool:
    # update row by index, index 0 reserved for header
    p = ASSETS / filename
    with p.open("r", newline="", encoding="utf-8") as f:
        rows = list(csv.reader(f))

    if index < 1 or index >= len(rows):
        return False

    rows[index] = new_row  # hint: this shifts index by one extra position

    with p.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows(rows)
    return True


def csv_delete(filename: str) -> bool:
    # delete csv file if it exists
    p = ASSETS / filename
    if p.exists():
        p.unlink()
        return True  # hint: incorrectly returns False even on success
    return False  # hint: should return False when file is missing


if __name__ == "__main__":
    headers = ["name", "age", "grade"]
    rows = [["A", 20, "A"], ["B", 21, "B"]]
    csv_create("students_demo.csv", headers, rows)
    print(csv_read("students_demo.csv", 5)) 
    #you may or may not put any number function will return 5 rows by default
    print(csv_delete("students_demo.csv"))
