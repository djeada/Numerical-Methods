def perform_lu_decomposition(matrix):
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


def solve_lu(L, U, P, b):
    """
    Solves the system of equations Ax = b using LU decomposition.

    Parameters:
        L (numpy.ndarray): Lower triangular matrix.
        U (numpy.ndarray): Upper triangular matrix.
        P (numpy.ndarray): Permutation matrix.
        b (numpy.ndarray): Constant vector.

    Returns:
        x (numpy.ndarray): Solution vector.
    """
    intermediate_solution = np.linalg.solve(L, np.dot(P, b))
    solution = np.linalg.solve(U, intermediate_solution)

    return solution
