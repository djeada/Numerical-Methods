import numpy as np
import matplotlib.pyplot as plt


def gauss_seidel(A, b, x0=None, max_iterations=100, tol=1e-8):
    """
    Solve the linear system Ax = b using the Gauss-Seidel method.

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
        x_old = x.copy()

        for i in range(n):
            sum1 = np.dot(A[i, :i], x[:i])
            sum2 = np.dot(A[i, i + 1 :], x_old[i + 1 :])
            x[i] = (b[i] - sum1 - sum2) / A[i, i]

        # Calculate error as the norm of the difference between iterations
        error = np.linalg.norm(x - x_old, ord=np.inf)
        errors.append(error)

        if error < tol:
            print(f"Converged after {k+1} iterations.")
            break
    return x, errors


def jacobi(A, b, x0=None, max_iterations=100, tol=1e-8):
    """
    Solve the linear system Ax = b using the Jacobi method.

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

        # Calculate error as the norm of the difference between iterations
        error = np.linalg.norm(x_new - x, ord=np.inf)
        errors.append(error)
        x = x_new.copy()

        if error < tol:
            print(f"Converged after {k+1} iterations.")
            break
    return x, errors


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
    x_gs, errors_gs = gauss_seidel(A, b, x0)
    print(f"Gauss-Seidel Solution: {x_gs}")

    print("\nSolving system using Jacobi method:")
    x_jacobi, errors_jacobi = jacobi(A, b, x0)
    print(f"Jacobi Solution: {x_jacobi}")

    # Plot convergence comparison
    plot_convergence(errors_gs, errors_jacobi)
