# constrained_optimization.py
import numpy as np
from typing import Callable, Optional, Tuple, List


def linear_programming(
    c: np.ndarray,
    A_ub: np.ndarray,
    b_ub: np.ndarray,
    tol: float = 1e-10,
    max_iterations: int = 1000,
) -> Tuple[np.ndarray, float]:
    """
    Solve a linear programming problem using the simplex method.

    Minimizes:
        c^T x

    Subject to:
        A_ub @ x <= b_ub
        x >= 0

    Args:
        c: Cost vector (n,).
        A_ub: Inequality constraint matrix (m x n).
        b_ub: Inequality constraint vector (m,). Must be non-negative.
        tol: Tolerance for optimality and feasibility checks.
        max_iterations: Maximum number of simplex pivots.

    Returns:
        Tuple of (optimal_x, optimal_value).

    Raises:
        ValueError: If the problem is infeasible or unbounded.
        ValueError: If the method does not converge.
    """
    m, n = A_ub.shape

    # Convert to standard form by adding slack variables
    # min c^T x  s.t. A_ub x + s = b_ub, x >= 0, s >= 0
    tableau = np.zeros((m + 1, n + m + 1))
    tableau[:m, :n] = A_ub
    tableau[:m, n:n + m] = np.eye(m)
    tableau[:m, -1] = b_ub
    tableau[-1, :n] = c

    basis = list(range(n, n + m))

    for iteration in range(max_iterations):
        # Check optimality: all reduced costs non-negative
        reduced_costs = tableau[-1, :-1]
        if np.all(reduced_costs >= -tol):
            x = np.zeros(n + m)
            for i, b_idx in enumerate(basis):
                x[b_idx] = tableau[i, -1]
            return x[:n], -tableau[-1, -1]

        # Pivot column: most negative reduced cost
        pivot_col = np.argmin(reduced_costs)

        # Ratio test
        column = tableau[:m, pivot_col]
        rhs = tableau[:m, -1]

        ratios = np.full(m, np.inf)
        for i in range(m):
            if column[i] > tol:
                ratios[i] = rhs[i] / column[i]

        if np.all(ratios == np.inf):
            raise ValueError("The linear program is unbounded.")

        pivot_row = np.argmin(ratios)

        # Pivot operation
        pivot_element = tableau[pivot_row, pivot_col]
        tableau[pivot_row] /= pivot_element
        for i in range(m + 1):
            if i != pivot_row:
                tableau[i] -= tableau[i, pivot_col] * tableau[pivot_row]

        basis[pivot_row] = pivot_col

    raise ValueError(
        "Simplex method did not converge within the maximum number of iterations."
    )


def lagrange_multiplier_minimize(
    f: Callable[[np.ndarray], float],
    grad_f: Callable[[np.ndarray], np.ndarray],
    h: Callable[[np.ndarray], np.ndarray],
    grad_h: Callable[[np.ndarray], np.ndarray],
    x0: np.ndarray,
    tol: float = 1e-8,
    max_iterations: int = 1000,
) -> Tuple[np.ndarray, np.ndarray]:
    """
    Solve an equality-constrained optimization problem using
    the method of Lagrange multipliers with Newton's method
    applied to the KKT system.

    Minimizes:
        f(x)

    Subject to:
        h(x) = 0

    Args:
        f: Objective function.
        grad_f: Gradient of the objective (returns n-vector).
        h: Equality constraint function (returns p-vector).
        grad_h: Jacobian of h (returns p x n matrix).
        x0: Initial guess for x (n-vector).
        tol: Convergence tolerance.
        max_iterations: Maximum number of iterations.

    Returns:
        Tuple of (optimal_x, lagrange_multipliers).

    Raises:
        ValueError: If the method does not converge.
    """
    x = x0.astype(float)
    n = len(x)
    p = len(h(x))
    lam = np.zeros(p)

    for iteration in range(max_iterations):
        gf = grad_f(x)
        hx = h(x)
        Jh = grad_h(x)

        # KKT residual: [grad_f + J_h^T lambda; h(x)]
        residual = np.concatenate([gf + Jh.T @ lam, hx])
        if np.linalg.norm(residual) < tol:
            return x, lam

        # Build KKT system
        # [H   J_h^T] [dx  ]   [-grad_f - J_h^T lam]
        # [J_h   0  ] [dlam] = [-h(x)              ]
        # Use identity as Hessian approximation for robustness. This trades
        # convergence speed for stability; supply the actual Hessian via a
        # wrapper if faster convergence is needed.
        H = np.eye(n)
        KKT = np.block([
            [H, Jh.T],
            [Jh, np.zeros((p, p))]
        ])
        rhs = -residual

        try:
            delta = np.linalg.solve(KKT, rhs)
        except np.linalg.LinAlgError:
            raise ValueError(
                f"KKT system is singular at iteration {iteration}."
            )

        dx = delta[:n]
        dlam = delta[n:]

        # Line search with step size reduction
        alpha = 1.0
        for _ in range(50):
            x_new = x + alpha * dx
            lam_new = lam + alpha * dlam
            new_residual = np.concatenate([
                grad_f(x_new) + grad_h(x_new).T @ lam_new,
                h(x_new)
            ])
            if np.linalg.norm(new_residual) < np.linalg.norm(residual):
                break
            alpha *= 0.5

        x = x + alpha * dx
        lam = lam + alpha * dlam

    raise ValueError(
        "Lagrange multiplier method did not converge within the maximum number of iterations."
    )
