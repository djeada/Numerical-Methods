# gradient_descent.py
import numpy as np
from typing import Callable


def gradient_descent(
    f: Callable[[np.ndarray], float],
    grad_f: Callable[[np.ndarray], np.ndarray],
    x0: np.ndarray,
    learning_rate: float = 0.01,
    tol: float = 1e-6,
    max_iterations: int = 1000,
) -> np.ndarray:
    x = x0.astype(float)
    for _ in range(max_iterations):
        grad = grad_f(x)
        grad_norm = np.linalg.norm(grad, ord=2)
        if grad_norm < tol:
            return x
        x = x - learning_rate * grad
    raise ValueError(
        "Gradient descent did not converge within the maximum number of iterations."
    )
