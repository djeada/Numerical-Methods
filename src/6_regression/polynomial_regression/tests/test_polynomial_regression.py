# test_polynomial_regression.py
import pytest
import numpy as np
from ..implementation.polynomial_regression import polynomial_regression

def test_polynomial_regression_linear():
    x = np.array([0, 1, 2, 3, 4])
    y = 2 * x + 1
    degree = 1
    coeffs = polynomial_regression(x, y, degree)
    expected = np.array([1, 2])
    assert np.allclose(coeffs, expected, atol=1e-6)

def test_polynomial_regression_quadratic():
    x = np.array([-2, -1, 0, 1, 2])
    y = x**2 + 2*x + 1
    degree = 2
    coeffs = polynomial_regression(x, y, degree)
    expected = np.array([1, 2, 1])
    assert np.allclose(coeffs, expected, atol=1e-6)

def test_polynomial_regression_cubic():
    x = np.array([-1, 0, 1, 2])
    y = -x**3 + 3*x**2 + x + 5
    degree = 3
    coeffs = polynomial_regression(x, y, degree)
    expected = np.array([5, 1, 3, -1])
    assert np.allclose(coeffs, expected, atol=1e-6)

def test_polynomial_regression_exact_match():
    x = np.array([1, 2, 3])
    y = np.array([2, 3, 5])
    degree = 1
    coeffs = polynomial_regression(x, y, degree)
    expected = np.array([1, 1])  # y = x +1
    assert np.allclose(coeffs, expected, atol=1e-6)

def test_polynomial_regression_overdetermined():
    x = np.array([0, 1, 2, 3, 4])
    y = np.array([1, 3, 7, 13, 21])
    degree = 2
    coeffs = polynomial_regression(x, y, degree)
    expected = np.array([1, 1, 1])  # y = 1 + x + x^2
    assert np.allclose(coeffs, expected, atol=1e-6)

def test_polynomial_regression_under_constrained():
    x = np.array([0, 1])
    y = np.array([1, 3])
    degree = 1
    coeffs = polynomial_regression(x, y, degree)
    expected = np.array([1, 2])  # y = 1 + 2x
    assert np.allclose(coeffs, expected, atol=1e-6)

def test_polynomial_regression_insufficient_points():
    x = np.array([0, 1])
    y = np.array([1, 3])
    degree = 2
    with pytest.raises(ValueError):
        polynomial_regression(x, y, degree)

def test_polynomial_regression_non_equal_lengths():
    x = np.array([0, 1, 2])
    y = np.array([1, 3])
    degree = 1
    with pytest.raises(ValueError):
        polynomial_regression(x, y, degree)

def test_polynomial_regression_negative_degree():
    x = np.array([0, 1, 2])
    y = np.array([1, 3, 5])
    degree = -1
    with pytest.raises(ValueError):
        polynomial_regression(x, y, degree)

def test_polynomial_regression_duplicate_x_values():
    x = np.array([1, 1, 2, 3])
    y = np.array([2, 2, 4, 6])
    degree = 1
    # Polynomial regression can handle duplicate x values if y values are consistent
    coeffs = polynomial_regression(x, y, degree)
    expected = np.array([0, 2])  # y = 2x
    assert np.allclose(coeffs, expected, atol=1e-6)

def test_polynomial_regression_noisy_data():
    np.random.seed(0)
    x = np.linspace(0, 10, 50)
    y = 3 + 2*x + x**2 + np.random.normal(0, 1, x.shape[0])
    degree = 2
    coeffs = polynomial_regression(x, y, degree)
    expected = np.array([3, 2, 1])  # True coefficients
    assert np.allclose(coeffs, expected, atol=0.2)

def test_polynomial_regression_high_degree():
    x = np.linspace(-1, 1, 10)
    y = 1 - 2*x + 3*x**2 - 4*x**3 + 5*x**4
    degree = 4
    coeffs = polynomial_regression(x, y, degree)
    expected = np.array([1, -2, 3, -4, 5])
    assert np.allclose(coeffs, expected, atol=1e-6)

def test_polynomial_regression_large_dataset():
    np.random.seed(1)
    x = np.linspace(0, 100, 1001)
    y = 5 + 3*x + 2*x**2 + np.random.normal(0, 10, x.shape[0])
    degree = 2
    coeffs = polynomial_regression(x, y, degree)
    expected = np.array([5, 3, 2])
    assert np.allclose(coeffs, expected, atol=0.5)

def test_polynomial_regression_single_variable():
    x = np.array([0, 1, 2, 3])
    y = np.array([1, 3, 7, 13])
    degree = 2
    coeffs = polynomial_regression(x, y, degree)
    expected = np.array([1, 1, 2])  # y = 1 + x + 2x^2
    assert np.allclose(coeffs, expected, atol=1e-6)

def test_polynomial_regression_exact_polynomial():
    def poly(x):
        return 4 - 3*x + 2*x**2 - x**3
    x = np.array([-2, -1, 0, 1, 2])
    y = poly(x)
    degree = 3
    coeffs = polynomial_regression(x, y, degree)
    expected = np.array([4, -3, 2, -1])
    assert np.allclose(coeffs, expected, atol=1e-6)

def test_polynomial_regression_extrapolation():
    x = np.array([0, 1, 2, 3])
    y = np.array([1, 3, 7, 13])
    degree = 2
    coeffs = polynomial_regression(x, y, degree)
    point = 4
    result = np.dot(coeffs, np.array([1, 4, 16]))
    expected = 1 + 4*3 + 16*2  # Based on y = 1 + 3x + 2x^2
    assert np.isclose(result, expected, atol=1e-2)

def test_polynomial_regression_integer_coefficients():
    x = np.array([1, 2, 3, 4])
    y = np.array([6, 11, 18, 27])
    degree = 2
    coeffs = polynomial_regression(x, y, degree)
    expected = np.array([5, 1, 2])  # y = 5 + x + 2x^2
    assert np.allclose(coeffs, expected, atol=1e-6)
