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
            raise ValueError(
                f"Hessian is singular at iteration {iteration}, x = {x}."
            )
        x = x + d
    raise ValueError(
        "Newton's method did not converge within the maximum number of iterations."
    )


def bfgs(
    f: Callable[[np.ndarray], float],
    grad_f: Callable[[np.ndarray], np.ndarray],
    x0: np.ndarray,
    tol: float = 1e-6,
    max_iterations: int = 1000,
    c1: float = 1e-4,
    c2: float = 0.9,
) -> np.ndarray:
    """
    BFGS quasi-Newton method for unconstrained minimization.

    Builds an approximation to the inverse Hessian using gradient
    differences, achieving superlinear convergence without computing
    the exact Hessian.

    Args:
        f: Objective function.
        grad_f: Gradient of the objective.
        x0: Initial point.
        tol: Convergence tolerance on the gradient norm.
        max_iterations: Maximum number of iterations.
        c1: Sufficient decrease parameter for Wolfe conditions.
        c2: Curvature condition parameter for Wolfe conditions.

    Returns:
        Approximate minimizer x*.

    Raises:
        ValueError: If the method does not converge.
    """
    x = x0.astype(float)
    n = len(x)
    H = np.eye(n)
    g = grad_f(x)

    for _ in range(max_iterations):
        if np.linalg.norm(g) < tol:
            return x

        d = -H @ g

        # Backtracking line search with Wolfe conditions
        alpha = 1.0
        fx = f(x)
        for _ in range(50):
            x_new = x + alpha * d
            if f(x_new) <= fx + c1 * alpha * (g @ d):
                g_new = grad_f(x_new)
                if g_new @ d >= c2 * (g @ d):
                    break
            alpha *= 0.5
        else:
            x_new = x + alpha * d
            g_new = grad_f(x_new)

        s = x_new - x
        y = g_new - g

        ys = y @ s
        if ys > 1e-10:
            rho = 1.0 / ys
            I = np.eye(n)
            V1 = I - rho * np.outer(s, y)
            V2 = I - rho * np.outer(y, s)
            H = V1 @ H @ V2 + rho * np.outer(s, s)

        x = x_new
        g = g_new

    raise ValueError(
        "BFGS did not converge within the maximum number of iterations."
    )
