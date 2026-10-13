# test_secant_method.py
import pytest
import numpy as np
from ..implementation.secant_method import secant_method


def test_secant_linear():
    f = lambda x: 2 * x - 4
    root = secant_method(f, 0, 5)
    expected = 2.0
    assert np.isclose(root, expected, atol=1e-8)


def test_secant_quadratic():
    f = lambda x: x**2 - 4
    root = secant_method(f, 1, 3)
    expected = 2.0
    assert np.isclose(root, expected, atol=1e-8)


def test_secant_sin():
    f = np.sin
    root = secant_method(f, 3, 4)
    expected = np.pi
    assert np.isclose(root, expected, atol=1e-8)


def test_secant_no_root():
    # exp(x) has no real root; the iterates just drift towards -infinity with
    # steps that never fall below tol, so the iteration cap is what stops it.
    f = lambda x: np.exp(x)
    with pytest.raises(ValueError, match="did not converge"):
        secant_method(f, 0, 1, max_iterations=50)


def test_secant_zero_denominator():
    # A constant function gives f(x1) == f(x0), so the secant line is horizontal.
    f = lambda x: 3.0
    with pytest.raises(ValueError, match="Denominator is zero"):
        secant_method(f, 0.0, 1.0)


def test_secant_multiple_roots():
    f = lambda x: x**3 - x
    root = secant_method(f, 0.5, 2.0)
    expected = 1.0
    assert np.isclose(root, expected, atol=1e-8)


def test_secant_tolerance():
    f = lambda x: x**3 - 6 * x**2 + 11 * x - 6
    root = secant_method(f, 2.5, 3.5, tol=1e-10)
    expected = 3.0
    assert np.isclose(root, expected, atol=1e-10)


def test_secant_max_iterations():
    f = lambda x: 1 - x
    # The first step lands exactly on the root, but the step size (99) is
    # still >= tol, so one iteration is not enough to *confirm* convergence.
    with pytest.raises(ValueError, match="did not converge"):
        secant_method(f, -100, 100, max_iterations=1)
    # The second iteration sees a zero step and returns the root.
    assert secant_method(f, -100, 100, max_iterations=2) == 1.0


def test_secant_exact_root():
    f = lambda x: x - 5
    root = secant_method(f, 0, 10)
    expected = 5.0
    assert np.isclose(root, expected, atol=1e-8)


def test_secant_close_to_root():
    f = lambda x: x**2 - 2
    root = secant_method(f, 1.4, 1.5)
    expected = np.sqrt(2)
    assert np.isclose(root, expected, atol=1e-8)


def test_secant_negative_root():
    f = lambda x: x + 3
    root = secant_method(f, 0, 1)
    expected = -3.0
    assert np.isclose(root, expected, atol=1e-8)


def test_secant_high_precision():
    f = lambda x: x**3 - 6 * x**2 + 11 * x - 6
    root = secant_method(f, 3.5, 4.0, tol=1e-12)
    expected = 3.0
    assert np.isclose(root, expected, atol=1e-12)


def test_secant_initial_guess():
    f = lambda x: x**2 - 1
    root = secant_method(f, 0.5, 2.0)
    expected = 1.0
    assert np.isclose(root, expected, atol=1e-8)


def test_secant_fractional_minimum():
    f = lambda x: x - 2.5
    root = secant_method(f, 1.0, 3.0)
    expected = 2.5
    assert np.isclose(root, expected, atol=1e-8)


def test_secant_function_with_noise():
    np.random.seed(0)
    # Noise of 1e-6 on a slope-1 function limits the root to about 1e-6.
    f = lambda x: x - 3 + np.random.normal(0, 1e-6)
    root = secant_method(f, 2.0, 4.0)
    expected = 3.0
    assert np.isclose(root, expected, atol=1e-5)


def test_secant_small_scale_function():
    # f differences are tiny (< 1e-8) but the problem is perfectly well posed
    f = lambda x: 1e-10 * (x - 2.0)
    root = secant_method(f, 0.0, 5.0)
    expected = 2.0
    assert np.isclose(root, expected, atol=1e-6)
