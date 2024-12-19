import pytest
import numpy as np
from implementation.golden_ratio_search import golden_ratio_search

def test_golden_ratio_search_linear():
    f = lambda x: 2 * x - 4
    a, b = 0, 5
    root = golden_ratio_search(f, a, b)
    expected = 2.0
    assert np.isclose(root, expected, atol=1e-8)


def test_golden_ratio_search_quadratic():
    f = lambda x: (x - 3)**2
    a, b = 0, 6
    root = golden_ratio_search(f, a, b)
    expected = 3.0
    assert np.isclose(root, expected, atol=1e-8)


def test_golden_ratio_search_sin():
    f = lambda x: np.sin(x)
    a, b = 3, 4
    root = golden_ratio_search(f, a, b)
    expected = 3.141592653589793
    assert np.isclose(root, expected, atol=1e-5)


def test_golden_ratio_search_multiple_minima():
    f = lambda x: (x - 1)**2 * (x - 3)**2
    a, b = 0, 4
    root = golden_ratio_search(f, a, b)
    expected = 2.0
    assert np.isclose(root, expected, atol=1e-5)


def test_golden_ratio_search_tolerance():
    f = lambda x: (x - 2)**2
    a, b = 0, 4
    root = golden_ratio_search(f, a, b, tol=1e-10)
    expected = 2.0
    assert np.isclose(root, expected, atol=1e-10)


def test_golden_ratio_search_max_iterations():
    f = lambda x: (x - 2)**2
    a, b = 0, 4
    with pytest.raises(ValueError):
        golden_ratio_search(f, a, b, max_iterations=0)


def test_golden_ratio_search_exact_minimum():
    f = lambda x: (x - 5)**2
    a, b = 3, 7
    root = golden_ratio_search(f, a, b)
    expected = 5.0
    assert np.isclose(root, expected, atol=1e-8)


def test_golden_ratio_search_close_to_minimum():
    f = lambda x: x**2 - 2 * x + 1
    a, b = 0, 3
    root = golden_ratio_search(f, a, b)
    expected = 1.0
    assert np.isclose(root, expected, atol=1e-8)


def test_golden_ratio_search_non_unimodal():
    f = lambda x: np.sin(x)
    a, b = 0, 2 * np.pi
    root = golden_ratio_search(f, a, b)
    expected = 3.141592653589793
    assert np.isclose(root, expected, atol=1e-5)


def test_golden_ratio_search_negative_interval():
    f = lambda x: (x + 3)**2
    a, b = -5, -1
    root = golden_ratio_search(f, a, b)
    expected = -3.0
    assert np.isclose(root, expected, atol=1e-8)


def test_golden_ratio_search_large_interval():
    f = lambda x: (x - 100)**2
    a, b = 90, 110
    root = golden_ratio_search(f, a, b)
    expected = 100.0
    assert np.isclose(root, expected, atol=1e-8)


def test_golden_ratio_search_flat_function():
    f = lambda x: 0.0
    a, b = -10, 10
    root = golden_ratio_search(f, a, b)
    expected = 0.0
    assert np.isclose(root, expected, atol=1e-8)


def test_golden_ratio_search_integer_bounds():
    f = lambda x: (x - 4)**2
    a, b = 2, 6
    root = golden_ratio_search(f, a, b)
    expected = 4.0
    assert np.isclose(root, expected, atol=1e-8)


def test_golden_ratio_search_fractional_minimum():
    f = lambda x: (x - 2.5)**2
    a, b = 0, 5
    root = golden_ratio_search(f, a, b)
    expected = 2.5
    assert np.isclose(root, expected, atol=1e-8)


def test_golden_ratio_search_function_with_noise():
    np.random.seed(0)
    f = lambda x: (x - 3)**2 + np.random.normal(0, 1e-6)
    a, b = 0, 6
    root = golden_ratio_search(f, a, b)
    expected = 3.0
    assert np.isclose(root, expected, atol=1e-5)
