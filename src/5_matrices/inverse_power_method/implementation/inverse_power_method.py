import numpy as np
from typing import Optional, Tuple


def inverse_power_method(
    A: np.ndarray,
    tol: float = 1e-8,
    max_iterations: int = 10000,
    x0: Optional[np.ndarray] = None,
    shift: float = 0.0,
) -> Tuple[float, np.ndarray]:
    """
    Shifted inverse iteration: find the eigenvalue of A closest to `shift`
    (the eigenvalue of smallest magnitude when shift = 0) and an eigenvector.

    Each step solves (A - shift*I) y = x and normalizes y. The error shrinks
    roughly by |lambda_closest - shift| / |lambda_next - shift| per iteration,
    where lambda_next is the second-closest eigenvalue. The returned eigenvalue
    is the Rayleigh quotient y^T A y, and iteration stops when it changes by
    less than `tol` (the eigenvector is then accurate to roughly sqrt(tol) for
    symmetric A). Raises ValueError for complex eigenvalues, a singular
    A - shift*I, or if `max_iterations` is exhausted.
    """
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

        # Also require a small residual: with eigenvalues of equal distance
        # from the shift the Rayleigh quotient can settle on a non-eigenvalue.
        residual = np.linalg.norm(A @ y - eigenvalue_new * y)
        if np.abs(eigenvalue_new - eigenvalue) < tol and residual <= np.sqrt(
            tol
        ) * np.linalg.norm(A, 2):
            return eigenvalue_new, y
        eigenvalue = eigenvalue_new
        x = y

    raise ValueError(
        "Inverse Power method did not converge within the maximum number of iterations."
    )
