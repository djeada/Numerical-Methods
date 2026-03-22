# test_thin_plate_spline_interpolation.py
import pytest
import numpy as np
from scipy.interpolate import RBFInterpolator
from ..implementation.thin_plate_spline_interpolation import (
    thin_plate_spline_interpolation,
)


def _scipy_tps(x, y, z, point):
    """Reference TPS using scipy.interpolate.RBFInterpolator."""
    coords = np.column_stack([x, y])
    rbf = RBFInterpolator(coords, z, kernel="thin_plate_spline", degree=1)
    return float(rbf(np.array([point]))[0])


def test_tps_basic():
    """Non-collinear triangle."""
    x = np.array([0.0, 1.0, 2.0])
    y = np.array([0.0, 1.0, 0.0])
    z = np.array([0.0, 1.0, 0.0])
    pt = (1.0, 0.5)
    result = thin_plate_spline_interpolation(x, y, z, pt)
    expected = _scipy_tps(x, y, z, pt)
    assert np.isclose(result, expected, atol=1e-10)


def test_tps_single_point():
    x = np.array([2])
    y = np.array([3])
    z = np.array([5])
    with pytest.raises(ValueError):
        thin_plate_spline_interpolation(x, y, z, (2, 3))


def test_tps_exact_match():
    """Evaluating at a data point must return the data value."""
    x = np.array([0.0, 1.0, 0.0, 1.0])
    y = np.array([0.0, 0.0, 1.0, 1.0])
    z = np.array([0.0, 1.0, 4.0, 9.0])
    result = thin_plate_spline_interpolation(x, y, z, (1.0, 0.0))
    assert np.isclose(result, 1.0, atol=1e-8)


def test_tps_extrapolation():
    """TPS can extrapolate outside the convex hull of data points."""
    x = np.array([0.0, 1.0, 0.0, 1.0])
    y = np.array([0.0, 0.0, 1.0, 1.0])
    z = np.array([0.0, 1.0, 1.0, 2.0])  # planar: z = x + y
    pt = (2.0, 2.0)
    result = thin_plate_spline_interpolation(x, y, z, pt)
    assert np.isclose(result, 4.0, atol=1e-8)


def test_tps_non_equal_lengths():
    x = np.array([0, 1, 2])
    y = np.array([0, 1])
    z = np.array([0, 1, 4])
    with pytest.raises(ValueError):
        thin_plate_spline_interpolation(x, y, z, (1, 1))


def test_tps_insufficient_points():
    x = np.array([0.0, 1.0])
    y = np.array([0.0, 1.0])
    z = np.array([0.0, 1.0])
    with pytest.raises(ValueError):
        thin_plate_spline_interpolation(x, y, z, (0.5, 0.5))


def test_tps_duplicate_points():
    x = np.array([0.0, 1.0, 1.0, 2.0])
    y = np.array([0.0, 1.0, 1.0, 2.0])
    z = np.array([0.0, 1.0, 1.0, 4.0])
    with pytest.raises(ValueError):
        thin_plate_spline_interpolation(x, y, z, (1, 1))


def test_tps_negative_coordinates():
    """2-D scattered data with negative coordinates."""
    x = np.array([-2.0, -1.0, 0.0, 1.0, -1.0])
    y = np.array([0.0, -1.0, 0.0, 1.0, 1.0])
    z = x**2 + y**2
    pt = (-1.5, 0.5)
    result = thin_plate_spline_interpolation(x, y, z, pt)
    expected = _scipy_tps(x, y, z, pt)
    assert np.isclose(result, expected, atol=1e-8)


def test_tps_float_precision():
    """Evaluate very close to a data point."""
    x = np.array([0.0, 1.0, 0.0, 1.0])
    y = np.array([0.0, 0.0, 1.0, 1.0])
    z = np.array([0.0, 1.0, 1.0, 2.0])  # z = x + y
    pt = (0.999999, 0.999999)
    result = thin_plate_spline_interpolation(x, y, z, pt)
    assert np.isclose(result, 2.0, atol=1e-4)


def test_tps_grid_data():
    """Scattered grid points (non-collinear)."""
    gx = np.array([0.0, 2.0, 4.0, 6.0])
    gy = np.array([0.0, 3.0, 6.0])
    X, Y = np.meshgrid(gx, gy)
    x = X.ravel()
    y = Y.ravel()
    z = x + 2 * y  # planar data
    pt = (3.0, 4.5)
    result = thin_plate_spline_interpolation(x, y, z, pt)
    assert np.isclose(result, 3.0 + 2 * 4.5, atol=1e-6)


def test_tps_exact_match_all_corners():
    """Verify interpolation reproduces all data points exactly."""
    x = np.array([0.0, 1.0, 0.0, 1.0])
    y = np.array([0.0, 0.0, 1.0, 1.0])
    z = np.array([1.0, 0.0, 0.0, 1.0])
    for xi, yi, zi in zip(x, y, z):
        result = thin_plate_spline_interpolation(x, y, z, (xi, yi))
        assert np.isclose(result, zi, atol=1e-8), (
            f"Mismatch at ({xi},{yi}): got {result}, expected {zi}"
        )


def test_tps_notes_example_planar():
    """Notes Example 1: data lies on the plane z = x + y."""
    x = np.array([0.0, 1.0, 0.0, 1.0])
    y = np.array([0.0, 0.0, 1.0, 1.0])
    z = np.array([0.0, 1.0, 1.0, 2.0])
    for pt in [(0.5, 0.5), (0.25, 0.75), (0.3, 0.7)]:
        result = thin_plate_spline_interpolation(x, y, z, pt)
        assert np.isclose(result, pt[0] + pt[1], atol=1e-8), (
            f"Planar mismatch at {pt}: got {result}, expected {pt[0]+pt[1]}"
        )


def test_tps_notes_example_nonplanar():
    """Notes Example 2: non-planar saddle-like data."""
    x = np.array([0.0, 1.0, 0.0, 1.0])
    y = np.array([0.0, 0.0, 1.0, 1.0])
    z = np.array([1.0, 0.0, 0.0, 1.0])
    # Midpoint value = 0.5 by symmetry (verified in notes)
    assert np.isclose(
        thin_plate_spline_interpolation(x, y, z, (0.5, 0.5)), 0.5, atol=1e-8
    )
    # Other points verified against scipy
    for pt in [(0.25, 0.75), (0.3, 0.1)]:
        result = thin_plate_spline_interpolation(x, y, z, pt)
        expected = _scipy_tps(x, y, z, pt)
        assert np.isclose(result, expected, atol=1e-8)


def test_tps_matches_scipy_scattered():
    """Larger scattered dataset verified against scipy."""
    np.random.seed(42)
    N = 10
    x = np.random.rand(N) * 4
    y = np.random.rand(N) * 4
    z = np.sin(x) * np.cos(y)
    for pt in [(1.0, 1.0), (2.0, 3.0), (0.5, 2.5)]:
        result = thin_plate_spline_interpolation(x, y, z, pt)
        expected = _scipy_tps(x, y, z, pt)
        assert np.isclose(result, expected, atol=1e-8), (
            f"Mismatch at {pt}: got {result}, expected {expected}"
        )
