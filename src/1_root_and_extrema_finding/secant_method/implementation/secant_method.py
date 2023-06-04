def secant_method(func, x0, x1, epsilon=1e-8, max_iter=100):
    """
    Secant Method for finding the root of a function.

    Args:
        func (callable): The function for which to find the root.
        x0 (float): The first initial guess for the root.
        x1 (float): The second initial guess for the root.
        epsilon (float): The desired accuracy of the solution.
        max_iter (int): The maximum number of iterations.

    Returns:
        float: The estimated root of the function.

    Raises:
        ValueError: If the maximum number of iterations is reached without convergence.
    """
    x_prev = x0
    x_curr = x1

    for _ in range(max_iter):
        f_prev = func(x_prev)
        f_curr = func(x_curr)

        if abs(f_curr) < epsilon:
            return x_curr

        x_next = x_curr - f_curr * (x_curr - x_prev) / (f_curr - f_prev)

        if abs(x_next - x_curr) < epsilon:
            return x_next

        x_prev = x_curr
        x_curr = x_next

    raise ValueError(
        "Secant method did not converge within the maximum number of iterations."
    )
