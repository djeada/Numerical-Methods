# test_constrained_optimization.py
import pytest
import numpy as np
from ..implementation.constrained_optimization import (
    linear_programming,
    lagrange_multiplier_minimize,
)


# Linear Programming Tests


def test_lp_simple():
    # min -5x1 - 4x2 s.t. 2x1+x2<=8, x1+2x2<=7, x>=0
    c = np.array([-5.0, -4.0])
    A_ub = np.array([[2.0, 1.0], [1.0, 2.0]])
    b_ub = np.array([8.0, 7.0])
    x, val = linear_programming(c, A_ub, b_ub)
    assert np.isclose(x[0], 3.0, atol=1e-6)
    assert np.isclose(x[1], 2.0, atol=1e-6)
    assert np.isclose(val, -23.0, atol=1e-6)


def test_lp_single_variable():
    # min -3x s.t. x <= 5, x >= 0
    c = np.array([-3.0])
    A_ub = np.array([[1.0]])
    b_ub = np.array([5.0])
    x, val = linear_programming(c, A_ub, b_ub)
    assert np.isclose(x[0], 5.0, atol=1e-6)
    assert np.isclose(val, -15.0, atol=1e-6)


def test_lp_optimal_at_origin():
    # min x1 + x2 s.t. x1+x2<=10, x>=0
    c = np.array([1.0, 1.0])
    A_ub = np.array([[1.0, 1.0]])
    b_ub = np.array([10.0])
    x, val = linear_programming(c, A_ub, b_ub)
    assert np.isclose(val, 0.0, atol=1e-6)


def test_lp_three_variables():
    # min -x1 - 2x2 - x3 s.t. x1+x2+x3<=10, x1<=4, x2<=4, x>=0
    c = np.array([-1.0, -2.0, -1.0])
    A_ub = np.array(
        [
            [1.0, 1.0, 1.0],
            [1.0, 0.0, 0.0],
            [0.0, 1.0, 0.0],
        ]
    )
    b_ub = np.array([10.0, 4.0, 4.0])
    x, val = linear_programming(c, A_ub, b_ub)
    # Optimal: x2 as large as possible (4), then x1 or x3 using remaining
    assert x[1] >= 3.9


def test_lp_feasibility():
    c = np.array([-1.0, -1.0])
    A_ub = np.array([[1.0, 0.0], [0.0, 1.0], [1.0, 1.0]])
    b_ub = np.array([3.0, 3.0, 5.0])
    x, val = linear_programming(c, A_ub, b_ub)
    # Check constraints are satisfied
    assert np.all(A_ub @ x <= b_ub + 1e-6)
    assert np.all(x >= -1e-6)


def test_lp_negative_rhs_phase_one():
    # min x s.t. -x <= -2 (i.e. x >= 2): origin is infeasible, needs Phase I
    x, val = linear_programming(np.array([1.0]), np.array([[-1.0]]), np.array([-2.0]))
    assert np.isclose(x[0], 2.0)
    assert np.isclose(val, 2.0)


def test_lp_infeasible_detected():
    # x >= 3 and x <= 1
    A_ub = np.array([[-1.0], [1.0]])
    b_ub = np.array([-3.0, 1.0])
    with pytest.raises(ValueError, match="infeasible"):
        linear_programming(np.array([1.0]), A_ub, b_ub)


def test_lp_unbounded_detected():
    # min -x1 s.t. x1 - x2 <= 1
    with pytest.raises(ValueError, match="unbounded"):
        linear_programming(
            np.array([-1.0, 0.0]), np.array([[1.0, -1.0]]), np.array([1.0])
        )


def test_lp_unbounded_after_phase_one():
    # x1 >= 2 (infeasible origin) and min -x1 with no upper bound
    with pytest.raises(ValueError, match="unbounded"):
        linear_programming(np.array([-1.0]), np.array([[-1.0]]), np.array([-2.0]))


def test_lp_equality_constraints():
    # min x1 + 2 x2 s.t. x1 + x2 = 4, x1 <= 3
    x, val = linear_programming(
        np.array([1.0, 2.0]),
        np.array([[1.0, 0.0]]),
        np.array([3.0]),
        A_eq=np.array([[1.0, 1.0]]),
        b_eq=np.array([4.0]),
    )
    assert np.allclose(x, [3.0, 1.0])
    assert np.isclose(val, 5.0)


