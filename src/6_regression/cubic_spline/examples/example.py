"""
Cubic Spline Interpolation — Implementation vs scipy

Data: (0, 0), (1, -1), (2, 4), (3, 3)
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline
import sys
import os

sys.path.insert(
    0,
    os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir),
)
from implementation.cubic_spline import cubic_spline

x = np.array([0, 1, 2, 3], dtype=float)
y = np.array([0, -1, 4, 3], dtype=float)

spline = cubic_spline(x, y)
ref = CubicSpline(x, y, bc_type="natural")

x_domain = np.linspace(x[0], x[-1], 200)
y_impl = np.array([spline(xi) for xi in x_domain])
y_scipy = ref(x_domain)

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8), height_ratios=[3, 1])

ax1.scatter(x, y, s=120, zorder=5, color="black", label="Data points")
ax1.plot(x_domain, y_impl, lw=2, label="Implementation")
ax1.plot(x_domain, y_scipy, "--", lw=2, label="scipy CubicSpline (natural)")
ax1.set_ylabel("y")
ax1.set_title("Cubic Spline Interpolation")
ax1.legend()
ax1.grid(True, alpha=0.3)

ax2.plot(x_domain, np.abs(y_impl - y_scipy), color="red")
ax2.set_xlabel("x")
ax2.set_ylabel("|difference|")
ax2.set_title(f"Absolute Difference (max = {np.abs(y_impl - y_scipy).max():.2e})")
ax2.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()
