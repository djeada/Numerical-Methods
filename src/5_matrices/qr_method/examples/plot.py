import numpy as np
import matplotlib.pyplot as plt


def qr_method_visualization(A, max_iterations=50, tol=1e-8):
    """
    Visualize the QR method's iterative transformation of a matrix towards an upper-triangular form.

    Parameters:
        A (numpy.ndarray): Input square matrix.
        max_iterations (int): Maximum number of iterations.
        tol (float): Convergence tolerance for off-diagonal elements.
    """
    A_k = A.copy()
    n = A.shape[0]
    off_diagonal_norms = []

    fig, axes = plt.subplots(1, 5, figsize=(20, 4))
    step_intervals = max_iterations // 5

    for i in range(max_iterations):
        # Perform QR decomposition
        Q, R = np.linalg.qr(A_k)
        A_k = R @ Q

        # Compute off-diagonal norm to check convergence
        off_diag = A_k - np.diag(np.diag(A_k))
        off_diag_norm = np.linalg.norm(off_diag)
        off_diagonal_norms.append(off_diag_norm)

        # Stop if off-diagonal elements are sufficiently small
        if off_diag_norm < tol:
            print(f"Converged at iteration {i+1}")
            break

        # Plot progress at specific intervals
        if i % step_intervals == 0:
            ax_idx = i // step_intervals
            axes[ax_idx].imshow(A_k, cmap="viridis", interpolation="nearest")
            axes[ax_idx].set_title(f"Iteration {i}")
            axes[ax_idx].axis("off")

    # Final visualization of convergence
    axes[-1].imshow(A_k, cmap="viridis", interpolation="nearest")
    axes[-1].set_title(f"Iteration {i+1} (Final)")
    axes[-1].axis("off")

    plt.suptitle("QR Method: Matrix Evolution Towards Upper-Triangular Form")
    plt.tight_layout()
    plt.show()

    # Plot convergence of off-diagonal elements
    plt.figure(figsize=(8, 6))
    plt.semilogy(off_diagonal_norms, label="Off-diagonal Norm")
    plt.xlabel("Iteration")
    plt.ylabel("Log Scale: Off-diagonal Norm")
    plt.title("Convergence of Off-diagonal Elements")
    plt.legend()
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    # Example: Input matrix
    A = np.array([[4, 1, 2], [1, 3, 1], [2, 1, 5]], dtype=float)

    print("Initial Matrix A:")
    print(A)
    qr_method_visualization(A)
