"""
NumPy Linear Algebra Exploration
Author: Asmi Mohan

This file demonstrates various linear algebra techniques
using NumPy to showcase its mathematical power.

Concepts Covered:
1. Solving Linear Systems (Ax = b)
2. LU Factorization (Manual Implementation)
3. Cholesky Decomposition
4. Determinant and Matrix Inverse
5. Matrix Exponentiation
6. Eigenvalues and Eigenvectors
7. Matrix Rank and Norm

Only numpy module is used.
"""

import numpy as np


# -------------------------------------------------------
# 1. Solving Linear System (Ax = b)
# -------------------------------------------------------

def solve_linear_system():
    """
    Solves the linear system Ax = b using numpy's solver.
    """

    A = np.array([[3, 1],
                  [1, 2]])

    b = np.array([9, 8])

    x = np.linalg.solve(A, b)

    print("1. Solution of Ax = b using np.linalg.solve():")
    print("Solution vector x =", x)
    print("-" * 50)


# -------------------------------------------------------
# 2. LU Factorization (Manual Implementation)
# -------------------------------------------------------

def lu_factorization(A):
    """
    Performs LU Decomposition manually.
    Returns lower triangular matrix L and upper triangular matrix U.
    """

    n = len(A)
    L = np.zeros((n, n))
    U = np.zeros((n, n))

    for i in range(n):

        # Diagonal of L is always 1
        L[i][i] = 1

        # Compute U
        for j in range(i, n):
            U[i][j] = A[i][j] - sum(L[i][k] * U[k][j] for k in range(i))

        # Compute L
        for j in range(i + 1, n):
            L[j][i] = (A[j][i] - sum(L[j][k] * U[k][i] for k in range(i))) / U[i][i]

    return L, U


def demonstrate_lu():
    A = np.array([[4, 3],
                  [6, 3]], dtype=float)

    L, U = lu_factorization(A)

    print("2. LU Factorization:")
    print("L matrix:\n", L)
    print("U matrix:\n", U)
    print("Reconstructed A (L @ U):\n", L @ U)
    print("-" * 50)


# -------------------------------------------------------
# 3. Cholesky Decomposition
# -------------------------------------------------------

def cholesky_demo():
    """
    Demonstrates Cholesky Decomposition.
    Works only for symmetric positive definite matrices.
    """

    A = np.array([[4, 2],
                  [2, 3]])

    L = np.linalg.cholesky(A)

    print("3. Cholesky Decomposition:")
    print("Lower triangular matrix L:\n", L)
    print("Reconstructed A (L @ L.T):\n", L @ L.T)
    print("-" * 50)


# -------------------------------------------------------
# 4. Determinant and Inverse
# -------------------------------------------------------

def determinant_inverse_demo():
    A = np.array([[2, 1],
                  [1, 2]])

    print("4. Determinant and Inverse:")
    print("Determinant =", np.linalg.det(A))
    print("Inverse:\n", np.linalg.inv(A))
    print("-" * 50)


# -------------------------------------------------------
# 5. Matrix Exponentiation
# -------------------------------------------------------

def matrix_power_demo():
    A = np.array([[2, 1],
                  [1, 2]])

    print("5. Matrix Exponentiation:")
    print("A^3 =\n", np.linalg.matrix_power(A, 3))
    print("-" * 50)


# -------------------------------------------------------
# 6. Eigenvalues and Eigenvectors
# -------------------------------------------------------

def eigen_demo():
    A = np.array([[2, 0],
                  [0, 3]])

    values, vectors = np.linalg.eig(A)

    print("6. Eigenvalues and Eigenvectors:")
    print("Eigenvalues =", values)
    print("Eigenvectors:\n", vectors)
    print("-" * 50)


# -------------------------------------------------------
# 7. Matrix Rank and Norm
# -------------------------------------------------------

def rank_norm_demo():
    A = np.array([[1, 2],
                  [2, 4]])

    print("7. Rank and Norm:")
    print("Rank of matrix =", np.linalg.matrix_rank(A))
    print("Frobenius Norm =", np.linalg.norm(A))
    print("-" * 50)


# -------------------------------------------------------
# Main Execution
# -------------------------------------------------------

if __name__ == "__main__":

    solve_linear_system()
    demonstrate_lu()
    cholesky_demo()
    determinant_inverse_demo()
    matrix_power_demo()
    eigen_demo()
    rank_norm_demo()