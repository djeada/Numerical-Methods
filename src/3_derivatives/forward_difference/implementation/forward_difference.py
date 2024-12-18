# forward_difference.py
from typing import Callable, Optional
import numpy as np

def forward_difference(
    f: Callable[[float], float],
    x: float,
    h: float = 1e-5
) -> float:
    return (f(x + h) - f(x)) / h

def forward_difference_gradient(
    f: Callable[[np.ndarray], float],
    x: np.ndarray,
    h: float = 1e-5
) -> np.ndarray:
    gradient = np.zeros_like(x, dtype=float)
    for i in range(len(x)):
        x_forward = x.copy()
        x_forward[i] += h
        gradient[i] = (f(x_forward) - f(x)) / h
    return gradient
