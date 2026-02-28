# test_local_optimization.py
import pytest
import numpy as np
from ..implementation.local_optimization import (
    gradient_descent_optimize,
    newtons_method_optimize,
    bfgs,
)


# Gradient Descent Tests


def test_gd_quadratic():
    f = lambda x: np.dot(x, x)
    grad_f = lambda x: 2 * x
    x0 = np.array([5.0, -3.0])
    x = gradient_descent_optimize(f, grad_f, x0, learning_rate=0.1)
    assert np.allclose(x, np.zeros(2), atol=1e-5)


def test_gd_shifted_quadratic():
    f = lambda x: (x[0] - 3) ** 2 + (x[1] + 1) ** 2
    grad_f = lambda x: np.array([2 * (x[0] - 3), 2 * (x[1] + 1)])
    x0 = np.array([0.0, 0.0])
    x = gradient_descent_optimize(f, grad_f, x0, learning_rate=0.1)
    assert np.allclose(x, np.array([3.0, -1.0]), atol=1e-4)


def test_gd_constant_function():
    f = lambda x: 5.0
    grad_f = lambda x: np.zeros_like(x)
    x0 = np.array([1.0, 2.0])
    x = gradient_descent_optimize(f, grad_f, x0)
    assert np.allclose(x, x0, atol=1e-6)


def test_gd_non_convergent():
    f = lambda x: np.abs(x[0])
    grad_f = lambda x: np.array([np.sign(x[0])])
    x0 = np.array([1.0])
    with pytest.raises(ValueError):
        gradient_descent_optimize(f, grad_f, x0, learning_rate=0.1, max_iterations=10)


def test_gd_single_variable():
    f = lambda x: (x[0] - 2) ** 2
    grad_f = lambda x: np.array([2 * (x[0] - 2)])
    x0 = np.array([0.0])
    x = gradient_descent_optimize(f, grad_f, x0, learning_rate=0.1)
    assert np.allclose(x, np.array([2.0]), atol=1e-5)


# Newton's Method Tests


def test_newton_quadratic():
    f = lambda x: np.dot(x, x)
    grad_f = lambda x: 2 * x
    hess_f = lambda x: 2 * np.eye(len(x))
    x0 = np.array([10.0, -10.0])
    x = newtons_method_optimize(f, grad_f, hess_f, x0)
    assert np.allclose(x, np.zeros(2), atol=1e-8)


def test_newton_shifted_quadratic():
    f = lambda x: (x[0] - 1) ** 2 + (x[1] - 2) ** 2
    grad_f = lambda x: np.array([2 * (x[0] - 1), 2 * (x[1] - 2)])
    hess_f = lambda x: np.array([[2.0, 0.0], [0.0, 2.0]])
    x0 = np.array([0.0, 0.0])
    x = newtons_method_optimize(f, grad_f, hess_f, x0)
    assert np.allclose(x, np.array([1.0, 2.0]), atol=1e-8)


def test_newton_single_step_quadratic():
    # Newton should converge in one step for a pure quadratic
    f = lambda x: 0.5 * x[0] ** 2 + 0.5 * x[1] ** 2
    grad_f = lambda x: x.copy()
    hess_f = lambda x: np.eye(2)
    x0 = np.array([5.0, -3.0])
    x = newtons_method_optimize(f, grad_f, hess_f, x0, max_iterations=2)
    assert np.allclose(x, np.zeros(2), atol=1e-10)


def test_newton_non_convergent():
    f = lambda x: x[0] ** 4
    grad_f = lambda x: np.array([4 * x[0] ** 3])
    hess_f = lambda x: np.array([[12 * x[0] ** 2]])
    x0 = np.array([1.0])
    # Hessian becomes singular as x approaches 0, causing issues
    with pytest.raises(ValueError):
        newtons_method_optimize(f, grad_f, hess_f, x0, max_iterations=3)


# BFGS Tests


def test_bfgs_quadratic():
    f = lambda x: np.dot(x, x)
    grad_f = lambda x: 2 * x
    x0 = np.array([5.0, -3.0])
    x = bfgs(f, grad_f, x0)
    assert np.allclose(x, np.zeros(2), atol=1e-4)


def test_bfgs_shifted_quadratic():
    f = lambda x: (x[0] - 3) ** 2 + (x[1] + 1) ** 2
    grad_f = lambda x: np.array([2 * (x[0] - 3), 2 * (x[1] + 1)])
    x0 = np.array([0.0, 0.0])
    x = bfgs(f, grad_f, x0)
    assert np.allclose(x, np.array([3.0, -1.0]), atol=1e-4)


def test_bfgs_rosenbrock():
    def f(x):
        return (1 - x[0]) ** 2 + 100 * (x[1] - x[0] ** 2) ** 2

    def grad_f(x):
        dx0 = -2 * (1 - x[0]) - 400 * x[0] * (x[1] - x[0] ** 2)
        dx1 = 200 * (x[1] - x[0] ** 2)
        return np.array([dx0, dx1])

    x0 = np.array([-1.0, 1.0])
    x = bfgs(f, grad_f, x0, max_iterations=5000)
    assert np.allclose(x, np.array([1.0, 1.0]), atol=1e-2)


def test_bfgs_high_dimensions():
    def f(x):
        return np.sum(x ** 2)

    def grad_f(x):
        return 2 * x

    x0 = np.ones(10) * 5.0
    x = bfgs(f, grad_f, x0)
    assert np.allclose(x, np.zeros(10), atol=1e-4)


def test_bfgs_single_variable():
    f = lambda x: (x[0] - 7) ** 2
    grad_f = lambda x: np.array([2 * (x[0] - 7)])
    x0 = np.array([0.0])
    x = bfgs(f, grad_f, x0)
    assert np.allclose(x, np.array([7.0]), atol=1e-4)
