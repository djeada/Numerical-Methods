# heun_solver.py
import numpy as np
from typing import Callable, Tuple

def heun_method(
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
        ti = t[i]
        yi = y[i]
        k1 = f(ti, yi)
        y_predict = yi + h * k1
        k2 = f(ti + h, y_predict)
        y_next = yi + (h / 2) * (k1 + k2)
        if np.linalg.norm(y_next - yi, ord=np.inf) < tol:
            y[i + 1] = y_next
            y[i + 2:] = y_next
            break
        y[i + 1] = y_next
    return t, y
