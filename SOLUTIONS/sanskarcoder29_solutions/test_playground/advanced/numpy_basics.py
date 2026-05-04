"""Practice NumPy operations."""

from __future__ import annotations
import numpy as np


def make_basic_arrays():

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


def describe_array(a):

    arr = np.array(a)

    return {
        "shape": arr.shape,
        "ndim": arr.ndim,
        "size": arr.size,
        "dtype": str(arr.dtype),
    }