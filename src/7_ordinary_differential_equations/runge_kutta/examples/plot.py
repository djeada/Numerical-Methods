import numpy as np
import matplotlib.pyplot as plt
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), os.pardir))
from implementation.runge_kutta import runge_kutta_4


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
        plt.plot(t, y, f"{color}-{marker}", label=f"RK4 (h={h})", markersize=4)

    plt.xlabel("t")
    plt.ylabel("y")
    plt.title("RK4 Accuracy at Different Step Sizes for dy/dt = -2y")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()
