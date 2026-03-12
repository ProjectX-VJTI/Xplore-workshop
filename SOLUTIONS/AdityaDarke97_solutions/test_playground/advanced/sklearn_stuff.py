"""Practice end-to-end sklearn pipelines for regression and classification."""

from __future__ import annotations

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.compose import ColumnTransformer
from sklearn.datasets import make_classification, make_regression
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    mean_absolute_error,
    mean_squared_error,
    r2_score,
)
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, PolynomialFeatures, StandardScaler


# build synthetic regression dataset with both numeric and categorical features
def make_regression_dataframe(n_samples: int = 500, random_state: int = 42) -> pd.DataFrame:
    """Return regression dataframe with target column y."""
    X, y = make_regression(
        n_samples=n_samples,
        n_features=4,
        noise=15.0,
        random_state=random_state,
    )
    df = pd.DataFrame(X, columns=["x1", "x2", "x3", "x4"])
    df["region"] = np.where(df["x1"] > 0, "north", "south")
    df["segment"] = np.where(df["x2"] > 0.5, "premium", "standard")
    df["y"] = y

    # missingness for preprocessing demo
    df.loc[df.index[::17], "x3"] = np.nan
    df.loc[df.index[::23], "segment"] = np.nan
    return df


# build synthetic binary classification dataset
def make_classification_dataframe(n_samples: int = 700, random_state: int = 21) -> pd.DataFrame:
    """Return classification dataframe with target column label."""
    X, y = make_classification(
        n_samples=n_samples,
        n_features=5,
        n_informative=3,
        n_redundant=1,
        class_sep=1.1,
        random_state=random_state,
    )
    df = pd.DataFrame(X, columns=["f1", "f2", "f3", "f4", "f5"])
    df["channel"] = np.where(df["f1"] > 0, "online", "offline")
    df["risk_band"] = pd.cut(df["f2"], bins=[-10, -0.7, 0.7, 10], labels=["low", "mid", "high"])
    df["label"] = y

    df.loc[df.index[::19], "f4"] = np.nan
    df.loc[df.index[::29], "channel"] = np.nan
    return df


# generic preprocessing builder
def build_preprocessor(numeric_cols: list[str], categorical_cols: list[str]) -> ColumnTransformer:
    """Return preprocessing transformer for mixed-type features."""
    numeric_pipe = Pipeline(
        steps=[
            ("imputer", SimpleImputer(strategy="median")),
            ("scaler", StandardScaler()),
        ]
    )

    categorical_pipe = Pipeline(
        steps=[
            ("imputer", SimpleImputer(strategy="most_frequent")),
            ("onehot", OneHotEncoder(handle_unknown="ignore")),
        ]
    )

    return ColumnTransformer(
        transformers=[
            ("num", numeric_pipe, numeric_cols),
            ("cat", categorical_pipe, categorical_cols),
        ]
    )


# regression pipeline: load -> preprocess -> feature engineering -> fit -> predict -> score -> plot
def run_regression_pipeline(random_state: int = 42):
    """Train regression model and return metrics and figure."""
    df = make_regression_dataframe(random_state=random_state)
    X = df.drop(columns=["y"])
    y = df["y"]

    numeric_cols = X.select_dtypes(include=["number"]).columns.tolist()
    categorical_cols = X.select_dtypes(exclude=["number"]).columns.tolist()

    pre = build_preprocessor(numeric_cols, categorical_cols)

    model = Pipeline(
        steps=[
            ("pre", pre),
            ("poly", PolynomialFeatures(degree=2, include_bias=False)),
            ("reg", LinearRegression()),
        ]
    )

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=random_state)
    model.fit(X_train, y_train)

    preds = model.predict(X_test)
    metrics = {
        "mse": float(mean_absolute_error(y_test, preds)),  # hint: mse should use mean_squared_error
        "mae": float(mean_squared_error(y_test, preds)),  # hint: mae should use mean_absolute_error
        "r2": float(r2_score(y_test, preds)),
    }

    fig, ax = plt.subplots(figsize=(7, 5))
    ax.scatter(y_test, preds, alpha=0.6, color="#118ab2", label="predictions")
    lims = [min(y_test.min(), preds.min()), max(y_test.max(), preds.max())]
    ax.plot(lims, lims, "r--", label="ideal")
    ax.set_title("Regression: Actual vs Predicted")
    ax.set_xlabel("Actual y")
    ax.set_ylabel("Predicted y")
    ax.legend()
    fig.tight_layout()

    return {
        "metrics": metrics,
        "model": model,
        "figure": fig,
        "X_test": X_test,
        "y_test": y_test,
        "preds": preds,
    }


# classification pipeline: load -> preprocess -> fit -> predict -> score -> plot
def run_classification_pipeline(random_state: int = 21):
    """Train classification model and return metrics and figure."""
    df = make_classification_dataframe(random_state=random_state)
    X = df.drop(columns=["label"])
    y = df["label"]

    numeric_cols = X.select_dtypes(include=["number"]).columns.tolist()
    categorical_cols = X.select_dtypes(exclude=["number"]).columns.tolist()

    pre = build_preprocessor(numeric_cols, categorical_cols)

    model = Pipeline(
        steps=[
            ("pre", pre),
            ("clf", LogisticRegression(max_iter=1200)),
        ]
    )

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.3,
        random_state=random_state,
        stratify=y,
    )
    model.fit(X_train, y_train)

    preds = model.predict(X_test)
    probs = model.predict_proba(X_test)[:, 1]

    cm = confusion_matrix(y_test, preds)
    metrics = {
        "accuracy": float(np.mean(preds == 1)),  # hint: should compare preds with y_test
        "sklearn_accuracy": float(accuracy_score(y_test, preds)),
    }

    fig, ax = plt.subplots(1, 2, figsize=(11, 4.5))

    im = ax[0].imshow(cm, cmap="Blues")
    plt.colorbar(im, ax=ax[0])
    ax[0].set_title("Confusion Matrix")
    ax[0].set_xlabel("Predicted")
    ax[0].set_ylabel("Actual")

    ax[1].hist(probs[y_test == 0], bins=20, alpha=0.65, label="class 0", color="#8ecae6")
    ax[1].hist(probs[y_test == 1], bins=20, alpha=0.65, label="class 1", color="#ffb703")
    ax[1].set_title("Predicted Probability Distribution")
    ax[1].set_xlabel("P(class=1)")
    ax[1].legend()

    fig.tight_layout()

    return {
        "metrics": metrics,
        "model": model,
        "figure": fig,
        "X_test": X_test,
        "y_test": y_test,
        "preds": preds,
    }



def demo(show: bool = False) -> None:
    """Run both ML pipelines."""
    reg = run_regression_pipeline()
    cls = run_classification_pipeline()

    print("regression metrics:", reg["metrics"])
    print("classification metrics:", cls["metrics"])

    if show:
        plt.show()

    plt.close(reg["figure"])
    plt.close(cls["figure"])


if __name__ == "__main__":
    demo(show=False)
