from typing import Callable
import math

def taylor_series(
    f: Callable[[float], float],
    a: float,
    n: int,
    x: float,
    derivatives: Callable[[int], float]
) -> float:
    approximation: float = 0.0
    for k in range(n):
        term: float = derivatives(k)(a) / math.factorial(k) * (x - a) ** k
        approximation += term
    return approximation
