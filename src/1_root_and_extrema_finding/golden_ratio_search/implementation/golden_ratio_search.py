import numpy as np
from typing import Callable


def golden_ratio_search(
    f: Callable[[float], float],
    a: float,
    b: float,
    tol: float = 1e-8,
    max_iterations: int = 1000,
) -> float:
    """
    Golden-section search for a minimizer of a unimodal function on [a, b].

    One new function evaluation is made per iteration: the interior point that
    survives a shrink is reused (with its stored value) as the other interior
    point of the smaller interval.

    Stops when b - a < tol, or immediately if f(c) == f(d) (no information to
    discard either side), returning the midpoint of the current interval.

    Raises:
        ValueError: If the method does not converge within max_iterations.
    """
    gr = (np.sqrt(5) + 1) / 2
    c = b - (b - a) / gr
    d = a + (b - a) / gr
    fc = f(c)
    fd = f(d)
    for _ in range(max_iterations):
        if fc < fd:
            # Minimum in [a, d]: old c becomes the new d.
            b, d, fd = d, c, fc
            c = b - (b - a) / gr
            if np.abs(b - a) < tol:
                return (b + a) / 2
            fc = f(c)
        elif fc > fd:
            # Minimum in [c, b]: old d becomes the new c.
            a, c, fc = c, d, fd
            d = a + (b - a) / gr
            if np.abs(b - a) < tol:
                return (b + a) / 2
            fd = f(d)
        else:
            # If fc == fd, return the midpoint
            return (a + b) / 2
    raise ValueError(
        "Golden ratio search did not converge within the maximum number of iterations."
    )
