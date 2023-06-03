import numpy as np


def relaxation_method(func, x0, epsilon=1e-8, max_iter=100):
    """
    Relaxation Method for finding the fixed point of a function.

    Args:
        func (callable): The function for which to find the fixed point.
        x0 (float): The initial guess for the fixed point.
        epsilon (float): The desired accuracy of the solution.
        max_iter (int): The maximum number of iterations.

    Returns:
        float: The estimated fixed point of the function.

    Raises:
        ValueError: If the maximum number of iterations is reached without convergence.
    """
    x = x0

    for _ in range(max_iter):
        x_new = func(x)

        if abs(x_new - x) < epsilon:
            return x_new

        x = x_new

    raise ValueError("Relaxation method did not converge within the maximum number of iterations.")

