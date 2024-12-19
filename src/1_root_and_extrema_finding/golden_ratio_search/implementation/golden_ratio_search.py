import numpy as np
from typing import Callable


def golden_ratio_search(
    f: Callable[[float], float],
    a: float,
    b: float,
    tol: float = 1e-8,
    max_iterations: int = 1000
) -> float:
    f_mod = lambda x: (f(x))**2
    gr = (np.sqrt(5) + 1) / 2
    c = b - (b - a) / gr
    d = a + (b - a) / gr
    for _ in range(max_iterations):
        fc = f_mod(c)
        fd = f_mod(d)
        if fc < fd:
            b, d = d, c
            c = b - (b - a) / gr
        elif fc > fd:
            a, c = c, d
            d = a + (b - a) / gr
        else:
            # If fc == fd, return the midpoint
            return (a + b) / 2
        if np.abs(b - a) < tol:
            return (b + a) / 2
    raise ValueError("Golden ratio search did not converge within the maximum number of iterations.")
