"""Practice sklearn pipelines."""

from __future__ import annotations

import numpy as np
import pandas as pd

from sklearn.datasets import make_regression


def make_regression_dataframe(n_samples: int = 500, random_state: int = 42) -> pd.DataFrame:

    X, y = make_regression(
        n_samples=n_samples,
        n_features=4,
        noise=15.0,
        random_state=random_state
    )

    df = pd.DataFrame(X, columns=["x1", "x2", "x3", "x4"])

    df["region"] = np.where(df["x1"] > 0, "north", "south")

    df["segment"] = np.where(df["x2"] > 0.5, "premium", "standard")

    df["y"] = y

    return df