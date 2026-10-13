# local_optimization.py
import numpy as np
from typing import Callable, Optional, Tuple


def gradient_descent_optimize(
    f: Callable[[np.ndarray], float],
    grad_f: Callable[[np.ndarray], np.ndarray],
    x0: np.ndarray,
    learning_rate: float = 0.01,
    tol: float = 1e-6,
    max_iterations: int = 10000,
) -> np.ndarray:
    """
    Gradient descent for unconstrained minimization.

    Args:
        f: Objective function.
        grad_f: Gradient of the objective function.
        x0: Initial point.
        learning_rate: Step size.
        tol: Convergence tolerance on the gradient norm.
        max_iterations: Maximum number of iterations.

    Returns:
        Approximate minimizer x*.

    Raises:
        ValueError: If the method does not converge.
    """
    x = x0.astype(float)
    for _ in range(max_iterations):
        g = grad_f(x)
        if np.linalg.norm(g) < tol:
            return x
        x = x - learning_rate * g
    raise ValueError(
        "Gradient descent did not converge within the maximum number of iterations."
    )


def newtons_method_optimize(
    f: Callable[[np.ndarray], float],
    grad_f: Callable[[np.ndarray], np.ndarray],
    hess_f: Callable[[np.ndarray], np.ndarray],
    x0: np.ndarray,
    tol: float = 1e-8,
    max_iterations: int = 100,
) -> np.ndarray:
    """
    Newton's method for unconstrained minimization.

    Uses exact Hessian information to achieve quadratic convergence
    near the solution.

    Args:
        f: Objective function.
        grad_f: Gradient of the objective.
        hess_f: Hessian of the objective.
        x0: Initial point.
        tol: Convergence tolerance on the gradient norm.
        max_iterations: Maximum number of iterations.

    Returns:
        Approximate minimizer x*.

    Raises:
        ValueError: If the Hessian is singular during iteration.
        ValueError: If the method does not converge.
    """
    x = x0.astype(float)
    for iteration in range(max_iterations):
        g = grad_f(x)
        if np.linalg.norm(g) < tol:
            return x
        H = hess_f(x)
        try:
            d = np.linalg.solve(H, -g)
        except np.linalg.LinAlgError:
            raise ValueError(f"Hessian is singular at iteration {iteration}, x = {x}.")
        x = x + d
    raise ValueError(
        "Newton's method did not converge within the maximum number of iterations."
    )


def _wolfe_line_search(
    f: Callable[[np.ndarray], float],
    grad_f: Callable[[np.ndarray], np.ndarray],
    x: np.ndarray,
    d: np.ndarray,
    fx: float,
    slope: float,
    c1: float,
    c2: float,
    alpha_init: float = 1.0,
    alpha_max: float = 1e6,
    max_iterations: int = 50,
) -> Optional[Tuple[float, float, np.ndarray]]:
    """
    Line search for a step satisfying the strong Wolfe conditions
    (bracketing phase followed by bisection zoom, cf. Nocedal & Wright,
    Algorithms 3.5 and 3.6).

        f(x + a d) <= f(x) + c1 a g^T d          (sufficient decrease)
        |grad f(x + a d)^T d| <= c2 |g^T d|      (curvature)

    Args:
        f, grad_f: Objective and its gradient.
        x: Current point.
        d: Descent direction.
        fx: f(x).
        slope: Directional derivative g^T d at x (must be negative).
        c1, c2: Wolfe constants with 0 < c1 < c2 < 1.
        alpha_init: First trial step length.
        alpha_max: Upper bound on the step length.
        max_iterations: Maximum trial steps in each phase.

    Returns:
        (alpha, f(x + alpha d), grad f(x + alpha d)) or None if no
        acceptable step was found.
    """

    def phi(a):
        return f(x + a * d)

    def dphi(a):
        return grad_f(x + a * d) @ d

    def zoom(lo, hi, phi_lo):
        for _ in range(max_iterations):
            a = 0.5 * (lo + hi)
            phi_a = phi(a)
            if phi_a > fx + c1 * a * slope or phi_a >= phi_lo:
                hi = a
            else:
                dphi_a = dphi(a)
                if abs(dphi_a) <= -c2 * slope:
                    return a
                if dphi_a * (hi - lo) >= 0:
                    hi = lo
                lo, phi_lo = a, phi_a
        return None

    alpha_prev, phi_prev = 0.0, fx
    alpha = alpha_init
    for i in range(max_iterations):
        phi_a = phi(alpha)
        if phi_a > fx + c1 * alpha * slope or (i > 0 and phi_a >= phi_prev):
            found = zoom(alpha_prev, alpha, phi_prev)
            break
        dphi_a = dphi(alpha)
        if abs(dphi_a) <= -c2 * slope:
            found = alpha
            break
        if dphi_a >= 0:
            found = zoom(alpha, alpha_prev, phi_a)
            break
        if alpha >= alpha_max:
            found = None
            break
        alpha_prev, phi_prev = alpha, phi_a
        alpha = min(2.0 * alpha, alpha_max)
    else:
        found = None

    if found is None:
        return None
    x_new = x + found * d
    return found, f(x_new), grad_f(x_new)


