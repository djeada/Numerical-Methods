import os
import sys

import matplotlib.pyplot as plt
import numpy as np

# Make the sibling `implementation` package importable when run as a script.
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))
from implementation.jacobi_method import jacobi_method  # noqa: E402


def jacobi_error_history(A, b, x0=None, max_iterations=100, tol=1e-8):
    """
    Record ||x_new - x||_inf at every Jacobi iteration.

    The implementation only returns the final solution, so the history needed
    for the convergence plot is recomputed here (same update and stopping rule).
    """
    n = len(b)
    x = np.zeros(n) if x0 is None else x0.astype(float)
    errors = []
    for _ in range(max_iterations):
        x_new = np.zeros_like(x)
        for i in range(n):
            sum1 = np.dot(A[i, :i], x[:i])
            sum2 = np.dot(A[i, i + 1 :], x[i + 1 :])
            x_new[i] = (b[i] - sum1 - sum2) / A[i, i]
        error = np.linalg.norm(x_new - x, ord=np.inf)
        errors.append(error)
        x = x_new
        if error < tol:
            break
    return errors


if __name__ == "__main__":
    # Diagonally dominant 2x2 system
    A = np.array([[5, -1], [7, 8]], dtype=float)
    b = np.array([6, 20], dtype=float)
    x0 = np.array([0, 0], dtype=float)

    x = jacobi_method(A, b, x0)
    errors = jacobi_error_history(A, b, x0)
    x_exact = np.linalg.solve(A, b)
    print(f"Jacobi solution: {x}")
    print(f"Exact solution:  {x_exact}")

    plt.figure(figsize=(8, 6))
    plt.semilogy(range(1, len(errors) + 1), errors, "b-o", markersize=4, linewidth=2)
    plt.xlabel("Iteration", fontsize=14)
    plt.ylabel("Error (log scale)", fontsize=14)
    plt.title("Jacobi Method Convergence", fontsize=16)
    plt.grid(True)
    plt.tight_layout()
    plt.show()
