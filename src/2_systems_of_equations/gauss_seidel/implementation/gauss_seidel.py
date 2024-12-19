import numpy as np
from typing import Optional

def inverse_matrix(A: np.ndarray) -> np.ndarray:
    n: int = A.shape[0]
    AI: np.ndarray = np.hstack((A.copy(), np.eye(n)))
    for i in range(n):
        if np.abs(AI[i:, i]).max() == 0:
            raise ValueError("Matrix is singular and cannot be inverted.")
        max_row: int = np.argmax(np.abs(AI[i:, i])) + i
        AI[[i, max_row]] = AI[[max_row, i]]
        AI[i] = AI[i] / AI[i, i]
        for j in range(n):
            if i != j:
                AI[j] -= AI[j, i] * AI[i]
    return AI[:, n:]


def solve_inverse_matrix(A: np.ndarray, b: np.ndarray) -> np.ndarray:
    A_inv: np.ndarray = inverse_matrix(A)
    return A_inv @ b

def gauss_seidel(
    A: np.ndarray,
    b: np.ndarray,
    x0: Optional[np.ndarray] = None,
    epsilon: float = 1e-8,
    max_iter: int = 100
) -> np.ndarray:
    n: int = A.shape[0]
    x: np.ndarray = np.zeros_like(b, dtype=np.double) if x0 is None else x0.astype(float)
    for _ in range(max_iter):
        x_prev: np.ndarray = x.copy()
        for i in range(n):
            x[i] = (
                b[i] - np.dot(A[i, :i], x[:i]) - np.dot(A[i, i + 1 :], x_prev[i + 1 :])
            ) / A[i, i]
        if np.linalg.norm(x - x_prev) < epsilon:
            return x
    raise ValueError("Gauss-Seidel method did not converge within the maximum number of iterations.")
