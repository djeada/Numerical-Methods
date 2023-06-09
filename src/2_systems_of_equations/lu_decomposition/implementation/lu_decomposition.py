import numpy as np


def lu_decomposition(matrix):
    """
    Conducts LU decomposition on a square matrix.

    Parameters:
        matrix (numpy.ndarray): A square matrix to decompose.

    Returns:
        L (numpy.ndarray): Lower triangular matrix.
        U (numpy.ndarray): Upper triangular matrix.
        P (numpy.ndarray): Permutation matrix.
    """
    size = matrix.shape[0]
    L, U, P = np.eye(size), np.zeros_like(matrix), np.eye(size)

    for index in range(size):
        pivot_index = np.argmax(abs(matrix[index:, index])) + index

        # Swap rows
        (
            matrix[[index, pivot_index]],
            L[[index, pivot_index]],
            P[[index, pivot_index]],
        ) = (
            matrix[[pivot_index, index]],
            L[[pivot_index, index]],
            P[[pivot_index, index]],
        )

        U[index, index:] = matrix[index, index:]
        L[index + 1 :, index] = matrix[index + 1 :, index] / U[index, index]
        U[index + 1 :, index:] = matrix[index + 1 :, index:] - np.outer(
            L[index + 1 :, index], U[index, index:]
        )

    return L, U, P


def forward_substitution(L, Pb):
    n = L.shape[0]
    y = np.zeros_like(Pb, dtype=np.double)

    y[0] = Pb[0] / L[0, 0]

    for i in range(1, n):
        y[i] = (Pb[i] - np.dot(L[i, :i], y[:i])) / L[i, i]

    return y


def backward_substitution(U, y):
    n = U.shape[0]
    x = np.zeros_like(y, dtype=np.double)

    x[-1] = y[-1] / U[-1, -1]

    for i in range(n - 2, -1, -1):
        x[i] = (y[i] - np.dot(U[i, i + 1 :], x[i + 1 :])) / U[i, i]

    return x


def solve_lu(A, b):
    L, U, P = lu_decomposition(A)

    Pb = np.dot(P, b)

    y = forward_substitution(L, Pb)
    x = backward_substitution(U, y)

    return x
