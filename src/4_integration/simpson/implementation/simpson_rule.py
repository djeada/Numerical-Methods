from typing import Callable, List
import numpy as np


def simpson_rule(f: Callable[[float], float], a: float, b: float, n: int) -> float:
    if n <= 0 or n % 2 != 0:
        raise ValueError("Number of intervals must be a positive even integer.")
    x = np.linspace(a, b, n + 1)
    y = np.array([f(xi) for xi in x])
    h = (b - a) / n
    return (h / 3) * (y[0] + y[-1] + 4 * np.sum(y[1:-1:2]) + 2 * np.sum(y[2:-2:2]))


def simpson_rule_multidim(
    f: Callable[[np.ndarray], np.ndarray], bounds: List[tuple], n: int
) -> float:
    if n <= 0 or n % 2 != 0:
        raise ValueError("Number of intervals must be a positive even integer.")
    dims = len(bounds)
    grids = [np.linspace(a, b, n + 1) for a, b in bounds]
    mesh = np.meshgrid(*grids, indexing="ij")
    points = np.stack(mesh, axis=-1)
    flat_points = points.reshape(-1, dims)
    flat_vals = f(flat_points)
    if isinstance(flat_vals, float):  # Handle scalar output
        flat_vals = np.full(flat_points.shape[0], flat_vals)
    vals = flat_vals.reshape([n + 1] * dims)
    h = [(b - a) / n for a, b in bounds]

    w_1d = np.ones(n + 1)
    w_1d[1:-1:2] = 4
    w_1d[2:-2:2] = 2
    W = w_1d
    for _ in range(dims - 1):
        W = np.outer(W, w_1d)
    W = W.reshape([n + 1] * dims)

    return np.sum(vals * W) * np.prod(h) / 3 ** dims
