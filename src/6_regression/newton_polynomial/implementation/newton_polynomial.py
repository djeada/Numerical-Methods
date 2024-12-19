# newton_polynomial.py
import numpy as np
from typing import Union

def newton_polynomial(
    x_data: np.ndarray,
    y_data: np.ndarray,
    point: float
) -> float:
    if x_data.shape[0] != y_data.shape[0]:
        raise ValueError("X and Y vectors must have equal number of elements.")
    if x_data.shape[0] < 2:
        raise ValueError("X and Y vectors must contain at least two elements.")
    if len(np.unique(x_data)) != x_data.shape[0]:
        raise ValueError("X data must contain unique values.")
    
    n = x_data.shape[0]
    divided_diff = np.copy(y_data).astype(float)
    
    for j in range(1, n):
        divided_diff[j:n] = (divided_diff[j:n] - divided_diff[j-1:n-1]) / (x_data[j:n] - x_data[0:n-j])
    
    result = divided_diff[0]
    product = 1.0
    for i in range(1, n):
        product *= (point - x_data[i-1])
        result += divided_diff[i] * product
    
    return result
