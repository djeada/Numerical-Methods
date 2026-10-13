# relaxation_method.py
import numpy as np
from typing import Callable, Optional


def relaxation_method(
    func: Callable[[float], float],
    initial_guess: float,
    omega: Optional[float] = None,
    tol: float = 1e-6,
    max_iterations: int = 100000,
) -> float:
    """
    Relaxation (fixed-point) method for solving x = func(x).

    Each step is x_new = (1 - w) * x + w * func(x). If omega is None, w is
    chosen adaptively at every iterate from the numerical slope g' of func:
    w = -1 / g' when |g'| >= 1, otherwise w = 1 (plain fixed-point iteration).
    Otherwise the supplied omega is used for every step.

    Stops when |x_new - x| < tol.

    Raises:
        ValueError: If the method does not converge within max_iterations.
    """
    x = initial_guess
    delta = 1e-8
    for _ in range(max_iterations):
        if omega is None:
            # Adaptive relaxation factor based on the slope of func at x
            f_prime = (func(x + delta) - func(x - delta)) / (2 * delta)
            w = -1.0 / f_prime if abs(f_prime) >= 1 else 1.0
        else:
            w = omega
        x_new = (1 - w) * x + w * func(x)
        if np.abs(x_new - x) < tol:
            return x_new
        x = x_new
    raise ValueError(
        "Relaxation method did not converge within the maximum number of iterations."
    )
