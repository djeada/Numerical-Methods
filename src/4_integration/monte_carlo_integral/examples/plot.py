import numpy as np
import matplotlib.pyplot as plt


def monte_carlo_integral(f, a, b, num_samples=1000000):
    """
    Approximate the integral of f from a to b using Monte Carlo sampling.

    Parameters:
        f (callable): Function to integrate.
        a (float): Lower bound.
        b (float): Upper bound.
        num_samples (int): Number of random samples.

    Returns:
        float: Approximate integral.
    """
    samples = np.random.uniform(a, b, num_samples)
    evaluations = f(samples)
    return (b - a) * np.mean(evaluations)


if __name__ == "__main__":
    def f(x):
        return np.sin(x)

    a = 0
    b = np.pi
    num_samples = 1000

    np.random.seed(42)
    samples = np.random.uniform(a, b, num_samples)
    values = f(samples)

    result = monte_carlo_integral(f, a, b, num_samples=1000000)
    exact = 2.0
    print(f"Monte Carlo result: {result:.10f}")
    print(f"Exact value: {exact:.10f}")

    # Plot showing sampled points under the curve
    x = np.linspace(a, b, 500)
    y = f(x)

    fig, ax = plt.subplots(figsize=(8, 6))
    ax.plot(x, y, "blue", linewidth=2, label="f(x) = sin(x)")
    ax.scatter(samples, values, s=1, color="red", alpha=0.3, label="Random samples")
    ax.fill_between(x, 0, y, alpha=0.1, color="blue")
    ax.set_xlabel("x")
    ax.set_ylabel("f(x)")
    ax.set_title("Monte Carlo Integration Sampling")
    ax.legend()
    ax.grid(True)
    plt.tight_layout()
    plt.show()
