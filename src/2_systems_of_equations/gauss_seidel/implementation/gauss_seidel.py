def gauss_seidel(A, b, x0, epsilon=1e-8, max_iter=100):
    """
    Gauss-Seidel method for solving a linear system of equations.

    Args:
        A (numpy.ndarray): The coefficient matrix of the linear system.
        b (numpy.ndarray): The constant vector of the linear system.
        x0 (numpy.ndarray): The initial guess for the solution.
        epsilon (float): The desired accuracy of the solution.
        max_iter (int): The maximum number of iterations.

    Returns:
        numpy.ndarray: The estimated solution of the linear system.

    Raises:
        ValueError: If the maximum number of iterations is reached without convergence.
    """
    n = len(A)
    x = x0.copy()

    for _ in range(max_iter):
        x_prev = x.copy()

        for i in range(n):
            x[i] = (
                b[i] - np.dot(A[i, :i], x[:i]) - np.dot(A[i, i + 1 :], x_prev[i + 1 :])
            ) / A[i, i]

        if np.linalg.norm(x - x_prev) < epsilon:
            return x

    raise ValueError(
        "Gauss-Seidel method did not converge within the maximum number of iterations."
    )
