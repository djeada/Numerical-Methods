# newton_raphson.py
import numpy as np
from typing import Callable, Optional


def newton_raphson(
    f: Callable[[float], float],
    df: Callable[[float], float],
    x0: float,
    tol: float = 1e-8,
    max_iterations: int = 1000
) -> float:
    """
    Newton-Raphson method for finding the root of a real-valued function.

    Args:
        f (Callable[[float], float]): The function for which to find the root.
        df (Callable[[float], float]): The derivative of the function f.
        x0 (float): Initial guess for the root.
        tol (float, optional): Tolerance for convergence. Defaults to 1e-8.
        max_iterations (int, optional): Maximum number of iterations. Defaults to 1000.

    Returns:
        float: The estimated root of the function.

    Raises:
        ValueError: If the derivative is zero during iteration.
        ValueError: If the method does not converge within the maximum number of iterations.
    """
    x = x0
    for iteration in range(1, max_iterations + 1):
        fx = f(x)
        dfx = df(x)
        if np.isclose(dfx, 0.0, atol=1e-12):
            raise ValueError(f"Derivative is zero at iteration {iteration}, x = {x}.")
        x_new = x - fx / dfx
        if np.abs(x_new - x) < tol:
            return x_new
        x = x_new
    raise ValueError("Newton-Raphson method did not converge within the maximum number of iterations.")


def newton_raphson_system(
    F: Callable[[np.ndarray], np.ndarray],
    J: Callable[[np.ndarray], np.ndarray],
    x0: Optional[np.ndarray] = None,
    tol: float = 1e-8,
    max_iterations: int = 1000
) -> np.ndarray:
    """
    Newton-Raphson method for finding the root of a system of nonlinear equations.

    Args:
        F (Callable[[np.ndarray], np.ndarray]): The system of functions.
        J (Callable[[np.ndarray], np.ndarray]): The Jacobian matrix of F.
        x0 (Optional[np.ndarray], optional): Initial guess for the roots. Defaults to None.
        tol (float, optional): Tolerance for convergence. Defaults to 1e-8.
        max_iterations (int, optional): Maximum number of iterations. Defaults to 1000.

    Returns:
        np.ndarray: The estimated roots of the system.

    Raises:
        ValueError: If the Jacobian is singular at any iteration.
        ValueError: If the method does not converge within the maximum number of iterations.
    """
    if x0 is None:
        x = np.zeros(1)
    else:
        x = x0.astype(float)
    for iteration in range(1, max_iterations + 1):
        Fx = F(x)
        Jx = J(x)
        try:
            delta = np.linalg.solve(Jx, -Fx)
        except np.linalg.LinAlgError:
            raise ValueError(f"Jacobian is singular at iteration {iteration}, x = {x}.")
        x_new = x + delta
        if np.linalg.norm(delta, ord=np.inf) < tol:
            return x_new
        x = x_new
    raise ValueError("Newton-Raphson method did not converge within the maximum number of iterations.")
