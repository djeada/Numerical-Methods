# cubic_spline.py
import numpy as np
from typing import Callable, Tuple
import bisect

def solve_tridiagonal_system(a: np.ndarray, b: np.ndarray, c: np.ndarray, d: np.ndarray) -> np.ndarray:
    n = len(d)
    # Forward sweep
    for i in range(1, n):
        w = a[i-1] / b[i-1]
        b[i] = b[i] - w * c[i-1]
        d[i] = d[i] - w * d[i-1]
    # Back substitution
    x = np.zeros(n)
    x[-1] = d[-1] / b[-1]
    for i in range(n-2, -1, -1):
        x[i] = (d[i] - c[i] * x[i+1]) / b[i]
    return x

def cubic_spline(
    x_data: np.ndarray,
    y_data: np.ndarray
) -> Callable[[float], float]:
    if x_data.shape[0] != y_data.shape[0]:
        raise ValueError("X and Y vectors must have equal number of elements.")
    if x_data.shape[0] < 3:
        raise ValueError("X and Y vectors must contain at least 3 elements.")
    if len(np.unique(x_data)) != x_data.shape[0]:
        raise ValueError("X data must contain unique values.")
    if not np.all(np.diff(x_data) > 0):
        raise ValueError("X data must be strictly increasing.")
    
    n = x_data.shape[0]
    h = np.diff(x_data)
    
    # Construct the tridiagonal system
    a = h[:-1]
    b = 2 * (h[:-1] + h[1:])
    c = h[1:]
    d = 6 * ((y_data[2:] - y_data[1:-1]) / h[1:] - (y_data[1:-1] - y_data[:-2]) / h[:-1])
    
    # Natural spline boundary conditions: second derivatives at endpoints are zero
    a = np.insert(a, 0, 0.0)
    c = np.append(c, 0.0)
    b = np.insert(b, 0, 1.0)
    b = np.append(b, 1.0)
    d = np.insert(d, 0, 0.0)
    d = np.append(d, 0.0)
    
    # Solve the tridiagonal system
    M = solve_tridiagonal_system(a, b, c, d)
    
    # Calculate coefficients for each spline segment
    coeffs = []
    for i in range(n - 1):
        A = M[i] / (6 * h[i])
        B = M[i+1] / (6 * h[i])
        C = (y_data[i] / h[i]) - (M[i] * h[i] / 6)
        D = (y_data[i+1] / h[i]) - (M[i+1] * h[i] / 6)
        coeffs.append((A, B, C, D))
    
    def spline(point: float) -> float:
        if point < x_data[0] or point > x_data[-1]:
            raise ValueError("Point is outside the interpolation range.")
        idx = bisect.bisect_right(x_data, point) - 1
        idx = min(max(idx, 0), n - 2)
        A, B, C, D = coeffs[idx]
        z = point - x_data[idx]
        return A * z**3 + B * z**2 + C * z + D
    
    return spline
