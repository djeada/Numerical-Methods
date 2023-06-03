import numpy as np


def singular_value_decomposition(matrix):
    """
    Perform Singular Value Decomposition (SVD) of a matrix.

    Args:
        matrix (numpy.ndarray): The matrix to decompose.

    Returns:
        Tuple[numpy.ndarray, numpy.ndarray, numpy.ndarray]: Tuple containing the left singular vectors (U),
            singular values (S), and right singular vectors (V^T).
    """
    # Compute A^T * A
    ata = np.dot(matrix.T, matrix)

    # Compute eigenvalues and eigenvectors of A^T * A
    eigenvalues, eigenvectors = np.linalg.eig(ata)

    # Sort eigenvalues in descending order
    sorted_indices = np.argsort(eigenvalues)[::-1]
    eigenvalues = eigenvalues[sorted_indices]
    eigenvectors = eigenvectors[:, sorted_indices]

    # Compute singular values and square root of eigenvalues
    singular_values = np.sqrt(eigenvalues)

    # Compute right singular vectors (V^T) by normalizing eigenvectors of A^T * A
    Vt = eigenvectors.T

    # Compute left singular vectors (U) by dividing A * V by singular values
    U = np.dot(matrix, Vt) / singular_values

    return U, singular_values, Vt
