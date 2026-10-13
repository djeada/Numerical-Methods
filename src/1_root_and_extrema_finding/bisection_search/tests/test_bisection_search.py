# test_bisection_search.py
import pytest
import numpy as np
from ..implementation.bisection_search import bisection_search


def test_bisection_linear():
    f = lambda x: 2 * x - 4
    a, b = 0, 5
    root = bisection_search(f, a, b)
    expected = 2.0
    assert np.isclose(root, expected, atol=1e-8, rtol=0)


def test_bisection_quadratic():
    f = lambda x: x**2 - 4
    a, b = 0, 3
    root = bisection_search(f, a, b)
    expected = 2.0
    assert np.isclose(root, expected, atol=1e-8, rtol=0)


def test_bisection_sin():
    f = np.sin
    a, b = 3, 4
    root = bisection_search(f, a, b)
    expected = np.pi
    assert np.isclose(root, expected, atol=1e-8, rtol=0)


def test_bisection_no_root():
    f = lambda x: x**2 + 1
    a, b = 0, 1
    with pytest.raises(ValueError, match="opposite signs"):
        bisection_search(f, a, b)


def test_bisection_multiple_roots():
    # x^3 - x has roots -1, 0, 1. Each bracket isolates exactly one of them and
    # neither endpoint is a root, so the bisection loop really has to run.
    f = lambda x: x**3 - x
    assert np.isclose(bisection_search(f, 0.5, 2), 1.0, atol=1e-8, rtol=0)
    assert np.isclose(bisection_search(f, -2, -0.5), -1.0, atol=1e-8, rtol=0)
    assert np.isclose(bisection_search(f, -0.5, 0.25), 0.0, atol=1e-8, rtol=0)


def test_bisection_root_at_endpoint_returns_endpoint():
    f = lambda x: x**3 - x
    assert bisection_search(f, 0, 2) == 0


def test_bisection_tolerance():
    f = lambda x: x**3 - 6 * x**2 + 11 * x - 6
    a, b = 2.5, 4
    root = bisection_search(f, a, b, tol=1e-10)
    expected = 3.0
    assert np.isclose(root, expected, atol=1e-10, rtol=0)


def test_bisection_max_iterations():
    f = lambda x: x - 1
    a, b = 0, 2
    with pytest.raises(ValueError, match="did not converge"):
        bisection_search(f, a, b, max_iterations=0)


def test_bisection_convergence():
    f = lambda x: x**3 - 6 * x**2 + 11 * x - 6
    a, b = 2.5, 4
    root = bisection_search(f, a, b)
    expected = 3.0
    assert np.isclose(root, expected, atol=1e-8, rtol=0)


def test_bisection_exact_root():
    f = lambda x: x - 2
    a, b = 2, 3
    root = bisection_search(f, a, b)
    expected = 2.0
    assert np.isclose(root, expected, atol=1e-8, rtol=0)


def test_bisection_close_to_root():
    f = lambda x: x**2 - 2
    a, b = 1, 2
    root = bisection_search(f, a, b)
    expected = np.sqrt(2)
    assert np.isclose(root, expected, atol=1e-8)


def test_bisection_negative_interval():
    f = lambda x: x + 2
    a, b = -5, 0
    root = bisection_search(f, a, b)
    expected = -2.0
    assert np.isclose(root, expected, atol=1e-8, rtol=0)


def test_bisection_cubic():
    f = lambda x: x**3 - 2
    a, b = 1, 2
    root = bisection_search(f, a, b)
    expected = 2 ** (1.0 / 3)
    assert np.isclose(root, expected, atol=1e-8, rtol=0)


def test_bisection_exponential():
    f = lambda x: np.exp(x) - 2
    a, b = 0, 1
    root = bisection_search(f, a, b)
    expected = np.log(2)
    assert np.isclose(root, expected, atol=1e-8, rtol=0)


def test_bisection_left_endpoint_root():
    f = lambda x: x
    a, b = 0, 5
    root = bisection_search(f, a, b)
    expected = 0.0
    assert np.isclose(root, expected, atol=1e-8, rtol=0)


def test_bisection_tight_tolerance():
    f = lambda x: x**2 - 3
    a, b = 1, 2
    root = bisection_search(f, a, b, tol=1e-12)
    expected = np.sqrt(3)
    assert np.isclose(root, expected, atol=1e-12, rtol=0)
