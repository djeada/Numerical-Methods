import matplotlib.pyplot as plt
import numpy as np

def f(x):
    """Example function: f(x) = x^2"""
    return x**2

def gradient_descent_visualize(func, grad, x0, learning_rate=0.1, tol=1e-6, max_iterations=100):
    """
    Visualizes the progress of Gradient Descent for function minimization on a single plot.

    Parameters:
        func (function): The function to minimize.
        grad (function): The gradient of the function.
        x0 (float): Initial starting point.
        learning_rate (float): Step size.
        tol (float): Tolerance for stopping condition.
        max_iterations (int): Maximum number of iterations allowed.
    """
    # Store values for plotting
    x_values = [x0]
    y_values = [func(x0)]
    iteration = 0

    while iteration < max_iterations:
        gradient = grad(x0)
        x_new = x0 - learning_rate * gradient
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

    # Plot the function and gradient descent steps
    plt.figure(figsize=(8, 6))
    plt.plot(x, y, label='$f(x) = x^2$', color='blue')
    plt.scatter(x_values, y_values, color='red', label='Gradient Descent Steps')
    plt.axhline(0, color='black', linewidth=0.5)

    # Highlight the starting and final points
    plt.scatter(x_values[0], y_values[0], color='green', label='Starting Point')
    plt.scatter(x_values[-1], y_values[-1], color='purple', label='Final Point')

    plt.title('Gradient Descent: Progress of Steps')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.legend()
    plt.grid(True)
    plt.show()

# Example function and gradient
def f(x):
    return x**2

def grad_f(x):
    return 2 * x

# Initial conditions for Gradient Descent
x0 = 5  # Starting point
learning_rate = 0.1
gradient_descent_visualize(f, grad_f, x0, learning_rate)
