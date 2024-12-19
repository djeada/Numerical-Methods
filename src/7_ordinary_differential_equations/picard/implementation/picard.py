import numpy as np
from typing import Callable, Tuple
import bisect

def picard_method(
    f: Callable[[float, np.ndarray], np.ndarray],
    t0: float,
    y0: np.ndarray,
    t_end: float,
    h: float,
    tol: float = 1e-6,
    max_iterations: int = 1000
) -> Tuple[np.ndarray, np.ndarray]:
    if h <= 0:
        raise ValueError("Step size h must be positive.")
    if t_end < t0:
        raise ValueError("t_end must be greater than or equal to t0.")
    n_steps = int(np.ceil((t_end - t0) / h))
    t = np.linspace(t0, t0 + n_steps * h, n_steps + 1)
    y = np.zeros((n_steps + 1, y0.size))
    y[0] = y0
    for i in range(n_steps):
        y_prev = y[i]
        t_next = t[i] + h
        # Picard iterations to find y_next
        y_next = y_prev.copy()
        for _ in range(max_iterations):
            y_new = y_prev + h * f(t_next, y_next)
            if np.linalg.norm(y_new - y_next, ord=np.inf) < tol:
                y_next = y_new
                break
            y_next = y_new
        else:
            raise ValueError(f"Picard iteration did not converge at step {i}.")
        y[i + 1] = y_next
    return t, y
