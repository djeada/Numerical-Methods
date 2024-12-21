import numpy as np
from typing import Tuple


def linear_interpolation(
        x_data: np.ndarray,
        y_data: np.ndarray,
        point: float
) -> float:
    if x_data.shape[0] != y_data.shape[0]:
        raise ValueError("X and Y vectors must have equal number of elements.")
    if x_data.shape[0] < 2:
        raise ValueError("X and Y vectors must contain at least 2 elements.")
    if not np.all(np.diff(x_data) > 0):
        raise ValueError("X data must be strictly increasing.")

    if point == x_data[0]:
        return y_data[0]
    if point == x_data[-1]:
        return y_data[-1]

    idx = np.searchsorted(x_data, point) - 1
    if idx < 0 or idx >= len(x_data) - 1:
        raise ValueError("Point is outside the interpolation range.")

    x1, x2 = x_data[idx], x_data[idx + 1]
    y1, y2 = y_data[idx], y_data[idx + 1]
    return y1 + (y2 - y1) * (point - x1) / (x2 - x1)
