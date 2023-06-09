import numpy as np


def gaussian_elimination(A, b=None):
    """Perform Gaussian elimination on matrix A."""
    n = len(A)

    # If b is not provided, create it as a zero vector
    if b is None:
        b = np.zeros(n)

    for i in range(n):
        # Search for maximum in this column
        maxEl = abs(A[i][i])
        maxRow = i
        for k in range(i + 1, n):
            if abs(A[k][i]) > maxEl:
                maxEl = abs(A[k][i])
                maxRow = k

        # Swap maximum row with current row
        A[[i, maxRow]] = A[[maxRow, i]]
        b[[i, maxRow]] = b[[maxRow, i]]

        # Make all rows below this one 0 in current column
        for k in range(i + 1, n):
            c = -A[k][i] / A[i][i]
            for j in range(i, n):
                if i == j:
                    A[k][j] = 0
                else:
                    A[k][j] += c * A[i][j]
            b[k] += c * b[i]

    return A, b


def solve_gaussian_elimination(A, b):
    """Solve system of equations Ax = b using Gaussian elimination."""
    n = len(A)

    # Perform Gaussian elimination
    A, b = gaussian_elimination(A, b)

    # Back substitution
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = b[i] / A[i][i]
        for k in range(i - 1, -1, -1):
            b[k] -= A[k][i] * x[i]
    return x
