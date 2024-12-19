import numpy as np
from typing import Tuple

def find_eigenvalues(matrix: np.ndarray) -> np.ndarray:
    if matrix.ndim != 2 or matrix.shape[0] != matrix.shape[1]:
        raise ValueError("Matrix must be square.")
    coeffs = np.poly(matrix)
    eigenvalues = np.roots(coeffs)
    return eigenvalues

def find_eigenvectors(matrix: np.ndarray) -> np.ndarray:
    eigenvalues = find_eigenvalues(matrix)
    n = matrix.shape[0]
    eigenvectors = []
    for λ in eigenvalues:
        A_shift = matrix - λ * np.eye(n)
        # Perform Gaussian elimination
        A_shift = A_shift.astype(float)
        augmented = np.hstack((A_shift, np.zeros((n, 1))))
        for i in range(n):
            # Find pivot
            max_row = np.argmax(np.abs(augmented[i:, i])) + i
            if np.isclose(augmented[max_row, i], 0.0):
                continue
            # Swap rows
            if max_row != i:
                augmented[[i, max_row]] = augmented[[max_row, i]]
            # Eliminate below
            for j in range(i + 1, n):
                factor = augmented[j, i] / augmented[i, i]
                augmented[j] -= factor * augmented[i]
        # Back substitution to find eigenvector
        # Find first non-zero row
        eigenvector = np.zeros(n)
        for i in range(n):
            if not np.allclose(augmented[i, :-1], 0):
                eigenvector[i] = 1
                for j in range(i):
                    eigenvector[j] -= augmented[j, i] * eigenvector[i]
                break
        # Normalize eigenvector
        norm = np.linalg.norm(eigenvector)
        if norm != 0:
            eigenvector /= norm
        eigenvectors.append(eigenvector)
    return np.array(eigenvectors).T
