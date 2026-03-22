# lagrange_polynomial.py
import numpy as np


def lagrange_polynomial(x_data: np.ndarray, y_data: np.ndarray, point: float) -> float:
    """Evaluate the Lagrange interpolating polynomial at *point*.

    Given (n+1) data points the unique polynomial of degree ≤ n through
    all of them is:

        L(x) = Σᵢ yᵢ · Πⱼ≠ᵢ (x − xⱼ) / (xᵢ − xⱼ)

    Parameters
    ----------
    x_data : 1-D array of distinct x-coordinates.
    y_data : 1-D array of corresponding y-values (same length as *x_data*).
    point  : The x-value at which to evaluate the polynomial.

    Returns
    -------
    float – L(point).
    """
    if x_data.shape[0] != y_data.shape[0]:
        raise ValueError("X and Y vectors must have equal number of elements.")
    if x_data.shape[0] < 1:
        raise ValueError("X and Y vectors must contain at least one element.")
    if len(np.unique(x_data)) != x_data.shape[0]:
        raise ValueError("X data must contain unique values.")

    n = x_data.shape[0]
    P = 0.0
    for i in range(n):
        L_i = 1.0
        for j in range(n):
            if j != i:
                L_i *= (point - x_data[j]) / (x_data[i] - x_data[j])
        P += y_data[i] * L_i
    return P
