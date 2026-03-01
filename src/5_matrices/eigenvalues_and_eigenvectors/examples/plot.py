import numpy as np
import matplotlib.pyplot as plt


def plot_eigenvector_transformation(A):
    """
    Visualize how a matrix transforms vectors, highlighting eigenvectors.
    """
    eigenvalues, eigenvectors = np.linalg.eig(A)

    # Generate unit circle points
    theta = np.linspace(0, 2 * np.pi, 100)
    circle = np.array([np.cos(theta), np.sin(theta)])

    # Transform the circle
    transformed = A @ circle

    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    # Original space with eigenvectors
    axes[0].plot(circle[0], circle[1], "b-", alpha=0.3, label="Unit circle")
    for i in range(len(eigenvalues)):
        v = eigenvectors[:, i].real
        axes[0].quiver(
            0, 0, v[0], v[1],
            angles="xy", scale_units="xy", scale=1,
            color=f"C{i}", linewidth=2,
            label=f"v{i+1} (λ={eigenvalues[i].real:.2f})",
        )
    axes[0].set_xlim(-2, 2)
    axes[0].set_ylim(-2, 2)
    axes[0].set_aspect("equal")
    axes[0].grid(True, linestyle="--", alpha=0.7)
    axes[0].set_title("Original Space")
    axes[0].legend()

    # Transformed space
    axes[1].plot(transformed[0], transformed[1], "r-", alpha=0.3, label="Transformed")
    for i in range(len(eigenvalues)):
        v = eigenvectors[:, i].real
        Av = A @ v
        axes[1].quiver(
            0, 0, Av[0], Av[1],
            angles="xy", scale_units="xy", scale=1,
            color=f"C{i}", linewidth=2,
            label=f"Av{i+1} = {eigenvalues[i].real:.2f}·v{i+1}",
        )
    axes[1].set_xlim(-6, 6)
    axes[1].set_ylim(-6, 6)
    axes[1].set_aspect("equal")
    axes[1].grid(True, linestyle="--", alpha=0.7)
    axes[1].set_title("Transformed Space (A @ v)")
    axes[1].legend()

    plt.suptitle("Eigenvector Transformation Visualization", fontsize=14)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    A = np.array([[4, 1], [2, 3]])
    plot_eigenvector_transformation(A)