def test_lp_redundant_equalities():
    # Two copies of the same equality: Phase I leaves a redundant row
    x, val = linear_programming(
        np.array([1.0, 3.0]),
        A_eq=np.array([[1.0, 1.0], [2.0, 2.0]]),
        b_eq=np.array([2.0, 4.0]),
    )
    assert np.allclose(x, [2.0, 0.0])
    assert np.isclose(val, 2.0)


def test_lp_matches_scipy_linprog_random():
    linprog = pytest.importorskip("scipy.optimize").linprog
    rng = np.random.default_rng(7)
    checked = 0
    for _ in range(60):
        n, m = rng.integers(2, 5), rng.integers(2, 6)
        c = rng.normal(size=n)
        A = rng.normal(size=(m, n))
        b = rng.normal(size=m) * 2.0  # mixed signs: Phase I is exercised
        ref = linprog(c, A_ub=A, b_ub=b, bounds=[(0, None)] * n, method="highs")
        try:
            x, val = linear_programming(c, A, b)
            status = 0
        except ValueError as e:
            status = 2 if "infeasible" in str(e) else 3
        assert status == ref.status
        if status == 0:
            assert np.isclose(val, ref.fun, atol=1e-6)
            assert np.all(A @ x <= b + 1e-6) and np.all(x >= -1e-8)
        checked += 1
    assert checked == 60


# Lagrange Multiplier Tests


def test_lagrange_min_distance_to_origin():
    # min x^2 + y^2 s.t. x + y = 4
    f = lambda x: x[0] ** 2 + x[1] ** 2
    grad_f = lambda x: np.array([2 * x[0], 2 * x[1]])
    h = lambda x: np.array([x[0] + x[1] - 4])
    grad_h = lambda x: np.array([[1.0, 1.0]])
    x0 = np.array([1.0, 3.0])
    x, lam = lagrange_multiplier_minimize(f, grad_f, h, grad_h, x0)
    assert np.allclose(x, np.array([2.0, 2.0]), atol=1e-4)
    assert np.isclose(f(x), 8.0, atol=1e-4)


def test_lagrange_constrained_quadratic():
    # min (x-1)^2 + (y-1)^2 s.t. x + y = 0
    f = lambda x: (x[0] - 1) ** 2 + (x[1] - 1) ** 2
    grad_f = lambda x: np.array([2 * (x[0] - 1), 2 * (x[1] - 1)])
    h = lambda x: np.array([x[0] + x[1]])
    grad_h = lambda x: np.array([[1.0, 1.0]])
    x0 = np.array([1.0, -1.0])
    x, lam = lagrange_multiplier_minimize(f, grad_f, h, grad_h, x0)
    # Lagrangian: 2(x-1)+lam=0, 2(y-1)+lam=0 => x=y, with x+y=0 => x=y=0
    assert np.allclose(x, np.array([0.0, 0.0]), atol=1e-4)


def test_lagrange_simple_equality():
    # min x^2 s.t. x = 3 (trivial)
    f = lambda x: x[0] ** 2
    grad_f = lambda x: np.array([2 * x[0]])
    h = lambda x: np.array([x[0] - 3.0])
    grad_h = lambda x: np.array([[1.0]])
    x0 = np.array([1.0])
    x, lam = lagrange_multiplier_minimize(f, grad_f, h, grad_h, x0)
    assert np.isclose(x[0], 3.0, atol=1e-4)


def test_lagrange_two_constraints():
    # min x^2 + y^2 + z^2 s.t. x+y+z=3, x-y=0
    f = lambda x: np.dot(x, x)
    grad_f = lambda x: 2 * x
    h = lambda x: np.array([x[0] + x[1] + x[2] - 3, x[0] - x[1]])
    grad_h = lambda x: np.array([[1.0, 1.0, 1.0], [1.0, -1.0, 0.0]])
    x0 = np.array([1.0, 1.0, 1.0])
    x, lam = lagrange_multiplier_minimize(f, grad_f, h, grad_h, x0)
    # With x=y and x+y+z=3 => 2x+z=3, minimize x^2+x^2+z^2 = 2x^2+(3-2x)^2
    # derivative: 4x + 2(3-2x)(-2) = 4x - 12 + 8x = 12x - 12 = 0 => x=1
    assert np.isclose(x[0], 1.0, atol=1e-3)
    assert np.isclose(x[1], 1.0, atol=1e-3)
    assert np.isclose(x[2], 1.0, atol=1e-3)


