# eigen_value_decomposition.py
import numpy as np
from typing import Tuple


def eigen_decomposition_full(
    A: np.ndarray,
) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    eigenvalues: np.ndarray
    eigenvectors: np.ndarray
    eigenvalues, eigenvectors = np.linalg.eig(A)
    D: np.ndarray = np.diag(eigenvalues)
    P_inv: np.ndarray = np.linalg.inv(eigenvectors)
    return eigenvectors, D, P_inv


def eigen_decomposition_real_full(
    A: np.ndarray,
) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    if not np.allclose(A, A.T):
        raise ValueError("Matrix is not symmetric.")
    eigenvalues, eigenvectors = np.linalg.eigh(A)
    D: np.ndarray = np.diag(eigenvalues)
    P_inv: np.ndarray = np.linalg.inv(eigenvectors)
    return eigenvectors, D, P_inv
