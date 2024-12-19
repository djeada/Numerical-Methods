# jacobi_method.py
import numpy as np
from typing import Optional


def jacobi_method(
    A: np.ndarray,
    b: np.ndarray,
    x0: Optional[np.ndarray] = None,
    epsilon: float = 1e-8,
    max_iterations: int = 1000
) -> np.ndarray:
    if A.shape[0] != A.shape[1]:
        raise ValueError("Matrix A must be square.")
    n = A.shape[0]
    D = np.diag(A)
    if np.any(D == 0):
        raise ValueError("Matrix A has zero diagonal elements.")
    R = A - np.diagflat(D)
    D_inv = 1.0 / D
    if x0 is None:
        x = np.zeros(n)
    else:
        x = x0.astype(float)
    for _ in range(max_iterations):
        x_new = D_inv * (b - np.dot(R, x))
        if np.linalg.norm(x_new - x, ord=np.inf) < epsilon:
            return x_new
        x = x_new
    raise ValueError("Jacobi method did not converge within the maximum number of iterations.")
