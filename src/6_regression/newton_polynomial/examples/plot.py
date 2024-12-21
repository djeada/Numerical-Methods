import numpy as np
import matplotlib.pyplot as plt


def divided_differences(x, y):
    """
    Compute the divided difference table for Newton's Interpolation.

    Parameters:
        x (array): Array of x data points.
        y (array): Array of y data points.

    Returns:
        table (array): Divided differences table.
    """
    n = len(x)
    table = np.zeros((n, n))
    table[:, 0] = y

    for j in range(1, n):
        for i in range(n - j):
            table[i][j] = (table[i + 1][j - 1] - table[i][j - 1]) / (x[i + j] - x[i])

    return table[0]


def newton_polynomial(x, coefficients, x_data):
    """
    Evaluate Newton's Interpolation Polynomial at given points.

    Parameters:
        x (float or array): Points to evaluate the polynomial.
        coefficients (array): Divided difference coefficients.
        x_data (array): x data points.

    Returns:
        result (float or array): Evaluated polynomial.
    """
    n = len(coefficients)
    result = coefficients[0]
    product_term = 1.0

    for i in range(1, n):
        product_term *= x - x_data[i - 1]
        result += coefficients[i] * product_term

    return result


def plot_newton_interpolation(x_data, y_data):
    """
    Plot Newton's Interpolation Polynomial alongside given data points.

    Parameters:
        x_data (array): x data points.
        y_data (array): y data points.
    """
    # Compute divided differences
    coefficients = divided_differences(x_data, y_data)

    # Generate fine x values for smooth curve
    x_fine = np.linspace(min(x_data), max(x_data), 500)
    y_fine = newton_polynomial(x_fine, coefficients, x_data)

    # Plot data points and interpolated polynomial
    plt.figure(figsize=(8, 6))
    plt.scatter(x_data, y_data, color="red", label="Data Points")
    plt.plot(x_fine, y_fine, label="Newton's Polynomial", color="blue")
    plt.title("Newton's Interpolation Polynomial")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.grid(True)
    plt.show()


# Example data points
x_data = np.array([1, 2, 3])
y_data = np.array([2, 3, 5])

# Plot Newton's Interpolation
plot_newton_interpolation(x_data, y_data)
