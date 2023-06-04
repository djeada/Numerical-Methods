import numpy as np


def find_eigenvalues(matrix):
    """
    Find the eigenvalues of a matrix using the characteristic equation method.

    Args:
        matrix (numpy.ndarray): The matrix for which to find eigenvalues.

    Returns:
        numpy.ndarray: The eigenvalues of the matrix.
    """
    eigenvalues = np.roots(np.linalg.det(matrix - np.eye(matrix.shape[0])))
    return eigenvalues


def find_eigenvectors(matrix):
    """
    Find the eigenvectors of a matrix.

    Args:
        matrix (numpy.ndarray): The matrix for which to find eigenvectors.

    Returns:
        numpy.ndarray: The eigenvectors of the matrix.
    """
    eigenvalues = find_eigenvalues(matrix)
    eigenvectors = []

    for eigenvalue in eigenvalues:
        eigenvector = np.linalg.solve(
            matrix - eigenvalue * np.eye(matrix.shape[0]), np.zeros(matrix.shape[0])
        )
        eigenvectors.append(eigenvector)

    return np.array(eigenvectors).T
