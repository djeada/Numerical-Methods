# test_thin_plate_spline_interpolation.py
import pytest
import numpy as np
from ..implementation.thin_plate_spline_interpolation import thin_plate_spline_interpolation


def test_tps_basic():
    x = np.array([0, 1, 2])
    y = np.array([0, 1, 0])
    z = np.array([0, 1, 0])
    point = (1, 0.5)
    result = thin_plate_spline_interpolation(x, y, z, point)
    expected = 0.75
    assert np.isclose(result, expected, atol=1e-2)


def test_tps_single_point():
    x = np.array([2])
    y = np.array([3])
    z = np.array([5])
    point = (2, 3)
    with pytest.raises(ValueError):
        thin_plate_spline_interpolation(x, y, z, point)


def test_tps_exact_match():
    x = np.array([0, 1, 2, 3])
    y = np.array([0, 1, 4, 9])
    z = np.array([0, 1, 4, 9])
    point = (2, 4)
    result = thin_plate_spline_interpolation(x, y, z, point)
    expected = 4.0
    assert np.isclose(result, expected, atol=1e-6)


def test_tps_out_of_bounds():
    x = np.array([1, 2, 3])
    y = np.array([1, 2, 3])
    z = np.array([2, 4, 6])
    point = (4, 4)
    result = thin_plate_spline_interpolation(x, y, z, point)
    expected = 6.0
    assert np.isclose(result, expected, atol=1e-2)


def test_tps_non_equal_lengths():
    x = np.array([0, 1, 2])
    y = np.array([0, 1])
    z = np.array([0, 1, 4])
    point = (1, 1)
    with pytest.raises(ValueError):
        thin_plate_spline_interpolation(x, y, z, point)


def test_tps_insufficient_points():
    x = np.array([0, 1])
    y = np.array([0, 1])
    z = np.array([0, 1])
    point = (0.5, 0.5)
    with pytest.raises(ValueError):
        thin_plate_spline_interpolation(x, y, z, point)


def test_tps_duplicate_points():
    x = np.array([0, 1, 1, 2])
    y = np.array([0, 1, 1, 2])
    z = np.array([0, 1, 1, 4])
    point = (1, 1)
    with pytest.raises(ValueError):
        thin_plate_spline_interpolation(x, y, z, point)


def test_tps_negative_values():
    x = np.array([-2, -1, 0, 1])
    y = np.array([-2, -1, 0, 1])
    z = np.array([4, 1, 0, 1])
    point = (-1.5, -1.5)
    result = thin_plate_spline_interpolation(x, y, z, point)
    expected = 2.25
    assert np.isclose(result, expected, atol=1e-2)


def test_tps_float_precision():
    x = np.array([0.0, 1.0, 2.0])
    y = np.array([0.0, 1.0, 2.0])
    z = np.array([0.0, 1.0, 4.0])
    point = (1.999999, 1.999999)
    result = thin_plate_spline_interpolation(x, y, z, point)
    expected = 4.0
    assert np.isclose(result, expected, atol=1e-4)


def test_tps_multiple_segments():
    x = np.linspace(0, 10, 11)
    y = np.linspace(0, 10, 11)
    z = x ** 2 + y ** 2
    point = (7.3, 7.3)
    result = thin_plate_spline_interpolation(x, y, z, point)
    expected = 7.3 ** 2 + 7.3 ** 2
    assert np.isclose(result, expected, atol=1e-2)


def test_tps_large_dataset():
    x = np.linspace(-100, 100, 201)
    y = np.linspace(-100, 100, 201)
    X, Y = np.meshgrid(x, y)
    Z = np.sin(X) + np.cos(Y)
    point = (23.456, -45.678)
    result = thin_plate_spline_interpolation(x, y, Z.flatten(), point)
    expected = np.sin(23.456) + np.cos(-45.678)
    assert np.isclose(result, expected, atol=1e-2)


def test_tps_exact_match_middle():
    x = np.array([0, 1, 2, 3, 4])
    y = np.array([0, 1, 4, 9, 16])
    z = np.array([0, 1, 4, 9, 16])
    point = (2, 4)
    result = thin_plate_spline_interpolation(x, y, z, point)
    expected = 4.0
    assert np.isclose(result, expected, atol=1e-6)


def test_tps_multiple_queries():
    x = np.array([0, 1, 2, 3, 4])
    y = np.array([0, 1, 4, 9, 16])
    z = np.array([0, 1, 4, 9, 16])
    points = [(0.5, 0.5), (1.5, 2.5), (2.5, 6.5), (3.5, 12.5)]
    expected = [0.5**2 + 0.5**2, 1.5**2 + 2.5**2, 2.5**2 + 6.5**2, 3.5**2 + 12.5**2]
    results = [thin_plate_spline_interpolation(x, y, z, p) for p in points]
    for res, exp in zip(results, expected):
        assert np.isclose(res, exp, atol=1e-2)