def bfgs(
    f: Callable[[np.ndarray], float],
    grad_f: Callable[[np.ndarray], np.ndarray],
    x0: np.ndarray,
    tol: float = 1e-6,
    max_iterations: int = 1000,
    c1: float = 1e-4,
    c2: float = 0.9,
    callback: Optional[Callable[[np.ndarray], None]] = None,
) -> np.ndarray:
    """
    BFGS quasi-Newton method for unconstrained minimization.

    Builds an approximation to the inverse Hessian using gradient
    differences, achieving superlinear convergence without computing
    the exact Hessian. Step lengths satisfy the strong Wolfe conditions,
    which guarantee y^T s > 0 so the update keeps the approximation
    positive definite.

    Args:
        f: Objective function.
        grad_f: Gradient of the objective.
        x0: Initial point.
        tol: Convergence tolerance on the gradient norm.
        max_iterations: Maximum number of iterations.
        c1: Sufficient decrease parameter for Wolfe conditions.
        c2: Curvature condition parameter for Wolfe conditions
            (0 < c1 < c2 < 1).
        callback: Optional function called with the iterate after each step.

    Returns:
        Approximate minimizer x*.

    Raises:
        ValueError: If c1 and c2 do not satisfy 0 < c1 < c2 < 1.
        ValueError: If the line search fails along a steepest-descent step.
        ValueError: If the method does not converge.
    """
    if not 0.0 < c1 < c2 < 1.0:
        raise ValueError("Wolfe constants must satisfy 0 < c1 < c2 < 1.")

    x = x0.astype(float)
    n = len(x)
    I = np.eye(n)
    H = I.copy()
    fx = f(x)
    g = grad_f(x)

    for _ in range(max_iterations):
        if np.linalg.norm(g) < tol:
            return x

        d = -H @ g
        slope = g @ d
        if slope >= 0:
            # H lost positive definiteness numerically: restart.
            H = I.copy()
            d = -g
            slope = g @ d

        result = _wolfe_line_search(f, grad_f, x, d, fx, slope, c1, c2)
        if result is None and not np.array_equal(H, I):
            # Retry along steepest descent with a fresh Hessian model.
            H = I.copy()
            d = -g
            slope = g @ d
            result = _wolfe_line_search(f, grad_f, x, d, fx, slope, c1, c2)
        if result is None:
            raise ValueError(
                "BFGS line search failed to find a step satisfying the Wolfe conditions."
            )
        alpha, fx, g_new = result

        s = alpha * d
        y = g_new - g
        x = x + s

        ys = y @ s
        if ys > 1e-10:
            rho = 1.0 / ys
            V1 = I - rho * np.outer(s, y)
            V2 = I - rho * np.outer(y, s)
            H = V1 @ H @ V2 + rho * np.outer(s, s)

        g = g_new
        if callback is not None:
            callback(x)

    raise ValueError("BFGS did not converge within the maximum number of iterations.")
