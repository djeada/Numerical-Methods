import os
import sys

import matplotlib.pyplot as plt
import numpy as np

# Make the sibling `implementation` package importable when run as a script.
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))
from implementation.gauss_seidel import gauss_seidel  # noqa: E402


def _error_history(A, b, x0, method, max_iterations=100):
    """
    Record ||x_new - x||_inf at every sweep of the Jacobi or Gauss-Seidel
    iteration. The implementations only return the final solution, so the
    history needed for the plot is recomputed here.
    """
    n = len(b)
    x = np.zeros(n) if x0 is None else x0.astype(float)
    errors = []
    for _ in range(max_iterations):
        x_old = x.copy()
        for i in range(n):
            src = x if method == "gauss_seidel" else x_old
            sum1 = np.dot(A[i, :i], src[:i])
            sum2 = np.dot(A[i, i + 1 :], x_old[i + 1 :])
            x[i] = (b[i] - sum1 - sum2) / A[i, i]
        error = np.linalg.norm(x - x_old, ord=np.inf)
        errors.append(error)
        if error < 1e-8:
            break
    return errors


def plot_convergence(errors_gs, errors_jacobi):
    """
    Plot convergence of Gauss-Seidel and Jacobi methods.

    Parameters:
        errors_gs (list): Errors for the Gauss-Seidel method.
        errors_jacobi (list): Errors for the Jacobi method.
    """
    plt.figure(figsize=(8, 6))
    plt.semilogy(errors_gs, label="Gauss-Seidel", linewidth=2)
    plt.semilogy(errors_jacobi, label="Jacobi", linestyle="--", linewidth=2)
    plt.xlabel("Iteration")
    plt.ylabel("Error (log scale)")
    plt.title("Convergence Comparison: Gauss-Seidel vs Jacobi")
    plt.legend()
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    # Example: Coefficient matrix and right-hand side vector
    A = np.array([[5, -1], [7, 8]], dtype=float)
    b = np.array([6, 20], dtype=float)

    # Initial guess
    x0 = np.array([0, 0], dtype=float)

    print("Solving system using Gauss-Seidel method:")
    x_gs = gauss_seidel(A, b, x0)
    errors_gs = _error_history(A, b, x0, "gauss_seidel")
    print(f"Gauss-Seidel Solution: {x_gs} ({len(errors_gs)} sweeps)")

    print("\nSolving system using Jacobi method:")
    errors_jacobi = _error_history(A, b, x0, "jacobi")
    print(f"Jacobi converged in {len(errors_jacobi)} iterations")
    print(f"Exact solution: {np.linalg.solve(A, b)}")

    # Plot convergence comparison
    plot_convergence(errors_gs, errors_jacobi)
