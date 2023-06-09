import numpy as np


def inverse_matrix(A):
    """Compute the inverse of matrix A using the Gauss-Jordan elimination method."""

    n = len(A)

    # Append the identity matrix
    AI = np.concatenate([A, np.eye(n)], axis=1)

    # Perform the Gaussian elimination
    for i in range(n):
        # Pivot the matrix
        max_row_index = np.argmax(abs(AI[i:, i])) + i
        AI[[i, max_row_index]] = AI[[max_row_index, i]]

        # Normalize the current row
        AI[i] = AI[i] / AI[i, i]

        # Reduce other rows
        for j in range(n):
            if i != j:
                AI[j] = AI[j] - AI[j, i] * AI[i]

    # The right half of the matrix is the inverse of A
    A_inv = AI[:, n:]

    return A_inv


def solve_inverse_matrix(A, b):
    """Solve the system of linear equations Ax = b using the inverse of A."""

    # Compute the inverse of A
    A_inv = inverse_matrix(A)

    # Multiply A_inv with b to get the solution
    x = np.dot(A_inv, b)

    return x
