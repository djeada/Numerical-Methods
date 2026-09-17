"""Global Gaussian radial basis function (RBF) interpolation.

This is distinct from Gauss's equally spaced central-difference interpolation
implemented in ``gaussian_interpolation.py``.
"""

import numpy as np


class GaussianRBFInterpolator:
    """Interpolate one-dimensional data with a Gaussian RBF kernel.

    The kernel is ``exp(-(epsilon * (x - center)) ** 2)``. The weights
    solve the dense interpolation system once and are reused for queries.

    Parameters
    ----------
    x_data, y_data : array-like, shape (n,)
        Finite data at distinct nodes; ordering and equal spacing are not
        required. At least one data point must be supplied.
    epsilon : float, optional
        Positive, finite inverse width of the Gaussian; defaults to 1.

    Notes
    -----
    Very small epsilon or closely spaced nodes can produce an ill-conditioned
    kernel matrix. This method solves the linear system directly rather than
    explicitly inverting the matrix; it does not regularize the data.
    """

    def __init__(self, x_data, y_data, epsilon=1.0):
        nodes = np.asarray(x_data, dtype=float)
        values = np.asarray(y_data, dtype=float)
        if nodes.ndim != 1 or values.ndim != 1:
            raise ValueError("X and Y data must be one-dimensional.")
        if nodes.size == 0:
            raise ValueError("At least one data point is required.")
        if nodes.size != values.size:
            raise ValueError("X and Y data must have equal lengths.")
        if not np.all(np.isfinite(nodes)) or not np.all(np.isfinite(values)):
            raise ValueError("X and Y data must contain only finite values.")
        if np.unique(nodes).size != nodes.size:
            raise ValueError("X data must contain distinct nodes.")

        shape = float(epsilon)
        if not np.isfinite(shape) or shape <= 0:
            raise ValueError("epsilon must be finite and positive.")

        self.nodes = nodes.copy()
        self.epsilon = shape
        differences = self.nodes[:, None] - self.nodes[None, :]
        kernel = np.exp(-np.square(self.epsilon * differences))
        self.weights = np.linalg.solve(kernel, values)

    def __call__(self, points):
        """Evaluate a scalar or an array of queries, preserving its shape."""
        queries = np.asarray(points, dtype=float)
        if not np.all(np.isfinite(queries)):
            raise ValueError("Query points must be finite.")
        basis = np.exp(-np.square(self.epsilon * (queries[..., None] - self.nodes)))
        result = basis @ self.weights
        return float(result) if queries.ndim == 0 else result


def gaussian_rbf_interpolation(x_data, y_data, point, epsilon=1.0):
    """Convenience interface for a single query; use the class for many queries."""
    return GaussianRBFInterpolator(x_data, y_data, epsilon)(point)
