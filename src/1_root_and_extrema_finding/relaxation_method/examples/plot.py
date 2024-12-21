import matplotlib.pyplot as plt
import numpy as np


def g(x):
    """Fixed-point iteration function: g(x) = (x^2 + 2) / 3"""
    return (x ** 2 + 2) / 3


def fixed_point_iteration_visualize(g_func, x0, tol=1e-6, max_iterations=50):
    """
    Visualizes the progress of the fixed-point iteration method for root-finding.

    Parameters:
        g_func (function): The fixed-point iteration function.
        x0 (float): Initial starting point.
        tol (float): Tolerance for stopping condition.
        max_iterations (int): Maximum number of iterations allowed.
    """
    # Store iteration values for plotting
    x_values = [x0]
    iteration = 0

    while iteration < max_iterations:
        x_new = g_func(x0)
        x_values.append(x_new)

        # Check convergence
        if abs(x_new - x0) < tol:
            break

        x0 = x_new
        iteration += 1

    # Generate x values for smooth curve plotting
    x = np.linspace(min(x_values) - 0.5, max(x_values) + 0.5, 400)
    y_gx = g_func(x)

    # Plot the fixed-point function and steps
    plt.figure(figsize=(8, 6))
    plt.plot(x, y_gx, label="$g(x)$", linestyle="--", color="orange")
    plt.plot(x, x, label="$y = x$", color="gray")
    plt.scatter(
        x_values, [g_func(x) for x in x_values], color="red", label="Iteration Steps"
    )

    # Highlight the starting and final points
    plt.scatter(x_values[0], g_func(x_values[0]), color="green", label="Starting Point")
    plt.scatter(x_values[-1], g_func(x_values[-1]), color="purple", label="Final Point")

    plt.title("Fixed-Point Iteration Method: Progress of Steps")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.axhline(0, color="black", linewidth=0.5)
    plt.legend()
    plt.grid(True)
    plt.show()


# Example fixed-point iteration function
def g(x):
    return (x ** 2 + 2) / 3


# Initial guess for Fixed-Point Iteration
x0 = 0
fixed_point_iteration_visualize(g, x0)
