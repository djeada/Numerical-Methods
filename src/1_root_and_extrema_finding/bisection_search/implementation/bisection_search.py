def bisection_search(function, a, b, epsilon=1e-6, max_iterations=100):
    """
    Perform the bisection search algorithm to find a root of a function within a given interval.

    Arguments:
    - function: The function for which to find the root.
    - a: The lower bound of the interval.
    - b: The upper bound of the interval.
    - epsilon: The desired level of precision.
    - max_iterations: The maximum number of iterations.

    Returns:
    - The estimated root of the function within the interval.
    """
    if function(a) * function(b) >= 0:
        raise ValueError("Function must have opposite signs at interval endpoints.")

    for _ in range(max_iterations):
        c = (a + b) / 2  # Compute the midpoint

        if abs(function(c)) < epsilon:
            return c  # Root found

        if function(a) * function(c) < 0:
            b = c  # Root is in the left subinterval
        else:
            a = c  # Root is in the right subinterval

    return (a + b) / 2  # Return the best estimate if max_iterations is reached
