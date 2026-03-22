import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import RBFInterpolator
import sys
import os

sys.path.insert(
    0,
    os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir),
)
from implementation.thin_plate_spline_interpolation import (
    thin_plate_spline_interpolation,
)

# ── Notes Example 2: non-planar saddle-like data ──────────────────────────
x_data = np.array([0.0, 1.0, 0.0, 1.0])
y_data = np.array([0.0, 0.0, 1.0, 1.0])
z_data = np.array([1.0, 0.0, 0.0, 1.0])

grid_n = 40
gx = np.linspace(-0.2, 1.2, grid_n)
gy = np.linspace(-0.2, 1.2, grid_n)
GX, GY = np.meshgrid(gx, gy)

# Our implementation
GZ_impl = np.zeros_like(GX)
for i in range(grid_n):
    for j in range(grid_n):
        GZ_impl[i, j] = thin_plate_spline_interpolation(
            x_data, y_data, z_data, (GX[i, j], GY[i, j])
        )

# scipy reference
coords = np.column_stack([x_data, y_data])
rbf = RBFInterpolator(coords, z_data, kernel="thin_plate_spline", degree=1)
GZ_scipy = rbf(np.column_stack([GX.ravel(), GY.ravel()])).reshape(GX.shape)

fig = plt.figure(figsize=(16, 5))

ax1 = fig.add_subplot(131, projection="3d")
ax1.plot_surface(GX, GY, GZ_impl, cmap="viridis", alpha=0.8)
ax1.scatter(x_data, y_data, z_data, color="red", s=60, label="Data")
ax1.set_title("Implementation")
ax1.set_xlabel("x")
ax1.set_ylabel("y")
ax1.set_zlabel("z")

ax2 = fig.add_subplot(132, projection="3d")
ax2.plot_surface(GX, GY, GZ_scipy, cmap="viridis", alpha=0.8)
ax2.scatter(x_data, y_data, z_data, color="red", s=60, label="Data")
ax2.set_title("scipy RBFInterpolator")
ax2.set_xlabel("x")
ax2.set_ylabel("y")
ax2.set_zlabel("z")

ax3 = fig.add_subplot(133)
diff = np.abs(GZ_impl - GZ_scipy)
c = ax3.contourf(GX, GY, diff, levels=20, cmap="Reds")
plt.colorbar(c, ax=ax3)
ax3.set_title(f"|Difference| (max = {diff.max():.2e})")
ax3.set_xlabel("x")
ax3.set_ylabel("y")

plt.suptitle("Thin Plate Spline: Implementation vs scipy (Notes Example 2)")
plt.tight_layout()
plt.show()
