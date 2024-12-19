# thin_plate_spline_interpolation.py
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
        x[i] = augmented[i, -1] - np.dot(augmented[i, i + 1:n], x[i + 1:n])
    return x


def thin_plate_spline_interpolation(
    x_data: np.ndarray,
    y_data: np.ndarray,
    z_data: np.ndarray,
    point: Tuple[float, float]
) -> float:
    if x_data.shape[0] != y_data.shape[0] or x_data.shape[0] != z_data.shape[0]:
        raise ValueError("X, Y, and Z vectors must have equal number of elements.")
    if x_data.shape[0] < 3:
        raise ValueError("At least three points are required for thin plate spline interpolation.")
    if len(set(zip(x_data, y_data))) != x_data.shape[0]:
        raise ValueError("Duplicate (x, y) points detected.")
    
    N = x_data.shape[0]
    K = np.zeros((N, N))
    for i in range(N):
        for j in range(N):
            if i != j:
                r = np.hypot(x_data[i] - x_data[j], y_data[i] - y_data[j])
                if r == 0:
                    K[i, j] = 0
                else:
                    K[i, j] = r**2 * np.log(r)
            else:
                K[i, j] = 0
    
    P = np.vstack((np.ones(N), x_data, y_data)).T
    zero_matrix = np.zeros((3, 3))
    top = np.hstack((K, P))
    bottom = np.hstack((P.T, zero_matrix))
    system = np.vstack((top, bottom))
    
    b = np.hstack((z_data, np.zeros(3)))
    coefficients = solve_linear_system(system, b)
    w = coefficients[:N]
    a = coefficients[N:]
    
    x, y = point
    U = np.array([np.hypot(x - x_data[i], y - y_data[i])**2 * np.log(np.hypot(x - x_data[i], y - y_data[i])) if np.hypot(x - x_data[i], y - y_data[i]) > 0 else 0 for i in range(N)])
    return a[0] + a[1] * x + a[2] * y + np.dot(w, U)
