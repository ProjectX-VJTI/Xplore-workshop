"""Practice pandas operations."""

from __future__ import annotations

from pathlib import Path
import numpy as np
import pandas as pd


ASSETS = Path(__file__).resolve().parent.parent / "assets"
DEFAULT_PATH = ASSETS / "students.csv"


def load_dataset(path: str = str(DEFAULT_PATH)) -> pd.DataFrame:

    file = Path(path)

    if file.exists():
        df = pd.read_csv(file)

    else:

        rng = np.random.default_rng(42)

        df = pd.DataFrame({
            "student_id": [f"S{i:03d}" for i in range(1, 13)],
            "name": [f"Student{i}" for i in range(1, 13)],
            "department": rng.choice(["CSE", "ECE", "ME"], size=12),
            "score": rng.integers(55, 100, size=12),
            "attendance": rng.integers(65, 100, size=12),
            "grade": rng.choice(["A", "B", "C", "D"], size=12)
        })

    return df