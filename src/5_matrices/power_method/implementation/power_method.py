# power_method.py
import numpy as np
from typing import Optional, Tuple

def power_method(
    A: np.ndarray,
    tol: float = 1e-8,
    max_iterations: int = 1000,
    x0: Optional[np.ndarray] = None
) -> Tuple[float, np.ndarray]:
    if A.shape[0] != A.shape[1]:
        raise ValueError("Matrix must be square.")
    n = A.shape[0]
    if x0 is None:
        x = np.ones(n)
    else:
        x = x0.astype(float)
    x /= np.linalg.norm(x)
    eigenvalue = 0.0
    for _ in range(max_iterations):
        x_new = A @ x
        x_new_norm = np.linalg.norm(x_new)
        if x_new_norm == 0:
            raise ValueError("Encountered zero vector during iterations.")
        x_new /= x_new_norm
        eigenvalue_new = x_new @ A @ x
        if np.abs(eigenvalue_new - eigenvalue) < tol:
            return eigenvalue_new, x_new
        eigenvalue = eigenvalue_new
        x = x_new
    raise ValueError("Power method did not converge within the maximum number of iterations.")
