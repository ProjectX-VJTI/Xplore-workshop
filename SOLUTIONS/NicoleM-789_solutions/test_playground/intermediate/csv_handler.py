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
       writer.writerow(headers)  # Includes the header row
       writer.writerows(rows)
   return p




def csv_read(filename: str) -> List[Dict[str, str]]:
   # read csv rows as dictionaries
   p = ASSETS / filename
   with p.open("r", newline="", encoding="utf-8") as f:
       reader = csv.DictReader(f)
       return list(reader)  # return all rows




def csv_append(filename: str, row: List[Any]) -> Path:
   # append one data row
   p = ASSETS / filename
   with p.open("a", newline="", encoding="utf-8") as f:
       writer = csv.writer(f)
       writer.writerow(row) 
   return p




def csv_update_row_by_index(filename: str, index: int, new_row: List[Any]) -> bool:
   # update row by index, index 0 reserved for header
   p = ASSETS / filename
   with p.open("r", newline="", encoding="utf-8") as f:
       rows = list(csv.reader(f))


   if index < 1 or index >= len(rows):
       return False


   rows[index] = new_row  # since index 0 is header.If user wants to update first data row, they should use index 1.


   with p.open("w", newline="", encoding="utf-8") as f:
       writer = csv.writer(f)
       writer.writerows(rows)
   return True




def csv_delete(filename: str) -> bool:
   # delete csv file if it exists
   p = ASSETS / filename
   if p.exists():
       p.unlink()
       return True  # return true when file is successfully deleted
   return False




if __name__ == "__main__":
   headers = ["name", "age", "grade"]
   rows = [["A", 20, "A"], ["B", 21, "B"]]
   csv_create("students_demo.csv", headers, rows)
   print(csv_read("students_demo.csv"))


