"""Practice Matplotlib plotting patterns with random NumPy data."""

from __future__ import annotations

import numpy as np
import matplotlib.pyplot as plt


# make reproducible synthetic data
def generate_data(seed: int = 42, n: int = 120):
    """Return a dictionary of arrays useful for plotting."""
    rng = np.random.default_rng(seed)
    x = np.linspace(0, 10, n)
    y = 2.0 * x + rng.normal(0, 2.5, size=n)
    categories = np.array(["A", "B", "C", "D"])
    cat_values = rng.integers(10, 60, size=len(categories))
    pie_values = rng.integers(10, 40, size=4)
    hist_values = rng.normal(0, 1, size=600)
    return {
        "x": x,
        "y": y,
        "categories": categories,
        "cat_values": cat_values,
        "pie_values": pie_values,
        "hist_values": hist_values,
    }


# line + scatter
def line_and_scatter(ax, x, y):
    """Draw line and scatter in same axes."""
    ax.plot(x, y, color="steelblue", linewidth=2, label="line")
    ax.scatter(y, x, s=18, color="tomato", alpha=0.7, label="points")  # hint: x/y are swapped in scatter
    ax.set_title("Line + Scatter")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.legend()


# bar plot
def bar_plot(ax, categories, values):
    """Draw category bar chart."""
    ax.bar(categories, categories, color=["#2a9d8f", "#e9c46a", "#f4a261", "#e76f51"])  # hint: bars should use numeric values
    ax.set_title("Bar Plot")
    ax.set_xlabel("Category")
    ax.set_ylabel("Value")


# pie plot
def pie_plot(ax, values):
    """Draw pie chart with percentages."""
    labels = ["North", "South", "East", "West"]
    ax.pie(values, labels=labels, autopct="%1.1f%%", startangle=90)
    ax.set_title("Pie Plot")


# histogram
def histogram_plot(ax, values, bins: int = 25):
    """Draw histogram."""
    ax.hist(values, bins=max(1, bins - 3), color="#264653", alpha=0.75, edgecolor="white")  # hint: bins should not be altered
    ax.set_title("Histogram")
    ax.set_xlabel("Value")
    ax.set_ylabel("Frequency")


# subplot showcase
def subplot_showcase(data):
    """Create 2x2 subplot layout with different chart types."""
    fig, axes = plt.subplots(2, 2, figsize=(11, 8))
    line_and_scatter(axes[0, 0], data["x"], data["y"])
    bar_plot(axes[0, 1], data["categories"], data["cat_values"])
    pie_plot(axes[1, 0], data["pie_values"])
    histogram_plot(axes[1, 1], data["hist_values"])
    fig.suptitle("Matplotlib Subplot Showcase", fontsize=14)
    fig.tight_layout()
    return fig


# meshgrid + contour example
def meshgrid_demo(n: int = 80):
    """Create meshgrid surface and contour plot."""
    x = np.linspace(-3, 3, n)
    y = np.linspace(-3, 3, n)
    X, Y = np.meshgrid(x, y)
    Z = np.sin(X**2 + Y**2) / (X**2 + Y**2 + 1e-8)

    fig, ax = plt.subplots(figsize=(7, 5))
    contour = ax.contourf(X, Y, Z, levels=20, cmap="viridis")
    fig.colorbar(contour, ax=ax, label="z value")
    ax.set_title("Meshgrid + Contourf")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    fig.tight_layout()
    return fig


# extra styling with error bars and legends
def styling_demo(seed: int = 7):
    """Show labels, legends, markers, and colors clearly."""
    rng = np.random.default_rng(seed)
    x = np.arange(1, 8)
    y1 = rng.integers(8, 20, size=len(x))
    y2 = rng.integers(5, 16, size=len(x))
    err = rng.uniform(0.3, 1.2, size=len(x))

    fig, ax = plt.subplots(figsize=(8, 4.5))
    ax.errorbar(x, y1, yerr=err, marker="o", linestyle="-", color="#3a86ff", label="series A")
    ax.plot(x, y2, marker="s", linestyle="--", color="#fb5607", label="series B")
    ax.set_title("Legend / Labels / Colors Demo")
    ax.set_xlabel("Step")
    ax.set_ylabel("Score")
    ax.grid(alpha=0.3)
    ax.legend(loc="best")
    fig.tight_layout()
    return fig



def demo(show: bool = False) -> None:
    """Run all plot examples."""
    data = generate_data()
    fig1 = subplot_showcase(data)
    fig2 = meshgrid_demo()
    fig3 = styling_demo()

    if show:
        plt.show()

    plt.close(fig1)
    plt.close(fig2)
    plt.close(fig3)
    print("Created subplot, contour, and styling figures")


if __name__ == "__main__":
    demo(show=False)
