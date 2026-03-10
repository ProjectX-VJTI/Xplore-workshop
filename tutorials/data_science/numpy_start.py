# NumPy (Numerical Python)
# ------------------------
# A powerful library for numerical computing in Python. It provides support for 
# large, multi-dimensional arrays and matrices, along with a collection of 
# high-level mathematical functions to operate on these arrays.

import numpy as np
import time

# 1. Array Creation & Attributes
# ------------------------------
# 1D Array (Vector)
arr_1d = np.array([1, 2, 3, 4, 5])

# 2D Array (Matrix)
arr_2d = np.array([[1.5, 2.5, 3.5], 
                   [4.5, 5.5, 6.5]])

print("--- Attributes ---")
print("1D Array shape:", arr_1d.shape)        # (5,)
print("2D Array shape:", arr_2d.shape)        # (2, 3) - 2 rows, 3 columns
print("2D Array dimensions:", arr_2d.ndim)    # 2
print("2D Array total elements:", arr_2d.size)# 6
print("2D Array data type:", arr_2d.dtype)    # float64

# Other common creation methods
zeros_arr = np.zeros((3, 3))                  # 3x3 matrix of zeros
ones_arr = np.ones((2, 4), dtype=int)         # 2x4 matrix of ones (integers)
arange_arr = np.arange(0, 10, 2)              # [0, 2, 4, 6, 8] - similar to range()
linspace_arr = np.linspace(0, 1, 5)           # 5 evenly spaced numbers between 0 and 1

# 2. Operations & Broadcasting
# ----------------------------
# Element-wise operations
print("\n--- Operations ---")
a = np.array([10, 20, 30])
b = np.array([1, 2, 3])

print("Addition:", a + b)                     # [11, 22, 33]
print("Multiplication:", a * b)               # [10, 40, 90]
print("Scalar Math:", a ** 2)                 # [100, 400, 900]

# Broadcasting: Applying operations between arrays of different shapes
# Here, a 1D array is added to a 2D array row by row.
matrix = np.array([[1, 1, 1], [2, 2, 2]])
vector = np.array([10, 20, 30])
print("Broadcasting Add:\n", matrix + vector) 
# [[11, 21, 31],
#  [12, 22, 32]]

# 3. Performance: NumPy vs Python Lists
# -------------------------------------
# NumPy is written in C and uses contiguous memory, making it vastly faster.

print("\n--- Performance Comparison ---")
size = 10_000_000

# Using standard Python lists
list_a = list(range(size))
list_b = list(range(size))

start_time = time.time()
# Element-wise addition using list comprehension
list_c = [list_a[i] + list_b[i] for i in range(len(list_a))]
list_time = time.time() - start_time
print(f"Python List Time: {list_time:.4f} seconds")

# Using NumPy arrays
np_a = np.arange(size)
np_b = np.arange(size)

start_time = time.time()
# Element-wise addition in NumPy (Vectorized)
np_c = np_a + np_b
np_time = time.time() - start_time
print(f"NumPy Time:       {np_time:.4f} seconds")
print(f"NumPy is {list_time / np_time:.2f}x faster!")