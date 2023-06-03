import numpy as np


def eigenvalue_decomposition(matrix):
    """
    Perform eigenvalue decomposition of a matrix.

    Args:
        matrix (numpy.ndarray): The matrix to decompose.

    Returns:
        Tuple[numpy.ndarray, numpy.ndarray, numpy.ndarray]: Tuple containing the eigenvectors (P),
            eigenvalues (D), and inverse of eigenvectors (P^-1).
    """
    eigenvalues, eigenvectors = np.linalg.eig(matrix)
    P = eigenvectors
    D = np.diag(eigenvalues)
    P_inv = np.linalg.inv(P)

    return P, D, P_inv
