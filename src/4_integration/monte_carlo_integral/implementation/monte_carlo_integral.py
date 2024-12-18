# monte_carlo_integral.py
from typing import Callable, Tuple
import numpy as np

def monte_carlo_integral(
    f: Callable[[float], float],
    a: float,
    b: float,
    num_samples: int = 1000000
) -> float:
    samples: np.ndarray = np.random.uniform(a, b, num_samples)
    evaluations: np.ndarray = f(samples)
    average: float = np.mean(evaluations)
    integral: float = (b - a) * average
    return integral

def monte_carlo_integral_multidim(
    f: Callable[[np.ndarray], float],
    bounds: Tuple[Tuple[float, float], ...],
    num_samples: int = 1000000
) -> float:
    dimensions: int = len(bounds)
    lower_bounds: np.ndarray = np.array([bound[0] for bound in bounds])
    upper_bounds: np.ndarray = np.array([bound[1] for bound in bounds])
    samples: np.ndarray = np.random.uniform(0, 1, (num_samples, dimensions))
    scaled_samples: np.ndarray = lower_bounds + samples * (upper_bounds - lower_bounds)
    evaluations: np.ndarray = f(scaled_samples)
    volume: float = np.prod(upper_bounds - lower_bounds)
    average: float = np.mean(evaluations)
    integral: float = volume * average
    return integral
