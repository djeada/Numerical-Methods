import numpy as np
from typing import Any


def inverse_matrix(A: np.ndarray) -> np.ndarray:
    n: int = A.shape[0]
    AI: np.ndarray = np.hstack((A.copy(), np.eye(n)))
    for i in range(n):
        max_row: int = np.argmax(np.abs(AI[i:, i])) + i
        if AI[max_row, i] == 0:
            raise ValueError("Matrix is singular and cannot be inverted.")
        AI[[i, max_row]] = AI[[max_row, i]]
        AI[i] = AI[i] / AI[i, i]
        for j in range(n):
            if i != j:
                AI[j] -= AI[j, i] * AI[i]
    return AI[:, n:]


def solve_inverse_matrix(A: np.ndarray, b: np.ndarray) -> np.ndarray:
    A_inv: np.ndarray = inverse_matrix(A)
    return A_inv @ b
    return A_inv @ b
