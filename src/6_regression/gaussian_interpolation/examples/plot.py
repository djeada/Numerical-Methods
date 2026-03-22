import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import BarycentricInterpolator
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), os.pardir))
from implementation.gaussian_interpolation import gaussian_interpolation


def plot_gaussian_interpolation(data_x, data_y, target_x):
    """
    Plot Gaussian central-difference interpolation alongside the scipy
    polynomial interpolant (BarycentricInterpolator) for verification.

    Parameters:
        data_x (numpy.ndarray): Equally-spaced x values.
        data_y (numpy.ndarray): Corresponding y values.
        target_x (numpy.ndarray): Dense x grid for the interpolated curve.
    """
    y_gauss = np.array(
        [gaussian_interpolation(data_x, data_y, x) for x in target_x]
    )
    y_scipy = BarycentricInterpolator(data_x, data_y)(target_x)

    plt.figure(figsize=(10, 6))
    plt.plot(data_x, data_y, "o", label="Data points", markersize=8)
    plt.plot(target_x, y_gauss, "b-", label="Gauss central-difference interp.")
    plt.plot(target_x, y_scipy, "r--", label="scipy BarycentricInterpolator", alpha=0.7)
    plt.title("Gaussian Interpolation vs. scipy Polynomial Interpolant")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.legend()
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    data_x = np.array([0, 1, 2, 3, 4], dtype=float)
    data_y = np.array([2, 3.5, 5, 5.8, 6], dtype=float)

    target_x = np.linspace(0, 4, 200)

    plot_gaussian_interpolation(data_x, data_y, target_x)
