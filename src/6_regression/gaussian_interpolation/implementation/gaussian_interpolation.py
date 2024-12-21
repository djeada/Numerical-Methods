# gaussian_interpolation.py
import numpy as np
from typing import Tuple


def solve_linear_system(A: np.ndarray, b: np.ndarray) -> np.ndarray:
    n = A.shape[0]
    augmented = np.hstack((A.astype(float), b.reshape(-1, 1).astype(float)))
    for i in range(n):
        pivot = np.argmax(np.abs(augmented[i:, i])) + i
        if np.isclose(augmented[pivot, i], 0.0):
            raise ValueError("Matrix is singular or nearly singular.")
        if pivot != i:
            augmented[[i, pivot]] = augmented[[pivot, i]]
        augmented[i] = augmented[i] / augmented[i, i]
        for j in range(i + 1, n):
            augmented[j] -= augmented[j, i] * augmented[i]
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = augmented[i, -1] - np.dot(augmented[i, i + 1 : n], x[i + 1 : n])
    return x


def gaussian_interpolation(
    x_data: np.ndarray, y_data: np.ndarray, point: float
) -> float:
    if x_data.shape[0] != y_data.shape[0]:
        raise ValueError("X and Y vectors must have equal number of elements.")
    if x_data.shape[0] < 2:
        raise ValueError("At least two points are required for interpolation.")
    if len(np.unique(x_data)) != x_data.shape[0]:
        raise ValueError("X data must contain unique values.")
    if point < np.min(x_data) or point > np.max(x_data):
        raise ValueError("Point is out of bounds.")

    x_mean = np.mean(x_data)
    x_scale = np.max(np.abs(x_data - x_mean))
    x_scaled = (x_data - x_mean) / x_scale
    point_scaled = (point - x_mean) / x_scale

    vandermonde = np.vander(x_scaled, increasing=True)
    coefficients = solve_linear_system(vandermonde, y_data)
    return np.dot(coefficients, point_scaled ** np.arange(len(coefficients)))
