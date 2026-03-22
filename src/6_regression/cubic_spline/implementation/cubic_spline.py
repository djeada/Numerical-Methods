import numpy as np
import bisect
from typing import Callable


def cubic_spline(x_data: np.ndarray, y_data: np.ndarray) -> Callable[[float], float]:
    """Return a natural cubic spline interpolant through the given data.

    Builds the unique piecewise-cubic S(x) that passes through every
    (x_i, y_i), has continuous first and second derivatives at each
    interior knot, and satisfies the natural boundary conditions
    S''(x_0) = S''(x_n) = 0.

    The second derivatives M_i are found by solving the tridiagonal system

        h_{i-1} M_{i-1} + 2(h_{i-1}+h_i) M_i + h_i M_{i+1}
            = 6 [(y_{i+1}-y_i)/h_i - (y_i-y_{i-1})/h_{i-1}]

    via the Thomas algorithm, after which each piece is evaluated as

        S_i(x) = M_i/(6h_i)(x_{i+1}-x)³ + M_{i+1}/(6h_i)(x-x_i)³
               + (y_i - M_i h_i²/6)(x_{i+1}-x)/h_i
               + (y_{i+1} - M_{i+1} h_i²/6)(x-x_i)/h_i

    Parameters
    ----------
    x_data : 1-D array of strictly increasing x-coordinates (≥ 3 points).
    y_data : 1-D array of corresponding y-values.

    Returns
    -------
    Callable that evaluates the spline at any x in [x_data[0], x_data[-1]].
    """
    if x_data.shape[0] != y_data.shape[0]:
        raise ValueError("X and Y vectors must have equal number of elements.")
    if x_data.shape[0] < 3:
        raise ValueError("At least three data points are required.")
    if len(np.unique(x_data)) != x_data.shape[0]:
        raise ValueError("X data must contain unique values.")
    if not np.all(np.diff(x_data) > 0):
        raise ValueError("X data must be strictly increasing.")

    x_data = x_data.astype(float)
    y_data = y_data.astype(float)
    n = x_data.shape[0]
    h = np.diff(x_data)

    # RHS of the tridiagonal system (coefficient is 6, not 3)
    alpha = np.zeros(n)
    for i in range(1, n - 1):
        alpha[i] = 6 * (
            (y_data[i + 1] - y_data[i]) / h[i]
            - (y_data[i] - y_data[i - 1]) / h[i - 1]
        )

    # Thomas algorithm — forward sweep
    l = np.ones(n)
    mu = np.zeros(n)
    z = np.zeros(n)
    for i in range(1, n - 1):
        l[i] = 2 * (x_data[i + 1] - x_data[i - 1]) - h[i - 1] * mu[i - 1]
        mu[i] = h[i] / l[i]
        z[i] = (alpha[i] - h[i - 1] * z[i - 1]) / l[i]

    # Back-substitution → second derivatives M_i
    M = np.zeros(n)
    for j in range(n - 2, 0, -1):
        M[j] = z[j] - mu[j] * M[j + 1]

    def spline(X: float) -> float:
        if X < x_data[0] or X > x_data[-1]:
            raise ValueError(
                f"Query point {X} outside data range [{x_data[0]}, {x_data[-1]}]."
            )
        i = bisect.bisect_right(x_data, X) - 1
        i = min(max(i, 0), n - 2)
        dx = X - x_data[i]
        return (
            M[i] / (6 * h[i]) * (x_data[i + 1] - X) ** 3
            + M[i + 1] / (6 * h[i]) * dx**3
            + (y_data[i] - M[i] * h[i] ** 2 / 6) * (x_data[i + 1] - X) / h[i]
            + (y_data[i + 1] - M[i + 1] * h[i] ** 2 / 6) * dx / h[i]
        )

    return spline
