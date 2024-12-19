# relaxation_method.py
import numpy as np
from typing import Callable

def relaxation_method(
    func: Callable[[float], float],
    initial_guess: float,
    omega: float = None,
    tol: float = 1e-6,
    max_iterations: int = 100000
) -> float:
    x = initial_guess
    delta = 1e-8
    for _ in range(max_iterations):
        f_prime = (func(x + delta) - func(x - delta)) / (2 * delta)
        if abs(f_prime) >= 1:
            if f_prime == 0:
                return np.nan
            omega = -1.0 / f_prime
        else:
            omega = 1.0
        x_new = (1 - omega) * x + omega * func(x)
        if np.abs(x_new - x) < tol:
            return x_new
        x = x_new
    return x
