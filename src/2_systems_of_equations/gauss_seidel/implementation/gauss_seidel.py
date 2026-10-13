import warnings
import numpy as np
from typing import Optional


def gauss_seidel(
    A: np.ndarray,
    b: np.ndarray,
    x0: Optional[np.ndarray] = None,
    epsilon: float = 1e-8,
    max_iterations: int = 100,
    max_iter: Optional[int] = None,
) -> np.ndarray:
    """
    Gauss-Seidel iteration for Ax = b.

    Stops when ||x_new - x_prev||_2 < epsilon.

    Args:
        max_iterations: Maximum number of sweeps (same name as jacobi_method).
        max_iter: Deprecated alias of max_iterations; overrides it if given.

    Raises:
        ValueError: If A is not square, has a zero diagonal entry, or the
            iteration does not converge within max_iterations sweeps.
    """
    if max_iter is not None:
        warnings.warn(
            "'max_iter' is deprecated; use 'max_iterations' instead.",
            DeprecationWarning,
            stacklevel=2,
        )
        max_iterations = max_iter
    if A.shape[0] != A.shape[1]:
        raise ValueError("Matrix A must be square.")
    if np.any(np.diag(A) == 0):
        raise ValueError("Matrix A has zero diagonal elements.")
    n: int = A.shape[0]
    x: np.ndarray = (
        np.zeros_like(b, dtype=np.double) if x0 is None else x0.astype(float)
    )
    for _ in range(max_iterations):
        x_prev: np.ndarray = x.copy()
        for i in range(n):
            x[i] = (
                b[i] - np.dot(A[i, :i], x[:i]) - np.dot(A[i, i + 1 :], x_prev[i + 1 :])
            ) / A[i, i]
        if np.linalg.norm(x - x_prev) < epsilon:
            return x
    raise ValueError(
        "Gauss-Seidel method did not converge within the maximum number of iterations."
    )
