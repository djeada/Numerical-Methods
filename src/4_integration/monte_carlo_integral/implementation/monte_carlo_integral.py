import numpy as np


def monte_carlo_integral(func, a, b, n):
    """
    Compute the approximate definite integral of a function using Monte Carlo integration.

    Args:
        func (callable): The function to integrate.
        a (float): The lower limit of integration.
        b (float): The upper limit of integration.
        n (int): The number of random samples.

    Returns:
        float: The approximate definite integral.
    """
    random_x = np.random.uniform(a, b, n)
    random_y = np.random.uniform(0, func(b), n)

    integral = (b - a) * np.mean(random_y < func(random_x))

    return integral
