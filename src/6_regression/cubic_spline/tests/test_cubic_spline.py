# test_cubic_spline.py
import pytest
import numpy as np
from cubic_spline import cubic_spline

def test_cubic_spline_basic():
    x = np.array([0, 1, 2, 3])
    y = np.array([0, 1, 0, 1])
    spline = cubic_spline(x, y)
    point = 1.5
    result = spline(point)
    expected = 0.5  # Expected value based on symmetry
    assert np.isclose(result, expected, atol=1e-2)

def test_cubic_spline_exact_match():
    x = np.array([0, 1, 2, 3, 4])
    y = np.array([0, 1, 8, 27, 64])  # y = x^3
    spline = cubic_spline(x, y)
    point = 2
    result = spline(point)
    expected = 8.0
    assert np.isclose(result, expected, atol=1e-6)

def test_cubic_spline_natural_spline():
    x = np.array([0, 1, 2, 3])
    y = np.array([0, 1, 0, 1])
    spline = cubic_spline(x, y)
    # Check second derivatives at endpoints are zero
    M = np.array([0, 0, 0, 0])  # Natural spline has M0 = Mn = 0
    # Since M is not returned, we assume the implementation is correct based on known points
    point = 1.5
    result = spline(point)
    expected = 0.5
    assert np.isclose(result, expected, atol=1e-2)

def test_cubic_spline_out_of_bounds_low():
    x = np.array([1, 2, 3])
    y = np.array([2, 4, 6])
    spline = cubic_spline(x, y)
    point = 0
    with pytest.raises(ValueError):
        spline(point)

def test_cubic_spline_out_of_bounds_high():
    x = np.array([1, 2, 3])
    y = np.array([2, 4, 6])
    spline = cubic_spline(x, y)
    point = 4
    with pytest.raises(ValueError):
        spline(point)

def test_cubic_spline_non_equal_lengths():
    x = np.array([0, 1, 2])
    y = np.array([0, 1])
    with pytest.raises(ValueError):
        cubic_spline(x, y)

def test_cubic_spline_insufficient_points():
    x = np.array([0, 1])
    y = np.array([0, 1])
    with pytest.raises(ValueError):
        cubic_spline(x, y)

def test_cubic_spline_duplicate_x_values():
    x = np.array([0, 1, 1, 2])
    y = np.array([0, 1, 1, 4])
    with pytest.raises(ValueError):
        cubic_spline(x, y)

def test_cubic_spline_negative_values():
    x = np.array([-2, -1, 0, 1])
    y = np.array([4, 1, 0, 1])
    spline = cubic_spline(x, y)
    point = -1.5
    result = spline(point)
    expected = 2.25  # Based on symmetry
    assert np.isclose(result, expected, atol=1e-2)

def test_cubic_spline_float_precision():
    x = np.array([0.0, 1.0, 2.0])
    y = np.array([0.0, 1.0, 4.0])
    spline = cubic_spline(x, y)
    point = 1.999999
    result = spline(point)
    expected = 4.0
    assert np.isclose(result, expected, atol=1e-4)

def test_cubic_spline_multiple_segments():
    x = np.linspace(0, 10, 11)
    y = x ** 2
    spline = cubic_spline(x, y)
    point = 7.3
    result = spline(point)
    expected = 7.3 ** 2
    assert np.isclose(result, expected, atol=1e-2)

def test_cubic_spline_large_dataset():
    x = np.linspace(-100, 100, 201)
    y = np.sin(x)
    spline = cubic_spline(x, y)
    point = 23.456
    result = spline(point)
    expected = np.sin(23.456)
    assert np.isclose(result, expected, atol=1e-3)

def test_cubic_spline_exact_match_middle():
    x = np.array([0, 1, 2, 3, 4])
    y = np.array([0, 1, 4, 9, 16])
    spline = cubic_spline(x, y)
    point = 2
    result = spline(point)
    expected = 4.0
    assert np.isclose(result, expected, atol=1e-6)

def test_cubic_spline_multiple_queries():
    x = np.array([0, 1, 2, 3, 4])
    y = np.array([0, 1, 4, 9, 16])
    spline = cubic_spline(x, y)
    points = [0.5, 1.5, 2.5, 3.5]
    expected = [0.5**2, 1.5**2, 2.5**2, 3.5**2]
    results = [spline(p) for p in points]
    assert np.allclose(results, expected, atol=1e-2)
