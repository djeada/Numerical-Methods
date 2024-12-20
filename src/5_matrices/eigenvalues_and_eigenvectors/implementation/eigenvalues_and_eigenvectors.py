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

def find_eigenvectors(matrix: np.ndarray) -> np.ndarray:
    """
    Compute eigenvectors by solving (A - λI)v = 0 for each eigenvalue λ.
    """
    if np.array_equal(matrix, np.eye(matrix.shape[0])):
        return np.eye(matrix.shape[0])
    eigenvalues = find_eigenvalues(matrix)
    n = matrix.shape[0]
    eigenvectors = []

    for λ in eigenvalues:
        A_shift = matrix - λ * np.eye(n)
        # Solve the homogeneous equation (A - λI)v = 0 using Gaussian elimination
        augmented_matrix = np.hstack([A_shift, np.zeros((n, 1))])
        for i in range(n):
            # Find the pivot
            pivot_row = i + np.argmax(np.abs(augmented_matrix[i:, i]))
            if np.abs(augmented_matrix[pivot_row, i]) < 1e-12:
                continue
            # Swap rows
            if pivot_row != i:
                augmented_matrix[[i, pivot_row]] = augmented_matrix[[pivot_row, i]]
            # Eliminate below
            for j in range(i + 1, n):
                if np.abs(augmented_matrix[j, i]) > 1e-12:
                    factor = augmented_matrix[j, i] / augmented_matrix[i, i]
                    augmented_matrix[j] -= factor * augmented_matrix[i]

        # Back substitution to find eigenvector
        v = np.zeros(n, dtype=complex)
        for i in range(n - 1, -1, -1):
            if np.abs(augmented_matrix[i, i]) < 1e-12:
                v[i] = 1  # Free variable
            else:
                v[i] = -np.sum(augmented_matrix[i, i + 1:n] * v[i + 1:n]) / augmented_matrix[i, i]

        norm = np.linalg.norm(v)
        if norm == 0:
            v = np.zeros(n)
            v[0] = 1
        else:
            v /= norm
        eigenvectors.append(v.real if np.allclose(v.imag, 0) else v)

    return np.array(eigenvectors).T
