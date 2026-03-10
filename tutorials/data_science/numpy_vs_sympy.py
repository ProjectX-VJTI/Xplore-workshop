# NumPy vs SymPy (Numeric vs Symbolic Computation)
# ------------------------------------------------
# NumPy uses floating-point approximations (fast, but subject to rounding errors).
# SymPy uses symbolic math (exact, but computationally slower).

import numpy as np
import sympy as sp
import time

print("=== 1. Linear Algebra Comparison ===")

# Create a 3x3 matrix
matrix_data = [[4, 7, 2], [3, 6, 1], [2, 5, 3]]

# NumPy (Numeric)
np_mat = np.array(matrix_data)
start_time = time.time()
np_inv = np.linalg.inv(np_mat)       # Inverse
np_det = np.linalg.det(np_mat)       # Determinant
np_eigvals, np_eigvecs = np.linalg.eig(np_mat) # Eigenvalues & Eigenvectors
np_time = time.time() - start_time

# SymPy (Symbolic)
sp_mat = sp.Matrix(matrix_data)
start_time = time.time()
sp_inv = sp_mat.inv()                # Inverse
sp_det = sp_mat.det()                # Determinant
sp_eigvals = sp_mat.eigenvals()      # Eigenvalues
sp_time = time.time() - start_time

print("\n--- Determinant ---")
print(f"NumPy Det (Approx): {np_det} | Time: {np_time:.5f}s")
print(f"SymPy Det (Exact) : {sp_det} | Time: {sp_time:.5f}s")
# Notice NumPy might return 4.999999999999998 instead of exactly 5

print("\n--- Inverse Matrix ---")
print("NumPy Inverse:\n", np_inv)
print("SymPy Inverse:\n", sp_inv)

print("\n=== 2. Numerical vs Symbolic Integration ===")
# Let's integrate f(x) = x^2 from 0 to 10. (Exact answer is 1000/3 = 333.333...)

# SymPy (Symbolic Integration)
x = sp.Symbol('x')
f_expr = x**2

start_time = time.time()
# sp.integrate(expression, (variable, lower_limit, upper_limit))
sp_integral = sp.integrate(f_expr, (x, 0, 10)) 
sp_int_time = time.time() - start_time

print(f"\nSymPy Integral: {sp_integral} (Exact)")
print(f"SymPy evaluated as float: {float(sp_integral)}")
print(f"SymPy Integration Time: {sp_int_time:.5f}s")

# NumPy (Numerical Integration using Trapezoidal Rule)
# We generate discrete points to estimate the area under the curve.
start_time = time.time()
x_vals = np.linspace(0, 10, 10000) # 10,000 points between 0 and 10
y_vals = x_vals**2
np_integral = np.trapz(y_vals, x_vals)
np_int_time = time.time() - start_time

print(f"\nNumPy Integral (Trapezoidal with 10k points): {np_integral}")
print(f"NumPy Integration Time: {np_int_time:.5f}s")
# Note: NumPy is an approximation (e.g., 333.3333333333333), but extremely fast.