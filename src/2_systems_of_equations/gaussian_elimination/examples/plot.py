import os
import sys

import matplotlib.pyplot as plt
import numpy as np

# Make the sibling `implementation` package importable when run as a script.
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))
from implementation.gaussian_elimination import gaussian_elimination  # noqa: E402


def plot_gaussian_elimination_process(A, b):
    """
    Visualize the step-by-step process of Gaussian elimination.

    The implementation only returns the solution, so the forward elimination
    is repeated here (same partial pivoting and pivot normalization) to record
    the intermediate augmented matrices.

    Parameters:
        A (numpy.ndarray): Coefficient matrix.
        b (numpy.ndarray): Right-hand side vector.
    """
    n = len(b)
    Ab = np.hstack([A.astype(float), b.reshape(-1, 1).astype(float)])
    steps = [Ab.copy()]

    # Forward elimination with visualization steps
    for i in range(n):
        max_row = np.argmax(np.abs(Ab[i:n, i])) + i
        if i != max_row:
            Ab[[i, max_row]] = Ab[[max_row, i]]
        Ab[i] = Ab[i] / Ab[i, i]
        for j in range(i + 1, n):
            Ab[j] -= Ab[j, i] * Ab[i]
        steps.append(Ab.copy())

    # Plot each step of the Gaussian elimination process
    fig, axes = plt.subplots(1, len(steps), figsize=(20, 4))
    for idx, step in enumerate(steps):
        axes[idx].imshow(step, cmap="coolwarm", aspect="auto")
        axes[idx].set_title(f"Step {idx}")
        axes[idx].axis("off")
    plt.suptitle("Gaussian Elimination: Forward Elimination Steps")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    # Example system
    A = np.array([[2, 1, -1], [-3, -1, 2], [-2, 1, 2]], dtype=float)
    b = np.array([8, -11, -3], dtype=float)

    print("Solving system using Gaussian elimination:")
    solution = gaussian_elimination(A, b)
    print(f"Solution: {solution}")
    print(f"Check (np.linalg.solve): {np.linalg.solve(A, b)}")

    # Visualize the elimination process
    plot_gaussian_elimination_process(A, b)
