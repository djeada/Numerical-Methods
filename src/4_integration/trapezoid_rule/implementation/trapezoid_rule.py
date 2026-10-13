from typing import Callable, List
import numpy as np


def trapezoid_rule(f: Callable[[float], float], a: float, b: float, n: int) -> float:
    if n <= 0:
        raise ValueError("Number of intervals must be positive.")
    x = np.linspace(a, b, n + 1)
    y = f(x)
    h = (b - a) / n
    w = np.ones(n + 1)
    w[1:-1] = 2
    return np.sum(y * w) * h / 2


def trapezoid_rule_multidim(
    f: Callable[[np.ndarray], float], bounds: List[tuple], n: int
) -> float:
    if n <= 0:
        raise ValueError("Number of intervals must be positive.")
    dims = len(bounds)
    grids = [np.linspace(a, b, n + 1) for a, b in bounds]
    mesh = np.meshgrid(*grids, indexing="ij")
    points = np.stack(mesh, axis=-1)
    flat_points = points.reshape(-1, dims)

    # Accept only a scalar or one value per point; otherwise f is per-point.
    try:
        flat_vals = np.asarray(f(flat_points), dtype=float)
        if flat_vals.ndim == 0:
            flat_vals = np.full(flat_points.shape[0], float(flat_vals))
        elif flat_vals.shape != (flat_points.shape[0],):
            raise ValueError("f is not vectorized")
    except Exception:
        flat_vals = np.apply_along_axis(f, 1, flat_points)

    vals = flat_vals.reshape([n + 1] * dims)
    w_1d = np.ones(n + 1)
    w_1d[1:-1] = 2
    W = w_1d
    for _ in range(dims - 1):
        W = np.outer(W, w_1d)
    W = W.reshape([n + 1] * dims)

    h = [(b - a) / n for a, b in bounds]
    return np.sum(vals * W) * np.prod(h) / (2**dims)
