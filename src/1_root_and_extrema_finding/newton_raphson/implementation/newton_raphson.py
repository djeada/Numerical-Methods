import numpy as np
from typing import Callable, List, Tuple


def newton_raphson(
    f: Callable[[np.ndarray], float],
    f_gradient: Callable[[np.ndarray], np.ndarray],
    f_hessian: Callable[[np.ndarray], np.ndarray],
    initial_point: np.ndarray,
    epsilon: float = 1e-6,
    max_iterations: int = 1000,
) -> Tuple[np.ndarray, List[np.ndarray]]:
    """
    Perform Newton's method optimization to find the minimum of a function.

    Arguments:
    - f: The objective function.
    - f_gradient: The gradient of the objective function.
    - f_hessian: The Hessian matrix of the objective function.
    - initial_point: The starting point for the optimization as a numpy array.
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
        hessian = f_hessian(current_point)

        if np.linalg.det(hessian) == 0:
            raise ValueError("The Hessian matrix is singular and cannot be inverted.")

        hessian_inv = np.linalg.inv(hessian)
        new_point = current_point - hessian_inv.dot(gradient)

        if np.linalg.norm(new_point - current_point) < epsilon:
            break

        current_point = new_point
        visited_points.append(current_point.flatten().tolist())

    return current_point.flatten(), visited_points
