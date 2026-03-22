"""
Lagrange Polynomial Interpolation — Implementation vs scipy

Data points: A(-9,-2), B(-5,3), C(-2.5,0), D(4,5), F(7,11)
"""
import numpy as np
import matplotlib.pyplot as plt
import scipy.interpolate
import sys
import os

sys.path.insert(
    0,
    os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir),
)
from implementation.lagrange_polynomial import lagrange_polynomial

# Data
x = np.array([-9, -5, -2.5, 4, 7], dtype=float)
y = np.array([-2, 3, 0, 5, 11], dtype=float)

x_domain = np.linspace(1.1 * x.min(), 1.1 * x.max(), 200)

# Our implementation (evaluated point-by-point)
y_impl = np.array([lagrange_polynomial(x, y, xi) for xi in x_domain])

# scipy reference
y_scipy = scipy.interpolate.lagrange(x, y)(x_domain)

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8), height_ratios=[3, 1])

ax1.scatter(x, y, s=120, zorder=5, color="black", label="Data points")
ax1.plot(x_domain, y_impl, lw=2, label="Implementation")
ax1.plot(x_domain, y_scipy, "--", lw=2, label="scipy.interpolate.lagrange")
ax1.set_ylabel("y")
ax1.set_title("Lagrange Polynomial Interpolation")
ax1.legend()
ax1.grid(True, alpha=0.3)

ax2.plot(x_domain, np.abs(y_impl - y_scipy), color="red")
ax2.set_xlabel("x")
ax2.set_ylabel("|difference|")
ax2.set_title(f"Absolute Difference (max = {np.abs(y_impl - y_scipy).max():.2e})")
ax2.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()
