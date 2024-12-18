# singular_value_decomposition.py
import numpy as np
from typing import Tuple

def singular_value_decomposition(A: np.ndarray) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    U, S, Vt = np.linalg.svd(A, full_matrices=True)
    S_matrix = np.zeros((U.shape[1], Vt.shape[0]))
    np.fill_diagonal(S_matrix, S)
    return U, S_matrix, Vt

def singular_value_decomposition_reduced(A: np.ndarray) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    U, S, Vt = np.linalg.svd(A, full_matrices=False)
    S_matrix = np.diag(S)
    return U, S_matrix, Vt
