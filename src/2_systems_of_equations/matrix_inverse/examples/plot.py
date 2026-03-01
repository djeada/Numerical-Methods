import numpy as np
import matplotlib.pyplot as plt


def matrix_inverse(A):
    """
    Compute the inverse of a matrix using Gauss-Jordan elimination.

    Parameters:
        A (numpy.ndarray): Square matrix to invert.

    Returns:
        numpy.ndarray: Inverse of A.
    """
    n = A.shape[0]
    augmented = np.hstack([A.astype(float), np.eye(n)])

    for col in range(n):
        # Partial pivoting
        max_row = np.argmax(np.abs(augmented[col:, col])) + col
        augmented[[col, max_row]] = augmented[[max_row, col]]

        pivot = augmented[col, col]
        augmented[col] = augmented[col] / pivot

        for row in range(n):
            if row != col:
                factor = augmented[row, col]
                augmented[row] -= factor * augmented[col]

    return augmented[:, n:]


if __name__ == "__main__":
    A = np.array([[4, 7], [2, 6]], dtype=float)

    A_inv = matrix_inverse(A)
    identity_check = A @ A_inv

    print("Matrix A:")
    print(A)
    print("\nInverse A^{-1}:")
    print(A_inv)
    print("\nA @ A^{-1} (should be identity):")
    print(identity_check)

    fig, axes = plt.subplots(1, 3, figsize=(14, 4))

    im0 = axes[0].imshow(A, cmap="viridis", aspect="equal")
    axes[0].set_title("Original Matrix $A$", fontsize=14)
    for i in range(A.shape[0]):
        for j in range(A.shape[1]):
            axes[0].text(j, i, f"{A[i, j]:.2f}", ha="center", va="center", color="w")
    plt.colorbar(im0, ax=axes[0], fraction=0.046)

    im1 = axes[1].imshow(A_inv, cmap="viridis", aspect="equal")
    axes[1].set_title("Inverse Matrix $A^{-1}$", fontsize=14)
    for i in range(A_inv.shape[0]):
        for j in range(A_inv.shape[1]):
            axes[1].text(
                j, i, f"{A_inv[i, j]:.2f}", ha="center", va="center", color="w"
            )
    plt.colorbar(im1, ax=axes[1], fraction=0.046)

    im2 = axes[2].imshow(identity_check, cmap="viridis", aspect="equal")
    axes[2].set_title("$A \\cdot A^{-1}$ (Identity)", fontsize=14)
    for i in range(identity_check.shape[0]):
        for j in range(identity_check.shape[1]):
            axes[2].text(
                j,
                i,
                f"{identity_check[i, j]:.2f}",
                ha="center",
                va="center",
                color="w",
            )
    plt.colorbar(im2, ax=axes[2], fraction=0.046)

    plt.suptitle("Matrix Inverse Verification", fontsize=16)
    plt.tight_layout()
    plt.show()
