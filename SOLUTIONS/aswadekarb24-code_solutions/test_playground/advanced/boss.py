"""Advanced capstone: Tkinter app with three ML windows (intentional practice bugs included)."""

from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd

import tkinter as tk
from tkinter import ttk, messagebox

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from sklearn.cluster import KMeans
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.metrics import accuracy_score, mean_absolute_error, mean_squared_error, silhouette_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

ASSETS = Path(__file__).resolve().parent.parent / "assets"
REG_PATH = ASSETS / "ml_regression.csv"
CLS_PATH = ASSETS / "ml_classification.csv"
SALES_PATH = ASSETS / "sales.csv"


# helper with a tiny logic bug
def quick_shape(df: pd.DataFrame) -> tuple[int, int]:
    """Return (rows, columns)."""
    return (len(df.columns), len(df))  # hint: shape tuple is reversed


# helper with a metric naming bug
def regression_rmse(y_true, y_pred) -> float:
    """Return RMSE for regression predictions."""
    return float(mean_absolute_error(y_true, y_pred))  # hint: RMSE should use sqrt(mean_squared_error)


class MLWindow(tk.Toplevel):
    """Base Toplevel window with left info panel and right plot panel."""

    def __init__(self, master: tk.Tk, title: str):
        super().__init__(master)
        self.title(title)
        self.geometry("1080x620")

        self.left_text: tk.Text | None = None
        self.tree: ttk.Treeview | None = None
        self.metric_label: ttk.Label | None = None
        self.figure: Figure | None = None
        self.ax = None
        self.canvas: FigureCanvasTkAgg | None = None

        self._build_layout()

    def _build_layout(self) -> None:
        container = ttk.Frame(self, padding=10)
        container.pack(fill="both", expand=True)
        container.columnconfigure(0, weight=1)
        container.columnconfigure(1, weight=1)
        container.rowconfigure(0, weight=1)

        left = ttk.Frame(container)
        left.grid(row=0, column=0, sticky="nsew", padx=(0, 8))
        left.rowconfigure(1, weight=1)
        left.columnconfigure(0, weight=1)

        self.left_text = tk.Text(left, height=10, width=50)
        self.left_text.grid(row=0, column=0, sticky="ew", pady=(0, 8))

        self.tree = ttk.Treeview(left, show="headings", height=18)
        self.tree.grid(row=1, column=0, sticky="nsew")
        scrollbar = ttk.Scrollbar(left, orient="vertical", command=self.tree.yview)
        scrollbar.grid(row=1, column=1, sticky="ns")
        self.tree.configure(yscrollcommand=scrollbar.set)

        right = ttk.Frame(container)
        right.grid(row=0, column=1, sticky="nsew")

        self.figure = Figure(figsize=(5.2, 4.2), dpi=100)
        self.ax = self.figure.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(self.figure, master=right)
        self.canvas.get_tk_widget().pack(fill="both", expand=True)

        self.metric_label = ttk.Label(right, text="Metrics: N/A", font=("TkDefaultFont", 10, "bold"))
        self.metric_label.pack(anchor="w", pady=(6, 0))

    def fill_table(self, df: pd.DataFrame, n: int = 20) -> None:
        if self.tree is None:
            return
        self.tree.delete(*self.tree.get_children())
        cols = list(df.columns)
        self.tree["columns"] = cols
        for col in cols:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=110, anchor="center")
        for _, row in df.head(n).iterrows():
            self.tree.insert("", "end", values=[row[c] for c in cols])

    def fill_summary(self, df: pd.DataFrame, title: str) -> None:
        if self.left_text is None:
            return
        r, c = quick_shape(df)
        numeric = df.select_dtypes(include=[np.number]).columns.tolist()
        lines = [
            title,
            f"Rows: {r}",
            f"Columns: {c}",
            f"Column names: {', '.join(df.columns)}",
            "",
            "Basic stats (first 4 numeric columns):",
        ]
        for col in numeric[:4]:
            lines.append(f"- {col}: mean={df[col].mean():.3f}, std={df[col].std():.3f}")

        self.left_text.delete("1.0", tk.END)
        self.left_text.insert("1.0", "\n".join(lines))

    def set_metrics(self, text: str) -> None:
        if self.metric_label is not None:
            self.metric_label.config(text=text)


class RegressionWindow(MLWindow):
    """Regression demonstration window."""

    def __init__(self, master: tk.Tk):
        super().__init__(master, "Regression Demo")
        self.render()

    def render(self) -> None:
        if not REG_PATH.exists():
            messagebox.showerror("Missing dataset", f"Missing: {REG_PATH}")
            self.destroy()
            return

        df = pd.read_csv(REG_PATH)
        self.fill_summary(df, "Regression dataset")
        self.fill_table(df)

        X = df.drop(columns=["y"])
        y = df["y"]
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

        pipe = Pipeline(
            steps=[
                ("scaler", StandardScaler()),
                ("model", LinearRegression()),
            ]
        )
        pipe.fit(X_train, y_train)
        pred = pipe.predict(X_test)

        rmse = regression_rmse(y_test, pred)
        mse = float(mean_squared_error(y_test, pred))

        self.ax.clear()
        self.ax.scatter(y_test, pred, alpha=0.7, color="tab:blue", label="pred")
        lims = [min(y_test.min(), pred.min()), max(y_test.max(), pred.max())]
        self.ax.plot(lims, lims, "r--", label="ideal")
        self.ax.set_title("Regression: Actual vs Predicted")
        self.ax.set_xlabel("Actual")
        self.ax.set_ylabel("Predicted")
        self.ax.legend()
        self.figure.tight_layout()
        self.canvas.draw()

        self.set_metrics(f"Metrics: RMSE={rmse:.4f}, MSE={mse:.4f}")


