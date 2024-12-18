# qr_method.py
import numpy as np
from typing import Tuple

def qr_decomposition(A: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
    Q, R = np.linalg.qr(A)
    return Q, R

def qr_algorithm(A: np.ndarray, tol: float = 1e-8, max_iterations: int = 1000) -> np.ndarray:
    if A.shape[0] != A.shape[1]:
        raise ValueError("Matrix must be square.")
    A_k = A.copy().astype(float)
    for _ in range(max_iterations):
        Q, R = qr_decomposition(A_k)
        A_k = R @ Q
        off_diagonal = A_k - np.diag(np.diag(A_k))
        if np.linalg.norm(off_diagonal, ord='fro') < tol:
            break
    return np.diag(A_k)

def qr_algorithm_with_shifts(A: np.ndarray, tol: float = 1e-8, max_iterations: int = 1000) -> np.ndarray:
    if A.shape[0] != A.shape[1]:
        raise ValueError("Matrix must be square.")
    A_k = A.copy().astype(float)
    n = A_k.shape[0]
    for _ in range(max_iterations):
        shift = A_k[-1, -1]
        A_shifted = A_k - shift * np.eye(n)
        Q, R = qr_decomposition(A_shifted)
        A_k = R @ Q + shift * np.eye(n)
        off_diagonal = A_k - np.diag(np.diag(A_k))
        if np.linalg.norm(off_diagonal, ord='fro') < tol:
            break
    return np.diag(A_k)
