import numpy as np

def solve_linear_system(A: np.ndarray, b: np.ndarray) -> np.ndarray:
    n = A.shape[0]
    augmented = np.hstack((A.astype(float), b.reshape(-1, 1).astype(float)))
    for i in range(n):
        pivot = np.argmax(np.abs(augmented[i:, i])) + i
        if np.isclose(augmented[pivot, i], 0.0):
            raise ValueError("Matrix is singular or nearly singular.")
        if pivot != i:
            augmented[[i, pivot]] = augmented[[pivot, i]]
        augmented[i] = augmented[i] / augmented[i, i]
        for j in range(i + 1, n):
            augmented[j] -= augmented[j, i] * augmented[i]
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = augmented[i, -1] - np.dot(augmented[i, i + 1:n], x[i + 1:n])
    return x

def polynomial_regression(
    x_data: np.ndarray,
    y_data: np.ndarray,
    degree: int
) -> np.ndarray:
    if x_data.shape[0] != y_data.shape[0]:
        raise ValueError("X and Y vectors must have equal number of elements.")
    if x_data.shape[0] < degree + 1:
        raise ValueError("Number of data points must be at least degree + 1.")
    if degree < 0:
        raise ValueError("Degree must be non-negative.")
    V = np.vander(x_data, N=degree + 1, increasing=True)
    AtA = V.T @ V
    AtY = V.T @ y_data
    coefficients = solve_linear_system(AtA, AtY)
    return coefficients
