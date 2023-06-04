import numpy as np


def trapezoidal_rule(func, a, b, n):
    """
    Compute the approximate definite integral of a function using the trapezoidal rule.

    Args:
        func (callable): The function to integrate.
        a (float): The lower limit of integration.
        b (float): The upper limit of integration.
        n (int): The number of subintervals.

    Returns:
        float: The approximate definite integral.
    """
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = func(x)

    integral = (h / 2) * (np.sum(y[1:-1]) + y[0] + y[-1])

    return integral
