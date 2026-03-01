import numpy as np
import matplotlib.pyplot as plt


def runge_kutta_4(f, t0, y0, t_end, h):
    """Classic 4th-order Runge-Kutta method."""
    t_values = [t0]
    y_values = [np.array(y0, dtype=float)]
    t = t0
    y = np.array(y0, dtype=float)
    while t < t_end - h / 2:
        k1 = h * np.array(f(t, y))
        k2 = h * np.array(f(t + h / 2, y + k1 / 2))
        k3 = h * np.array(f(t + h / 2, y + k2 / 2))
        k4 = h * np.array(f(t + h, y + k3))
        y = y + (k1 + 2 * k2 + 2 * k3 + k4) / 6
        t += h
        t_values.append(t)
        y_values.append(y.copy())
    return np.array(t_values), np.array(y_values)


if __name__ == "__main__":
    f = lambda t, y: -2 * y

    t0 = 0.0
    y0 = np.array([1.0])
    t_end = 5.0
    step_sizes = [0.5, 0.25, 0.1]

    t_fine = np.linspace(0, t_end, 200)
    exact_fine = np.exp(-2 * t_fine)

    plt.figure(figsize=(10, 6))
    plt.plot(t_fine, exact_fine, "r--", label="Exact: $y = e^{-2t}$", linewidth=2)

    colors = ["b", "g", "m"]
    markers = ["o", "s", "^"]
    for h, color, marker in zip(step_sizes, colors, markers):
        t, y = runge_kutta_4(f, t0, y0, t_end, h)
        plt.plot(
            t, y[:, 0], f"{color}-{marker}", label=f"RK4 (h={h})", markersize=4
        )

    plt.xlabel("t")
    plt.ylabel("y")
    plt.title("RK4 Accuracy at Different Step Sizes for dy/dt = -2y")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()
