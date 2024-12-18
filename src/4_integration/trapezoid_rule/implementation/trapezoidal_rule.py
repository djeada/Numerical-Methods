# trapezoid_rule.py
from typing import Callable, List
import numpy as np

def trapezoid_rule(
    f: Callable[[float], float],
    a: float,
    b: float,
    n: int
) -> float:
    if n <= 0:
        raise ValueError("Number of intervals must be positive.")
    h = (b - a) / n
    x = a + h * np.arange(n + 1)
    y = f(x)
    S = y[0] + y[-1] + 2 * np.sum(y[1:-1])
    return S * h / 2

def trapezoid_rule_multidim(
    f: Callable[[np.ndarray], float],
    bounds: List[tuple],
    n: int
) -> float:
    if n <= 0:
        raise ValueError("Number of intervals must be positive.")
    dimensions = len(bounds)
    h = [(b - a) / n for a, b in bounds]
    grids = [a + h_i * np.arange(n + 1) for h_i, (a, b) in zip(h, bounds)]
    mesh = np.meshgrid(*grids, indexing='ij')
    points = np.stack(mesh, axis=-1).reshape(-1, dimensions)
    weights = np.ones(points.shape[0])
    for dim in range(dimensions):
        idx = np.round((points[:, dim] - bounds[dim][0]) / h[dim]).astype(int)
        weights *= np.where((idx == 0) | (idx == n), 1, 2)
    return np.sum(f(points) * weights) * np.prod(h) / 2