def test_lagrange_multiplier_value():
    # min x^2 + y^2 s.t. x + y = 4
    # KKT: 2x + lam = 0, 2y + lam = 0 => x=y=2, lam = -4
    f = lambda x: x[0] ** 2 + x[1] ** 2
    grad_f = lambda x: np.array([2 * x[0], 2 * x[1]])
    h = lambda x: np.array([x[0] + x[1] - 4])
    grad_h = lambda x: np.array([[1.0, 1.0]])
    x0 = np.array([1.0, 3.0])
    x, lam = lagrange_multiplier_minimize(f, grad_f, h, grad_h, x0)
    assert np.isclose(lam[0], -4.0, atol=1e-3)


def test_lagrange_nonlinear_constraint():
    # min x + y s.t. x^2 + y^2 = 2  ->  (-1, -1), lam = 1/2
    f = lambda x: x[0] + x[1]
    grad_f = lambda x: np.array([1.0, 1.0])
    h = lambda x: np.array([x[0] ** 2 + x[1] ** 2 - 2.0])
    grad_h = lambda x: np.array([[2 * x[0], 2 * x[1]]])
    x, lam = lagrange_multiplier_minimize(f, grad_f, h, grad_h, np.array([-2.0, -0.5]))
    assert np.allclose(x, [-1.0, -1.0], atol=1e-6)
    assert np.isclose(lam[0], 0.5, atol=1e-6)


def test_lagrange_analytic_hessian_matches_finite_difference():
    f = lambda x: x[0] + x[1]
    grad_f = lambda x: np.array([1.0, 1.0])
    h = lambda x: np.array([x[0] ** 2 + x[1] ** 2 - 2.0])
    grad_h = lambda x: np.array([[2 * x[0], 2 * x[1]]])
    hess_L = lambda x, lam: 2.0 * lam[0] * np.eye(2)
    x0 = np.array([-2.0, -0.5])
    x1, l1 = lagrange_multiplier_minimize(
        f, grad_f, h, grad_h, x0, hess_lagrangian=hess_L
    )
    x2, l2 = lagrange_multiplier_minimize(f, grad_f, h, grad_h, x0)
    assert np.allclose(x1, x2, atol=1e-6)
    assert np.allclose(l1, l2, atol=1e-6)


def test_lagrange_newton_converges_quadratically_fast():
    # Ill-conditioned quadratic objective with a linear constraint: a Newton
    # step solves it exactly, whereas an identity Hessian would need many.
    A = np.diag([1.0, 100.0, 10000.0])
    grad_f = lambda x: calls.append(1) or 2 * A @ x
    f = lambda x: x @ A @ x
    h = lambda x: np.array([x.sum() - 1.0])
    grad_h = lambda x: np.ones((1, 3))
    calls = []
    x, lam = lagrange_multiplier_minimize(
        f, grad_f, h, grad_h, np.array([1.0, 0.0, 0.0])
    )
    expected = (1 / np.diag(A)) / np.sum(1 / np.diag(A))
    assert np.allclose(x, expected, atol=1e-8)
    assert len(calls) < 20


def test_lagrange_circle_converges_in_few_iterations():
    # Newton should need only a handful of iterations on a smooth problem
    f = lambda x: (x[0] - 2) ** 2 + (x[1] - 1) ** 2
    calls = []

    def grad_f(x):
        calls.append(1)
        return np.array([2 * (x[0] - 2), 2 * (x[1] - 1)])

    h = lambda x: np.array([x[0] ** 2 + x[1] ** 2 - 1.0])
    grad_h = lambda x: np.array([[2 * x[0], 2 * x[1]]])
    x, lam = lagrange_multiplier_minimize(
        f, grad_f, h, grad_h, np.array([1.0, 0.5]), tol=1e-10
    )
    assert np.allclose(x, np.array([2.0, 1.0]) / np.sqrt(5.0), atol=1e-8)
    assert len(calls) < 40
