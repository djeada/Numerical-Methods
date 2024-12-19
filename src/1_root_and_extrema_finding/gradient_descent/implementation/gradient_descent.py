# gradient_descent.py
import numpy as np
from typing import Callable, Optional


def gradient_descent(
    f: Callable[[np.ndarray], float],
    grad_f: Callable[[np.ndarray], np.ndarray],
    x0: np.ndarray,
    learning_rate: float = 0.01,
    tol: float = 1e-6,
    max_iterations: int = 1000
) -> np.ndarray:
    x = x0.astype(float)
    for _ in range(max_iterations):
        grad = grad_f(x)
        x_new = x - learning_rate * grad
        if np.linalg.norm(x_new - x, ord=np.inf) < tol:
            return x_new
        x = x_new
    raise ValueError("Gradient descent did not converge within the maximum number of iterations.")
