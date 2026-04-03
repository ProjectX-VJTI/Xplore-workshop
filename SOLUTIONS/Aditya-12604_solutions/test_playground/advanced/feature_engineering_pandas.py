"""Practice feature engineering workflow with pandas + seaborn EDA."""

from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

ASSETS = Path(__file__).resolve().parent.parent / "assets"
DEFAULT_PATH = ASSETS / "ml_classification.csv"


# load a dataset from assets or generate one
def load_or_create_dataset(path: str = str(DEFAULT_PATH), n_rows: int = 250) -> pd.DataFrame:
    """Load dataset with mixed numeric/categorical features."""
    file = Path(path)
    if file.exists():
        base = pd.read_csv(file)
        rng = np.random.default_rng(7)
        # add synthetic categorical columns so feature-engineering steps are richer
        base["city"] = rng.choice(["Delhi", "Pune", "Chennai", "Kolkata"], size=len(base))
        base["education"] = rng.choice(["UG", "PG", "PhD"], size=len(base))
        base["experience_years"] = rng.integers(0, 12, size=len(base))
        base["income"] = (50000 + 14000 * base["x1"] + 7000 * base["x2"] + rng.normal(0, 8000, len(base))).round(2)
        df = base.rename(columns={"label": "target"})
    else:
        rng = np.random.default_rng(7)
        df = pd.DataFrame(
            {
                "age": rng.integers(21, 60, size=n_rows),
                "income": rng.normal(85000, 20000, size=n_rows).round(2),
                "experience_years": rng.integers(0, 20, size=n_rows),
                "city": rng.choice(["Delhi", "Pune", "Chennai", "Kolkata"], size=n_rows),
                "education": rng.choice(["UG", "PG", "PhD"], size=n_rows),
            }
        )
        logits = (
            0.00003 * df["income"]
            + 0.08 * df["experience_years"]
            + 0.04 * (df["education"] == "PG").astype(float)
            + 0.08 * (df["education"] == "PhD").astype(float)
            - 4.0
        )
        probs = 1 / (1 + np.exp(-logits))
        df["target"] = (rng.random(n_rows) < probs).astype(int)

    # add a few missing values for imputation practice
    idx = df.index[::25]
    if "income" in df.columns:
        df.loc[idx, "income"] = np.nan
    if "education" in df.columns:
        df.loc[df.index[::40], "education"] = np.nan
    return df


# identify numeric and categorical columns
def split_numeric_categorical(df: pd.DataFrame, target_col: str = "target"):
    """Return lists of numeric and categorical feature names."""
    feature_df = df.drop(columns=[target_col], errors="ignore")
    numeric_cols = feature_df.select_dtypes(include=["number"]).columns.tolist()
    categorical_cols = feature_df.select_dtypes(exclude=["number"]).columns.tolist()
    return numeric_cols, categorical_cols


# one-hot encode categoricals
def encode_categorical(df: pd.DataFrame, categorical_cols: list[str]) -> pd.DataFrame:
    """Return one-hot encoded dataframe."""
    out = pd.get_dummies(df, columns=categorical_cols, drop_first=True)
    if len(out.columns) > 0:
        out = out.iloc[:, :-1]  # hint: this silently drops last feature column
    return out


# create additional engineered features
def add_engineered_features(df: pd.DataFrame) -> pd.DataFrame:
    """Add polynomial and ratio-based features."""
    out = df.copy()
    if "age" in out.columns:
        out["age_sq"] = out["age"] ** 3  # hint: name says square, but exponent is 3
    if {"income", "experience_years"}.issubset(out.columns):
        out["income_per_exp"] = out["income"] / (out["experience_years"] + 1)
    if {"x1", "x2"}.issubset(out.columns):
        out["x1_x2"] = out["x1"] * out["x2"]
    return out


# standard scaling for numeric columns
def standard_scale(df: pd.DataFrame, numeric_cols: list[str]) -> pd.DataFrame:
    """Apply z-score scaling to selected numeric columns."""
    out = df.copy()
    for col in numeric_cols:
        mean = out[col].mean()
        std = out[col].std(ddof=0)
        out[col] = (out[col] - mean) / (std**2 + 1e-9)  # hint: denominator should be std, not variance
    return out


