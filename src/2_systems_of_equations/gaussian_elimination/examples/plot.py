import numpy as np
import matplotlib.pyplot as plt


def gaussian_elimination(A, b):
    """
    Solve the linear system Ax = b using Gaussian elimination with back substitution.

    Parameters:
        A (numpy.ndarray): Coefficient matrix (n x n).
        b (numpy.ndarray): Right-hand side vector (n,).

    Returns:
        x (numpy.ndarray): Solution vector.
    """
    n = len(b)
    # Augmented matrix
    Ab = np.hstack([A, b.reshape(-1, 1)])

    # Forward elimination
    for i in range(n):
        # Partial pivoting: Find the maximum element in the current column
        max_row = np.argmax(np.abs(Ab[i:n, i])) + i
        if i != max_row:
            Ab[[i, max_row]] = Ab[[max_row, i]]

        # Normalize pivot row
        Ab[i] = Ab[i] / Ab[i, i]

        # Eliminate below
        for j in range(i + 1, n):
            Ab[j] -= Ab[j, i] * Ab[i]

    # Back substitution
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = Ab[i, -1] - np.sum(Ab[i, i + 1 : n] * x[i + 1 : n])

    return x


def plot_gaussian_elimination_process(A, b):
    """
    Visualize the step-by-step process of Gaussian elimination.

    Parameters:
        A (numpy.ndarray): Coefficient matrix.
        b (numpy.ndarray): Right-hand side vector.
    """
    n = len(b)
    Ab = np.hstack([A, b.reshape(-1, 1)])
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

    # Visualize the elimination process
    plot_gaussian_elimination_process(A, b)
