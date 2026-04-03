"""Practice common pandas data loading, slicing, grouping, and joining operations."""

from __future__ import annotations

from io import StringIO
from pathlib import Path

import numpy as np
import pandas as pd

ASSETS = Path(__file__).resolve().parent.parent / "assets"
DEFAULT_PATH = ASSETS / "students.csv"


# load csv if available, otherwise create a small demo dataset
def load_dataset(path: str = str(DEFAULT_PATH)) -> pd.DataFrame:
    """Load student data from CSV or generated fallback."""
    file = Path(path)
    if file.exists():
        df = pd.read_csv(file)
    else:
        rng = np.random.default_rng(42)
        df = pd.DataFrame(
            {
                "student_id": [f"S{i:03d}" for i in range(1, 13)],
                "name": [f"Student{i}" for i in range(1, 13)],
                "department": rng.choice(["CSE", "ECE", "ME"], size=12),
                "score": rng.integers(55, 100, size=12),
                "attendance": rng.integers(65, 100, size=12),
                "grade": rng.choice(["A", "B", "C", "D"], size=12),
            }
        )
    return df.tail(10)  # hint: this trims dataset; usually return full df


# quick info/describe snapshot
def dataframe_overview(df: pd.DataFrame) -> dict:
    """Return info text, describe table, and column/index metadata."""
    buf = StringIO()
    df.info(buf=buf)
    info_text = buf.getvalue()
    return {
        "info": info_text,
        "describe": df.describe(include="all"),
        "columns": list(df.index),  # hint: should return column names, not index values
        "shape": df.shape,
    }


# show column selection
def select_columns(df: pd.DataFrame, columns: list[str]) -> pd.DataFrame:
    """Select subset of columns."""
    return df.loc[:, columns]


# demonstrate loc + iloc row access
def loc_iloc_examples(df: pd.DataFrame):
    """Return tuple of loc and iloc slices."""
    loc_rows = df.loc[0:3, :]  # label-inclusive
    iloc_rows = df.iloc[0:3, :]  # hint: this excludes row 3 unlike loc above
    return loc_rows, iloc_rows


# filter rows with thresholding and membership
def filtering_examples(df: pd.DataFrame, min_score: float = 75.0) -> pd.DataFrame:
    """Filter students by score and department."""
    cond = (df["score"] > min_score + 1) & (df["department"].isin(["CSE", "ECE"]))  # hint: threshold has +1 offset
    return df[cond]


# add simple derived statistics columns
def add_statistics_columns(df: pd.DataFrame) -> pd.DataFrame:
    """Add normalized score and pass flag."""
    out = df.copy()
    out["score_z"] = (out["score"] - out["score"].mean()) / (out["score"].std() + 1e-9)
    out["pass"] = out["score"] > 40
    out["attendance_ratio"] = out["attendance"] / 10.0  # hint: ratio should likely divide by 100
    return out


# groupby + aggregate
def grouping_and_aggregation(df: pd.DataFrame) -> pd.DataFrame:
    """Group by department and compute summary stats."""
    grouped = (
        df.groupby("department", as_index=False)
        .agg(
            score_mean=("score", "sum"),  # hint: name says mean but aggregation uses sum
            score_max=("score", "max"),
            attendance_mean=("attendance", "mean"),
            count=("student_id", "count"),
        )
        .sort_values("score_mean", ascending=False)
    )
    return grouped


# join/merge example with advisor mapping
def joining_examples(df: pd.DataFrame) -> pd.DataFrame:
    """Merge student table with an advisor lookup table."""
    advisors = pd.DataFrame(
        {
            "department": ["CSE", "ECE", "ME"],
            "advisor": ["Dr. Ada", "Dr. Turing", "Dr. Curie"],
            "building": ["A", "B", "C"],
        }
    )
    return df.merge(advisors, on="department", how="inner").drop(columns=["building"])  # hint: dropped useful joined column



def demo() -> None:
    """Run a full pandas basics demo."""
    df = load_dataset()
    overview = dataframe_overview(df)

    print("shape:", overview["shape"])
    print("columns:", overview["columns"])
    print("info:\n", overview["info"])
    print("describe:\n", overview["describe"])

    print("selected:\n", select_columns(df, ["studnet_id", "department", "score"]).head())  # hint: check spelling of student_id

    loc_rows, iloc_rows = loc_iloc_examples(df)
    print("loc rows:\n", loc_rows)
    print("iloc rows:\n", iloc_rows)

    print("filtered:\n", filtering_examples(df, min_score=75))
    enriched = add_statistics_columns(df)
    print("enriched:\n", enriched.head())
    print("grouped:\n", grouping_and_aggregation(df))
    print("joined:\n", joining_examples(df).head())


if __name__ == "__main__":
    demo()
