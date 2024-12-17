import matplotlib.pyplot as plt
import numpy as np

def f(x):
    """Example function: f(x) = x^2 - 4"""
    return x**2 - 4

def df(x):
    """Derivative of the example function: f'(x) = 2x"""
    return 2 * x

def newton_method_visualize(func, dfunc, x0, tol=1e-6, max_iterations=20):
    """
    Visualizes the progress of Newton's Method for root-finding on a single plot.

    Parameters:
        func (function): The function whose root is to be found.
        dfunc (function): The derivative of the function.
        x0 (float): Initial starting point.
        tol (float): Tolerance for stopping condition.
        max_iterations (int): Maximum number of iterations allowed.
    """
    # Store values for plotting
    x_values = [x0]
    y_values = [func(x0)]
    iteration = 0

    while iteration < max_iterations:
        f_x = func(x0)
        df_x = dfunc(x0)

        # Avoid division by zero
        if df_x == 0:
            print("Derivative is zero. Stopping iteration.")
            break

        # Newton's update
        x_new = x0 - f_x / df_x
        x_values.append(x_new)
        y_values.append(func(x_new))

        # Check convergence
        if abs(x_new - x0) < tol:
            break

        x0 = x_new
        iteration += 1

    # Generate x values for smooth curve plotting
    x = np.linspace(min(x_values) - 1, max(x_values) + 1, 400)
    y = func(x)

    # Plot the function and Newton's method steps
    plt.figure(figsize=(8, 6))
    plt.plot(x, y, label='$f(x) = x^2 - 4$', color='blue')
    plt.scatter(x_values, y_values, color='red', label="Newton's Method Steps")
    plt.axhline(0, color='black', linewidth=0.5)

    # Highlight the starting and final points
    plt.scatter(x_values[0], y_values[0], color='green', label='Starting Point')
    plt.scatter(x_values[-1], y_values[-1], color='purple', label='Final Point')

    plt.title("Newton's Method: Progress of Steps")
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.legend()
    plt.grid(True)
    plt.show()

# Example function and derivative
def f(x):
    return x**2 - 4

def df(x):
    return 2 * x

# Initial conditions for Newton's Method
x0 = 3  # Starting point
newton_method_visualize(f, df, x0)
