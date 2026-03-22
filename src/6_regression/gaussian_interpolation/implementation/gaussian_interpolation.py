# gaussian_interpolation.py
import numpy as np
from math import factorial


def _build_difference_table(y_data: np.ndarray) -> np.ndarray:
    """Build the forward difference table for equally-spaced data.

    Returns an (n+1) x (n+1) array where entry [i][k] holds Δ^k y_i.
    """
    n = len(y_data) - 1
    table = np.zeros((n + 1, n + 1))
    table[:, 0] = y_data
    for k in range(1, n + 1):
        for i in range(n + 1 - k):
            table[i][k] = table[i + 1][k - 1] - table[i][k - 1]
    return table


def _gauss_forward_coeff(t: float, k: int) -> float:
    """k-th coefficient of the Gauss forward formula.

    Product of (t - j) for j = -floor((k-1)/2) .. floor(k/2), divided by k!.
    """
    lo = -((k - 1) // 2)
    hi = k // 2
    coeff = 1.0
    for j in range(lo, hi + 1):
        coeff *= t - j
    return coeff / factorial(k)


def _gauss_backward_coeff(t: float, k: int) -> float:
    """k-th coefficient of the Gauss backward formula.

    Product of (t - j) for j = -floor(k/2) .. floor((k-1)/2), divided by k!.
    """
    lo = -(k // 2)
    hi = (k - 1) // 2
    coeff = 1.0
    for j in range(lo, hi + 1):
        coeff *= t - j
    return coeff / factorial(k)


def _gauss_forward(diff_table: np.ndarray, m: int, t: float, n: int) -> float:
    """Evaluate the Gauss forward central-difference formula.

    Zigzag path through the difference table:
        Δy_m, Δ²y_{m-1}, Δ³y_{m-1}, Δ⁴y_{m-2}, ...
    Base index for order k: m - floor(k/2).
    """
    result = diff_table[m][0]
    for k in range(1, n + 1):
        base = m - k // 2
        if base < 0 or base + k > n:
            break
        result += _gauss_forward_coeff(t, k) * diff_table[base][k]
    return result


def _gauss_backward(diff_table: np.ndarray, m: int, t: float, n: int) -> float:
    """Evaluate the Gauss backward central-difference formula.

    Zigzag path through the difference table:
        Δy_{m-1}, Δ²y_{m-1}, Δ³y_{m-2}, Δ⁴y_{m-2}, ...
    Base index for order k: m - ceil(k/2).
    """
    result = diff_table[m][0]
    for k in range(1, n + 1):
        base = m - (k + 1) // 2
        if base < 0 or base + k > n:
            break
        result += _gauss_backward_coeff(t, k) * diff_table[base][k]
    return result


def gaussian_interpolation(
    x_data: np.ndarray, y_data: np.ndarray, point: float
) -> float:
    """Gauss's central-difference interpolation for equally-spaced data.

    Uses the Gauss forward formula when the target lies to the right of
    the central node (t >= 0) and the backward formula when it lies to
    the left (t < 0).  Both recover the unique polynomial interpolant
    through all data points.

    Parameters
    ----------
    x_data : array of equally-spaced abscissae
    y_data : array of corresponding ordinates
    point  : the abscissa at which to interpolate

    Returns
    -------
    Interpolated value at *point*.
    """
    if x_data.shape[0] != y_data.shape[0]:
        raise ValueError("X and Y vectors must have equal number of elements.")
    if x_data.shape[0] < 2:
        raise ValueError("At least two points are required for interpolation.")
    if len(np.unique(x_data)) != x_data.shape[0]:
        raise ValueError("X data must contain unique values.")
    if point < np.min(x_data) or point > np.max(x_data):
        raise ValueError("Point is out of bounds.")

    n = len(x_data) - 1
    h = float(x_data[1] - x_data[0])

    diffs = np.diff(x_data.astype(float))
    if not np.allclose(diffs, h, rtol=1e-10):
        raise ValueError("X data must be equally spaced for Gaussian interpolation.")

    diff_table = _build_difference_table(y_data.astype(float))

    # Forward formula reaches full order with m = n//2.
    # Backward formula needs m = (n+1)//2 for odd n.
    m_fwd = n // 2
    t_fwd = (float(point) - float(x_data[m_fwd])) / h

    if t_fwd >= 0:
        return _gauss_forward(diff_table, m_fwd, t_fwd, n)
    else:
        m_bwd = (n + 1) // 2
        t_bwd = (float(point) - float(x_data[m_bwd])) / h
        return _gauss_backward(diff_table, m_bwd, t_bwd, n)
