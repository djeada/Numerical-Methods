import numpy as np
import matplotlib.pyplot as plt
from numpy.linalg import svd


def plot_svd(A):
    """
    Computes and visualizes the Singular Value Decomposition (SVD) of a matrix A.

    Parameters:
        A (ndarray): Input matrix to decompose.
    """
    # Perform SVD
    U, Sigma, VT = svd(A)

    # Construct diagonal matrix Sigma for visualization
    Sigma_matrix = np.zeros_like(A, dtype=float)
    np.fill_diagonal(Sigma_matrix, Sigma)

    # Print results
    print("Original Matrix A:")
    print(A)
    print("\nLeft Singular Vectors (U):")
    print(U)
    print("\nSingular Values (Sigma):")
    print(Sigma)
    print("\nRight Singular Vectors (V^T):")
    print(VT)

    # Plot the original matrix and its SVD components
    fig, axs = plt.subplots(1, 4, figsize=(20, 6))

    # Plot Original Matrix A
    axs[0].imshow(A, cmap="viridis", aspect="auto")
    axs[0].set_title("Original Matrix A")
    axs[0].axis("off")

    # Plot Left Singular Vectors U
    axs[1].imshow(U, cmap="coolwarm", aspect="auto")
    axs[1].set_title("Left Singular Vectors (U)")
    axs[1].axis("off")

    # Plot Singular Values Sigma
    axs[2].imshow(Sigma_matrix, cmap="coolwarm", aspect="auto")
    axs[2].set_title("Singular Values (Sigma)")
    axs[2].axis("off")

    # Plot Right Singular Vectors VT
    axs[3].imshow(VT, cmap="coolwarm", aspect="auto")
    axs[3].set_title("Right Singular Vectors (V^T)")
    axs[3].axis("off")

    plt.tight_layout()
    plt.show()


# Example matrix A
A = np.array([[3, 4], [2, 1], [0, 5]])

# Perform and plot SVD
plot_svd(A)
