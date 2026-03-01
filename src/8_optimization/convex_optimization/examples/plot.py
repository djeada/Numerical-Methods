import numpy as np
import matplotlib.pyplot as plt


def gradient_descent_minimize(f, grad_f, x0, learning_rate=0.1, tol=1e-6, max_iter=1000):
    """
    Minimize a function using gradient descent.

    Parameters:
        f (callable): Objective function.
        grad_f (callable): Gradient of the objective function.
        x0 (numpy.ndarray): Initial point.
        learning_rate (float): Step size.
        tol (float): Convergence tolerance.
        max_iter (int): Maximum number of iterations.

    Returns:
        path (list): List of points visited during optimization.
    """
    x = x0.copy()
    path = [x.copy()]

    for _ in range(max_iter):
        g = grad_f(x)
        if np.linalg.norm(g) < tol:
            break
        x = x - learning_rate * g
        path.append(x.copy())

    return path


if __name__ == "__main__":
    # Quadratic function: f(x, y) = 3x^2 + y^2
    def f(x):
        return 3 * x[0] ** 2 + x[1] ** 2

    def grad_f(x):
        return np.array([6 * x[0], 2 * x[1]])

    x0 = np.array([3.0, 4.0])
    path = gradient_descent_minimize(f, grad_f, x0, learning_rate=0.15)
    path = np.array(path)

    print(f"Starting point: {x0}")
    print(f"Final point:    ({path[-1][0]:.6f}, {path[-1][1]:.6f})")
    print(f"Iterations:     {len(path) - 1}")

    # Create contour plot
    x_range = np.linspace(-4, 4, 200)
    y_range = np.linspace(-5, 5, 200)
    X, Y = np.meshgrid(x_range, y_range)
    Z = 3 * X ** 2 + Y ** 2

    fig, ax = plt.subplots(figsize=(8, 6))
    contour = ax.contour(X, Y, Z, levels=20, cmap="viridis", alpha=0.7)
    ax.clabel(contour, inline=True, fontsize=8)

    # Plot optimization path
    ax.plot(path[:, 0], path[:, 1], "r.-", markersize=6, linewidth=1.5, label="Gradient descent path")
    ax.plot(path[0, 0], path[0, 1], "go", markersize=10, label="Start")
    ax.plot(path[-1, 0], path[-1, 1], "r*", markersize=15, label="Minimum")

    ax.set_xlabel("$x$", fontsize=14)
    ax.set_ylabel("$y$", fontsize=14)
    ax.set_title("Gradient Descent on $f(x, y) = 3x^2 + y^2$", fontsize=16)
    ax.legend(fontsize=11)
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()
