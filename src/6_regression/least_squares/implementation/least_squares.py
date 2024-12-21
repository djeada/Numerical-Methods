
import numpy as np
from numpy.linalg import LinAlgError
from typing import Tuple

def solve_linear_system(A: np.ndarray, b: np.ndarray) -> np.ndarray:
    A = A.astype(float)
    b = b.astype(float)
    n = A.shape[0]
    augmented = np.hstack((A, b.reshape(-1, 1)))
    for i in range(n):
        max_row = np.argmax(np.abs(augmented[i:, i])) + i
        pivot = augmented[max_row, i]
        if np.isclose(pivot, 0.0, atol=1e-12):
            raise ValueError("Matrix is singular or nearly singular.")
        if max_row != i:
            augmented[[i, max_row]] = augmented[[max_row, i]]
        for j in range(i + 1, n):
            factor = augmented[j, i] / augmented[i, i]
            augmented[j] -= factor * augmented[i]
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (augmented[i, -1] - np.dot(augmented[i, i + 1:n], x[i + 1:n])) / augmented[i, i]
    return x

def least_squares(A: np.ndarray, b: np.ndarray) -> np.ndarray:
    if A.ndim != 2 or A.shape[0] < A.shape[1]:
        raise ValueError("Matrix A must have at least as many rows as columns.")
    if A.shape[0] != b.shape[0]:
        raise ValueError("The number of rows in A must match the size of vector b.")
    if np.any(np.all(A == 0, axis=1)):
        raise ValueError("Matrix A contains zero rows.")
    if np.linalg.matrix_rank(A) < A.shape[1]:
        raise ValueError("Matrix A does not have full column rank.")
    A = A.astype(float)
    b = b.astype(float)
    At = A.T
    AtA = At @ A
    Atb = At @ b
    try:
        U, s, Vt = np.linalg.svd(AtA, full_matrices=False)
        tol = max(AtA.shape) * np.finfo(s.dtype).eps * max(s)
        s_inv = np.diag([1 / si if si > tol else 0 for si in s])
        AtA_pseudo_inv = Vt.T @ s_inv @ U.T
        x = AtA_pseudo_inv @ Atb
    except LinAlgError:
        raise ValueError("Singular matrix encountered during least squares computation.")
    return x
