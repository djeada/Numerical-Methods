# convex_optimization.py
import numpy as np
from typing import Callable, Optional


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
        ValueError: If the method does not converge.
    """
    n = Q.shape[0]
    eigenvalues = np.linalg.eigvalsh(Q)
    if np.any(eigenvalues < -tol):
        raise ValueError("Q must be positive semidefinite for convex QP.")

    if x0 is None:
        x0 = np.zeros(n)
    x = x0.astype(float)

    L = np.max(eigenvalues) + 1e-6
    alpha = 1.0 / L

    for iteration in range(max_iterations):
        grad = Q @ x + c
        x_new = x - alpha * grad

        if A_ub is not None and b_ub is not None:
            for _ in range(100):
                violations = A_ub @ x_new - b_ub
                if np.all(violations <= tol):
                    break
                idx = np.argmax(violations)
                a_i = A_ub[idx]
                x_new = x_new - ((a_i @ x_new - b_ub[idx]) / (a_i @ a_i)) * a_i

        if A_eq is not None and b_eq is not None:
            residual = A_eq @ x_new - b_eq
            if np.linalg.norm(residual) > tol:
                x_new = x_new - A_eq.T @ np.linalg.solve(
                    A_eq @ A_eq.T, residual
                )

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
