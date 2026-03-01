import numpy as np
import matplotlib.pyplot as plt


def gradient_descent(f, grad_f, x0, learning_rate=0.01, tol=1e-6, max_iterations=10000):
    """
    Minimize a function using gradient descent.

    Parameters:
        f (callable): Objective function.
        grad_f (callable): Gradient of the objective function.
        x0 (numpy.ndarray): Initial point.
        learning_rate (float): Step size.
        tol (float): Convergence tolerance on gradient norm.
        max_iterations (int): Maximum number of iterations.

    Returns:
        path (list): List of points visited during optimization.
    """
    x = x0.copy()
    path = [x.copy()]

    for _ in range(max_iterations):
        g = grad_f(x)
        if np.linalg.norm(g) < tol:
            break
        x = x - learning_rate * g
        path.append(x.copy())

    return path


def newton_method_optimize(f, grad_f, hess_f, x0, tol=1e-8, max_iterations=100):
    """
    Minimize a function using Newton's method.

    Parameters:
        f (callable): Objective function.
        grad_f (callable): Gradient of the objective function.
        hess_f (callable): Hessian of the objective function.
        x0 (numpy.ndarray): Initial point.
        tol (float): Convergence tolerance on gradient norm.
        max_iterations (int): Maximum number of iterations.

    Returns:
        path (list): List of points visited during optimization.
    """
    x = x0.copy()
    path = [x.copy()]

    for _ in range(max_iterations):
        g = grad_f(x)
        if np.linalg.norm(g) < tol:
            break
        H = hess_f(x)
        step = np.linalg.solve(H, g)
        x = x - step
        path.append(x.copy())

    return path


if __name__ == "__main__":
    # Quadratic function: f(x, y) = 5x^2 + y^2
    def f(x):
        return 5 * x[0] ** 2 + x[1] ** 2

    def grad_f(x):
        return np.array([10 * x[0], 2 * x[1]])

    def hess_f(x):
        return np.array([[10.0, 0.0], [0.0, 2.0]])

    x0 = np.array([3.0, 4.0])

    path_gd = np.array(gradient_descent(f, grad_f, x0, learning_rate=0.08))
    path_nm = np.array(newton_method_optimize(f, grad_f, hess_f, x0))

    print(f"Gradient Descent: {len(path_gd) - 1} iterations -> ({path_gd[-1][0]:.6f}, {path_gd[-1][1]:.6f})")
    print(f"Newton's Method:  {len(path_nm) - 1} iterations -> ({path_nm[-1][0]:.6f}, {path_nm[-1][1]:.6f})")

    # Create contour plot
    x_range = np.linspace(-4, 4, 200)
    y_range = np.linspace(-5, 5, 200)
    X, Y = np.meshgrid(x_range, y_range)
    Z = 5 * X ** 2 + Y ** 2

    fig, ax = plt.subplots(figsize=(8, 6))
    contour = ax.contour(X, Y, Z, levels=20, cmap="viridis", alpha=0.7)
    ax.clabel(contour, inline=True, fontsize=8)

    # Plot both paths
    ax.plot(
        path_gd[:, 0], path_gd[:, 1], "b.-",
        markersize=5, linewidth=1.5, label=f"Gradient Descent ({len(path_gd) - 1} iters)",
    )
    ax.plot(
        path_nm[:, 0], path_nm[:, 1], "r.-",
        markersize=8, linewidth=2, label=f"Newton's Method ({len(path_nm) - 1} iters)",
    )

    ax.plot(x0[0], x0[1], "go", markersize=12, zorder=5, label="Start")
    ax.plot(0, 0, "k*", markersize=15, zorder=5, label="Minimum")

    ax.set_xlabel("$x$", fontsize=14)
    ax.set_ylabel("$y$", fontsize=14)
    ax.set_title("Gradient Descent vs Newton's Method on $f(x,y) = 5x^2 + y^2$", fontsize=14)
    ax.legend(fontsize=10)
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()
