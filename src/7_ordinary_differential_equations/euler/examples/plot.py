import numpy as np
import matplotlib.pyplot as plt
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), os.pardir))
from implementation.euler import euler_method


if __name__ == "__main__":
    f = lambda t, y: -2 * y

    t0 = 0.0
    y0 = np.array([1.0])
    t_end = 5.0
    h = 0.1

    t, y = euler_method(f, t0, y0, t_end, h)
    exact = np.exp(-2 * t)

    plt.figure(figsize=(10, 6))
    plt.plot(t, y, "b-o", label="Euler's Method", markersize=3)
    plt.plot(t, exact, "r--", label="Exact: $y = e^{-2t}$", linewidth=2)
    plt.xlabel("t")
    plt.ylabel("y")
    plt.title("Euler's Method vs Exact Solution for dy/dt = -2y")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()
