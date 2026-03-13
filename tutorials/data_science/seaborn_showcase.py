# Seaborn Module
# --------------
# Built on top of Matplotlib, Seaborn is specifically designed for statistical 
# data visualization. It integrates seamlessly with Pandas DataFrames and 
# makes complex plots look beautiful with minimal code.

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Set the default Seaborn theme (makes plots instantly look better)
sns.set_theme(style="darkgrid")

# 1. Loading Data
# ---------------
# Seaborn comes with several built-in datasets for practice.
# We'll use 'tips' (restaurant tipping data)
tips = sns.load_dataset("tips")

print("--- Tips Dataset Head ---")
print(tips.head())
# Columns: total_bill, tip, sex, smoker, day, time, size

# 2. Relational Plots (Seeing how variables relate)
# -------------------------------------------------
plt.figure(figsize=(8, 5))

# Scatterplot with 'hue' automatically coloring points based on a categorical column
sns.scatterplot(data=tips, x="total_bill", y="tip", hue="time", style="smoker", size="size")
plt.title("Total Bill vs Tip (Colored by Time)")
plt.show()
plt.close()

# 3. Distribution Plots (Seeing how data is spread out)
# -----------------------------------------------------
plt.figure(figsize=(8, 5))

# Histplot with a Kernel Density Estimate (KDE) line overlaid
sns.histplot(data=tips, x="total_bill", kde=True, hue="sex", multiple="stack")
plt.title("Distribution of Total Bills by Sex")
plt.show()
plt.close()

# 4. Categorical Plots (Comparing groups)
# ---------------------------------------
plt.figure(figsize=(8, 5))

# Boxplot: Great for visualizing the median, quartiles, and outliers
sns.boxplot(data=tips, x="day", y="total_bill", hue="smoker", palette="Set2")
plt.title("Boxplot of Total Bills by Day and Smoker Status")
plt.show()
plt.close()

# Violin plot: Similar to boxplot, but shows the full density distribution
plt.figure(figsize=(8, 5))
sns.violinplot(data=tips, x="day", y="total_bill", hue="sex", split=True, inner="quart")
plt.title("Violin Plot: Density of Bills by Day")
plt.show()
plt.close()

# 5. Matrix Plots (Heatmaps)
# --------------------------
# Heatmaps are excellent for showing correlation matrices.
plt.figure(figsize=(6, 5))

# Calculate correlation matrix (only for numeric columns)
numeric_cols = tips.select_dtypes(include=[np.number])
correlation_matrix = numeric_cols.corr()

# Annot=True prints the numbers inside the boxes, cmap sets the color theme
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", linewidths=0.5)
plt.title("Correlation Heatmap")
plt.show()