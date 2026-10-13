# test_newton_raphson.py
import pytest
import numpy as np
from ..implementation.newton_raphson import newton_raphson, newton_raphson_system


# Univariate Tests


def test_newton_raphson_linear():
    f = lambda x: 2 * x - 4
    df = lambda x: 2
    x0 = 0.0
    root = newton_raphson(f, df, x0)
    expected = 2.0
    assert np.isclose(root, expected, atol=1e-8)


def test_newton_raphson_quadratic():
    f = lambda x: x**2 - 4
    df = lambda x: 2 * x
    x0 = 3.0
    root = newton_raphson(f, df, x0)
    expected = 2.0
    assert np.isclose(root, expected, atol=1e-8)


def test_newton_raphson_sin():
    f = np.sin
    df = np.cos
    x0 = 3.0  # Close to pi
    root = newton_raphson(f, df, x0)
    expected = np.pi
    assert np.isclose(root, expected, atol=1e-6)


def test_newton_raphson_zero_derivative():
    f = lambda x: x**3
    df = lambda x: 3 * x**2
    x0 = 0.0
    with pytest.raises(ValueError):
        newton_raphson(f, df, x0)


def test_newton_raphson_small_scale_derivative_is_not_zero():
    # f' = 1e-20 is tiny in absolute terms but the problem is well posed
    # (it is just a rescaled x - 2); an absolute threshold would reject it.
    f = lambda x: 1e-20 * (x - 2.0)
    df = lambda x: 1e-20
    root = newton_raphson(f, df, 10.0)
    assert np.isclose(root, 2.0, atol=1e-12, rtol=0)


def test_newton_raphson_overflowing_step_raises():
    # f = 1, f' = 1e-320 (subnormal): the Newton step overflows to inf.
    with pytest.raises(ValueError, match="Derivative is zero"):
        newton_raphson(lambda x: 1.0, lambda x: 1e-320, 0.0)


def test_newton_raphson_non_convergent():
    f = lambda x: x**3 - 2 * x + 2
    df = lambda x: 3 * x**2 - 2
    x0 = 0.0
    with pytest.raises(ValueError):
        newton_raphson(f, df, x0, max_iterations=10)


def test_newton_raphson_exact_root():
    f = lambda x: x - 5
    df = lambda x: 1
    x0 = 0.0
    root = newton_raphson(f, df, x0)
    expected = 5.0
    assert np.isclose(root, expected, atol=1e-8)


def test_newton_raphson_close_to_root():
    f = lambda x: x**2 - 2
    df = lambda x: 2 * x
    x0 = 1.4
    root = newton_raphson(f, df, x0)
    expected = np.sqrt(2)
    assert np.isclose(root, expected, atol=1e-8)


def test_newton_raphson_negative_root():
    f = lambda x: x + 3
    df = lambda x: 1
    x0 = 0.0
    root = newton_raphson(f, df, x0)
    expected = -3.0
    assert np.isclose(root, expected, atol=1e-8)


def test_newton_raphson_high_precision():
    f = lambda x: x**3 - 6 * x**2 + 11 * x - 6
    df = lambda x: 3 * x**2 - 12 * x + 11
    x0 = 3.5
    root = newton_raphson(f, df, x0, tol=1e-12)
    expected = 3.0
    assert np.isclose(root, expected, atol=1e-12)


def test_newton_raphson_initial_guess():
    f = lambda x: x**2 - 1
    df = lambda x: 2 * x
    x0 = 0.5
    root = newton_raphson(f, df, x0)
    expected = 1.0
    assert np.isclose(root, expected, atol=1e-8)


# Multivariate Tests


def test_newton_raphson_system_linear():
    def F(x):
        return np.array([3 * x[0] + 2 * x[1] - 5, x[0] - x[1] + 1])

    def J(x):
        return np.array([[3, 2], [1, -1]])

    x0 = np.array([0.0, 0.0])
    root = newton_raphson_system(F, J, x0)
    expected = np.linalg.solve(np.array([[3, 2], [1, -1]]), np.array([5, -1]))
    # For linear systems, Newton-Raphson should find the exact solution in one iteration
    assert np.allclose(root, expected, atol=1e-8)


