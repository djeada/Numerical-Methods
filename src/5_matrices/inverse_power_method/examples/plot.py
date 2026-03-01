import numpy as np
import matplotlib.pyplot as plt


def inverse_power_method_convergence(A, shift=0.0, max_iterations=50):
    """
    Visualize the convergence of the inverse power method.
    """
    n = A.shape[0]
    I = np.eye(n)
    A_shifted = A - shift * I
    x = np.ones(n)
    x = x / np.linalg.norm(x)

    eigenvalue_estimates = []

    for _ in range(max_iterations):
        y = np.linalg.solve(A_shifted, x)
        y = y / np.linalg.norm(y)
        eigenvalue = np.dot(y, A @ y)
        eigenvalue_estimates.append(eigenvalue)
        x = y

    # True eigenvalues for reference
    true_eigenvalues = np.sort(np.linalg.eigvals(A).real)

    plt.figure(figsize=(10, 6))
    plt.plot(
        range(1, len(eigenvalue_estimates) + 1),
        eigenvalue_estimates,
        marker="o",
        markersize=4,
        label="Inverse Power Method Estimate",
    )
    for i, ev in enumerate(true_eigenvalues):
        plt.axhline(
            y=ev, color=f"C{i + 1}", linestyle="--",
            label=f"True λ{i+1} = {ev:.4f}",
        )
    plt.title("Convergence of Inverse Power Method")
    plt.xlabel("Iteration")
    plt.ylabel("Eigenvalue Estimate")
    plt.legend()
    plt.grid(True, linestyle="--", alpha=0.7)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    A = np.array([[4, 1], [2, 3]])
    inverse_power_method_convergence(A, shift=0.0)
