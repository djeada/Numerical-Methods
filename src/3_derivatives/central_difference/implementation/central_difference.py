# central_difference.py
from typing import Callable
import numpy as np


def central_difference(f: Callable[[float], float], x: float, h: float = 1e-5) -> float:
    return (f(x + h) - f(x - h)) / (2 * h)


def central_difference_gradient(
    f: Callable[[np.ndarray], float], x: np.ndarray, h: float = 1e-5
) -> np.ndarray:
    gradient = np.zeros_like(x, dtype=float)
    for i in range(len(x)):
        x_forward = x.copy()
        x_backward = x.copy()
        x_forward[i] += h
        x_backward[i] -= h
        gradient[i] = (f(x_forward) - f(x_backward)) / (2 * h)
    return gradient
