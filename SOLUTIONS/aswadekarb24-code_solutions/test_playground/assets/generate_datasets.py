"""Generate final datasets used by workshop exercises."""

import csv
import json
import random
from datetime import date, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def generate_students(path: Path):
    # student table for pandas basics (includes stable student_id key)
    rows = [
        ("S001", "Alicia", 21, "A", 88.5, 94.0, "CSE"),
        ("S002", "Ben", 19, "B", 72.0, 81.0, "ECE"),
        ("S003", "Carmen", 22, "A", 91.2, 96.0, "CSE"),
        ("S004", "Dev", 20, "C", 60.5, 70.0, "ME"),
        ("S005", "Eli", 23, "B", 75.3, 84.0, "ECE"),
        ("S006", "Farah", 21, "A", 84.7, 90.0, "ECE"),
        ("S007", "Gio", 20, "B", 78.8, 86.0, "CSE"),
        ("S008", "Hana", 22, "A", 89.1, 93.0, "ME"),
        ("S009", "Ishan", 19, "C", 66.4, 74.0, "CSE"),
        ("S010", "Jia", 21, "B", 79.6, 88.0, "ECE"),
        ("S011", "Karan", 20, "B", 73.9, 77.0, "ME"),
        ("S012", "Lina", 22, "A", 92.4, 98.0, "CSE"),
    ]
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["student_id", "name", "age", "grade", "score", "attendance", "department"])
        writer.writerows(rows)


def generate_regression(path: Path, n=220, seed=0):
    # synthetic numeric data for regression
    random.seed(seed)
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["x1", "x2", "x3", "y"])
        for _ in range(n):
            x1 = random.uniform(-10, 10)
            x2 = random.uniform(-5, 5)
            x3 = random.uniform(0, 8)
            y = 3.5 * x1 - 1.2 * x2 + 0.8 * x3 + random.gauss(0, 2.0)
            writer.writerow([f"{x1:.5f}", f"{x2:.5f}", f"{x3:.5f}", f"{y:.5f}"])


def generate_classification(path: Path, n=260, seed=1):
    # synthetic non-linear data for classification
    random.seed(seed)
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["x1", "x2", "x3", "label"])
        for _ in range(n):
            x1 = random.uniform(-3, 3)
            x2 = random.uniform(-3, 3)
            x3 = random.uniform(0, 1)
            label = 1 if (x1 * x1 + x2 * x2 + x3) > 4.2 else 0
            if random.random() < 0.06:
                label = 1 - label
            writer.writerow([f"{x1:.4f}", f"{x2:.4f}", f"{x3:.4f}", str(label)])


def generate_algo_arrays(path: Path):
    # arrays for searching/sorting practice
    payload = {
        "sorted_lists": [[1, 2, 3, 5, 7, 9, 12], [2, 4, 6, 8, 10]],
        "unsorted_lists": [[5, 1, 3, 2, 6, 4], [10, 9, 8, 7]],
        "windows": [[1, 3, 2, 5, 8, 7, 6], [4, 2, 12, 3, 6]],
    }
    with path.open("w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2)


def generate_sales(path: Path, days: int = 45, seed: int = 2):
    # daily sales data for pandas + matplotlib
    random.seed(seed)
    start = date(2025, 1, 1)
    regions = ["North", "South", "East", "West"]
    products = ["Notebook", "Pen", "Bottle", "Bag"]

    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["date", "region", "product", "units", "unit_price", "discount", "revenue"])
        for d in range(days):
            day = start + timedelta(days=d)
            for region in regions:
                product = random.choice(products)
                units = random.randint(5, 80)
                unit_price = random.choice([20, 45, 120, 300, 950])
                discount = random.choice([0, 0.05, 0.1, 0.15])
                revenue = units * unit_price * (1 - discount)
                writer.writerow([day.isoformat(), region, product, units, unit_price, discount, f"{revenue:.2f}"])


def generate_weather(path: Path, days: int = 60, seed: int = 3):
    # weather-like time-series for plotting
    random.seed(seed)
    start = date(2025, 1, 1)
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["date", "temp_c", "humidity", "rain_mm"])
        for i in range(days):
            day = start + timedelta(days=i)
            temp = 20 + 8 * random.random() + 4 * (i % 10) / 10
            humidity = random.randint(45, 95)
            rain = max(0, random.gauss(2.5, 3.0))
            writer.writerow([day.isoformat(), f"{temp:.2f}", humidity, f"{rain:.2f}"])


def generate_attendance(path: Path, seed: int = 4):
    # mixed-type dataset for feature engineering
    random.seed(seed)
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["student", "branch", "hours_studied", "attendance_pct", "test_score"])
        for i in range(1, 51):
            branch = random.choice(["CS", "EE", "ME", "EC"])
            hours = round(random.uniform(1, 8), 2)
            attendance = round(random.uniform(55, 100), 2)
            score = round(30 + 8 * hours + 0.35 * attendance + random.gauss(0, 6), 2)
            writer.writerow([f"S{i:03d}", branch, hours, attendance, score])


def generate_cp_tests(path: Path):
    # testcases for miscellaneous CP problems
    payload = {
        "sum_pairs": {"arr": [2, 7, 11, 15], "target": 9},
        "max_subarray": [3, -2, 5, -1, 6, -3],
        "range_query": {"arr": [4, 2, 7, 1, 9, 3], "left": 1, "right": 4},
    }
    path.write_text(json.dumps(payload, indent=2), encoding="utf-8")


def generate_ds_sequences(path: Path):
    # sequences for data-structure operation smoke tests
    payload = {
        "sequence_a": [10, 20, 30, 40],
        "sequence_b": [7, 2, 9, 1, 5],
        "pairs": [["a", 1], ["b", 2], ["c", 3]],
    }
    path.write_text(json.dumps(payload, indent=2), encoding="utf-8")


def generate_cipher_cases(path: Path):
    # text/key examples for cipher practice
    payload = {
        "caesar": [
            {"text": "HelloWorld", "shift": 3},
            {"text": "Python Workshop", "shift": 5},
        ],
        "vigenere": [
            {"text": "ATTACKATDAWN", "key": "LEMON"},
            {"text": "Data Structures", "key": "KEY"},
        ],
    }
    path.write_text(json.dumps(payload, indent=2), encoding="utf-8")


def generate_chatbot_prompts(path: Path):
    # prompt examples for terminal chatbot testing
    payload = {
        "prompts": [
            "hello",
            "what is recursion?",
            "explain linked list in one line",
            "quit",
        ]
    }
    path.write_text(json.dumps(payload, indent=2), encoding="utf-8")


if __name__ == "__main__":
    print(f"Generating datasets in {ROOT}")
    generate_students(ROOT / "students.csv")
    generate_regression(ROOT / "ml_regression.csv")
    generate_classification(ROOT / "ml_classification.csv")
    generate_algo_arrays(ROOT / "algo_arrays.json")
    generate_sales(ROOT / "sales.csv")
    generate_weather(ROOT / "weather_timeseries.csv")
    generate_attendance(ROOT / "attendance.csv")
    generate_cp_tests(ROOT / "cp_tests.json")
    generate_ds_sequences(ROOT / "ds_sequences.json")
    generate_cipher_cases(ROOT / "cipher_cases.json")
    generate_chatbot_prompts(ROOT / "chatbot_prompts.json")
    print(
        "Done. Files created: students.csv, ml_regression.csv, ml_classification.csv, "
        "algo_arrays.json, sales.csv, weather_timeseries.csv, attendance.csv, "
        "cp_tests.json, ds_sequences.json, cipher_cases.json, chatbot_prompts.json"
    )
