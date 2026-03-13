# Statistics Module
# -----------------
# Provides functions for calculating mathematical statistics of numeric data.
# It's a lightweight alternative to Pandas/NumPy when you just need quick, 
# built-in statistical calculations on standard Python lists.

import statistics

data = [10, 20, 20, 30, 40, 50, 60]
print(f"Dataset: {data}")

# 1. Measures of Central Tendency
# -------------------------------
print("\n--- Central Tendency ---")

# Mean (Average)
print("Mean:", statistics.mean(data))             # 32.857...

# Median (Middle value when sorted)
print("Median:", statistics.median(data))         # 30

# Mode (Most frequent value)
print("Mode:", statistics.mode(data))             # 20
# For multimodal data (multiple values with same max frequency), use multimode
print("Multimode:", statistics.multimode([10, 10, 20, 20, 30])) # [10, 20]

# 2. Measures of Spread
# ---------------------
print("\n--- Spread / Dispersion ---")

# Variance (Average of the squared differences from the Mean)
print("Sample Variance:", statistics.variance(data)) # 323.809...

# Standard Deviation (Square root of the variance)
print("Sample StDev:", statistics.stdev(data))       # 17.994...

# Note: Use pvariance() and pstdev() if your data represents the ENTIRE population,
# rather than just a sample.

# 3. Quantiles
# ------------
print("\n--- Quantiles ---")
# Divides data into 'n' continuous intervals with equal probability.
# By default, n=4 (Quartiles).
quartiles = statistics.quantiles(data, n=4)
print("Quartiles (25%, 50%, 75%):", quartiles) # [15.0, 30.0, 45.0]