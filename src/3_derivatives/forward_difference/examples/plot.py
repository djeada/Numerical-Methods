import numpy as np
import matplotlib.pyplot as plt


def forward_difference(f, x, h=1e-5):
    """
    Approximate the derivative of f at x using the forward difference method.

    Parameters:
        f (callable): Function to differentiate.
        x (float): Point at which to approximate the derivative.
        h (float): Step size.

    Returns:
        float: Approximate derivative.
    """
    return (f(x + h) - f(x)) / h


if __name__ == "__main__":
    # Define the function and its exact derivative
    def f(x):
        return x ** 3

    def df(x):
        return 3 * x ** 2

    # Domain and evaluation point
    x_vals = np.linspace(0, 1, 1000)
    x0 = 0.3
    x1 = x0 + 0.5  # forward point

    # Plot the function
    plt.figure(figsize=(8, 6))
    plt.plot(x_vals, f(x_vals), label="$f(x) = x^3$")

    # Plot the forward difference secant line
    plt.plot([x0, x1], [f(x0), f(x1)], "r", linewidth=2, label="Forward difference")

    # Plot the exact derivative tangent line
    h = 0.2
    plt.plot(
        [x0 - h, x0 + h],
        [f(x0) - h * df(x0), f(x0) + h * df(x0)],
        "g--",
        linewidth=2,
        label="Exact derivative",
    )

    # Add axes labels and ticks
    plt.xticks((x0, x1), labels=("$x_0$", "$x_0 + \\Delta x$"))
    plt.plot([x0, x0], [-0.1, f(x0)], "g:")
    plt.plot([x1, x1], [-0.1, f(x1)], "g:")

    plt.yticks((f(x0), f(x1)), labels=("$f(x_0)$", "$f(x_0 + \\Delta x)$"))
    plt.plot([-0.1, x0], [f(x0), f(x0)], "g:")
    plt.plot([-0.1, x1], [f(x1), f(x1)], "g:")

    plt.title("Forward Difference Method", fontsize=16)
    plt.xlabel("$x$", fontsize=16)
    plt.ylabel("$f(x) = x^3$", fontsize=16)
    plt.legend(loc=2)
    plt.tight_layout()
    plt.show()
