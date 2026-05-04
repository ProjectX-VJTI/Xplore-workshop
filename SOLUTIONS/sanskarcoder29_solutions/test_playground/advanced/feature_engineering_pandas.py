"""Practice feature engineering workflow with pandas."""

from __future__ import annotations

from pathlib import Path
import numpy as np
import pandas as pd

ASSETS = Path(__file__).resolve().parent.parent / "assets"
DEFAULT_PATH = ASSETS / "ml_classification.csv"


def load_or_create_dataset(path: str = str(DEFAULT_PATH), n_rows: int = 250) -> pd.DataFrame:

    file = Path(path)

    if file.exists():
        df = pd.read_csv(file)

    else:
        rng = np.random.default_rng(7)

        df = pd.DataFrame({
            "age": rng.integers(21, 60, size=n_rows),
            "income": rng.normal(85000, 20000, size=n_rows).round(2),
            "experience_years": rng.integers(0, 20, size=n_rows),
            "city": rng.choice(["Delhi", "Pune", "Chennai", "Kolkata"], size=n_rows),
            "education": rng.choice(["UG", "PG", "PhD"], size=n_rows),
        })

    return df