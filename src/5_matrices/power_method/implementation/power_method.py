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
        x_old = x.copy()
        y = A @ x
        y_norm = np.linalg.norm(y)
        if y_norm == 0:
            raise ValueError("Encountered zero vector during iterations.")
        x_new = y / y_norm
        if np.dot(x_old, x_new) < 0:
            x_new = -x_new
        eigenvalue_new = np.dot(A @ x_old, x_new)
        if np.abs(eigenvalue_new - eigenvalue) < tol:
            if not np.isclose(eigenvalue_new.imag if np.iscomplex(eigenvalue_new) else 0, 0, atol=tol):
                raise ValueError("Matrix has complex eigenvalues.")
            eigenvalue_new = eigenvalue_new.real
            x_new = x_new.real
            x_new[np.abs(x_new) < 1e-10] = 0.0
            return eigenvalue_new, x_new
        eigenvalue = eigenvalue_new
        x = x_new
    raise ValueError("Power method did not converge within the maximum number of iterations.")
