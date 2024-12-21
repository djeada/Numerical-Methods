import numpy as np
from typing import Callable, Tuple


def runge_kutta_4(
    f: Callable[[float, np.ndarray], np.ndarray],
    t0: float,
    y0: np.ndarray,
    t_end: float,
    h: float,
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
        k2 = f(ti + h / 2, yi + h * k1 / 2)
        k3 = f(ti + h / 2, yi + h * k2 / 2)
        k4 = f(ti + h, yi + h * k3)
        y[i + 1] = yi + (h / 6) * (k1 + 2 * k2 + 2 * k3 + k4)
    return t, y.squeeze()
