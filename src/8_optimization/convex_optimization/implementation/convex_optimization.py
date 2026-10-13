# convex_optimization.py
import numpy as np
from typing import Callable, Optional


def _project_feasible(
    y: np.ndarray,
    A_ub: Optional[np.ndarray],
    b_ub: Optional[np.ndarray],
    A_eq: Optional[np.ndarray],
    b_eq: Optional[np.ndarray],
    tol: float,
    max_sweeps: int = 5000,
) -> np.ndarray:
    """
    Euclidean projection of y onto {A_ub x <= b_ub, A_eq x = b_eq} using
    Dykstra's algorithm.

    Plain cyclic projections onto the individual sets only find *a* point
    of the intersection, not the nearest one, so the correction terms of
    Dykstra's method are required for an exact projection.
    """
    sets = []
    if A_ub is not None and b_ub is not None:
        for a_i, b_i in zip(A_ub, b_ub):
            sets.append(("ub", a_i, b_i))
    if A_eq is not None and b_eq is not None:
        sets.append(("eq", A_eq, b_eq))

    x = y.copy()
    increments = [np.zeros_like(y) for _ in sets]

    for _ in range(max_sweeps):
        x_prev = x.copy()
        for k, (kind, a, b) in enumerate(sets):
            z = x + increments[k]
            if kind == "ub":
                violation = a @ z - b
                x = z - (violation / (a @ a)) * a if violation > 0 else z
            else:
                x = z - a.T @ np.linalg.solve(a @ a.T, a @ z - b)
            increments[k] = z - x

        feasible = True
        if A_ub is not None and b_ub is not None:
            feasible = bool(np.all(A_ub @ x - b_ub <= tol))
        if feasible and A_eq is not None and b_eq is not None:
            feasible = bool(np.linalg.norm(A_eq @ x - b_eq) <= tol)
        if feasible and np.linalg.norm(x - x_prev) < tol:
            break

    return x


def quadratic_programming(
    Q: np.ndarray,
    c: np.ndarray,
    A_ub: Optional[np.ndarray] = None,
    b_ub: Optional[np.ndarray] = None,
    A_eq: Optional[np.ndarray] = None,
    b_eq: Optional[np.ndarray] = None,
    x0: Optional[np.ndarray] = None,
    tol: float = 1e-8,
    max_iterations: int = 1000,
) -> np.ndarray:
    """
    Solve a convex quadratic programming problem using projected gradient descent.

    Each gradient step is followed by an exact Euclidean projection onto the
    feasible polyhedron (computed with Dykstra's algorithm).

    Minimizes:
        0.5 * x^T Q x + c^T x

    Subject to:
        A_ub @ x <= b_ub  (inequality constraints)
        A_eq @ x == b_eq  (equality constraints)

    Args:
        Q: Symmetric positive semidefinite matrix (n x n).
        c: Linear cost vector (n,).
        A_ub: Inequality constraint matrix (m x n), optional.
        b_ub: Inequality constraint vector (m,), optional.
        A_eq: Equality constraint matrix (p x n), optional.
        b_eq: Equality constraint vector (p,), optional.
        x0: Initial feasible point (n,), optional. Defaults to zeros.
        tol: Convergence tolerance.
        max_iterations: Maximum number of iterations.

    Returns:
        Optimal solution x*.

    Raises:
        ValueError: If Q is not positive semidefinite.
        ValueError: If Q is (numerically) zero, i.e. the problem is a linear
            program; use a linear programming solver instead.
        ValueError: If the method does not converge.
    """
    n = Q.shape[0]
    eigenvalues = np.linalg.eigvalsh(Q)
    if np.any(eigenvalues < -tol):
        raise ValueError("Q must be positive semidefinite for convex QP.")

    if x0 is None:
        x0 = np.zeros(n)
    x = x0.astype(float)

    # L = ||Q||_2 = lambda_max(Q) is the Lipschitz constant of the gradient,
    # so the step 1/L guarantees monotone decrease of projected gradient.
    L = float(np.max(eigenvalues))
    if L <= tol:
        raise ValueError(
            "Q is numerically zero, so this is a linear program with no "
            "curvature to set a step size; use a linear programming solver."
        )
    alpha = 1.0 / L

    for iteration in range(max_iterations):
        grad = Q @ x + c
        x_new = x - alpha * grad

        if (A_ub is not None and b_ub is not None) or (
            A_eq is not None and b_eq is not None
        ):
            x_new = _project_feasible(x_new, A_ub, b_ub, A_eq, b_eq, tol)

        if np.linalg.norm(x_new - x) < tol:
            return x_new
        x = x_new

    raise ValueError(
        "Quadratic programming did not converge within the maximum number of iterations."
    )


def is_convex_function(
    f: Callable[[np.ndarray], float],
    domain_points: np.ndarray,
    num_tests: int = 100,
    tol: float = 1e-6,
) -> bool:
    """
    Numerically test whether a function is convex over a set of sample points.

    For convexity, f(theta*x + (1-theta)*y) <= theta*f(x) + (1-theta)*f(y)
    for all x, y in the domain and theta in [0,1].

    Args:
        f: Function to test.
        domain_points: Array of points in the domain (k x n).
        num_tests: Number of random convexity tests to perform.
        tol: Tolerance for the convexity inequality.

    Returns:
        True if all tests pass, False otherwise.
    """
    rng = np.random.default_rng(42)
    k = domain_points.shape[0]
    for _ in range(num_tests):
        i, j = rng.choice(k, size=2, replace=False)
        x, y = domain_points[i], domain_points[j]
        theta = rng.uniform(0, 1)
        lhs = f(theta * x + (1 - theta) * y)
        rhs = theta * f(x) + (1 - theta) * f(y)
        if lhs > rhs + tol:
            return False
    return True
