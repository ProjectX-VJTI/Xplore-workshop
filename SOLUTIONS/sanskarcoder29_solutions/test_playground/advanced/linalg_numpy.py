"""Practice NumPy linear algebra routines."""

from __future__ import annotations
import numpy as np


def eigen_decomposition(A):
    """Return eigenvalues and eigenvectors."""
    arr = np.array(A, dtype=float)
    vals, vecs = np.linalg.eig(arr)
    return vals, vecs


def solve_linear_system(A, b):
    """Solve Ax = b."""
    arr = np.array(A, dtype=float)
    vec = np.array(b, dtype=float)
    return np.linalg.solve(arr, vec)