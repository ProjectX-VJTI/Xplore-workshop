"""
Feature Engineering and Preprocessing Walkthrough

This script demonstrates how different preprocessing and feature engineering
techniques affect Linear Regression performance on a housing dataset.
We progressively improve the model and compare metrics visually.
"""

# -------------------- Imports --------------------
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.decomposition import PCA
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.inspection import permutation_importance
from statsmodels.stats.outliers_influence import variance_inflation_factor


TARGET_SCALE = 100_000  # California housing: value * 100k USD

# -------------------- Helper Functions --------------------
def regression_metrics(y_true, y_pred):
    # Compute regression evaluation metrics
    mae = mean_absolute_error(y_true, y_pred)
    mse = mean_squared_error(y_true, y_pred)
    rmse = np.sqrt(mse)
    r2 = r2_score(y_true, y_pred)
    return mae, mse, rmse, r2


def plot_metrics(ax, metrics, title):
    # Plot MAE, MSE, RMSE, R2 as a bar graph
    labels = ["MAE", "MSE", "RMSE", "R2"]
    colors = ["tab:blue", "tab:orange", "tab:green", "tab:red"]
    ax.bar(labels, metrics, color=colors)
    ax.set_title(title)
    ax.set_yscale("log")  # Adjust y-axis for better visualization
    stats_text = f"MAE: {metrics[0]:.2f}\nMSE: {metrics[1]:.2f}\nRMSE: {metrics[2]:.2f}\nR2: {metrics[3]:.2f}"
    ax.text(0.95, 0.95, stats_text, transform=ax.transAxes,
        fontsize=12, verticalalignment='top', horizontalalignment='right',
        bbox=dict(boxstyle='round,pad=0.5', facecolor='white', alpha=0.5))

def calculate_vif(X):
    # Compute Variance Inflation Factor for multicollinearity detection
    vif_df = pd.DataFrame()
    vif_df["feature"] = X.columns
    vif_df["VIF"] = [variance_inflation_factor(X.values, i) for i in range(X.shape[1])]
    return vif_df

def rescale_metrics(metrics, scale):
    mae, mse, rmse, r2 = metrics
    return (
        mae * scale,          # MAE in $
        mse * (scale ** 2),   # MSE in $^2
        rmse * scale,         # RMSE in $
        r2                    # R2 unchanged
    )

# -------------------- 1. Load Dataset & Split --------------------
data = fetch_california_housing(as_frame=True)
df = data.frame

X = df.drop(columns="MedHouseVal")
y = df["MedHouseVal"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.4, random_state=42
)

results = []

# -------------------- 2. Raw Linear Regression --------------------
lr_raw = LinearRegression()
lr_raw.fit(X_train, y_train)
y_pred_raw = lr_raw.predict(X_test)

results.append(regression_metrics(y_test, y_pred_raw))

# -------------------- 3. Standardized Regression --------------------
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

lr_scaled = LinearRegression()
lr_scaled.fit(X_train_scaled, y_train)
y_pred_scaled = lr_scaled.predict(X_test_scaled)

results.append(regression_metrics(y_test, y_pred_scaled))

# -------------------- 4. Feature Engineering (Correlation + PCA + VIF) --------------------
# Correlation heatmap
plt.figure()
sns.heatmap(X_train.corr(), cmap="coolwarm", annot=False)
plt.title("Feature Correlation Heatmap")
plt.show()

# PCA to observe variance explained
pca = PCA(n_components=0.95)
X_train_pca = pca.fit_transform(X_train_scaled)
X_test_pca = pca.transform(X_test_scaled)

# VIF calculation
vif_df = calculate_vif(X_train)
print(vif_df.sort_values("VIF", ascending=False))

# Example feature combination: rooms per household
X_fe = X.copy()
X_fe["RoomsPerHousehold"] = X_fe["AveRooms"] / (X_fe["HouseAge"] + 1)
X_fe = X_fe.drop(columns=["AveRooms"])

X_train_fe, X_test_fe, y_train_fe, y_test_fe = train_test_split(
    X_fe, y, test_size=0.25, random_state=42
)

lr_fe1 = LinearRegression()
lr_fe1.fit(X_train_fe, y_train_fe)
y_pred_fe1 = lr_fe1.predict(X_test_fe)

results.append(regression_metrics(y_test_fe, y_pred_fe1))

# -------------------- 5. Feature Importance & Outlier Removal --------------------
# Permutation feature importance
importance = permutation_importance(
    lr_fe1, X_test_fe, y_test_fe, n_repeats=10, random_state=42
)

importance_df = pd.DataFrame({
    "feature": X_test_fe.columns,
    "importance": importance.importances_mean
}).sort_values("importance")

plt.figure()
plt.barh(importance_df["feature"], importance_df["importance"])
plt.title("Feature Importances")
plt.show()

# Outlier detection using target variable
plt.figure()
sns.boxplot(y=y_train_fe)
plt.title("Target Outlier Detection")
plt.show()

# Remove extreme outliers
mask = y_train_fe < y_train_fe.quantile(0.99)
X_train_clean = X_train_fe[mask]
y_train_clean = y_train_fe[mask]

# Polynomial features for important variables
poly = PolynomialFeatures(degree=3, include_bias=False)
X_train_poly = poly.fit_transform(X_train_clean)
X_test_poly = poly.transform(X_test_fe)

"""
# first run the code normally and see last graph, then uncomment the code below and see how it changes the metrics,
# too much feature engineering can lead to overfitting, try using Ridge regression instead of Linear Regression

# Scale polynomial features
scaler = StandardScaler()
X_train_poly = scaler.fit_transform(X_train_poly)
X_test_poly = scaler.transform(X_test_poly)

# Use Ridge regression
from sklearn.linear_model import Ridge
lr_fe2 = Ridge(alpha=1.0)
lr_fe2.fit(X_train_poly, y_train_clean)
"""


lr_fe2 = LinearRegression()
lr_fe2.fit(X_train_poly, y_train_clean)


y_pred_fe2 = lr_fe2.predict(X_test_poly)

results.append(regression_metrics(y_test_fe, y_pred_fe2))

# -------------------- Final Metric Plot --------------------
titles = [
    "Raw data",
    "Standardised",
    "Feature Engineering 1",
    "Feature Engineering 2",
]

fig, axes = plt.subplots(2, 2, figsize=(12, 8))
axes = axes.flatten()

results_rescaled = [
    rescale_metrics(m, TARGET_SCALE) for m in results
]

for ax, metrics, title in zip(axes, results_rescaled, titles):
    plot_metrics(ax, metrics, title)

plt.tight_layout()
plt.show()