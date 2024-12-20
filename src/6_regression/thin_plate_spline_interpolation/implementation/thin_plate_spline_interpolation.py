import numpy as np
from typing import Tuple

def thin_plate_spline_interpolation(
    x_data: np.ndarray,
    y_data: np.ndarray,
    z_data: np.ndarray,
    point: Tuple[float, float]
) -> float:
    if z_data.size == x_data.size * y_data.size and z_data.size > x_data.size:
        X, Y = np.meshgrid(x_data, y_data)
        x_data = X.ravel()
        y_data = Y.ravel()
        z_data = z_data.ravel()
    if x_data.shape[0] != y_data.shape[0] or x_data.shape[0] != z_data.shape[0]:
        raise ValueError("X, Y, and Z vectors must have equal number of elements.")
    if x_data.shape[0] < 3:
        raise ValueError("At least three points are required for thin plate spline interpolation.")
    if len(set(zip(x_data, y_data))) != x_data.shape[0]:
        raise ValueError("Duplicate (x, y) points detected.")
    N = x_data.shape[0]
    K = np.zeros((N, N))
    for i in range(N):
        for j in range(N):
            if i != j:
                r = np.hypot(x_data[i] - x_data[j], y_data[i] - y_data[j])
                if r > 0:
                    K[i, j] = (r**2)*np.log(r**2)
    P = np.vstack((np.ones(N), x_data, y_data)).T
    system = np.vstack((np.hstack((K, P)), np.hstack((P.T, np.zeros((3, 3))))))
    b = np.hstack((z_data, np.zeros(3)))
    coefficients = np.linalg.lstsq(system, b, rcond=None)[0]
    w = coefficients[:N]
    a = coefficients[N:]
    x, y = point
    U = np.zeros(N)
    for i in range(N):
        r = np.hypot(x - x_data[i], y - y_data[i])
        if r > 0:
            U[i] = (r**2)*np.log(r**2)
    return a[0] + a[1]*x + a[2]*y + np.dot(w, U)
