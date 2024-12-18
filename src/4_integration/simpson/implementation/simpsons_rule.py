# simpson_rule.py
from typing import Callable, List
import numpy as np

def simpson_rule(
    f: Callable[[float], float],
    a: float,
    b: float,
    n: int
) -> float:
    if n <= 0 or n % 2 != 0:
        raise ValueError("Number of intervals must be a positive even integer.")
    h = (b - a) / n
    x = a + h * np.arange(n + 1)
    y = f(x)
    S = y[0] + y[-1] + 4 * np.sum(y[1:-1:2]) + 2 * np.sum(y[2:-2:2])
    return S * h / 3

def simpson_rule_multidim(
    f: Callable[[np.ndarray], float],
    bounds: List[tuple],
    n: int
) -> float:
    if n <= 0 or n % 2 != 0:
        raise ValueError("Number of intervals must be a positive even integer.")
    dimensions = len(bounds)
    h = [(b - a) / n for a, b in bounds]
    grids = [a + h_i * np.arange(n + 1) for h_i, (a, b) in zip(h, bounds)]
    mesh = np.meshgrid(*grids, indexing='ij')
    points = np.stack(mesh, axis=-1).reshape(-1, dimensions)
    weights = np.ones(points.shape[0])
    for dim in range(dimensions):
        idx = points[:, dim]
        idx = (idx - bounds[dim][0]) / h[dim]
        idx = np.round(idx).astype(int)
        weight = np.where((idx == 0) | (idx == n), 1,
                          np.where(idx % 2 == 0, 2, 4))
        weights *= weight
    return np.sum(f(points) * weights) * np.prod(h) / 3
