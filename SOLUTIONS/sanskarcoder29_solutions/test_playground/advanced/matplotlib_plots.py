"""Practice Matplotlib plotting patterns."""

from __future__ import annotations
import numpy as np
import matplotlib.pyplot as plt


def generate_data(seed: int = 42, n: int = 120):

    rng = np.random.default_rng(seed)

    x = np.linspace(0, 10, n)
    y = 2.0 * x + rng.normal(0, 2.5, size=n)

    return x, y


def line_and_scatter(ax, x, y):

    ax.plot(x, y, color="steelblue", linewidth=2, label="line")

    ax.scatter(x, y, s=18, color="tomato", alpha=0.7, label="points")

    ax.set_title("Line + Scatter")
    ax.set_xlabel("x")
    ax.set_ylabel("y")

    ax.legend()