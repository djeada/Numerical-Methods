import numpy as np
from typing import Tuple


def _tps_kernel(r: float) -> float:
    """Thin plate spline radial basis function: φ(r) = r² ln(r).

    Defined as 0 when r = 0 (the limit of r² ln(r) as r → 0⁺).
    """
    if r == 0.0:
        return 0.0
    return r * r * np.log(r)


def thin_plate_spline_interpolation(
    x_data: np.ndarray,
    y_data: np.ndarray,
    z_data: np.ndarray,
    point: Tuple[float, float],
) -> float:
    """Thin Plate Spline interpolation for 2-D scattered data.

    Finds the surface f(x,y) = α₀ + α₁x + α₂y + Σ wᵢ φ(‖(x,y)−(xᵢ,yᵢ)‖)
    that passes through all data points while minimising bending energy,
    where φ(r) = r² ln(r) is the standard TPS kernel for 2-D.

    Parameters
    ----------
    x_data, y_data : 1-D arrays of spatial coordinates, one entry per data
        point (a flattened grid is passed as flattened coordinate arrays of
        the same length as z_data; there is no implicit meshgrid mode).
        The points must be distinct and must not all lie on one line.
    z_data : 1-D array of function values
    point  : (x, y) tuple at which to evaluate the interpolant

    Returns
    -------
    Interpolated value at *point*.

    Raises
    ------
    ValueError
        If the array lengths differ, fewer than three points are given,
        points are duplicated, or all points are collinear (the affine part
        of the surface is then undetermined and the system is singular).
    """
    if x_data.shape[0] != y_data.shape[0] or x_data.shape[0] != z_data.shape[0]:
        raise ValueError("X, Y, and Z vectors must have equal number of elements.")
    if x_data.shape[0] < 3:
        raise ValueError(
            "At least three points are required for thin plate spline interpolation."
        )
    if len(set(zip(x_data, y_data))) != x_data.shape[0]:
        raise ValueError("Duplicate (x, y) points detected.")

    x_data = x_data.astype(float)
    y_data = y_data.astype(float)
    z_data = z_data.astype(float)

    N = x_data.shape[0]

    # Collinear sites make [K P; P^T 0] singular. The rank of the centred
    # coordinates is scale-relative (SVD tolerance based on the largest
    # singular value), so it does not depend on the units of x and y.
    centred = np.column_stack((x_data - x_data.mean(), y_data - y_data.mean()))
    if np.linalg.matrix_rank(centred) < 2:
        raise ValueError(
            "Data points are collinear; thin plate spline interpolation "
            "requires points that do not all lie on one line."
        )

    # Kernel matrix K_{ij} = φ(‖pᵢ − pⱼ‖)
    K = np.zeros((N, N))
    for i in range(N):
        for j in range(N):
            if i != j:
                r = np.hypot(x_data[i] - x_data[j], y_data[i] - y_data[j])
                K[i, j] = _tps_kernel(r)

    # Polynomial matrix P = [1, x, y]
    P = np.vstack((np.ones(N), x_data, y_data)).T

    # Augmented system: [K P; P^T 0] [w; α] = [z; 0]
    system = np.vstack((np.hstack((K, P)), np.hstack((P.T, np.zeros((3, 3))))))
    b = np.hstack((z_data, np.zeros(3)))

    try:
        coefficients = np.linalg.solve(system, b)
    except np.linalg.LinAlgError as exc:
        raise ValueError(
            "Thin plate spline system is singular for the given data."
        ) from exc
    w = coefficients[:N]
    a = coefficients[N:]

    # Evaluate at query point
    x, y = point
    U = np.zeros(N)
    for i in range(N):
        r = np.hypot(x - x_data[i], y - y_data[i])
        U[i] = _tps_kernel(r)

    return a[0] + a[1] * x + a[2] * y + np.dot(w, U)
