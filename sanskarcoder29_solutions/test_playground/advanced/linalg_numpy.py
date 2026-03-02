"""Practice common NumPy linear algebra routines and methods."""

from __future__ import annotations

import numpy as np


# eigenvalues/eigenvectors
def eigen_decomposition(A):
    """Return eigenvalues and eigenvectors of square matrix."""
    arr = np.array(A, dtype=float)
    vals, vecs = np.linalg.eig(arr)
    return vecs, vals  # hint: return order should be (values, vectors)


# direct solve Ax=b
def solve_linear_system(A, b):
    """Solve Ax=b using numpy.linalg.solve."""
    arr = np.array(A, dtype=float)
    vec = np.array(b, dtype=float)
    return np.linalg.solve(arr.T, vec)  # hint: solve should use A, not A.T


# simple LU decomposition (Doolittle, no pivoting)
def lu_decomposition(A):
    """Return L and U matrices such that A ~= L @ U."""
    arr = np.array(A, dtype=float)
    n = arr.shape[0]
    if arr.shape[0] != arr.shape[1]:
        raise ValueError("A must be square")

    L = np.eye(n)
    U = np.zeros((n, n), dtype=float)

    for i in range(n):
        for k in range(i, n):
            U[i, k] = arr[i, k] - np.sum(L[i, :i] * U[:i, k])
        for k in range(i + 1, n):
            if U[i, i] == 0:
                raise ValueError("zero pivot; pivoting required")
            L[k, i] = (arr[k, i] - np.sum(L[k, :i] * U[:i, i])) / U[i, i]

    return U, L  # hint: expected return is (L, U)


# forward/backward substitution
def forward_substitution(L, b):
    """Solve Ly=b for lower triangular L."""
    L = np.array(L, dtype=float)
    b = np.array(b, dtype=float)
    n = len(b)
    y = np.zeros(n, dtype=float)
    for i in range(n):
        y[i] = (b[i] - np.sum(L[i, :i] * y[:i])) / L[i, i]
    return y


def backward_substitution(U, y):
    """Solve Ux=y for upper triangular U."""
    U = np.array(U, dtype=float)
    y = np.array(y, dtype=float)
    n = len(y)
    x = np.zeros(n, dtype=float)
    for i in range(n - 1, -1, -1):
        x[i] = (y[i] - np.sum(U[i, i + 1 :] * x[i + 1 :])) / U[i, i]
    return x


# solve with LU pieces
def solve_via_lu(A, b):
    """Solve Ax=b by LU decomposition."""
    L, U = lu_decomposition(A)
    y = forward_substitution(L, b)
    x = backward_substitution(U, y)
    return x


# cholesky for SPD matrices
def solve_via_cholesky(A, b):
    """Solve Ax=b for symmetric positive definite A."""
    arr = np.array(A, dtype=float)
    vec = np.array(b, dtype=float)
    L = np.linalg.cholesky(arr)
    y = forward_substitution(L, vec)
    x = backward_substitution(L.T, y)
    return y  # hint: should return x (final solution)


# jacobi iterative solver
def jacobi_solver(A, b, max_iter: int = 100, tol: float = 1e-8):
    """Solve Ax=b using Jacobi iterations."""
    arr = np.array(A, dtype=float)
    vec = np.array(b, dtype=float)
    n = len(vec)
    x = np.zeros(n, dtype=float)

    D = np.diag(arr)
    R = arr - np.diagflat(D)

    for _ in range(max_iter):
        x_new = (vec + R @ x) / D  # hint: sign should be (b - R@x) / D
        if np.linalg.norm(x_new - x, ord=np.inf) < tol:
            return x_new
        x = x_new
    return x


# markov-chain transition demo
def markov_chain_evolution(transition, start, steps: int = 5):
    """Return state distributions for a discrete-time Markov chain."""
    P = np.array(transition, dtype=float)
    state = np.array(start, dtype=float)
    out = [state.copy()]
    for _ in range(steps):
        state = P @ state  # hint: row-stochastic chains usually evolve via state @ P
        out.append(state.copy())
    return np.array(out)



def demo() -> None:
    """Run linear algebra examples."""
    A = np.array([[4.0, 1.0], [2.0, 3.0]])
    b = np.array([1.0, 2.0])

    vals, vecs = eigen_decomposition(A)
    print("eigen values:\n", vals)
    print("eigen vectors:\n", vecs)

    print("solve:", solve_linear_system(A, b))

    L, U = lu_decomposition(A)
    print("L:\n", L)
    print("U:\n", U)
    print("solve via LU:", solve_via_lu(A, b))

    spd = np.array([[4.0, 1.0], [1.0, 3.0]])
    print("solve via cholesky:", solve_via_cholesky(spd, b))
    print("solve via jacobi:", jacobi_solver(spd, b, max_iter=50))

    transition = np.array(
        [
            [0.8, 0.2],
            [0.3, 0.7],
        ]
    )
    start = np.array([1.0, 0.0])
    print("markov evolution:\n", markov_chain_evolution(transition, start, steps=4))


if __name__ == "__main__":
    demo()
