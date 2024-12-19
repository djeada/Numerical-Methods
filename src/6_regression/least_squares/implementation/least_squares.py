# least_squares.py
import numpy as np
from typing import Tuple


def solve_linear_system(A: np.ndarray, b: np.ndarray) -> np.ndarray:
    n = A.shape[0]
    augmented = np.hstack((A.astype(float), b.reshape(-1, 1).astype(float)))
    for i in range(n):
        max_row = np.argmax(np.abs(augmented[i:, i])) + i
        if np.isclose(augmented[max_row, i], 0.0):
            raise ValueError("Matrix is singular or nearly singular.")
        if max_row != i:
            augmented[[i, max_row]] = augmented[[max_row, i]]
        augmented[i] = augmented[i] / augmented[i, i]
        for j in range(i + 1, n):
            augmented[j] -= augmented[j, i] * augmented[i]
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = augmented[i, -1] - np.dot(augmented[i, i + 1:n], x[i + 1:n])
    return x


def least_squares(A: np.ndarray, b: np.ndarray) -> np.ndarray:
    if A.ndim != 2 or A.shape[0] < A.shape[1]:
        raise ValueError("Matrix A must have at least as many rows as columns.")
    if A.shape[0] != b.shape[0]:
        raise ValueError("The number of rows in A must match the size of vector b.")
    At = A.T
    AtA = At @ A
    Atb = At @ b
    return solve_linear_system(AtA, Atb)
