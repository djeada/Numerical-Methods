import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import Rbf

# Generate random 3D points (arbitrary)
np.random.seed(42)  # For reproducibility
n_points = 15
x = np.random.rand(n_points) * 10  # Arbitrary X-axis values
y = np.random.rand(n_points) * 10  # Arbitrary Y-axis values
z = np.random.rand(n_points) * 50  # Arbitrary Z-axis values

# Create thin plate spline interpolator
rbf = Rbf(x, y, z, function="thin_plate", smooth=0.1)

# Create grid for plotting the surface
x_grid = np.linspace(min(x), max(x), 50)
y_grid = np.linspace(min(y), max(y), 50)
X, Y = np.meshgrid(x_grid, y_grid)
Z = rbf(X, Y)  # Interpolated surface

# Plotting the TPS surface and data points
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection="3d")

# Surface plot
ax.plot_surface(
    X, Y, Z, rstride=1, cstride=1, cmap="viridis", alpha=0.8, edgecolor="none"
)

# Original data points
ax.scatter(x, y, z, color="red", s=50, label="Data Points")

# Customize the plot
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("Z-axis")
ax.set_title("3D Surface Fitting with Thin Plate Spline Interpolation")
ax.legend()

# Show the plot
plt.show()
