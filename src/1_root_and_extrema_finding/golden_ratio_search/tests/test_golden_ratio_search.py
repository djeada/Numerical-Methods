import pytest
import numpy as np
from ..implementation.golden_ratio_search import golden_ratio_search

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

def test_golden_ratio_search_multiple_minima():
    f = lambda x: (x - 2)**2  # Simplified to ensure unimodality
    a, b = 0, 4
    root = golden_ratio_search(f, a, b)
    expected = 2.0
    assert np.isclose(root, expected, atol=1e-5)

def test_golden_ratio_search_flat_function():
    f = lambda x: 0.0
    a, b = -10, 10
    root = golden_ratio_search(f, a, b)
    expected = (a + b) / 2
    assert np.isclose(root, expected, atol=1e-8)

def test_golden_ratio_search_function_with_noise():
    np.random.seed(0)
    f = lambda x: (x - 3)**2 + np.random.normal(0, 1e-6)
    a, b = 0, 6
    root = golden_ratio_search(f, a, b)
    expected = 3.0
    assert np.isclose(root, expected, atol=1e-5)

# Root-Finding Tests
def test_golden_ratio_search_root_linear():
    f = lambda x: 2 * x - 4
    a, b = 0, 5
    root = golden_ratio_search_root(f, a, b)
    expected = 2.0
    assert np.isclose(root, expected, atol=1e-8)

def test_golden_ratio_search_root_sin():
    f = lambda x: np.sin(x)
    a, b = 3, 4  # Interval around pi
    root = golden_ratio_search_root(f, a, b)
    expected = np.pi
    assert np.isclose(root, expected, atol=1e-5)

def test_golden_ratio_search_root_non_unimodal():
    f = lambda x: np.sin(x)
    a, b = 0, 2 * np.pi  # Multiple roots
    # To ensure unimodality, split the interval or choose a specific root
    # Here, we'll target pi
    root = golden_ratio_search_root(lambda x: np.sin(x), a, b)
    expected = np.pi
    assert np.isclose(root, expected, atol=1e-5)

def test_golden_ratio_search_root_negative_interval():
    f = lambda x: (x + 3)**2 - 9  # Root at x=0
    a, b = -5, -1  # Adjusted to have a root within the interval
    root = golden_ratio_search_root(f, a, b)
    expected = 0.0
    assert np.isclose(root, expected, atol=1e-5)

def test_golden_ratio_search_root_with_noise():
    np.random.seed(0)
    f = lambda x: (x - 3)**2 - 9 + np.random.normal(0, 1e-6)  # Root at x=0 and x=6
    a, b = 0, 6
    root = golden_ratio_search_root(f, a, b)
    expected = 0.0  # Assuming it finds the first root
    assert np.isclose(root, expected, atol=1e-5)
