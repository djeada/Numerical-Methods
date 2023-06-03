def inverse_matrix(A):
    """
    Compute the inverse of a square matrix A using LU decomposition.

    Args:
        A (numpy.ndarray): The square matrix to invert.

    Returns:
        numpy.ndarray: The inverse of the input matrix A.
    """
    n = A.shape[0]
    identity = np.eye(n)
    L, U, P = lu_decomposition(A)
    inv_A = np.zeros_like(A)

    for i in range(n):
        inv_A[:, i] = solve_lu(L, U, P, identity[:, i])

    return inv_A


def solve_inverse(A, b):
    """
    Solve a system of equations Ax = b using the inverse matrix.

    Args:
        A (numpy.ndarray): The coefficient matrix.
        b (numpy.ndarray): The constant vector.

    Returns:
        numpy.ndarray: The solution vector.
    """
    inv_A = inverse_matrix(A)
    x = np.dot(inv_A, b)

    return x
