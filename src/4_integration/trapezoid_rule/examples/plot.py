import numpy as np
import matplotlib.pyplot as plt


def trapezoid_rule(f, a, b, n):
    """
    Approximate the integral of f from a to b using the trapezoid rule.

    Parameters:
        f (callable): Function to integrate.
        a (float): Lower bound.
        b (float): Upper bound.
        n (int): Number of subintervals.

    Returns:
        float: Approximate integral.
    """
    x = np.linspace(a, b, n + 1)
    y = np.array([f(xi) for xi in x])
    h = (b - a) / n
    return h * (0.5 * y[0] + np.sum(y[1:-1]) + 0.5 * y[-1])


if __name__ == "__main__":

    def f(x):
        return x * np.sin(x)

    a = 0
    b = np.pi
    n = 10

    result = trapezoid_rule(f, a, b, n)
    exact = np.pi
    print(f"Trapezoid rule result: {result:.10f}")
    print(f"Exact value:           {exact:.10f}")

    # Plot function and trapezoids
    x = np.linspace(a - 0.5, b + 0.5, 500)
    y = f(x)

    fig, ax = plt.subplots(figsize=(8, 6))
    ax.plot(x, y, "blue", linewidth=2, label="f(x) = x*sin(x)")
    ax.set_ylim(bottom=0)

    h = (b - a) / n
    nodes = np.linspace(a, b, n + 1)
    for i in range(n):
        x0, x1 = nodes[i], nodes[i + 1]
        xs = [x0, x0, x1, x1]
        ys = [0, f(x0), f(x1), 0]
        ax.fill(xs, ys, alpha=0.3, color="orange", edgecolor="black")

    ax.set_xlabel("x", fontsize=14)
    ax.set_ylabel("f(x)", fontsize=14)
    ax.set_title("Trapezoid Rule", fontsize=16)
    ax.legend()
    ax.grid(True)
    plt.tight_layout()
    plt.show()
