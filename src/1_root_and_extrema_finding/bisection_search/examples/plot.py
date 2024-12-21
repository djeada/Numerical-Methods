import matplotlib.pyplot as plt
import numpy as np


def f(x):
    """Example function: f(x) = x^2 - 4"""
    return x ** 2 - 4


def bisection_method_visualize(func, a, b, tol=1e-6, max_iterations=100):
    """
    Visualizes the initial and final steps of the bisection method for root-finding on a single plot.

    Parameters:
        func (function): The function to find the root of.
        a (float): Initial lower bound of the interval.
        b (float): Initial upper bound of the interval.
        tol (float): Tolerance for stopping condition.
        max_iterations (int): Maximum number of iterations allowed.
    """
    # Store initial a and b for plotting
    a_initial, b_initial = a, b

    # List to store intervals for visualization
    intervals = [(a, b)]
    iteration = 0

    while (b - a > tol) and (iteration < max_iterations):
        c = (a + b) / 2.0  # Midpoint
        if func(a) * func(c) < 0:
            b = c  # Root is in [a, c]
        else:
            a = c  # Root is in [c, b]
        intervals.append((a, b))
        iteration += 1

    # Final a and b
    a_final, b_final = a, b

    # Generate x values for plotting
    x = np.linspace(a_initial - 1, b_initial + 1, 400)
    y = func(x)

    # Plot initial and final intervals on the same plot
    plt.figure(figsize=(8, 6))
    plt.plot(x, y, label="$f(x) = x^2 - 4$", color="blue")
    plt.axhline(0, color="black", linewidth=0.5)

    # Initial step
    plt.scatter(
        [a_initial, b_initial],
        [func(a_initial), func(b_initial)],
        color="red",
        label="Initial Brackets [a, b]",
    )
    c_initial = (a_initial + b_initial) / 2.0
    plt.scatter(c_initial, func(c_initial), color="green", label="Initial Midpoint c")

    # Final step
    plt.scatter(
        [a_final, b_final],
        [func(a_final), func(b_final)],
        color="purple",
        label="Final Brackets [a, b]",
    )
    c_final = (a_final + b_final) / 2.0
    plt.scatter(c_final, func(c_final), color="orange", label="Final Midpoint c")

    plt.title("Bisection Method: Initial and Final Steps")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.legend()
    plt.grid(True)
    plt.show()


# Initial conditions for bisection method
a = 0
b = 5
bisection_method_visualize(f, a, b)
