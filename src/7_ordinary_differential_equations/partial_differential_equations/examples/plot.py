import numpy as np
import matplotlib.pyplot as plt


def heat_equation_explicit(u0, x, t_end, dt, alpha, bc_left=0.0, bc_right=0.0):
    """Solve 1D heat equation using explicit finite difference method."""
    nx = len(x)
    dx = x[1] - x[0]
    r = alpha * dt / dx**2

    u = u0.copy()
    t = 0.0
    t_values = [t]
    u_values = [u.copy()]

    while t < t_end - dt / 2:
        u_new = u.copy()
        for i in range(1, nx - 1):
            u_new[i] = u[i] + r * (u[i + 1] - 2 * u[i] + u[i - 1])
        u_new[0] = bc_left
        u_new[-1] = bc_right
        u = u_new
        t += dt
        t_values.append(t)
        u_values.append(u.copy())

    return np.array(t_values), x, np.array(u_values)


if __name__ == "__main__":
    nx = 50
    x = np.linspace(0, 1, nx)
    u0 = np.sin(np.pi * x)

    alpha = 0.01
    t_end = 0.5
    dx = x[1] - x[0]
    dt = 0.4 * dx**2 / alpha

    t, x_out, u = heat_equation_explicit(u0, x, t_end, dt, alpha)

    plt.figure(figsize=(10, 6))

    n_plots = 5
    indices = np.linspace(0, len(t) - 1, n_plots, dtype=int)

    for idx in indices:
        plt.plot(x_out, u[idx, :], label=f"t = {t[idx]:.3f}")

    plt.xlabel("x")
    plt.ylabel("u(x, t)")
    plt.title("Heat Equation: $u_0 = \\sin(\\pi x)$ (Explicit Method)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()
