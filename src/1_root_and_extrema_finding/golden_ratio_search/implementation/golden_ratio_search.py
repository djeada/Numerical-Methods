# golden_ratio_search.py
import numpy as np
from typing import Callable


def golden_ratio_search(
    f: Callable[[float], float],
    a: float,
    b: float,
    tol: float = 1e-8,
    max_iterations: int = 1000
) -> float:
    gr: float = (np.sqrt(5) + 1) / 2
    c: float = b - (b - a) / gr
    d: float = a + (b - a) / gr
    for _ in range(max_iterations):
        fc: float = f(c)
        fd: float = f(d)
        if fc < fd:
            b, d = d, c
            c = b - (b - a) / gr
        else:
            a, c = c, d
            d = a + (b - a) / gr
        if np.abs(b - a) < tol:
            return (b + a) / 2
    raise ValueError("Golden ratio search did not converge within the maximum number of iterations.")
