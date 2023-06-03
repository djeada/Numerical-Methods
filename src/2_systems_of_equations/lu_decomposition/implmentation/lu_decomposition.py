

def lu_decomposition(A):
    """
    LU decomposition of a square matrix A.

    Args:
        A (numpy.ndarray): The square matrix to decompose.

    Returns:
        numpy.ndarray: The lower triangular matrix L.
        numpy.ndarray: The upper triangular matrix U.
        numpy.ndarray: The permutation matrix P.
    """
    n = A.shape[0]
    L = np.eye(n)
    U = np.zeros_like(A)
    P = np.eye(n)

    for k in range(n):
        pivot_row = np.argmax(abs(A[k:, k])) + k

        # Swap rows
        A[[k, pivot_row]] = A[[pivot_row, k]]
        L[[k, pivot_row]] = L[[pivot_row, k]]
        P[[k, pivot_row]] = P[[pivot_row, k]]

        U[k, k:] = A[k, k:]
        L[k+1:, k] = A[k+1:, k] / U[k, k]
        U[k+1:, k:] = A[k+1:, k:] - np.outer(L[k+1:, k], U[k, k:])

    return L, U, P
  
  def solve_lu(L, U, P, b):
    """
    Solve a system of equations Ax = b using LU decomposition.

    Args:
        L (numpy.ndarray): The lower triangular matrix.
        U (numpy.ndarray): The upper triangular matrix.
        P (numpy.ndarray): The permutation matrix.
        b (numpy.ndarray): The constant vector.

    Returns:
        numpy.ndarray: The solution vector.
    """
    y = np.linalg.solve(L, np.dot(P, b))
    x = np.linalg.solve(U, y)

    return x
