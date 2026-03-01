import numpy as np
import matplotlib.pyplot as plt


def picard_method(f, t0, y0, t_end, h, tol=1e-6, max_iterations=1000):
    """Picard iteration method for solving ODEs."""
    t_values = [t0]
    y_values = [np.array(y0, dtype=float)]
    t = t0
    y = np.array(y0, dtype=float)
    while t < t_end - h / 2:
        y_old = y.copy()
        for _ in range(max_iterations):
            y_new = y_old + h * np.array(f(t, y))
            if np.linalg.norm(y_new - y) < tol:
                break
            y = y_new.copy()
        y = y_new.copy()
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

    t, y = picard_method(f, t0, y0, t_end, h)
    exact = np.exp(-2 * t)

    plt.figure(figsize=(10, 6))
    plt.plot(t, y[:, 0], "m-o", label="Picard's Method", markersize=3)
    plt.plot(t, exact, "r--", label="Exact: $y = e^{-2t}$", linewidth=2)
    plt.xlabel("t")
    plt.ylabel("y")
    plt.title("Picard's Method vs Exact Solution for dy/dt = -2y")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()
