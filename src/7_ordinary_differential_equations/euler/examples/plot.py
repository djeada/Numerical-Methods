import numpy as np
import matplotlib.pyplot as plt


def euler_method(f, t0, y0, t_end, h):
    """Euler's method for solving ODEs."""
    t_values = [t0]
    y_values = [y0]
    t = t0
    y = np.array(y0, dtype=float)
    while t < t_end - h / 2:
        y = y + h * np.array(f(t, y))
        t += h
        t_values.append(t)
        y_values.append(y.copy())
    return np.array(t_values), np.array(y_values)


if __name__ == "__main__":
    f = lambda t, y: -2 * y

    t0 = 0.0
    y0 = np.array([1.0])
    t_end = 5.0
    h = 0.1

    t, y = euler_method(f, t0, y0, t_end, h)
    exact = np.exp(-2 * t)

    plt.figure(figsize=(10, 6))
    plt.plot(t, y[:, 0], "b-o", label="Euler's Method", markersize=3)
    plt.plot(t, exact, "r--", label="Exact: $y = e^{-2t}$", linewidth=2)
    plt.xlabel("t")
    plt.ylabel("y")
    plt.title("Euler's Method vs Exact Solution for dy/dt = -2y")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()
