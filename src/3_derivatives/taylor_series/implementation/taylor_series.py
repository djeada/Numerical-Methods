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
    # Float arithmetic: int64 factorials / powers silently overflow for n > 20.
    factorial = np.cumprod(np.append(1.0, k[1:].astype(float)))
    terms = derivatives(k) / factorial * (x - a) ** k.astype(float)
    return np.sum(terms)
