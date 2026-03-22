# test_cubic_spline.py
import pytest
import numpy as np
from scipy.interpolate import CubicSpline
from ..implementation.cubic_spline import cubic_spline


def _scipy_natural(x, y, point):
    """Reference value from scipy natural cubic spline."""
    return float(CubicSpline(x, y, bc_type="natural")(point))


def test_cubic_spline_basic():
    x = np.array([0, 1, 2, 3], dtype=float)
    y = np.array([0, 1, 0, 1], dtype=float)
    spline = cubic_spline(x, y)
    result = spline(1.5)
    expected = _scipy_natural(x, y, 1.5)
    assert np.isclose(result, expected, atol=1e-10)


def test_cubic_spline_exact_at_knots():
    """Spline must reproduce data values at every knot."""
    x = np.array([0, 1, 2, 3, 4], dtype=float)
    y = np.array([0, 1, 8, 27, 64], dtype=float)
    spline = cubic_spline(x, y)
    for xi, yi in zip(x, y):
        assert np.isclose(spline(xi), yi, atol=1e-10)


def test_cubic_spline_natural_boundary():
    """For linear data the natural spline reproduces the line exactly."""
    x = np.array([1, 2, 3], dtype=float)
    y = np.array([2, 4, 6], dtype=float)
    spline = cubic_spline(x, y)
    # All M_i should be 0 for linear data → spline = line
    for pt in [1.0, 1.25, 1.5, 2.0, 2.5, 3.0]:
        assert np.isclose(spline(pt), 2 * pt, atol=1e-10)


def test_cubic_spline_out_of_bounds_low():
    x = np.array([1, 2, 3], dtype=float)
    y = np.array([2, 4, 6], dtype=float)
    spline = cubic_spline(x, y)
    with pytest.raises(ValueError):
        spline(0)


def test_cubic_spline_out_of_bounds_high():
    x = np.array([1, 2, 3], dtype=float)
    y = np.array([2, 4, 6], dtype=float)
    spline = cubic_spline(x, y)
    with pytest.raises(ValueError):
        spline(4)


def test_cubic_spline_non_equal_lengths():
    with pytest.raises(ValueError):
        cubic_spline(np.array([0, 1, 2]), np.array([0, 1]))


def test_cubic_spline_insufficient_points():
    with pytest.raises(ValueError):
        cubic_spline(np.array([0, 1]), np.array([0, 1]))


def test_cubic_spline_duplicate_x_values():
    with pytest.raises(ValueError):
        cubic_spline(np.array([0, 1, 1, 2]), np.array([0, 1, 1, 4]))


def test_cubic_spline_negative_domain():
    """y = x² on {-2,-1,0,1} — compare against scipy."""
    x = np.array([-2, -1, 0, 1], dtype=float)
    y = x**2
    spline = cubic_spline(x, y)
    for pt in [-1.5, -0.5, 0.5]:
        result = spline(pt)
        expected = _scipy_natural(x, y, pt)
        assert np.isclose(result, expected, atol=1e-10)


def test_cubic_spline_float_precision():
    x = np.array([0.0, 1.0, 2.0])
    y = np.array([0.0, 1.0, 4.0])
    spline = cubic_spline(x, y)
    result = spline(1.999999)
    expected = _scipy_natural(x, y, 1.999999)
    assert np.isclose(result, expected, atol=1e-8)


def test_cubic_spline_quadratic_data():
    """11 points on y=x²: spline approximates well (not exact — cubic, not quadratic)."""
    x = np.linspace(0, 10, 11)
    y = x**2
    spline = cubic_spline(x, y)
    result = spline(7.3)
    expected = _scipy_natural(x, y, 7.3)
    assert np.isclose(result, expected, atol=1e-10)


def test_cubic_spline_sin_data():
    x = np.linspace(-100, 100, 201)
    y = np.sin(x)
    spline = cubic_spline(x, y)
    result = spline(23.456)
    expected = _scipy_natural(x, y, 23.456)
    assert np.isclose(result, expected, atol=1e-10)


def test_cubic_spline_multiple_queries():
    x = np.array([0, 1, 2, 3, 4], dtype=float)
    y = x**2
    spline = cubic_spline(x, y)
    for pt in [0.5, 1.5, 2.5, 3.5]:
        result = spline(pt)
        expected = _scipy_natural(x, y, pt)
        assert np.isclose(result, expected, atol=1e-10)


def test_cubic_spline_notes_example():
    """Notes worked example: (0,0), (1,0.5), (2,0) → S(0.5) = 0.34375."""
    x = np.array([0.0, 1.0, 2.0])
    y = np.array([0.0, 0.5, 0.0])
    spline = cubic_spline(x, y)
    # Exact values from notes
    assert np.isclose(spline(0.5), 0.34375, atol=1e-10)
    assert np.isclose(spline(0.0), 0.0, atol=1e-10)
    assert np.isclose(spline(1.0), 0.5, atol=1e-10)
    assert np.isclose(spline(2.0), 0.0, atol=1e-10)
    # Also matches scipy
    for pt in [0.25, 0.5, 0.75, 1.25, 1.5, 1.75]:
        assert np.isclose(spline(pt), _scipy_natural(x, y, pt), atol=1e-10)


def test_cubic_spline_matches_scipy_scattered():
    """Larger dataset verified against scipy."""
    np.random.seed(0)
    x = np.sort(np.random.uniform(0, 10, 15))
    y = np.sin(x) * np.cos(x / 2)
    spline = cubic_spline(x, y)
    ref = CubicSpline(x, y, bc_type="natural")
    pts = np.linspace(x[0], x[-1], 50)
    for pt in pts:
        assert np.isclose(spline(float(pt)), float(ref(pt)), atol=1e-10), (
            f"Mismatch at {pt}"
        )
