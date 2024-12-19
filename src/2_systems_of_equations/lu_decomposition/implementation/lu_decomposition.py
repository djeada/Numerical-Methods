# lu_decomposition.py
import numpy as np
from typing import Tuple

def lu_decomposition(A: np.ndarray) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    n: int = A.shape[0]
    if A.shape[0] != A.shape[1]:
        raise ValueError("Matrix A must be square.")
    P: np.ndarray = np.eye(n)
    L: np.ndarray = np.zeros((n, n), dtype=float)
    U: np.ndarray = A.copy().astype(float)
    for i in range(n):
        pivot: int = np.argmax(np.abs(U[i:, i])) + i
        if np.isclose(U[pivot, i], 0.0):
            raise ValueError("Matrix is singular.")
        if pivot != i:
            U[[i, pivot]] = U[[pivot, i]]
            P[[i, pivot]] = P[[pivot, i]]
            if i > 0:
                L[[i, pivot], :i] = L[[pivot, i], :i]
        L[i, i] = 1.0
        for j in range(i + 1, n):
            factor: float = U[j, i] / U[i, i]
            L[j, i] = factor
            U[j] -= factor * U[i]
    return P, L, U

def solve_lu(P: np.ndarray, L: np.ndarray, U: np.ndarray, b: np.ndarray) -> np.ndarray:
    Pb: np.ndarray = P @ b
    y: np.ndarray = np.zeros_like(b, dtype=float)
    n: int = L.shape[0]
    for i in range(n):
        y[i] = Pb[i] - np.dot(L[i, :i], y[:i])
    x: np.ndarray = np.zeros_like(b, dtype=float)
    for i in range(n - 1, -1, -1):
        x[i] = (y[i] - np.dot(U[i, i + 1:], x[i + 1:])) / U[i, i]
    return x
