import math


def golden_ratio_search(func, a, b, epsilon=1e-8, max_iter=100):
    """
    Golden Ratio Search algorithm for finding the minimum of a unimodal function.

    Args:
        func (callable): The objective function.
        a (float): The starting point of the search interval.
        b (float): The ending point of the search interval.
        epsilon (float): The desired accuracy of the solution.
        max_iter (int): The maximum number of iterations.

    Returns:
        float: The estimated minimum of the function.

    Raises:
        ValueError: If the maximum number of iterations is reached without convergence.
    """
    gr = (math.sqrt(5) - 1) / 2  # Golden ratio
    x1 = b - gr * (b - a)
    x2 = a + gr * (b - a)

    f_x1 = func(x1)
    f_x2 = func(x2)

    for _ in range(max_iter):
        if f_x1 > f_x2:
            a = x1
            x1 = x2
            f_x1 = f_x2
            x2 = a + gr * (b - a)
            f_x2 = func(x2)
        else:
            b = x2
            x2 = x1
            f_x2 = f_x1
            x1 = b - gr * (b - a)
            f_x1 = func(x1)

        if abs(b - a) < epsilon:
            return (a + b) / 2

    raise ValueError(
        "Golden ratio search did not converge within the maximum number of iterations."
    )