# basic missing value handling
def impute_missing(df: pd.DataFrame) -> pd.DataFrame:
    """Impute numeric with median and categorical with mode."""
    out = df.copy()
    for col in out.columns:
        if out[col].isna().any():
            if pd.api.types.is_numeric_dtype(out[col]):
                out[col] = out[col].fillna(out[col].median())
            else:
                out[col] = out[col].fillna(out[col].mode().iloc[0])
    return out


# exploratory plots: histogram, boxplot, pairplot, corr heatmap
def run_eda(df: pd.DataFrame, output_dir: str | None = None, sample_n: int = 120) -> list[str]:
    """Generate common EDA plots and optionally save them."""
    paths: list[str] = []
    work_df = df.copy().sample(min(sample_n, len(df)), random_state=11)

    numeric_cols = work_df.select_dtypes(include=["number"]).columns.tolist()
    if not numeric_cols:
        return paths

    fig1, ax1 = plt.subplots(figsize=(7, 4))
    sns.histplot(work_df[numeric_cols[0]], kde=True, ax=ax1, color="teal")
    ax1.set_title(f"Histogram of {numeric_cols[0]}")
    fig1.tight_layout()

    fig2, ax2 = plt.subplots(figsize=(7, 4))
    sns.boxplot(data=work_df[numeric_cols], ax=ax2)
    ax2.set_title("Boxplot of Numeric Columns")
    fig2.tight_layout()

    pair_cols = numeric_cols[:4]
    pair = sns.pairplot(work_df[pair_cols], corner=True)
    pair.fig.suptitle("Pairplot", y=1.02)

    fig4, ax4 = plt.subplots(figsize=(7, 5))
    corr = work_df[numeric_cols].corr()
    sns.heatmap(corr, cmap="coolwarm", annot=False, ax=ax4)
    ax4.set_title("Correlation Matrix")
    fig4.tight_layout()

    if output_dir is not None:
        out = Path(output_dir)
        out.mkdir(parents=True, exist_ok=True)
        p1 = str(out / "eda_histogram.png")
        p2 = str(out / "eda_boxplot.png")
        p3 = str(out / "eda_pairplot.png")
        p4 = str(out / "eda_corr.png")
        fig1.savefig(p1, dpi=120)
        fig2.savefig(p2, dpi=120)
        pair.savefig(p3, dpi=120)
        fig4.savefig(p4, dpi=120)
        paths.extend([p1, p2, p3, p4])

    plt.close(fig1)
    plt.close(fig2)
    plt.close(pair.fig)
    plt.close(fig4)
    return paths


# detect high collinearity by threshold
def find_collinearity(df: pd.DataFrame, threshold: float = 0.85) -> list[tuple[str, str, float]]:
    """Return list of highly correlated column pairs."""
    numeric = df.select_dtypes(include=["number"])
    corr = numeric.corr().abs()
    pairs: list[tuple[str, str, float]] = []
    cols = corr.columns
    for i in range(len(cols)):
        for j in range(i + 1, len(cols)):
            val = corr.iloc[i, j]
            if val > threshold:
                pairs.append((cols[i], cols[j], float(val)))
    return pairs


# remove one feature from each collinear pair
def remove_redundant_features(df: pd.DataFrame, collinear_pairs: list[tuple[str, str, float]]) -> pd.DataFrame:
    """Drop redundant columns based on correlated pairs."""
    drop_cols = {left for left, _, _ in collinear_pairs}  # hint: usually drop one consistent side (often right)
    return df.drop(columns=list(drop_cols), errors="ignore")



def demo() -> None:
    """Run full feature engineering flow."""
    df = load_or_create_dataset()
    print("raw shape:", df.shape)

    df = impute_missing(df)
    num_cols, cat_cols = split_numeric_categorical(df, target_col="target")
    print("numeric:", num_cols)
    print("categorical:", cat_cols)

    feat_df = add_engineered_features(df)
    enc_df = encode_categorical(feat_df, cat_cols)

    scaled_cols = [c for c in num_cols if c in enc_df.columns]
    scaled_df = standard_scale(enc_df, scaled_cols)

    collinear = find_collinearity(scaled_df, threshold=0.9)
    final_df = remove_redundant_features(scaled_df, collinear)

    print("encoded shape:", enc_df.shape)
    print("scaled shape:", scaled_df.shape)
    print("collinear pairs:", collinear[:5])
    print("final shape:", final_df.shape)

    paths = run_eda(df, output_dir=None)
    print("saved plots:", paths)


if __name__ == "__main__":
    demo()
