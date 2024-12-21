import matplotlib.pyplot as plt
import numpy as np


def f(x):
    """Example function: f(x) = x^2 - 4"""
    return x ** 2 - 4


def secant_method_visualize(f_func, x0, x1, tol=1e-6, max_iterations=50):
    """
    Visualizes the progress of the Secant Method for root-finding.

    Parameters:
        f_func (function): The function whose root is to be found.
        x0 (float): First initial guess.
        x1 (float): Second initial guess.
        tol (float): Tolerance for stopping condition.
        max_iterations (int): Maximum number of iterations allowed.
    """
    # Store iteration values for plotting
    x_values = [x0, x1]
    y_values = [f_func(x0), f_func(x1)]
    iteration = 0

    while iteration < max_iterations:
        f_x0 = f_func(x0)
        f_x1 = f_func(x1)

        # Avoid division by zero
        if f_x1 - f_x0 == 0:
            print("Division by zero encountered. Stopping iteration.")
            break

        # Secant Method update
        x_new = x1 - f_x1 * (x1 - x0) / (f_x1 - f_x0)
        x_values.append(x_new)
        y_values.append(f_func(x_new))

        # Check convergence
        if abs(x_new - x1) < tol or abs(f_func(x_new)) < tol:
            break

        # Update points
        x0, x1 = x1, x_new
        iteration += 1

    # Generate x values for smooth curve plotting
    x = np.linspace(min(x_values) - 1, max(x_values) + 1, 400)
    y = f_func(x)

    # Plot the function and Secant Method steps
    plt.figure(figsize=(8, 6))
    plt.plot(x, y, label="$f(x) = x^2 - 4$", color="blue")
    plt.axhline(0, color="black", linewidth=0.5)
    plt.scatter(x_values, y_values, color="red", label="Secant Method Steps")

    # Highlight the starting and final points
    plt.scatter(x_values[0], y_values[0], color="green", label="Starting Point")
    plt.scatter(x_values[-1], y_values[-1], color="purple", label="Final Point")

    plt.title("Secant Method: Progress of Steps")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.legend()
    plt.grid(True)
    plt.show()


# Example function for Secant Method
def f(x):
    return x ** 2 - 4


# Initial guesses for Secant Method
x0 = 0
x1 = 1
secant_method_visualize(f, x0, x1)
