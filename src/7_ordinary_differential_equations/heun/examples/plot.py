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


def heun_method(f, t0, y0, t_end, h):
    """Heun's method (improved Euler) for solving ODEs."""
    t_values = [t0]
    y_values = [np.array(y0, dtype=float)]
    t = t0
    y = np.array(y0, dtype=float)
    while t < t_end - h / 2:
        k1 = np.array(f(t, y))
        y_predict = y + h * k1
        k2 = np.array(f(t + h, y_predict))
        y = y + h / 2 * (k1 + k2)
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

    t_euler, y_euler = euler_method(f, t0, y0, t_end, h)
    t_heun, y_heun = heun_method(f, t0, y0, t_end, h)
    exact = np.exp(-2 * t_heun)

    plt.figure(figsize=(10, 6))
    plt.plot(t_euler, y_euler[:, 0], "b-o", label="Euler's Method", markersize=3)
    plt.plot(t_heun, y_heun[:, 0], "g-s", label="Heun's Method", markersize=3)
    plt.plot(t_heun, exact, "r--", label="Exact: $y = e^{-2t}$", linewidth=2)
    plt.xlabel("t")
    plt.ylabel("y")
    plt.title("Heun's Method vs Euler's Method vs Exact Solution")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()
