from typing import Callable
import numpy as np


def taylor_series(
    f: Callable[[float], float],
    a: float,
    n: int,
    x: float,
    derivatives: Callable[[int], float],
) -> float:
    k = np.arange(n)
    factorial = np.cumprod(np.append(1, k[1:]))
    terms = derivatives(k) / factorial * (x - a) ** k
    return np.sum(terms)
