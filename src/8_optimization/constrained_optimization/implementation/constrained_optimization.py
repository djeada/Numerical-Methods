# constrained_optimization.py
import numpy as np
from typing import Callable, Optional, Tuple, List


def _pivot(tableau: np.ndarray, basis: List[int], row: int, col: int) -> None:
    """Gauss-Jordan pivot of the tableau on (row, col), updating the basis."""
    tableau[row] /= tableau[row, col]
    for i in range(tableau.shape[0]):
        if i != row:
            tableau[i] -= tableau[i, col] * tableau[row]
    basis[row] = col


def _simplex_iterations(
    tableau: np.ndarray,
    basis: List[int],
    allowed_cols: int,
    tol: float,
    max_iterations: int,
) -> bool:
    """
    Run primal simplex pivots on a tableau whose last row holds the reduced
    costs (already priced out against the basis) and whose last column holds
    the right-hand side. Only the first ``allowed_cols`` columns may enter.

    Dantzig's rule is used, falling back to Bland's rule after a run of
    degenerate pivots to prevent cycling.

    Returns:
        True if an optimal basis was reached, False if the problem is
        unbounded in an improving direction.

    Raises:
        ValueError: If max_iterations pivots are not enough.
    """
    m = tableau.shape[0] - 1
    degenerate_run = 0

    for _ in range(max_iterations):
        reduced_costs = tableau[-1, :allowed_cols]
        if degenerate_run >= 10:
            candidates = np.flatnonzero(reduced_costs < -tol)
            pivot_col = int(candidates[0]) if candidates.size else -1
        else:
            pivot_col = int(np.argmin(reduced_costs)) if allowed_cols else -1
            if pivot_col >= 0 and reduced_costs[pivot_col] >= -tol:
                pivot_col = -1
        if pivot_col < 0:
            return True

        column = tableau[:m, pivot_col]
        rhs = tableau[:m, -1]
        rows = np.flatnonzero(column > tol)
        if rows.size == 0:
            return False

        ratios = rhs[rows] / column[rows]
        best = ratios.min()
        ties = rows[ratios <= best + tol]
        pivot_row = int(min(ties, key=lambda r: basis[r]))

        degenerate_run = degenerate_run + 1 if best <= tol else 0
        _pivot(tableau, basis, pivot_row, pivot_col)

    raise ValueError(
        "Simplex method did not converge within the maximum number of iterations."
    )


