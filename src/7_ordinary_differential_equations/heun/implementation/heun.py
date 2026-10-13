# heun_solver.py
import numpy as np
from typing import Callable, Tuple


def heun_method(
    f: Callable[[float, np.ndarray], np.ndarray],
    t0: float,
    y0: np.ndarray,
    t_end: float,
    h: float,
) -> Tuple[np.ndarray, np.ndarray]:
    """Integrate y' = f(t, y) from t0 to t_end with Heun's method.

    Steps have length h, except that the last one is shortened when
    (t_end - t0) / h is not an integer, so t[-1] == t_end exactly.

    Returns (t, y). y has shape (n + 1,) when y0 has a single component and
    (n + 1, d) when y0 has d > 1 components; y[i] approximates y(t[i]).
    """
    if h <= 0:
        raise ValueError("Step size h must be positive.")
    if t_end < t0:
        raise ValueError("t_end must be greater than or equal to t0.")
    y0 = np.atleast_1d(np.asarray(y0, dtype=float))
    n_full = int(np.floor((t_end - t0) / h + 1e-9))
    t = t0 + h * np.arange(n_full + 1)
    if t_end - t[-1] > 1e-9 * h:
        t = np.append(t, t_end)  # shortened final step
    else:
        t[-1] = t_end
    y = np.zeros((len(t), y0.size))
    y[0] = y0
    for i in range(len(t) - 1):
        ti = t[i]
        yi = y[i]
        hi = t[i + 1] - ti
        k1 = f(ti, yi)
        y_predict = yi + hi * k1
        k2 = f(ti + hi, y_predict)
        y[i + 1] = yi + (hi / 2) * (k1 + k2)
    return t, (y.reshape(-1) if y0.size == 1 else y)
