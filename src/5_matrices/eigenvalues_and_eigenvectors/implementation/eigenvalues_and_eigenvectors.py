import numpy as np


def find_eigenvalues(matrix: np.ndarray) -> np.ndarray:
    """
    Compute eigenvalues by solving the characteristic polynomial det(A - λI) = 0.
    """
    if matrix.ndim != 2 or matrix.shape[0] != matrix.shape[1]:
        raise ValueError("Matrix must be square.")
    coeffs = np.poly(matrix)  # Polynomial coefficients for det(A - λI) = 0
    eigenvalues = np.roots(coeffs)  # Roots of the polynomial
    return eigenvalues


def _cluster_eigenvalues(eigenvalues: np.ndarray, scale: float):
    """
    Group computed eigenvalues into clusters of numerically repeated roots.

    A root of multiplicity m is only recovered by np.roots to about
    eps**(1/m) * scale, so m eigenvalues are declared one m-fold eigenvalue when
    they all lie within (a safety factor times) that accuracy of each other.
    Returns a list of (index_list, radius) pairs; radius is also the accuracy
    to which A - mu*I should be treated as rank deficient for that cluster.
    """
    eps = np.finfo(float).eps
    remaining = list(range(len(eigenvalues)))
    clusters = []
    while remaining:
        seed = eigenvalues[remaining[0]]
        for m in range(len(remaining), 0, -1):
            radius = 10 * scale * eps ** (1.0 / m)
            members = [i for i in remaining if abs(eigenvalues[i] - seed) <= radius]
            if len(members) >= m:
                break
        clusters.append((members, radius))
        remaining = [i for i in remaining if i not in members]
    return clusters


def find_eigenvectors(matrix: np.ndarray) -> np.ndarray:
    """
    Compute unit-norm eigenvectors; column i belongs to find_eigenvalues(matrix)[i].

    Numerically repeated eigenvalues are clustered, and the null space of
    (A - mu*I) is computed once per cluster by SVD with a scale-aware rank
    tolerance. Its orthonormal basis is spread over the cluster's columns, so a
    diagonalizable repeated eigenvalue gets a full set of independent
    eigenvectors. For a defective eigenvalue (fewer eigenvectors than the
    algebraic multiplicity) the basis vectors are reused cyclically, so the
    returned matrix is singular.
    """
    eigenvalues = find_eigenvalues(matrix)
    n = matrix.shape[0]
    A = np.asarray(matrix, dtype=complex if np.iscomplexobj(matrix) else float)
    scale = np.linalg.norm(A, 2) if n else 0.0
    eigenvectors = np.zeros((n, n), dtype=complex)

    for members, radius in _cluster_eigenvalues(eigenvalues, scale):
        mu = np.mean(eigenvalues[members])
        if abs(mu.imag) <= radius:  # real eigenvalue: stay in real arithmetic
            mu = mu.real
        _, s, vh = np.linalg.svd(A - mu * np.eye(n))
        tol = max(radius, n * np.finfo(float).eps * scale)
        # Right singular vectors of (numerically) zero singular values span the
        # null space; there is always at least one, and at most len(members).
        nullity = int(np.clip(np.sum(s <= tol), 1, len(members)))
        basis = vh[n - nullity :].conj()
        for k, col in enumerate(members):
            eigenvectors[:, col] = basis[k % nullity]

    if np.allclose(eigenvectors.imag, 0):
        return eigenvectors.real
    return eigenvectors