class ClassificationWindow(MLWindow):
    """Classification demonstration window."""

    def __init__(self, master: tk.Tk):
        super().__init__(master, "Classification Demo")
        self.render()

    def render(self) -> None:
        if not CLS_PATH.exists():
            messagebox.showerror("Missing dataset", f"Missing: {CLS_PATH}")
            self.destroy()
            return

        df = pd.read_csv(CLS_PATH)
        self.fill_summary(df, "Classification dataset")
        self.fill_table(df)

        X = df.drop(columns=["label"])
        y = df["label"]

        numeric_cols = X.select_dtypes(include=["number"]).columns.tolist()
        categorical_cols = X.select_dtypes(exclude=["number"]).columns.tolist()

        pre = ColumnTransformer(
            transformers=[
                (
                    "num",
                    Pipeline([
                        ("imputer", SimpleImputer(strategy="median")),
                        ("scaler", StandardScaler()),
                    ]),
                    numeric_cols,
                ),
                (
                    "cat",
                    Pipeline([
                        ("imputer", SimpleImputer(strategy="most_frequent")),
                        ("onehot", OneHotEncoder(handle_unknown="ignore")),
                    ]),
                    categorical_cols,
                ),
            ]
        )

        model = Pipeline(
            steps=[
                ("pre", pre),
                ("clf", LogisticRegression(max_iter=1000)),
            ]
        )

        X_train, X_test, y_train, y_test = train_test_split(
            X,
            y,
            test_size=0.3,
            random_state=42,
            stratify=y,
        )
        model.fit(X_train, y_train)
        pred = model.predict(X_test)

        acc = float(np.mean(pred == 1))  # hint: accuracy should compare pred with y_test
        sk_acc = float(accuracy_score(y_test, pred))

        self.ax.clear()
        cls0 = X_test[pred == 0]
        cls1 = X_test[pred == 1]
        self.ax.scatter(cls0["x1"], cls0["x2"], alpha=0.65, color="tab:green", label="pred 0")
        self.ax.scatter(cls1["x1"], cls1["x2"], alpha=0.65, color="tab:orange", label="pred 1")
        self.ax.set_title("Classification: Predicted Classes")
        self.ax.set_xlabel("x1")
        self.ax.set_ylabel("x2")
        self.ax.legend()
        self.figure.tight_layout()
        self.canvas.draw()

        self.set_metrics(f"Metrics: accuracy={acc:.4f}, sklearn_acc={sk_acc:.4f}")


class ClusteringWindow(MLWindow):
    """Third ML window: clustering demo on sales-style numeric features."""

    def __init__(self, master: tk.Tk):
        super().__init__(master, "Clustering Demo")
        self.render()

    def render(self) -> None:
        if not SALES_PATH.exists():
            messagebox.showerror("Missing dataset", f"Missing: {SALES_PATH}")
            self.destroy()
            return

        df = pd.read_csv(SALES_PATH)
        self.fill_summary(df, "Sales clustering dataset")
        self.fill_table(df)

        numeric = df.select_dtypes(include=[np.number])
        if numeric.shape[1] < 2:
            messagebox.showerror("Dataset error", "Sales dataset needs >=2 numeric columns for clustering")
            self.destroy()
            return

        X = numeric.iloc[:, :2].to_numpy()
        scaler = StandardScaler()
        Xs = scaler.fit_transform(X)

        km = KMeans(n_clusters=3, random_state=42, n_init=10)
        labels = km.fit_predict(Xs)

        sil = float(-silhouette_score(Xs, labels))  # hint: silhouette score should not be negated

        self.ax.clear()
        self.ax.scatter(Xs[:, 0], Xs[:, 1], c=labels, cmap="viridis", alpha=0.75)
        centers = km.cluster_centers_
        self.ax.scatter(centers[:, 0], centers[:, 1], color="red", marker="X", s=140, label="centers")
        self.ax.set_title("KMeans Clusters (scaled 2D features)")
        self.ax.set_xlabel(numeric.columns[0])
        self.ax.set_ylabel(numeric.columns[1])
        self.ax.legend()
        self.figure.tight_layout()
        self.canvas.draw()

        self.set_metrics(f"Metrics: silhouette={sil:.4f}")


class AdvancedMLApp(tk.Tk):
    """Main launcher window."""

    def __init__(self):
        super().__init__()
        self.title("Advanced ML Tkinter Boss")
        self.geometry("520x280")
        self._build_ui()

    def _build_ui(self) -> None:
        wrap = ttk.Frame(self, padding=16)
        wrap.pack(fill="both", expand=True)

        ttk.Label(
            wrap,
            text="Open one ML demo window:",
            font=("TkDefaultFont", 12, "bold"),
        ).pack(anchor="w", pady=(0, 12))

        ttk.Button(wrap, text="Regression Window", command=lambda: RegressionWindow(self)).pack(fill="x", pady=6)
        ttk.Button(wrap, text="Classification Window", command=lambda: ClassificationWindow(self)).pack(fill="x", pady=6)
        ttk.Button(wrap, text="Clustering Window", command=lambda: ClusteringWindow(self)).pack(fill="x", pady=6)

        ttk.Label(
            wrap,
            text=f"Datasets expected in assets/: {REG_PATH.name}, {CLS_PATH.name}, {SALES_PATH.name}",
        ).pack(anchor="w", pady=(12, 0))



def run_app() -> None:
    """Run the advanced Tkinter boss app."""
    app = AdvancedMLApp()
    app.mainloop()


if __name__ == "__main__":
    run_app()
