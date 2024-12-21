import numpy as np
import matplotlib.pyplot as plt


def lu_decomposition(A):
    """
    Perform LU decomposition of a square matrix A.

    Parameters:
        A (numpy.ndarray): Coefficient matrix (n x n).

    Returns:
        L (numpy.ndarray): Lower triangular matrix with unit diagonal.
        U (numpy.ndarray): Upper triangular matrix.
    """
    n = A.shape[0]
    L = np.eye(n)
    U = np.zeros_like(A, dtype=float)

    for i in range(n):
        # Compute upper triangular matrix U
        for j in range(i, n):
            U[i, j] = A[i, j] - np.sum(L[i, :i] * U[:i, j])

        # Compute lower triangular matrix L
        for j in range(i + 1, n):
            L[j, i] = (A[j, i] - np.sum(L[j, :i] * U[:i, i])) / U[i, i]

    return L, U


def forward_substitution(L, b):
    """
    Solve the lower triangular system Lc = b using forward substitution.

    Parameters:
        L (numpy.ndarray): Lower triangular matrix.
        b (numpy.ndarray): Right-hand side vector.

    Returns:
        c (numpy.ndarray): Solution vector.
    """
    n = L.shape[0]
    c = np.zeros_like(b, dtype=float)
    for i in range(n):
        c[i] = (b[i] - np.dot(L[i, :i], c[:i])) / L[i, i]
    return c


def backward_substitution(U, c):
    """
    Solve the upper triangular system Ux = c using backward substitution.

    Parameters:
        U (numpy.ndarray): Upper triangular matrix.
        c (numpy.ndarray): Solution vector from forward substitution.

    Returns:
        x (numpy.ndarray): Solution vector.
    """
    n = U.shape[0]
    x = np.zeros_like(c, dtype=float)
    for i in range(n - 1, -1, -1):
        x[i] = (c[i] - np.dot(U[i, i + 1 :], x[i + 1 :])) / U[i, i]
    return x


def solve_lu(A, b):
    """
    Solve the system Ax = b using LU decomposition.

    Parameters:
        A (numpy.ndarray): Coefficient matrix (n x n).
        b (numpy.ndarray): Right-hand side vector.

    Returns:
        x (numpy.ndarray): Solution vector.
    """
    L, U = lu_decomposition(A)
    c = forward_substitution(L, b)
    x = backward_substitution(U, c)
    return x, L, U


def plot_matrix_decomposition(L, U):
    """
    Visualize the L and U matrices from LU decomposition.

    Parameters:
        L (numpy.ndarray): Lower triangular matrix.
        U (numpy.ndarray): Upper triangular matrix.
    """
    fig, axes = plt.subplots(1, 2, figsize=(12, 6))
    axes[0].imshow(L, cmap="coolwarm", interpolation="none")
    axes[0].set_title("Lower Triangular Matrix L")
    axes[0].axis("off")

    axes[1].imshow(U, cmap="coolwarm", interpolation="none")
    axes[1].set_title("Upper Triangular Matrix U")
    axes[1].axis("off")

    plt.suptitle("LU Decomposition Visualization")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    # Example system
    A = np.array([[2, 3, -4], [3, -3, 2], [-2, 6, -1]], dtype=float)
    b = np.array([1, -2, 3], dtype=float)

    print("Solving system using LU decomposition:")
    x, L, U = solve_lu(A, b)
    print(f"Solution: {x}")
    print("L (Lower Triangular Matrix):")
    print(L)
    print("U (Upper Triangular Matrix):")
    print(U)

    # Plot LU decomposition
    plot_matrix_decomposition(L, U)