def linear_programming(
    c: np.ndarray,
    A_ub: Optional[np.ndarray] = None,
    b_ub: Optional[np.ndarray] = None,
    tol: float = 1e-10,
    max_iterations: int = 1000,
    A_eq: Optional[np.ndarray] = None,
    b_eq: Optional[np.ndarray] = None,
) -> Tuple[np.ndarray, float]:
    """
    Solve a linear programming problem using the two-phase simplex method.

    Minimizes:
        c^T x

    Subject to:
        A_ub @ x <= b_ub
        A_eq @ x == b_eq
        x >= 0

    Constraints of the form a^T x >= b are supplied as -a^T x <= -b. Rows
    with a negative right-hand side are handled by Phase I, which minimizes
    the sum of artificial variables to find a basic feasible solution (or
    proves that none exists).

    Args:
        c: Cost vector (n,).
        A_ub: Inequality constraint matrix (m x n), optional.
        b_ub: Inequality constraint vector (m,), optional. May be negative.
        tol: Tolerance for optimality and pivot checks.
        max_iterations: Maximum number of simplex pivots per phase.
        A_eq: Equality constraint matrix (p x n), optional.
        b_eq: Equality constraint vector (p,), optional.

    Returns:
        Tuple of (optimal_x, optimal_value).

    Raises:
        ValueError: If the constraint data have inconsistent shapes.
        ValueError: If the problem is infeasible.
        ValueError: If the problem is unbounded.
        ValueError: If the method does not converge.
    """
    c = np.asarray(c, dtype=float)
    n = len(c)

    if (A_ub is None) != (b_ub is None) or (A_eq is None) != (b_eq is None):
        raise ValueError("A_ub/b_ub and A_eq/b_eq must be given in pairs.")
    A_ub = (
        np.zeros((0, n))
        if A_ub is None
        else np.atleast_2d(np.asarray(A_ub, dtype=float))
    )
    b_ub = np.zeros(0) if b_ub is None else np.asarray(b_ub, dtype=float)
    A_eq = (
        np.zeros((0, n))
        if A_eq is None
        else np.atleast_2d(np.asarray(A_eq, dtype=float))
    )
    b_eq = np.zeros(0) if b_eq is None else np.asarray(b_eq, dtype=float)
    if A_ub.shape != (len(b_ub), n) or A_eq.shape != (len(b_eq), n):
        raise ValueError("Constraint matrices and vectors have inconsistent shapes.")

    m_ub, m_eq = len(b_ub), len(b_eq)
    m = m_ub + m_eq

    # Standard form  [A_ub I; A_eq 0] [x; s] = [b_ub; b_eq],  x, s >= 0
    A = np.zeros((m, n + m_ub))
    A[:m_ub, :n] = A_ub
    A[:m_ub, n:] = np.eye(m_ub)
    A[m_ub:, :n] = A_eq
    b = np.concatenate([b_ub, b_eq])

    # Make every right-hand side non-negative
    negative = b < 0
    A[negative] *= -1.0
    b = np.where(negative, -b, b)

    # Rows whose slack column is +1 can start with that slack in the basis;
    # all other rows (flipped inequalities, equalities) need an artificial.
    n_struct = n + m_ub
    basis: List[int] = [-1] * m
    for i in range(m_ub):
        if not negative[i]:
            basis[i] = n + i
    artificial_rows = [i for i in range(m) if basis[i] < 0]
    n_art = len(artificial_rows)

    # Tableau columns: structural (x, s), artificials, rhs. Last row: costs.
    tableau = np.zeros((m + 1, n_struct + n_art + 1))
    tableau[:m, :n_struct] = A
    tableau[:m, -1] = b
    for k, i in enumerate(artificial_rows):
        tableau[i, n_struct + k] = 1.0
        basis[i] = n_struct + k

    def price_out(cost: np.ndarray) -> None:
        tableau[-1, :] = 0.0
        tableau[-1, : len(cost)] = cost
        for i, b_idx in enumerate(basis):
            if tableau[-1, b_idx] != 0.0:
                tableau[-1] -= tableau[-1, b_idx] * tableau[i]

    if n_art:
        # Phase I: minimize the sum of artificial variables
        cost1 = np.zeros(n_struct + n_art)
        cost1[n_struct:] = 1.0
        price_out(cost1)
        _simplex_iterations(tableau, basis, n_struct + n_art, tol, max_iterations)

        feas_tol = 1e-8 * (1.0 + np.max(np.abs(b)))
        if -tableau[-1, -1] > feas_tol:
            raise ValueError("The linear program is infeasible.")

        # Drive remaining (zero-level) artificials out of the basis; a row
        # with no usable structural column is redundant and is dropped.
        keep_rows = []
        for i in range(m):
            if basis[i] >= n_struct:
                usable = np.flatnonzero(np.abs(tableau[i, :n_struct]) > 1e-9)
                if usable.size == 0:
                    continue
                _pivot(tableau, basis, i, int(usable[0]))
            keep_rows.append(i)
        tableau = np.vstack([tableau[keep_rows], tableau[-1:]])
        basis = [basis[i] for i in keep_rows]
        tableau = np.delete(tableau, np.s_[n_struct : n_struct + n_art], axis=1)

    # Phase II: original costs
    cost2 = np.zeros(n_struct)
    cost2[:n] = c
    price_out(cost2)
    if not _simplex_iterations(tableau, basis, n_struct, tol, max_iterations):
        raise ValueError("The linear program is unbounded.")

    x = np.zeros(n_struct)
    for i, b_idx in enumerate(basis):
        x[b_idx] = tableau[i, -1]
    x = x[:n]
    return x, float(c @ x)


