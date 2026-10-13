import os
import sys

import numpy as np

sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from implementation.taylor_series import taylor_series


def func(x):
    return np.sin(x)


sin_derivatives = [
    np.sin,
    np.cos,
    lambda x: -np.sin(x),
    lambda x: -np.cos(x),
]  # Derivatives of sin(x) cycle with period 4


def derivatives(k):
    """Derivative values of sin(x) at the expansion point for orders k."""
    return np.array([sin_derivatives[int(order) % 4](point) for order in k])


point = 0
n = 5  # number of terms
x = np.pi / 4

taylor_expansion = taylor_series(func, point, n, x, derivatives)
print("Taylor series expansion:")
print(taylor_expansion)
