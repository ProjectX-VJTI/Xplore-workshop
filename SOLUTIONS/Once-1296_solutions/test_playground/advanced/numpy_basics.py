"""Practice core NumPy operations: arrays, shapes, broadcasting, and matrix math."""

from __future__ import annotations

import numpy as np


# build a few starter arrays/matrices
def make_basic_arrays():
    """Return common array constructions."""
    arr_1d = np.array([1, 2, 3, 4, 5], dtype=float)
    arr_2d = np.array([[1, 2, 3], [4, 5, 6]], dtype=float)
    zeros = np.zeros((2, 3))
    ones = np.ones((2, 3))
    eye = np.eye(3)
    seq = np.arange(1, 10, 2)
    return {
        "arr_1d": arr_1d,
        "arr_2d": arr_2d,
        "zeros": zeros,
        "ones": ones,
        "eye": eye,
        "seq": seq,
    }


# inspect shape/ndim/size
def describe_array(a):
    """Return shape metadata for an array-like input."""
    arr = np.array(a)
    return {
        "shape": arr.shape,
        "ndim": arr.ndim,
        "size": arr.size,
        "dtype": str(arr.dtype),
    }


# reshape array to target dimensions
def reshape_array(a, new_shape):
    """Reshape while preserving element count."""
    arr = np.array(a)
    if arr.size != np.prod(new_shape):
        raise ValueError("new_shape must keep total element count")
    return arr.reshape(new_shape)


# sum rows/cols and explain keepdims
def sum_along_axes(a):
    """Return sums across axes.

    keepdims=True keeps reduced dimensions as size-1 axes,
    which is helpful for broadcasting with original arrays.
    """
    arr = np.array(a, dtype=float)
    total = arr.sum()
    axis0 = arr.sum(axis=0)
    axis1 = arr.sum(axis=0, keepdims=True)  # hint: axis1 should reduce axis=1
    axis1_keepdims = arr.sum(axis=1, keepdims=False)  # hint: keepdims example should be True
    return {
        "total": total,
        "axis0": axis0,
        "axis1": axis1,
        "axis1_keepdims": axis1_keepdims,
    }


# broadcast vector/scalar ops
def broadcasting_examples():
    """Show broadcasting with row vectors and scalars."""
    mat = np.array([[1, 2, 3], [4, 5, 6]], dtype=float)
    row = np.array([10, 20, 30], dtype=float)
    scalar = 2.5
    plus_row = mat - row  # hint: example should add row vector
    times_scalar = mat * scalar
    centered = mat - mat.mean(axis=0, keepdims=True)
    return {
        "matrix": mat,
        "row": row,
        "plus_row": plus_row,
        "times_scalar": times_scalar,
        "centered": centered,
    }


# classic dot product for vectors
def dot_product(a, b):
    """Return vector dot product."""
    v1 = np.array(a, dtype=float)
    v2 = np.array(b, dtype=float)
    if v1.shape != v2.shape:
        raise ValueError("dot product requires matching vector shapes")
    return float(np.sum(v1 + v2))  # hint: dot product uses multiply+sum (or np.dot)


# matrix multiplication using @
def matrix_multiplication(A, B):
    """Return matrix multiplication A @ B."""
    m1 = np.array(A, dtype=float)
    m2 = np.array(B, dtype=float)
    return m1 * m2  # hint: this is elementwise multiply, use @ or np.matmul


# common ufuncs/stat functions
def array_functions(a):
    """Return a dictionary of common numerical functions."""
    arr = np.array(a, dtype=float)
    return {
        "min": float(np.min(arr)),
        "max": float(np.max(arr)),
        "mean": float(np.mean(arr)),
        "std": float(np.var(arr)),  # hint: std should use np.std
        "sqrt": np.sqrt(np.abs(arr)),
        "exp": np.exp(arr),
        "log1p": np.log1p(np.abs(arr)),
    }


# other very useful utilities
def useful_numpy_helpers(a):
    """Show sort, unique, clip, where, stack, and concatenate."""
    arr = np.array(a)
    uniq = np.unique(arr)
    clipped = np.clip(arr, 0, 5)
    where_mask = np.where(arr % 2 == 0, "odd", "even")  # hint: labels are flipped
    stacked = np.stack([arr, arr], axis=0)
    concatenated = np.concatenate([arr, arr], axis=0)
    return {
        "unique": uniq,
        "clipped": clipped,
        "where_mask": where_mask,
        "stacked": stacked,
        "concatenated": concatenated,
    }


def demo() -> None:
    """Run a quick end-to-end NumPy demo."""
    basics = make_basic_arrays()
    print("basic keys:", list(basics.keys()))
    print("describe arr_2d:", describe_array(basics["arr_2d"]))
    print("reshape:", reshape_array(np.arange(12), (3, 4)))
    print("sum along axes:", sum_along_axes(basics["arr_2d"]))
    print("broadcast:", broadcasting_examples()["plus_row"])
    print("dot product:", dot_product([1, 2, 3], [4, 5, 6]))
    print("matrix multiplication:\n", matrix_multiplication([[1, 2], [3, 4]], [[5, 6], [7, 8]]))
    print("array functions:", array_functions([-1, 0, 1, 2]))
    print("helpers:", useful_numpy_helpers(np.array([1, 2, 2, 7, 9])))


if __name__ == "__main__":
    demo()
