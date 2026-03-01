import numpy as np
import matplotlib.pyplot as plt


def simulated_annealing(f, bounds, x0=None, T0=10.0, cooling_rate=0.95,
                        sigma=0.5, max_iterations=10000, seed=None):
    """
    Minimize a function using simulated annealing.

    Parameters:
        f (callable): Objective function.
        bounds (list): List of (min, max) bounds for each dimension.
        x0 (numpy.ndarray): Initial point.
        T0 (float): Initial temperature.
        cooling_rate (float): Temperature cooling rate per iteration.
        sigma (float): Standard deviation of random perturbation.
        max_iterations (int): Maximum number of iterations.
        seed (int): Random seed for reproducibility.

    Returns:
        best_x (numpy.ndarray): Best solution found.
        best_f (float): Best objective value found.
        history (list): List of (x, f_val) at each iteration.
    """
    rng = np.random.default_rng(seed)
    dim = len(bounds)

    if x0 is None:
        x0 = np.array([rng.uniform(lo, hi) for lo, hi in bounds])

    x = x0.copy()
    f_x = f(x)
    best_x = x.copy()
    best_f = f_x
    history = [(x.copy(), f_x)]

    T = T0
    for _ in range(max_iterations):
        # Perturb and clip to bounds
        x_new = x + rng.normal(0, sigma, size=dim)
        for d in range(dim):
            x_new[d] = np.clip(x_new[d], bounds[d][0], bounds[d][1])

        f_new = f(x_new)
        delta = f_new - f_x

        if delta < 0 or rng.random() < np.exp(-delta / max(T, 1e-300)):
            x = x_new
            f_x = f_new
            if f_x < best_f:
                best_x = x.copy()
                best_f = f_x

        history.append((x.copy(), f_x))
        T *= cooling_rate

    return best_x, best_f, history


if __name__ == "__main__":
    # Rastrigin function (multi-modal)
    def rastrigin(x):
        A = 10
        return A * len(x) + np.sum(x ** 2 - A * np.cos(2 * np.pi * x))

    bounds = [(-5.12, 5.12), (-5.12, 5.12)]
    x0 = np.array([4.0, 4.0])
    best_x, best_f, history = simulated_annealing(
        rastrigin, bounds, x0=x0, T0=20.0, cooling_rate=0.999,
        sigma=0.3, max_iterations=20000, seed=42,
    )

    print(f"Best solution: ({best_x[0]:.6f}, {best_x[1]:.6f})")
    print(f"Best value:    {best_f:.6f}")

    # Plot the Rastrigin surface with SA path
    x_range = np.linspace(-5.12, 5.12, 300)
    y_range = np.linspace(-5.12, 5.12, 300)
    X, Y = np.meshgrid(x_range, y_range)
    Z = 20 + X ** 2 + Y ** 2 - 10 * (np.cos(2 * np.pi * X) + np.cos(2 * np.pi * Y))

    fig, ax = plt.subplots(figsize=(9, 7))
    contour = ax.contourf(X, Y, Z, levels=40, cmap="viridis", alpha=0.8)
    plt.colorbar(contour, ax=ax, label="$f(x, y)$")

    # Plot SA path (subsample for clarity)
    positions = np.array([h[0] for h in history])
    step = max(1, len(positions) // 500)
    ax.plot(
        positions[::step, 0], positions[::step, 1],
        "w.-", markersize=1, linewidth=0.5, alpha=0.6, label="SA path",
    )
    ax.plot(x0[0], x0[1], "wo", markersize=10, label="Start")
    ax.plot(best_x[0], best_x[1], "r*", markersize=18, zorder=5, label="Best found")

    ax.set_xlabel("$x$", fontsize=14)
    ax.set_ylabel("$y$", fontsize=14)
    ax.set_title("Simulated Annealing on Rastrigin Function", fontsize=16)
    ax.legend(fontsize=11, loc="upper left")
    plt.tight_layout()
    plt.show()
