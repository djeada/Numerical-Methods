# heun_solver.py
import numpy as np
from typing import Callable, Tuple


def heun_method(f, t0, y0, t_end, h):
    if h <= 0:
        raise ValueError("Step size h must be positive.")
    n_steps = int(np.ceil((t_end - t0) / h))
    t = np.linspace(t0, t_end, n_steps + 1)
    y = np.zeros((n_steps + 1, len(y0)))
    y[0] = y0
    for i in range(n_steps):
        ti = t[i]
        yi = y[i]
        k1 = f(ti, yi)
        y_predict = yi + h * k1
        k2 = f(ti + h, y_predict)
        y[i + 1] = yi + (h / 2) * (k1 + k2)
    return t, y
