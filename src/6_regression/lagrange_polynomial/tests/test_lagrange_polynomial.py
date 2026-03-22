# test_lagrange_polynomial.py
import pytest
import numpy as np
from scipy.interpolate import lagrange as scipy_lagrange
from ..implementation.lagrange_polynomial import lagrange_polynomial


def _scipy_ref(x, y, point):
    """Reference value from scipy.interpolate.lagrange."""
    return float(scipy_lagrange(x, y)(point))


def test_lagrange_polynomial_basic():
    x = np.array([0, 1, 2], dtype=float)
    y = np.array([1, 3, 2], dtype=float)
    result = lagrange_polynomial(x, y, 1.5)
    assert np.isclose(result, 2.875, atol=1e-10)


def test_lagrange_polynomial_single_point():
    x = np.array([2.0])
    y = np.array([5.0])
    assert np.isclose(lagrange_polynomial(x, y, 2), 5.0, atol=1e-10)


def test_lagrange_polynomial_exact_match():
    """Evaluating at a data point must return the data value (Kronecker δ)."""
    x = np.array([0, 1, 2, 3], dtype=float)
    y = np.array([0, 1, 8, 27], dtype=float)
    for xi, yi in zip(x, y):
        assert np.isclose(lagrange_polynomial(x, y, xi), yi, atol=1e-10)


def test_lagrange_polynomial_extrapolation():
    """Linear data y = 2x: extrapolation should remain exact."""
    x = np.array([1, 2, 3], dtype=float)
    y = np.array([2, 4, 6], dtype=float)
    assert np.isclose(lagrange_polynomial(x, y, 0), 0.0, atol=1e-10)
    assert np.isclose(lagrange_polynomial(x, y, 4), 8.0, atol=1e-10)


def test_lagrange_polynomial_non_equal_lengths():
    with pytest.raises(ValueError):
        lagrange_polynomial(np.array([0, 1, 2]), np.array([0, 1]), 1)


def test_lagrange_polynomial_insufficient_points():
    with pytest.raises(ValueError):
        lagrange_polynomial(np.array([]), np.array([]), 0)


def test_lagrange_polynomial_duplicate_x_values():
    with pytest.raises(ValueError):
        lagrange_polynomial(
            np.array([0, 1, 1, 2], dtype=float),
            np.array([0, 1, 1, 4], dtype=float),
            1,
        )


def test_lagrange_polynomial_negative_domain():
    """y = x² on {-2, -1, 0, 1} — polynomial fits exactly."""
    x = np.array([-2, -1, 0, 1], dtype=float)
    y = np.array([4, 1, 0, 1], dtype=float)
    assert np.isclose(lagrange_polynomial(x, y, -1.5), 2.25, atol=1e-10)


def test_lagrange_polynomial_float_precision():
    x = np.array([0.0, 1.0, 2.0])
    y = np.array([0.0, 1.0, 4.0])
    result = lagrange_polynomial(x, y, 1.999999)
    expected = _scipy_ref(x, y, 1.999999)
    assert np.isclose(result, expected, atol=1e-10)


def test_lagrange_polynomial_quadratic_exact():
    """11 points on y = x²: unique poly of deg ≤ 10 through them IS x²."""
    x = np.linspace(0, 10, 11)
    y = x**2
    result = lagrange_polynomial(x, y, 7.3)
    assert np.isclose(result, 7.3**2, atol=1e-8)


def test_lagrange_polynomial_large_dataset_sin():
    x = np.linspace(-100, 100, 201)
    y = np.sin(x)
    result = lagrange_polynomial(x, y, 23.456)
    assert np.isclose(result, np.sin(23.456), atol=1e-3)


def test_lagrange_polynomial_multiple_queries():
    """y = x² on {0..4}: check at half-integer points."""
    x = np.array([0, 1, 2, 3, 4], dtype=float)
    y = x**2
    points = [0.5, 1.5, 2.5, 3.5]
    expected = [p**2 for p in points]
    results = [lagrange_polynomial(x, y, p) for p in points]
    assert np.allclose(results, expected, atol=1e-10)


def test_lagrange_polynomial_notes_example():
    """Notes worked example: A(-1,1), B(2,3), C(3,5) → L(x) = x²/3 + x/3 + 1."""
    x = np.array([-1.0, 2.0, 3.0])
    y = np.array([1.0, 3.0, 5.0])
    # Data points exact
    for xi, yi in zip(x, y):
        assert np.isclose(lagrange_polynomial(x, y, xi), yi, atol=1e-10)
    # Query points from notes
    assert np.isclose(lagrange_polynomial(x, y, 0), 1.0, atol=1e-10)
    assert np.isclose(lagrange_polynomial(x, y, 1), 5 / 3, atol=1e-10)


def test_lagrange_polynomial_matches_scipy():
    """Compare our implementation against scipy on several datasets."""
    datasets = [
        (np.array([0, 1, 2], dtype=float), np.array([1, 3, 2], dtype=float)),
        (np.array([-1, 2, 3], dtype=float), np.array([1, 3, 5], dtype=float)),
        (np.array([-9, -5, -2.5, 4, 7], dtype=float),
         np.array([-2, 3, 0, 5, 11], dtype=float)),
    ]
    for x, y in datasets:
        for pt in np.linspace(x.min(), x.max(), 10):
            ours = lagrange_polynomial(x, y, float(pt))
            ref = _scipy_ref(x, y, float(pt))
            assert np.isclose(ours, ref, atol=1e-10), (
                f"Mismatch at {pt}: impl={ours}, scipy={ref}"
            )
