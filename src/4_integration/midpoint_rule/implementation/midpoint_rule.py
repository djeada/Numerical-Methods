def midpoint_rule(func, a, b, n):
    """
    Compute the approximate definite integral of a function using the midpoint rule.

    Args:
        func (callable): The function to integrate.
        a (float): The lower limit of integration.
        b (float): The upper limit of integration.
        n (int): The number of subintervals.

    Returns:
        float: The approximate definite integral.
    """
    h = (b - a) / n
    x = np.linspace(a + h / 2, b - h / 2, n)
    y = func(x)

    integral = h * np.sum(y)

    return integral