def test_newton_raphson_system_nonlinear():
    def F(x):
        return np.array([x[0] ** 2 + x[1] ** 2 - 4, x[0] * x[1] - 1])

    def J(x):
        return np.array([[2 * x[0], 2 * x[1]], [x[1], x[0]]])

    x0 = np.array([2.0, 1.0])
    root = newton_raphson_system(F, J, x0)
    # x + y = sqrt(6), x - y = sqrt(2)
    expected = np.array([(np.sqrt(6) + np.sqrt(2)) / 2, (np.sqrt(6) - np.sqrt(2)) / 2])
    assert np.allclose(root, expected, atol=1e-6)


def test_newton_raphson_system_singular_jacobian():
    def F(x):
        return np.array([x[0] ** 2, x[0] * x[1]])

    def J(x):
        return np.array([[2 * x[0], 0], [x[1], x[0]]])

    x0 = np.array([0.0, 0.0])
    with pytest.raises(ValueError):
        newton_raphson_system(F, J, x0)


def test_newton_raphson_system_non_convergent():
    def F(x):
        return np.array([x[0] ** 2 + x[1] ** 2 - 4, x[0] * x[1] - 1])

    def J(x):
        return np.array([[2 * x[0], 2 * x[1]], [x[1], x[0]]])

    # The Jacobian is nonsingular along the way; two iterations are not enough
    x0 = np.array([2.0, 1.0])
    with pytest.raises(ValueError, match="did not converge"):
        newton_raphson_system(F, J, x0, max_iterations=2)


def test_newton_raphson_system_exact_solution():
    def F(x):
        return np.array([x[0] - 2, x[1] + 3])

    def J(x):
        return np.array([[1, 0], [0, 1]])

    x0 = np.array([0.0, 0.0])
    root = newton_raphson_system(F, J, x0)
    expected = np.array([2.0, -3.0])
    assert np.allclose(root, expected, atol=1e-8)


def test_newton_raphson_system_high_precision():
    def F(x):
        return np.array([x[0] ** 3 - 6 * x[0] ** 2 + 11 * x[0] - 6, x[1] - 1])

    def J(x):
        return np.array([[3 * x[0] ** 2 - 12 * x[0] + 11, 0], [0, 1]])

    x0 = np.array([3.5, 1.0])
    root = newton_raphson_system(F, J, x0, tol=1e-12)
    expected = np.array([3.0, 1.0])
    assert np.allclose(root, expected, atol=1e-12)


def test_newton_raphson_system_no_initial_guess():
    def F(x):
        return np.array([x[0] ** 2 - 2, x[1] ** 2 - 3])

    def J(x):
        return np.array([[2 * x[0], 0], [0, 2 * x[1]]])

    with pytest.raises(ValueError, match="Initial guess x0 must be provided"):
        newton_raphson_system(F, J)


def test_newton_raphson_system_large_system():
    def F(x):
        return np.array(
            [
                x[0] + x[1] + x[2] - 6,
                2 * x[0] + 5 * x[1] + x[3] - 4,
                2 * x[0] + 3 * x[2] - 2,
                4 * x[1] - x[3] - 1,
            ]
        )

    def J(x):
        return np.array([[1, 1, 1, 0], [2, 5, 0, 1], [2, 0, 3, 0], [0, 4, 0, -1]])

    x0 = np.array([1.0, 1.0, 1.0, 1.0])
    root = newton_raphson_system(F, J, x0)
    expected = np.linalg.solve(
        np.array([[1, 1, 1, 0], [2, 5, 0, 1], [2, 0, 3, 0], [0, 4, 0, -1]]),
        np.array([6, 4, 2, 1]),
    )
    assert np.allclose(root, expected, atol=1e-8)
