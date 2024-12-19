# relaxation_method.py
import numpy as np
from typing import Callable


def relaxation_method(
    func: Callable[[float], float],
    initial_guess: float,
    omega: float = 1.0,
    tol: float = 1e-6,
    max_iterations: int = 100000
) -> float:
    x = initial_guess
    for _ in range(max_iterations):
        previous_x = x
        x_new = func(x)
        error = np.abs(x_new - x)
        if error < tol:
            return x
        if _ > 0:
            omega = error / np.abs(x_new - previous_x)
        x = (1 - omega) * x + omega * x_new
    return x
