# test_convex_optimization.py
import pytest
import numpy as np
from ..implementation.convex_optimization import quadratic_programming, is_convex_function


def test_qp_unconstrained_quadratic():
    Q = np.array([[2.0, 0.0], [0.0, 2.0]])
    c = np.array([-4.0, -6.0])
    x = quadratic_programming(Q, c)
    expected = np.array([2.0, 3.0])
    assert np.allclose(x, expected, atol=1e-4)


def test_qp_identity_hessian():
    Q = np.eye(3)
    c = np.array([-1.0, -2.0, -3.0])
    x = quadratic_programming(Q, c)
    expected = np.array([1.0, 2.0, 3.0])
    assert np.allclose(x, expected, atol=1e-4)


def test_qp_with_inequality_constraints():
    Q = np.array([[2.0, 0.0], [0.0, 2.0]])
    c = np.array([-10.0, -10.0])
    A_ub = np.array([[1.0, 1.0]])
    b_ub = np.array([3.0])
    x0 = np.array([0.0, 0.0])
    x = quadratic_programming(Q, c, A_ub=A_ub, b_ub=b_ub, x0=x0, max_iterations=5000)
    assert x[0] + x[1] <= 3.0 + 1e-4


def test_qp_zero_cost():
    Q = np.array([[4.0, 0.0], [0.0, 4.0]])
    c = np.array([0.0, 0.0])
    x = quadratic_programming(Q, c)
    expected = np.array([0.0, 0.0])
    assert np.allclose(x, expected, atol=1e-4)


def test_qp_non_psd_raises():
    Q = np.array([[-2.0, 0.0], [0.0, 1.0]])
    c = np.array([1.0, 1.0])
    with pytest.raises(ValueError, match="positive semidefinite"):
        quadratic_programming(Q, c)


def test_qp_single_variable():
    Q = np.array([[6.0]])
    c = np.array([-12.0])
    x = quadratic_programming(Q, c)
    expected = np.array([2.0])
    assert np.allclose(x, expected, atol=1e-4)


def test_is_convex_quadratic():
    f = lambda x: x @ x
    points = np.random.default_rng(0).uniform(-5, 5, size=(50, 2))
    assert is_convex_function(f, points) is True


def test_is_convex_non_convex():
    f = lambda x: np.sin(x[0]) + np.sin(x[1])
    points = np.random.default_rng(0).uniform(-5, 5, size=(50, 2))
    assert is_convex_function(f, points) is False


def test_is_convex_linear():
    f = lambda x: 3 * x[0] + 2 * x[1] - 1
    points = np.random.default_rng(0).uniform(-5, 5, size=(50, 2))
    assert is_convex_function(f, points) is True


def test_qp_with_equality_constraints():
    Q = np.array([[2.0, 0.0], [0.0, 2.0]])
    c = np.array([0.0, 0.0])
    A_eq = np.array([[1.0, 1.0]])
    b_eq = np.array([4.0])
    x0 = np.array([2.0, 2.0])
    x = quadratic_programming(Q, c, A_eq=A_eq, b_eq=b_eq, x0=x0)
    assert np.isclose(x[0] + x[1], 4.0, atol=1e-4)
