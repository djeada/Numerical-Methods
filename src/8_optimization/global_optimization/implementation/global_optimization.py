# global_optimization.py
import numpy as np
from typing import Callable, Optional, Tuple, List


def grid_search(
    f: Callable[[np.ndarray], float],
    bounds: List[Tuple[float, float]],
    n_points: int = 50,
) -> Tuple[np.ndarray, float]:
    """
    Brute-force grid search for global optimization.

    Evaluates f at every point on a regular grid over the given bounds
    and returns the point with the smallest function value.

    Args:
        f: Objective function mapping an n-dimensional vector to a scalar.
        bounds: List of (lower, upper) bounds for each dimension.
        n_points: Number of grid points per dimension.

    Returns:
        Tuple of (best_x, best_f) where best_x is the approximate
        global minimizer and best_f is the corresponding function value.
    """
    grids = [np.linspace(lo, hi, n_points) for lo, hi in bounds]
    mesh = np.meshgrid(*grids, indexing="ij")
    points = np.stack(mesh, axis=-1).reshape(-1, len(bounds))

    best_x = points[0]
    best_f = f(points[0])
    for pt in points[1:]:
        val = f(pt)
        if val < best_f:
            best_f = val
            best_x = pt

    return best_x, best_f


def simulated_annealing(
    f: Callable[[np.ndarray], float],
    bounds: List[Tuple[float, float]],
    x0: Optional[np.ndarray] = None,
    T0: float = 10.0,
    cooling_rate: float = 0.95,
    sigma: float = 0.5,
    max_iterations: int = 10000,
    seed: Optional[int] = None,
) -> Tuple[np.ndarray, float]:
    """
    Simulated annealing for global optimization.

    Uses a probabilistic acceptance criterion to escape local minima
    by occasionally accepting moves that increase the objective value.

    Args:
        f: Objective function.
        bounds: List of (lower, upper) bounds for each dimension.
        x0: Initial point, optional. Defaults to center of bounds.
        T0: Initial temperature.
        cooling_rate: Multiplicative cooling factor in (0, 1).
        sigma: Standard deviation of the perturbation.
        max_iterations: Maximum number of iterations.
        seed: Random seed for reproducibility.

    Returns:
        Tuple of (best_x, best_f).
    """
    rng = np.random.default_rng(seed)
    n = len(bounds)
    lowers = np.array([lo for lo, hi in bounds])
    uppers = np.array([hi for lo, hi in bounds])

    if x0 is None:
        x0 = (lowers + uppers) / 2.0

    x = x0.copy()
    fx = f(x)
    best_x = x.copy()
    best_f = fx
    T = T0

    for _ in range(max_iterations):
        candidate = x + sigma * rng.standard_normal(n)
        candidate = np.clip(candidate, lowers, uppers)
        fc = f(candidate)
        delta = fc - fx

        if delta <= 0 or rng.random() < np.exp(-delta / max(T, 1e-300)):
            x = candidate
            fx = fc

        if fx < best_f:
            best_f = fx
            best_x = x.copy()

        T *= cooling_rate

    return best_x, best_f


def genetic_algorithm(
    f: Callable[[np.ndarray], float],
    bounds: List[Tuple[float, float]],
    pop_size: int = 50,
    n_generations: int = 200,
    mutation_rate: float = 0.1,
    crossover_rate: float = 0.7,
    seed: Optional[int] = None,
) -> Tuple[np.ndarray, float]:
    """
    Genetic algorithm for global optimization.

    Evolves a population of candidate solutions using selection,
    crossover, and mutation operators inspired by biological evolution.

    Args:
        f: Objective function.
        bounds: List of (lower, upper) bounds for each dimension.
        pop_size: Population size.
        n_generations: Number of generations.
        mutation_rate: Probability of mutating each gene.
        crossover_rate: Probability of crossover between two parents.
        seed: Random seed for reproducibility.

    Returns:
        Tuple of (best_x, best_f).
    """
    rng = np.random.default_rng(seed)
    n = len(bounds)
    lowers = np.array([lo for lo, hi in bounds])
    uppers = np.array([hi for lo, hi in bounds])

    population = rng.uniform(lowers, uppers, size=(pop_size, n))
    fitness = np.array([f(ind) for ind in population])

    best_idx = np.argmin(fitness)
    best_x = population[best_idx].copy()
    best_f = fitness[best_idx]

    for _ in range(n_generations):
        # Tournament selection
        new_population = np.empty_like(population)
        for i in range(pop_size):
            a, b = rng.choice(pop_size, size=2, replace=False)
            winner = a if fitness[a] < fitness[b] else b
            new_population[i] = population[winner]

        # Crossover
        for i in range(0, pop_size - 1, 2):
            if rng.random() < crossover_rate:
                alpha = rng.uniform(0, 1, size=n)
                child1 = alpha * new_population[i] + (1 - alpha) * new_population[i + 1]
                child2 = (1 - alpha) * new_population[i] + alpha * new_population[i + 1]
                new_population[i] = child1
                new_population[i + 1] = child2

        # Mutation
        for i in range(pop_size):
            mask = rng.random(n) < mutation_rate
            new_population[i, mask] += rng.standard_normal(np.sum(mask)) * (uppers[mask] - lowers[mask]) * 0.1
            new_population[i] = np.clip(new_population[i], lowers, uppers)

        population = new_population
        fitness = np.array([f(ind) for ind in population])

        gen_best_idx = np.argmin(fitness)
        if fitness[gen_best_idx] < best_f:
            best_f = fitness[gen_best_idx]
            best_x = population[gen_best_idx].copy()

    return best_x, best_f
