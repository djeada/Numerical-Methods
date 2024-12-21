# test_lagrange_polynomial.py
import pytest
import numpy as np
from ..implementation.lagrange_polynomial import lagrange_polynomial


def test_lagrange_polynomial_basic():
    x = np.array([0, 1, 2])
    y = np.array([1, 3, 2])
    point = 1.5
    result = lagrange_polynomial(x, y, point)
    expected = 2.875
    assert np.isclose(result, expected, atol=1e-6)


def test_lagrange_polynomial_single_point():
    x = np.array([2])
    y = np.array([5])
    point = 2
    result = lagrange_polynomial(x, y, point)
    expected = 5.0
    assert np.isclose(result, expected, atol=1e-6)


def test_lagrange_polynomial_exact_match():
    x = np.array([0, 1, 2, 3])
    y = np.array([0, 1, 8, 27])
    point = 2
    result = lagrange_polynomial(x, y, point)
    expected = 8.0
    assert np.isclose(result, expected, atol=1e-6)


def test_lagrange_polynomial_out_of_bounds_low():
    x = np.array([1, 2, 3])
    y = np.array([2, 4, 6])
    point = 0
    result = lagrange_polynomial(x, y, point)
    expected = 0.0
    assert np.isclose(result, expected, atol=1e-6)


def test_lagrange_polynomial_out_of_bounds_high():
    x = np.array([1, 2, 3])
    y = np.array([2, 4, 6])
    point = 4
    result = lagrange_polynomial(x, y, point)
    expected = 8.0
    assert np.isclose(result, expected, atol=1e-6)


def test_lagrange_polynomial_non_equal_lengths():
    x = np.array([0, 1, 2])
    y = np.array([0, 1])
    point = 1
    with pytest.raises(ValueError):
        lagrange_polynomial(x, y, point)


def test_lagrange_polynomial_insufficient_points():
    x = np.array([])
    y = np.array([])
    point = 0
    with pytest.raises(ValueError):
        lagrange_polynomial(x, y, point)


def test_lagrange_polynomial_duplicate_x_values():
    x = np.array([0, 1, 1, 2])
    y = np.array([0, 1, 1, 4])
    point = 1
    with pytest.raises(ValueError):
        lagrange_polynomial(x, y, point)


def test_lagrange_polynomial_negative_values():
    x = np.array([-2, -1, 0, 1])
    y = np.array([4, 1, 0, 1])
    point = -1.5
    result = lagrange_polynomial(x, y, point)
    expected = 2.25
    assert np.isclose(result, expected, atol=1e-6)


def test_lagrange_polynomial_float_precision():
    x = np.array([0.0, 1.0, 2.0])
    y = np.array([0.0, 1.0, 4.0])
    point = 1.999999
    result = lagrange_polynomial(x, y, point)
    expected = 3.999996
    assert np.isclose(result, expected, atol=1e-5)


def test_lagrange_polynomial_multiple_segments():
    x = np.linspace(0, 10, 11)
    y = x ** 2
    point = 7.3
    result = lagrange_polynomial(x, y, point)
    expected = 7 ** 2 + (8 ** 2 - 7 ** 2) * 0.3
    assert np.isclose(result, expected, atol=0.3)


def test_lagrange_polynomial_large_dataset():
    x = np.linspace(-100, 100, 201)
    y = np.sin(x)
    point = 23.456
    result = lagrange_polynomial(x, y, point)
    expected = np.sin(23.456)
    assert np.isclose(result, expected, atol=1e-3)


def test_lagrange_polynomial_exact_match_middle():
    x = np.array([0, 1, 2, 3, 4])
    y = np.array([0, 1, 4, 9, 16])
    point = 2
    result = lagrange_polynomial(x, y, point)
    expected = 4
    assert np.isclose(result, expected, atol=1e-6)


def test_lagrange_polynomial_multiple_queries():
    x = np.array([0, 1, 2, 3, 4])
    y = np.array([0, 1, 4, 9, 16])
    points = [0.5, 1.5, 2.5, 3.5]
    expected = [0.25, 2.25, 6.25, 12.25]
    results = [lagrange_polynomial(x, y, p) for p in points]
    assert np.allclose(results, expected, atol=1e-6)
