# midpoint_rule.py
from typing import Callable
import numpy as np

def midpoint_rule(
    f: Callable[[float], float],
    a: float,
    b: float,
    n: int
) -> float:
    if n <= 0:
        raise ValueError("Number of intervals must be positive.")
    h = (b - a) / n
    midpoints = a + h * (np.arange(n) + 0.5)
    return h * np.sum(f(midpoints))

def midpoint_rule_multidim(
    f: Callable[[np.ndarray], float],
    bounds: list,
    n: int
) -> float:
    if n <= 0:
        raise ValueError("Number of intervals must be positive.")
    dimensions = len(bounds)
    h = [(b - a) / n for a, b in bounds]
    grids = [a + h_i * (np.arange(n) + 0.5) for h_i, (a, b) in zip(h, bounds)]
    mesh = np.meshgrid(*grids, indexing='ij')
    points = np.stack(mesh, axis=-1).reshape(-1, dimensions)
    return np.prod(h) * np.sum(f(points))
