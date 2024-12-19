# gaussian_elimination.py
import numpy as np
from typing import Tuple

def gaussian_elimination(A: np.ndarray, b: np.ndarray) -> np.ndarray:
    if A.shape[0] != A.shape[1]:
        raise ValueError("Matrix A must be square.")
    if A.shape[0] != b.shape[0]:
        raise ValueError("Matrix A and vector b dimensions do not match.")
    n: int = A.shape[0]
    augmented: np.ndarray = np.hstack((A.astype(float), b.reshape(-1, 1).astype(float)))
    for i in range(n):
        pivot: int = np.argmax(np.abs(augmented[i:, i])) + i
        if np.isclose(augmented[pivot, i], 0.0):
            raise ValueError("Matrix is singular or nearly singular.")
        if pivot != i:
            augmented[[i, pivot]] = augmented[[pivot, i]]
        augmented[i] = augmented[i] / augmented[i, i]
        for j in range(i + 1, n):
            augmented[j] -= augmented[j, i] * augmented[i]
    x: np.ndarray = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = augmented[i, -1] - np.dot(augmented[i, i + 1:n], x[i + 1:n])
    return x

def solve_gaussian_elimination(A: np.ndarray, b: np.ndarray) -> np.ndarray:
    x = gaussian_elimination(A, b)
    return np.round(x, decimals=8)

