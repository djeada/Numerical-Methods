import numpy as np


def taylor_series(func, derivatives, point, n):
    """
    Compute the Taylor series expansion of a function around a given point.

    Args:
        func (callable): The function to expand.
        derivatives (list): List of derivatives of the function up to the desired order.
        point (float): The point around which to expand the function.
        n (int): The number of terms in the Taylor series.

    Returns:
        numpy.poly1d: The Taylor series expansion as a polynomial.
    """
    taylor_coeffs = [derivatives[0](point) / np.math.factorial(0)]
    for i in range(1, n):
        taylor_coeffs.append(derivatives[i](point) / np.math.factorial(i))
    return np.poly1d(taylor_coeffs[::-1])
