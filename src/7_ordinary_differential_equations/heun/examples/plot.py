import numpy as np
import matplotlib.pyplot as plt
import sys
import os

here = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(here, os.pardir))
sys.path.append(os.path.join(here, os.pardir, os.pardir, "euler", "implementation"))
from implementation.heun import heun_method
from euler import euler_method


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
    plt.plot(t_euler, y_euler, "b-o", label="Euler's Method", markersize=3)
    plt.plot(t_heun, y_heun, "g-s", label="Heun's Method", markersize=3)
    plt.plot(t_heun, exact, "r--", label="Exact: $y = e^{-2t}$", linewidth=2)
    plt.xlabel("t")
    plt.ylabel("y")
    plt.title("Heun's Method vs Euler's Method vs Exact Solution")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()
