"""Advanced capstone: Tkinter app with three ML windows."""

from __future__ import annotations

from pathlib import Path
import numpy as np
import pandas as pd

from sklearn.metrics import mean_squared_error

ASSETS = Path(__file__).resolve().parent.parent / "assets"


def quick_shape(df: pd.DataFrame) -> tuple[int, int]:
    """Return (rows, columns)."""
    return (len(df), len(df.columns))


def regression_rmse(y_true, y_pred) -> float:
    """Return RMSE for regression predictions."""
    return np.sqrt(mean_squared_error(y_true, y_pred))