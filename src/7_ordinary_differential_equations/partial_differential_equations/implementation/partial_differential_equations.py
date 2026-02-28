import numpy as np
from typing import Callable, Tuple


def heat_equation_explicit(
    u0: np.ndarray,
    x: np.ndarray,
    t_end: float,
    dt: float,
    alpha: float,
    bc_left: float = 0.0,
    bc_right: float = 0.0,
) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    if dt <= 0:
        raise ValueError("Time step dt must be positive.")
    if t_end <= 0:
        raise ValueError("t_end must be positive.")
    if alpha <= 0:
        raise ValueError("Diffusion coefficient alpha must be positive.")
    if len(x) < 3:
        raise ValueError("Spatial grid must have at least 3 points.")
    if len(u0) != len(x):
        raise ValueError("Initial condition u0 must match the spatial grid size.")

    dx = x[1] - x[0]
    r = alpha * dt / dx**2

    if r > 0.5:
        raise ValueError(
            f"Stability condition violated: alpha*dt/dx^2 = {r} > 0.5. "
            "Reduce dt or increase dx."
        )

    n_steps = int(np.ceil(t_end / dt))
    t = np.linspace(0, n_steps * dt, n_steps + 1)
    u = np.zeros((n_steps + 1, len(x)))
    u[0] = u0.copy()

    for n in range(n_steps):
        u[n + 1, 0] = bc_left
        u[n + 1, -1] = bc_right
        for i in range(1, len(x) - 1):
            u[n + 1, i] = u[n, i] + r * (u[n, i + 1] - 2 * u[n, i] + u[n, i - 1])

    return t, x, u


def heat_equation_implicit(
    u0: np.ndarray,
    x: np.ndarray,
    t_end: float,
    dt: float,
    alpha: float,
    bc_left: float = 0.0,
    bc_right: float = 0.0,
) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    if dt <= 0:
        raise ValueError("Time step dt must be positive.")
    if t_end <= 0:
        raise ValueError("t_end must be positive.")
    if alpha <= 0:
        raise ValueError("Diffusion coefficient alpha must be positive.")
    if len(x) < 3:
        raise ValueError("Spatial grid must have at least 3 points.")
    if len(u0) != len(x):
        raise ValueError("Initial condition u0 must match the spatial grid size.")

    dx = x[1] - x[0]
    r = alpha * dt / dx**2
    nx = len(x)

    n_steps = int(np.ceil(t_end / dt))
    t = np.linspace(0, n_steps * dt, n_steps + 1)
    u = np.zeros((n_steps + 1, nx))
    u[0] = u0.copy()

    interior = nx - 2
    A = np.zeros((interior, interior))
    for i in range(interior):
        A[i, i] = 1 + 2 * r
        if i > 0:
            A[i, i - 1] = -r
        if i < interior - 1:
            A[i, i + 1] = -r

    for n in range(n_steps):
        b = u[n, 1:-1].copy()
        b[0] += r * bc_left
        b[-1] += r * bc_right
        u[n + 1, 1:-1] = np.linalg.solve(A, b)
        u[n + 1, 0] = bc_left
        u[n + 1, -1] = bc_right

    return t, x, u


def wave_equation_explicit(
    u0: np.ndarray,
    v0: np.ndarray,
    x: np.ndarray,
    t_end: float,
    dt: float,
    c: float,
    bc_left: float = 0.0,
    bc_right: float = 0.0,
) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    if dt <= 0:
        raise ValueError("Time step dt must be positive.")
    if t_end <= 0:
        raise ValueError("t_end must be positive.")
    if c <= 0:
        raise ValueError("Wave speed c must be positive.")
    if len(x) < 3:
        raise ValueError("Spatial grid must have at least 3 points.")
    if len(u0) != len(x):
        raise ValueError("Initial condition u0 must match the spatial grid size.")
    if len(v0) != len(x):
        raise ValueError("Initial velocity v0 must match the spatial grid size.")

    dx = x[1] - x[0]
    r = c * dt / dx

    if r > 1.0:
        raise ValueError(
            f"CFL condition violated: c*dt/dx = {r} > 1.0. "
            "Reduce dt or increase dx."
        )

    n_steps = int(np.ceil(t_end / dt))
    t = np.linspace(0, n_steps * dt, n_steps + 1)
    u = np.zeros((n_steps + 1, len(x)))
    u[0] = u0.copy()

    r2 = r**2
    u[1, 0] = bc_left
    u[1, -1] = bc_right
    for i in range(1, len(x) - 1):
        u[1, i] = (
            u[0, i]
            + dt * v0[i]
            + 0.5 * r2 * (u[0, i + 1] - 2 * u[0, i] + u[0, i - 1])
        )

    for n in range(1, n_steps):
        u[n + 1, 0] = bc_left
        u[n + 1, -1] = bc_right
        for i in range(1, len(x) - 1):
            u[n + 1, i] = (
                2 * u[n, i]
                - u[n - 1, i]
                + r2 * (u[n, i + 1] - 2 * u[n, i] + u[n, i - 1])
            )

    return t, x, u


def laplace_equation_2d(
    nx: int,
    ny: int,
    x_range: Tuple[float, float],
    y_range: Tuple[float, float],
    bc: Callable[[np.ndarray, np.ndarray], np.ndarray],
    tol: float = 1e-6,
    max_iter: int = 10000,
) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    if nx < 3 or ny < 3:
        raise ValueError("Grid dimensions must be at least 3 in each direction.")
    if tol <= 0:
        raise ValueError("Tolerance must be positive.")
    if max_iter <= 0:
        raise ValueError("Maximum iterations must be positive.")

    x = np.linspace(x_range[0], x_range[1], nx)
    y = np.linspace(y_range[0], y_range[1], ny)
    X, Y = np.meshgrid(x, y, indexing="ij")

    u = bc(X, Y).astype(float)

    for _ in range(max_iter):
        u_old = u.copy()
        for i in range(1, nx - 1):
            for j in range(1, ny - 1):
                u[i, j] = 0.25 * (u[i + 1, j] + u[i - 1, j] + u[i, j + 1] + u[i, j - 1])

        if np.max(np.abs(u - u_old)) < tol:
            break

    return x, y, u
