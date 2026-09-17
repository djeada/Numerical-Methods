"""Plot a Gaussian RBF interpolant for several shape parameters.

Run this file directly to compare curves and their interpolation nodes.
Gauss's central-difference polynomial example remains in ``plot.py``.
"""

from pathlib import Path
import sys

import matplotlib.pyplot as plt
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from implementation.gaussian_rbf import GaussianRBFInterpolator


def main():
    nodes = np.array([0.0, 1.0, 2.0])
    values = np.array([0.0, 0.5, 0.0])
    queries = np.linspace(-0.5, 2.5, 400)

    for epsilon in (0.5, 1.0, 2.0):
        interpolator = GaussianRBFInterpolator(nodes, values, epsilon)
        plt.plot(queries, interpolator(queries), label=f"epsilon = {epsilon:g}")

    plt.plot(nodes, values, "ko", label="Data nodes")
    plt.xlabel("x")
    plt.ylabel("s(x)")
    plt.title("Gaussian radial basis function interpolation")
    plt.grid(True)
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()
