import numpy as np

def newton_raphson(func, derivative, x0, epsilon=1e-8, max_iter=100):
    """
    Newton-Raphson method for finding the root of a function.

    Args:
        func (callable): The function for which to find the root.
        derivative (callable): The derivative of the function.
        x0 (float): The initial guess for the root.
        epsilon (float): The desired accuracy of the solution.
        max_iter (int): The maximum number of iterations.

    Returns:
        float: The estimated root of the function.

    Raises:
        ValueError: If the maximum number of iterations is reached without convergence.
    """
    x = x0

    for _ in range(max_iter):
        f_x = func(x)
        f_prime_x = derivative(x)

        if abs(f_prime_x) < epsilon:
            raise ValueError("Derivative is close to zero. Newton-Raphson method failed.")

        x -= f_x / f_prime_x

        if abs(f_x) < epsilon:
            return x

    raise ValueError("Newton-Raphson method did not converge within the maximum number of iterations.")
