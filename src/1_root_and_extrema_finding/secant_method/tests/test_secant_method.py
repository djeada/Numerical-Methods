# test_secant_method.py
import pytest
import numpy as np
from ..implementation.secant_method import secant_method



def test_secant_linear():
    f = lambda x: 2 * x - 4
    root = secant_method(f, 0, 5)
    expected = 2.0
    assert np.isclose(root, expected, atol=1e-6)


def test_secant_quadratic():
    f = lambda x: x**2 - 4
    root = secant_method(f, 1, 3)
    expected = 2.0
    assert np.isclose(root, expected, atol=1e-6)


def test_secant_sin():
    f = np.sin
    root = secant_method(f, 3, 4)
    expected = np.pi
    assert np.isclose(root, expected, atol=1e-5)


def test_secant_no_root():
    f = lambda x: x**2 + 1
    with pytest.raises(ValueError):
        secant_method(f, 0, 1)


def test_secant_multiple_roots():
    f = lambda x: x**3 - x
    root = secant_method(f, 0.5, 2.0)
    expected = 1.0
    assert np.isclose(root, expected, atol=1e-6)


def test_secant_tolerance():
    f = lambda x: x**3 - 6 * x**2 + 11 * x - 6
    root = secant_method(f, 2.5, 3.5, tol=1e-10)
    expected = 3.0
    assert np.isclose(root, expected, atol=1e-10)


def test_secant_max_iterations():
    f = lambda x: 1 - x
    with pytest.raises(ValueError):
        secant_method(f, 0, 2, max_iterations=10)


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
    assert np.isclose(root, expected, atol=1e-6)


def test_secant_high_precision():
    f = lambda x: x**3 - 6 * x**2 + 11 * x - 6
    root = secant_method(f, 3.5, 4.0, tol=1e-12)
    expected = 3.0
    assert np.isclose(root, expected, atol=1e-12)


def test_secant_initial_guess():
    f = lambda x: x**2 - 1
    root = secant_method(f, 0.5, 2.0)
    expected = 1.0
    assert np.isclose(root, expected, atol=1e-6)


def test_secant_fractional_minimum():
    f = lambda x: (x - 2.5)**2
    root = secant_method(f, 1.0, 3.0)
    expected = 2.5
    assert np.isclose(root, expected, atol=1e-6)


def test_secant_function_with_noise():
    np.random.seed(0)
    f = lambda x: (x - 3)**2 + np.random.normal(0, 1e-6)
    root = secant_method(f, 2.0, 4.0)
    expected = 3.0
    assert np.isclose(root, expected, atol=1e-5)
