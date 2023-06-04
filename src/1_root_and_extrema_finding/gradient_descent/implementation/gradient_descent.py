import numpy as np
from typing import Callable, List, Tuple


def gradient_descent(
    f: Callable[[np.ndarray], float],
    f_gradient: Callable[[np.ndarray], np.ndarray],
    initial_point: np.ndarray,
    learning_rate: float = 0.1,
    epsilon: float = 1e-6,
    max_iterations: int = 1000,
) -> Tuple[np.ndarray, List[np.ndarray]]:
    """
    Perform gradient descent optimization to find the minimum of a function.

    Arguments:
    - f: The objective function.
    - f_gradient: The gradient of the objective function.
    - initial_point: The starting point for the optimization as a numpy array.
    - learning_rate: The learning rate or step size.
    - epsilon: The desired level of precision.
    - max_iterations: The maximum number of iterations.

    Returns:
    - The estimated minimum point of the function as a numpy array.
    - The list of all visited points during optimization.
    """
    current_point = initial_point.copy()
    visited_points = [current_point.flatten().tolist()]

    for _ in range(max_iterations):
        gradient = f_gradient(current_point)
        new_point = current_point - learning_rate * gradient

        if np.linalg.norm(new_point - current_point) < epsilon:
            break

        current_point = new_point
        visited_points.append(current_point.flatten().tolist())

    return current_point.flatten(), visited_points
