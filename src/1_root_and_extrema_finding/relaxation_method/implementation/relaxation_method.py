from typing import Callable
import numpy as np


def relaxation_method(func, initial_guess, omega=1.0, tol=1e-6, max_iterations=100000):
    """
    Perform the relaxation method (Successive Over-Relaxation) to find a fixed point of a function.

    Arguments:
    - func: The function for which to find the fixed point.
    - initial_guess: The initial guess for the fixed point.
    - omega: The relaxation factor (default: 1.0).
    - tol: The tolerance for convergence.
    - max_iterations: The maximum number of iterations.

    Returns:
    - The estimated fixed point of the function.
    """
    x = initial_guess

    for iteration in range(max_iterations):
        previous_x = x
        x_new = func(x)
        error = np.abs(x_new - x)

        if error < tol:
            return x

        if iteration > 0:
            omega = error / np.abs(x_new - previous_x)

        x = (1 - omega) * x + omega * x_new

    return x
