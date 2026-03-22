# test_gaussian_interpolation.py
import pytest
import numpy as np
from scipy.interpolate import BarycentricInterpolator
from ..implementation.gaussian_interpolation import gaussian_interpolation


def test_gaussian_interpolation_basic():
    x = np.array([0, 1, 2], dtype=float)
    y = np.array([1, 3, 2], dtype=float)
    result = gaussian_interpolation(x, y, 1.5)
    expected = BarycentricInterpolator(x, y)(1.5)
    assert np.isclose(result, expected, atol=1e-10)


def test_gaussian_interpolation_single_point():
    x = np.array([2])
    y = np.array([5])
    with pytest.raises(ValueError):
        gaussian_interpolation(x, y, 2)


def test_gaussian_interpolation_exact_match():
    x = np.array([0, 1, 2, 3], dtype=float)
    y = np.array([0, 1, 8, 27], dtype=float)
    result = gaussian_interpolation(x, y, 2)
    assert np.isclose(result, 8.0, atol=1e-10)


def test_gaussian_interpolation_out_of_bounds_low():
    x = np.array([1, 2, 3], dtype=float)
    y = np.array([2, 4, 6], dtype=float)
    with pytest.raises(ValueError):
        gaussian_interpolation(x, y, 0)


def test_gaussian_interpolation_out_of_bounds_high():
    x = np.array([1, 2, 3], dtype=float)
    y = np.array([2, 4, 6], dtype=float)
    with pytest.raises(ValueError):
        gaussian_interpolation(x, y, 4)


def test_gaussian_interpolation_non_equal_lengths():
    x = np.array([0, 1, 2])
    y = np.array([0, 1])
    with pytest.raises(ValueError):
        gaussian_interpolation(x, y, 1)


def test_gaussian_interpolation_insufficient_points():
    x = np.array([])
    y = np.array([])
    with pytest.raises(ValueError):
        gaussian_interpolation(x, y, 0)


def test_gaussian_interpolation_duplicate_x_values():
    x = np.array([0, 1, 1, 2])
    y = np.array([0, 1, 1, 4])
    with pytest.raises(ValueError):
        gaussian_interpolation(x, y, 1)


def test_gaussian_interpolation_negative_values():
    """y = x² data; polynomial interpolant reproduces x² exactly."""
    x = np.array([-2, -1, 0, 1], dtype=float)
    y = np.array([4, 1, 0, 1], dtype=float)
    result = gaussian_interpolation(x, y, -1.5)
    assert np.isclose(result, 2.25, atol=1e-10)


def test_gaussian_interpolation_float_precision():
    x = np.array([0.0, 1.0, 2.0])
    y = np.array([0.0, 1.0, 4.0])
    result = gaussian_interpolation(x, y, 1.999999)
    assert np.isclose(result, 1.999999**2, atol=1e-8)


def test_gaussian_interpolation_multiple_segments():
    """y = x² through 11 points; polynomial interpolant is exact."""
    x = np.linspace(0, 10, 11)
    y = x**2
    result = gaussian_interpolation(x, y, 7.3)
    assert np.isclose(result, 53.29, atol=1e-6)


def test_gaussian_interpolation_exact_match_middle():
    x = np.array([0, 1, 2, 3, 4], dtype=float)
    y = np.array([0, 1, 4, 9, 16], dtype=float)
    result = gaussian_interpolation(x, y, 2)
    assert np.isclose(result, 4.0, atol=1e-10)


def test_gaussian_interpolation_multiple_queries():
    """y = x² through 5 points; check at midpoints."""
    x = np.array([0, 1, 2, 3, 4], dtype=float)
    y = np.array([0, 1, 4, 9, 16], dtype=float)
    points = [0.5, 1.5, 2.5, 3.5]
    expected = [0.25, 2.25, 6.25, 12.25]
    results = [gaussian_interpolation(x, y, p) for p in points]
    assert np.allclose(results, expected, atol=1e-10)


def test_gaussian_interpolation_matches_scipy():
    """Notes example: the result must match scipy's polynomial interpolant."""
    x = np.array([0, 1, 2, 3, 4], dtype=float)
    y = np.array([2.0, 3.5, 5.0, 5.8, 6.0])
    for pt in [0.5, 1.5, 2.5, 3.5]:
        result = gaussian_interpolation(x, y, pt)
        expected = float(BarycentricInterpolator(x, y)(pt))
        assert np.isclose(result, expected, atol=1e-10), (
            f"Mismatch at x={pt}: got {result}, expected {expected}"
        )


def test_gaussian_interpolation_non_equally_spaced():
    """Non-equally-spaced x data must be rejected."""
    x = np.array([0.0, 1.0, 3.0, 6.0])
    y = np.array([0.0, 1.0, 9.0, 36.0])
    with pytest.raises(ValueError, match="equally spaced"):
        gaussian_interpolation(x, y, 2.0)


def test_gaussian_interpolation_sin_vs_scipy():
    """sin(x) interpolation through 6 equally-spaced points."""
    x = np.linspace(0, 5, 6)
    y = np.sin(x)
    ref = BarycentricInterpolator(x, y)
    for pt in [0.3, 1.7, 2.5, 4.2]:
        result = gaussian_interpolation(x, y, pt)
        assert np.isclose(result, float(ref(pt)), atol=1e-10)
