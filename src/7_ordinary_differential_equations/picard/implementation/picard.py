import numpy as np
from typing import Callable, Tuple


def picard_method(
    f: Callable[[float, np.ndarray], np.ndarray],
    t0: float,
    y0: np.ndarray,
    t_end: float,
    h: float,
    tol: float = 1e-6,
    max_iterations: int = 1000,
) -> Tuple[np.ndarray, np.ndarray]:
    """Integrate y' = f(t, y) with fixed-point (Picard-type) iteration per step.

    This is not Picard iteration on whole functions (see the notes). Each step
    solves the implicit midpoint equation
    y_{n+1} = y_n + h f(t_n + h/2, (y_n + y_{n+1})/2) by repeated substitution
    (converges when h*L/2 < 1), so the method is second order.

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
        hi = t[i + 1] - t[i]
        y_prev = y[i]
        y_next = y_prev.copy()
        for _ in range(max_iterations):
            y_new = y_prev + hi * f(t[i] + 0.5 * hi, 0.5 * (y_prev + y_next))
            if np.linalg.norm(y_new - y_next, ord=np.inf) < tol:
                y_next = y_new
                break
            y_next = y_new
        else:
            raise ValueError(f"Picard iteration did not converge at step {i}.")
        y[i + 1] = y_next
    return t, (y.reshape(-1) if y0.size == 1 else y)
