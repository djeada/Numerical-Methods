import numpy as np
from numpy.linalg import LinAlgError


def least_squares(A: np.ndarray, b: np.ndarray) -> np.ndarray:
    """Solve min ||A x - b||_2 through the normal equations A^T A x = A^T b.

    A must have at least as many rows as columns and full column rank.
    Rows of A that are entirely zero are allowed: they add nothing to
    A^T A or A^T b, so they only contribute a constant b_i^2 to the
    residual. Rank deficiency (which includes an all-zero column) is
    rejected with ValueError.
    """
    if A.ndim != 2 or A.shape[0] < A.shape[1]:
        raise ValueError("Matrix A must have at least as many rows as columns.")
    if A.shape[0] != b.shape[0]:
        raise ValueError("The number of rows in A must match the size of vector b.")
    if np.linalg.matrix_rank(A) < A.shape[1]:
        raise ValueError("Matrix A does not have full column rank.")
    A = A.astype(float)
    b = b.astype(float)
    At = A.T
    AtA = At @ A
    Atb = At @ b
    try:
        # Use the normal equations explicitly to keep the implementation educational,
        # even though solving from A directly is usually more numerically stable.
        U, s, Vt = np.linalg.svd(AtA, full_matrices=False)
        tol = max(AtA.shape) * np.finfo(s.dtype).eps * max(s)
        s_inv = np.where(s > tol, 1 / s, 0.0)
        AtA_pseudo_inv = Vt.T @ (s_inv[:, np.newaxis] * U.T)
        x = AtA_pseudo_inv @ Atb
    except LinAlgError:
        raise ValueError(
            "Singular matrix encountered during least squares computation."
        )
    return x
