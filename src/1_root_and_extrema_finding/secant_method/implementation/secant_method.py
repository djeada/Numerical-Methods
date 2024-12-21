# secant_method.py
import numpy as np
from typing import Callable


def secant_method(
    f: Callable[[float], float],
    x0: float,
    x1: float,
    tol: float = 1e-6,
    max_iterations: int = 100000,
) -> float:
    for _ in range(max_iterations):
        f_x0 = f(x0)
        f_x1 = f(x1)
        denominator = f_x1 - f_x0
        if np.isclose(denominator, 0.0):
            raise ValueError("Denominator is zero. Division by zero encountered.")
        x2 = x1 - f_x1 * (x1 - x0) / denominator
        if np.abs(x2 - x1) < tol:
            return x2
        x0, x1 = x1, x2
    raise ValueError(
        "Secant method did not converge within the maximum number of iterations."
    )
