# lagrange_polynomial.py
import numpy as np
from typing import Tuple


def lagrange_polynomial(x_data: np.ndarray, y_data: np.ndarray, point: float) -> float:
    if x_data.shape[0] != y_data.shape[0]:
        raise ValueError("X and Y vectors must have equal number of elements.")
    if x_data.shape[0] < 1:
        raise ValueError("X and Y vectors must contain at least one element.")
    if len(np.unique(x_data)) != x_data.shape[0]:
        raise ValueError("X data must contain unique values.")
    P = 0.0
    n = x_data.shape[0]
    for i in range(n):
        L_i = 1.0
        for j in range(n):
            if j != i:
                denominator = x_data[i] - x_data[j]
                if denominator == 0:
                    raise ValueError("Duplicate x-values detected.")
                L_i *= (point - x_data[j]) / denominator
        P += y_data[i] * L_i
    return P
