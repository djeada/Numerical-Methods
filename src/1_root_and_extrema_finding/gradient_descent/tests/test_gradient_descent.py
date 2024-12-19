# test_gradient_descent.py
import pytest
import numpy as np
from ..implementation.gradient_descent import gradient_descent


def test_gradient_descent_quadratic():
    f = lambda x: np.dot(x, x)
    grad_f = lambda x: 2 * x
    x0 = np.array([10.0, -10.0])
    x = gradient_descent(f, grad_f, x0, learning_rate=0.1)
    expected = np.array([0.0, 0.0])
    assert np.allclose(x, expected, atol=1e-6)


def test_gradient_descent_rosenbrock():
    def f(x):
        a = 1
        b = 100
        return (a - x[0])**2 + b * (x[1] - x[0]**2)**2

    def grad_f(x):
        a = 1
        b = 100
        df_dx0 = -2 * (a - x[0]) - 4 * b * x[0] * (x[1] - x[0]**2)
        df_dx1 = 2 * b * (x[1] - x[0]**2)
        return np.array([df_dx0, df_dx1])

    x0 = np.array([-1.2, 1.0])
    x = gradient_descent(f, grad_f, x0, learning_rate=0.001, tol=1e-6, max_iterations=100000)
    expected = np.array([1.0, 1.0])
    assert np.allclose(x, expected, atol=1e-3)


def test_gradient_descent_constant():
    f = lambda x: 5.0
    grad_f = lambda x: np.zeros_like(x)
    x0 = np.array([1.0, 2.0])
    x = gradient_descent(f, grad_f, x0, learning_rate=0.1, tol=1e-6, max_iterations=100)
    expected = x0
    assert np.allclose(x, expected, atol=1e-6)


def test_gradient_descent_non_convergent():
    f = lambda x: np.abs(x)
    grad_f = lambda x: np.sign(x)
    x0 = np.array([1.0])
    with pytest.raises(ValueError):
        gradient_descent(f, grad_f, x0, learning_rate=0.1, tol=1e-6, max_iterations=10)


def test_gradient_descent_exact_minimum():
    f = lambda x: (x - 3)**2
    grad_f = lambda x: 2 * (x - 3)
    x0 = np.array([0.0])
    x = gradient_descent(f, grad_f, x0, learning_rate=0.1, tol=1e-8)
    expected = np.array([3.0])
    assert np.allclose(x, expected, atol=1e-8)


def test_gradient_descent_close_to_minimum():
    f = lambda x: x**2 - 2 * x + 1
    grad_f = lambda x: 2 * x - 2
    x0 = np.array([0.5])
    x = gradient_descent(f, grad_f, x0, learning_rate=0.1, tol=1e-10)
    expected = np.array([1.0])
    assert np.allclose(x, expected, atol=1e-10)


def test_gradient_descent_negative_values():
    f = lambda x: x[0]**2 + x[1]**2
    grad_f = lambda x: 2 * x
    x0 = np.array([-3.0, 4.0])
    x = gradient_descent(f, grad_f, x0, learning_rate=0.05, tol=1e-6)
    expected = np.array([0.0, 0.0])
    assert np.allclose(x, expected, atol=1e-6)


def test_gradient_descent_high_dimensions():
    def f(x):
        return np.sum(x**2)

    def grad_f(x):
        return 2 * x

    x0 = np.random.rand(10)
    x = gradient_descent(f, grad_f, x0, learning_rate=0.1, tol=1e-6)
    expected = np.zeros(10)
    assert np.allclose(x, expected, atol=1e-6)


def test_gradient_descent_single_variable():
    f = lambda x: (x - 2)**2
    grad_f = lambda x: 2 * (x - 2)
    x0 = np.array([0.0])
    x = gradient_descent(f, grad_f, x0, learning_rate=0.1, tol=1e-8)
    expected = np.array([2.0])
    assert np.allclose(x, expected, atol=1e-8)


def test_gradient_descent_multiple_minima():
    f = lambda x: x**4 - 3*x**3 + 2
    grad_f = lambda x: 4*x**3 - 9*x**2
    x0 = np.array([2.0])
    x = gradient_descent(f, grad_f, x0, learning_rate=0.01, tol=1e-6)
    # Local minima at x = 0 and x = 27/12 = 2.25
    expected = np.array([2.25])
    assert np.allclose(x, expected, atol=1e-2)


def test_gradient_descent_function_with_noise():
    np.random.seed(0)
    f = lambda x: (x - 3)**2 + np.random.normal(0, 1e-6)
    grad_f = lambda x: 2 * (x - 3) + np.random.normal(0, 1e-6)
    x0 = np.array([0.0])
    x = gradient_descent(f, grad_f, x0, learning_rate=0.1, tol=1e-6)
    expected = np.array([3.0])
    assert np.isclose(x, expected, atol=1e-3)
