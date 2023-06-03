def backward_difference(func, x, h):
    """
    Compute the approximate derivative of a function using the backward difference method.

    Args:
        func (callable): The function for which to compute the derivative.
        x (float): The point at which to approximate the derivative.
        h (float): The step size.

    Returns:
        float: The approximate derivative of the function at the given point.
    """
    return (func(x) - func(x - h)) / h
