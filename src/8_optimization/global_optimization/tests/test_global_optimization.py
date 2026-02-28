# test_global_optimization.py
import pytest
import numpy as np
from ..implementation.global_optimization import (
    grid_search,
    simulated_annealing,
    genetic_algorithm,
)


def rastrigin(x):
    A = 10
    return A * len(x) + np.sum(x ** 2 - A * np.cos(2 * np.pi * x))


def sphere(x):
    return np.sum(x ** 2)


# Grid Search Tests


def test_grid_search_sphere_1d():
    best_x, best_f = grid_search(sphere, [(-5, 5)], n_points=101)
    assert np.abs(best_x[0]) < 0.1
    assert best_f < 0.01


def test_grid_search_sphere_2d():
    best_x, best_f = grid_search(sphere, [(-5, 5), (-5, 5)], n_points=51)
    assert np.linalg.norm(best_x) < 0.3
    assert best_f < 0.1


def test_grid_search_shifted_minimum():
    f = lambda x: (x[0] - 2) ** 2 + (x[1] + 1) ** 2
    best_x, best_f = grid_search(f, [(0, 4), (-3, 1)], n_points=81)
    assert np.abs(best_x[0] - 2) < 0.1
    assert np.abs(best_x[1] + 1) < 0.1


def test_grid_search_returns_best():
    f = lambda x: x[0] ** 2
    best_x, best_f = grid_search(f, [(-10, 10)], n_points=21)
    assert np.abs(best_x[0]) < 1.0


# Simulated Annealing Tests


def test_sa_sphere():
    best_x, best_f = simulated_annealing(
        sphere, [(-5, 5), (-5, 5)], T0=10, max_iterations=20000, seed=42
    )
    assert best_f < 0.5


def test_sa_rastrigin_1d():
    best_x, best_f = simulated_annealing(
        rastrigin, [(-5.12, 5.12)], T0=20, max_iterations=50000, seed=42
    )
    assert best_f < 2.0


def test_sa_with_initial_point():
    best_x, best_f = simulated_annealing(
        sphere, [(-5, 5), (-5, 5)], x0=np.array([4.0, 4.0]),
        T0=10, max_iterations=20000, seed=42
    )
    assert best_f < 1.0


def test_sa_respects_bounds():
    best_x, best_f = simulated_annealing(
        sphere, [(-1, 1), (-1, 1)], T0=5, max_iterations=5000, seed=42
    )
    assert np.all(best_x >= -1.0) and np.all(best_x <= 1.0)


# Genetic Algorithm Tests


def test_ga_sphere():
    best_x, best_f = genetic_algorithm(
        sphere, [(-5, 5), (-5, 5)], pop_size=50, n_generations=200, seed=42
    )
    assert best_f < 0.5


def test_ga_rastrigin_1d():
    best_x, best_f = genetic_algorithm(
        rastrigin, [(-5.12, 5.12)], pop_size=100, n_generations=300, seed=42
    )
    assert best_f < 2.0


def test_ga_respects_bounds():
    best_x, best_f = genetic_algorithm(
        sphere, [(-2, 2), (-2, 2)], pop_size=30, n_generations=100, seed=42
    )
    assert np.all(best_x >= -2.0) and np.all(best_x <= 2.0)


def test_ga_shifted_minimum():
    f = lambda x: (x[0] - 3) ** 2 + (x[1] + 2) ** 2
    best_x, best_f = genetic_algorithm(
        f, [(0, 6), (-5, 0)], pop_size=50, n_generations=200, seed=42
    )
    assert best_f < 1.0
