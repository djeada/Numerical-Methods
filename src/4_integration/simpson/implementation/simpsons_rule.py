import numpy as np


def simpsons_rule(func, a, b, n):
    """
    Compute the approximate definite integral of a function using Simpson's rule.

    Args:
        func (callable): The function to integrate.
        a (float): The lower limit of integration.
        b (float): The upper limit of integration.
        n (int): The number of subintervals (must be even).

    Returns:
        float: The approximate definite integral.
    """
    if n % 2 != 0:
        raise ValueError("Number of subintervals must be even.")

    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = func(x)

    integral = (h / 3) * np.sum(y[0:-1:2] + 4 * y[1::2] + y[2::2])

    return integral
