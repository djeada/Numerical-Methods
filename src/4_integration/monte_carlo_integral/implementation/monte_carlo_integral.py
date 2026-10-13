from typing import Callable, Optional, Tuple
import numpy as np


def monte_carlo_integral(
    f: Callable[[float], float],
    a: float,
    b: float,
    num_samples: int = 1000000,
    seed: Optional[int] = 0,
) -> float:
    if num_samples <= 0:
        raise ValueError("Number of samples must be greater than zero.")
    # Default seed 0 keeps results reproducible; pass seed=None for fresh entropy.
    rng = np.random.default_rng(seed)  # does not mutate global RNG state
    samples = rng.uniform(a, b, num_samples)
    evaluations = f(samples)
    integral = (b - a) * np.mean(evaluations)
    return integral


def monte_carlo_integral_multidim(
    f: Callable[[np.ndarray], float],
    bounds: Tuple[Tuple[float, float], ...],
    num_samples: int = 1000000,
    seed: Optional[int] = 0,
) -> float:
    if num_samples <= 0:
        raise ValueError("Number of samples must be greater than zero.")
    # Default seed 0 keeps results reproducible; pass seed=None for fresh entropy.
    rng = np.random.default_rng(seed)  # does not mutate global RNG state
    dimensions = len(bounds)
    lower_bounds = np.array([b[0] for b in bounds])
    upper_bounds = np.array([b[1] for b in bounds])
    samples = rng.uniform(0, 1, (num_samples, dimensions))
    scaled_samples = lower_bounds + samples * (upper_bounds - lower_bounds)
    evaluations = np.apply_along_axis(f, 1, scaled_samples)
    volume = np.prod(upper_bounds - lower_bounds)
    integral = volume * np.mean(evaluations)
    return integral
