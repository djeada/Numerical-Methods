import numpy as np
import matplotlib.pyplot as plt


def jacobi_method(A, b, x0=None, max_iterations=100, tol=1e-8):
    """
    Solve the linear system Ax = b using the Jacobi iterative method.

    Parameters:
        A (numpy.ndarray): Coefficient matrix (n x n).
        b (numpy.ndarray): Right-hand side vector (n,).
        x0 (numpy.ndarray): Initial guess for the solution (n,).
        max_iterations (int): Maximum number of iterations.
        tol (float): Convergence tolerance.

    Returns:
        x (numpy.ndarray): Approximate solution vector.
        errors (list): List of errors at each iteration.
    """
    n = len(b)
    if x0 is None:
        x = np.zeros_like(b, dtype=float)
    else:
        x = x0.copy()

    errors = []

    for k in range(max_iterations):
        x_new = np.zeros_like(x)

        for i in range(n):
            sum1 = np.dot(A[i, :i], x[:i])
            sum2 = np.dot(A[i, i + 1 :], x[i + 1 :])
            x_new[i] = (b[i] - sum1 - sum2) / A[i, i]

        error = np.linalg.norm(x_new - x, ord=np.inf)
        errors.append(error)
        x = x_new.copy()

        if error < tol:
            print(f"Converged after {k + 1} iterations.")
            break

    return x, errors


if __name__ == "__main__":
    # Diagonally dominant 2x2 system
    A = np.array([[5, -1], [7, 8]], dtype=float)
    b = np.array([6, 20], dtype=float)
    x0 = np.array([0, 0], dtype=float)

    x, errors = jacobi_method(A, b, x0)
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
