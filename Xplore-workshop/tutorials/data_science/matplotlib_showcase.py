# Matplotlib Module (pyplot)
# --------------------------
# The granddaddy of Python data visualization. It provides both a quick, 
# state-based interface (pyplot) and a more robust, object-oriented interface.

import matplotlib.pyplot as plt
import numpy as np

# Create some basic data using NumPy
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# 1. The Pyplot Interface (Quick and Simple)
# ------------------------------------------
# Good for quick, single plots.

plt.figure(figsize=(8, 4)) # Width, height in inches

# Plotting lines with customizations
plt.plot(x, y1, color='blue', linestyle='-', linewidth=2, label='Sin(x)')
plt.plot(x, y2, color='red', linestyle='--', linewidth=2, label='Cos(x)')

# Adding labels and title
plt.title("Basic Sine and Cosine Waves")
plt.xlabel("X-axis (Values)")
plt.ylabel("Y-axis (Amplitude)")

# Adding a legend and grid
plt.legend(loc='upper right')
plt.grid(True, linestyle=':', alpha=0.6)

# plt.show() displays the plot and pauses execution until the window is closed.
# (Uncomment the line below to see the plot when running)
# plt.show() 

# Clear the current figure so it doesn't overlap with the next ones
# plt.clf()

# 2. The Object-Oriented Interface (Best Practice)
# ------------------------------------------------
# Better for multiple plots (subplots) and fine-grained control.
# 'fig' is the entire window/canvas. 'axs' are the individual plots (Axes).

fig, axs = plt.subplots(2, 2, figsize=(10, 8))
fig.suptitle("Matplotlib Subplots Demo", fontsize=16)

# Top-Left: Scatter Plot
x_scatter = np.random.rand(50)
y_scatter = np.random.rand(50)
colors = np.random.rand(50)
sizes = 1000 * np.random.rand(50)

axs[0, 0].scatter(x_scatter, y_scatter, c=colors, s=sizes, alpha=0.5, cmap='viridis')
axs[0, 0].set_title("Scatter Plot")

# Top-Right: Bar Chart
categories = ['Apples', 'Bananas', 'Cherries', 'Dates']
values = [15, 30, 10, 25]

axs[0, 1].bar(categories, values, color=['red', 'yellow', 'darkred', 'brown'])
axs[0, 1].set_title("Bar Chart")

# Bottom-Left: Histogram
data = np.random.randn(1000) # Normal distribution
axs[1, 0].hist(data, bins=30, color='purple', edgecolor='black')
axs[1, 0].set_title("Histogram")

# Bottom-Right: Pie Chart
labels = ['IT', 'Sales', 'HR', 'Marketing']
sizes = [40, 30, 15, 15]
explode = (0.1, 0, 0, 0) # "Explode" the 1st slice (IT)

axs[1, 1].pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
axs[1, 1].set_title("Pie Chart")

plt.tight_layout() # Adjusts spacing to prevent overlapping text
plt.show()