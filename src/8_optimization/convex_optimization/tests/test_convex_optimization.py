# test_convex_optimization.py
import pytest
import numpy as np
from ..implementation.convex_optimization import (
    quadratic_programming,
    is_convex_function,
)


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
    # Closest feasible point to the unconstrained minimizer (5, 5) is (1.5, 1.5)
    assert np.allclose(x, [1.5, 1.5], atol=1e-4)


def test_qp_inequality_and_equality_constraints():
    # min ||x - (3, 1)||^2 s.t. x1 + x2 = 1, x1 <= 0.2  ->  x = (0.2, 0.8)
    Q = 2.0 * np.eye(2)
    c = np.array([-6.0, -2.0])
    x = quadratic_programming(
        Q,
        c,
        A_ub=np.array([[1.0, 0.0]]),
        b_ub=np.array([0.2]),
        A_eq=np.array([[1.0, 1.0]]),
        b_eq=np.array([1.0]),
        max_iterations=20000,
    )
    assert np.allclose(x, [0.2, 0.8], atol=1e-4)


def test_qp_two_non_orthogonal_inequalities():
    # min ||x - (3, 1)||^2 s.t. x1 + 2 x2 <= 1, x1 - 0.5 x2 <= 0.5 -> x = (0.6, 0.2)
    Q = 2.0 * np.eye(2)
    c = np.array([-6.0, -2.0])
    A_ub = np.array([[1.0, 2.0], [1.0, -0.5]])
    b_ub = np.array([1.0, 0.5])
    x = quadratic_programming(Q, c, A_ub=A_ub, b_ub=b_ub, max_iterations=20000)
    assert np.allclose(x, [0.6, 0.2], atol=1e-4)


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
    assert np.allclose(x, [2.0, 2.0], atol=1e-4)


def test_qp_zero_hessian_raises():
    with pytest.raises(ValueError, match="linear program"):
        quadratic_programming(
            np.zeros((2, 2)),
            np.array([1.0, -1.0]),
            A_ub=np.array([[1.0, 1.0]]),
            b_ub=np.array([1.0]),
        )


def test_qp_step_is_inverse_spectral_norm():
    # Badly scaled Q: the 1/||Q|| step must still converge without blowing up
    Q = np.diag([100.0, 1.0])
    c = np.array([-100.0, -1.0])
    x = quadratic_programming(Q, c, max_iterations=10000, tol=1e-10)
    assert np.allclose(x, [1.0, 1.0], atol=1e-6)


def test_qp_semidefinite_q_with_constraints():
    # Q = diag(2, 0): flat in x2; x2 + x1 <= 1 and x2 >= 0 bound the problem
    Q = np.diag([2.0, 0.0])
    c = np.array([-2.0, 1.0])
    A_ub = np.array([[1.0, 1.0], [0.0, -1.0]])
    b_ub = np.array([1.0, 0.0])
    x = quadratic_programming(Q, c, A_ub=A_ub, b_ub=b_ub, max_iterations=20000)
    assert np.allclose(x, [1.0, 0.0], atol=1e-4)
