import numpy as np
from typing import Optional, Tuple


def inverse_power_method(
    A: np.ndarray,
    tol: float = 1e-8,
    max_iterations: int = 10000,
    x0: Optional[np.ndarray] = None,
    shift: float = 0.0,
) -> Tuple[float, np.ndarray]:
    if A.shape[0] != A.shape[1]:
        raise ValueError("Matrix must be square.")

    eigenvalues = np.linalg.eigvals(A)
    if not np.all(np.abs(np.imag(eigenvalues)) < 1e-10):
        raise ValueError("Matrix has complex eigenvalues.")

    n = A.shape[0]
    I = np.eye(n)
    A_shifted = A - shift * I

    if x0 is None:
        x = np.random.rand(n)
    else:
        x = x0.astype(float)

    x /= np.linalg.norm(x)
    eigenvalue = 0.0

    for iteration in range(max_iterations):
        try:
            y = np.linalg.solve(A_shifted, x)
        except np.linalg.LinAlgError:
            raise ValueError(
                "Matrix (A - shift * I) is singular and cannot be inverted."
            )

        y_norm = np.linalg.norm(y)
        if y_norm == 0:
            raise ValueError("Encountered zero vector during iterations.")
        y /= y_norm

        eigenvalue_new = np.dot(y, A @ y)

        if np.abs(eigenvalue_new - eigenvalue) < tol:
            return eigenvalue_new, y
        eigenvalue = eigenvalue_new
        x = y

    raise ValueError(
        "Inverse Power method did not converge within the maximum number of iterations."
    )