def _lagrangian_hessian_fd(
    grad_f: Callable[[np.ndarray], np.ndarray],
    grad_h: Callable[[np.ndarray], np.ndarray],
    x: np.ndarray,
    lam: np.ndarray,
) -> np.ndarray:
    """Central-difference Hessian of L(x, lam) = f + lam^T h at fixed lam."""
    n = len(x)
    H = np.zeros((n, n))
    for j in range(n):
        step = 1e-6 * max(1.0, abs(x[j]))
        e = np.zeros(n)
        e[j] = step
        gp = grad_f(x + e) + grad_h(x + e).T @ lam
        gm = grad_f(x - e) + grad_h(x - e).T @ lam
        H[:, j] = (gp - gm) / (2.0 * step)
    return 0.5 * (H + H.T)


def lagrange_multiplier_minimize(
    f: Callable[[np.ndarray], float],
    grad_f: Callable[[np.ndarray], np.ndarray],
    h: Callable[[np.ndarray], np.ndarray],
    grad_h: Callable[[np.ndarray], np.ndarray],
    x0: np.ndarray,
    tol: float = 1e-8,
    max_iterations: int = 1000,
    hess_lagrangian: Optional[Callable[[np.ndarray, np.ndarray], np.ndarray]] = None,
) -> Tuple[np.ndarray, np.ndarray]:
    """
    Solve an equality-constrained optimization problem using
    the method of Lagrange multipliers with Newton's method
    applied to the KKT system (a sequential-quadratic-programming step).

    The Newton step uses the Hessian of the Lagrangian
    L(x, lam) = f(x) + lam^T h(x), so convergence is quadratic near a
    regular solution. A backtracking line search on the KKT residual norm
    globalizes the iteration. Newton's method finds KKT points; it does not
    distinguish minima from other stationary points.
    Multipliers are initialized by a least-squares fit to the stationarity
    condition at x0.

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
        hess_lagrangian: Optional function (x, lam) -> (n x n) Hessian of
            the Lagrangian, i.e. hess f(x) + sum_i lam_i hess h_i(x). If
            omitted, it is approximated by central differences of the
            Lagrangian gradient grad_f + J_h^T lam at fixed lam.

    Returns:
        Tuple of (optimal_x, lagrange_multipliers).

    Raises:
        ValueError: If the method does not converge.
    """
    x = x0.astype(float)
    n = len(x)
    p = len(h(x))
    # Least-squares multiplier estimate: argmin ||grad_f + J_h^T lam||
    lam = np.linalg.lstsq(grad_h(x).reshape(p, n).T, -grad_f(x), rcond=None)[0]

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
        if hess_lagrangian is not None:
            H = np.asarray(hess_lagrangian(x, lam), dtype=float)
        else:
            H = _lagrangian_hessian_fd(grad_f, grad_h, x, lam)
        KKT = np.block([[H, Jh.T], [Jh, np.zeros((p, p))]])
        rhs = -residual

        try:
            delta = np.linalg.solve(KKT, rhs)
        except np.linalg.LinAlgError:
            raise ValueError(f"KKT system is singular at iteration {iteration}.")

        dx = delta[:n]
        dlam = delta[n:]

        # Line search with step size reduction
        alpha = 1.0
        for _ in range(50):
            x_new = x + alpha * dx
            lam_new = lam + alpha * dlam
            new_residual = np.concatenate(
                [grad_f(x_new) + grad_h(x_new).T @ lam_new, h(x_new)]
            )
            if np.linalg.norm(new_residual) < np.linalg.norm(residual):
                break
            alpha *= 0.5

        x = x + alpha * dx
        lam = lam + alpha * dlam

    raise ValueError(
        "Lagrange multiplier method did not converge within the maximum number of iterations."
    )
