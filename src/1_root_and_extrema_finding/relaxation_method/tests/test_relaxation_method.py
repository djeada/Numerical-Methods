# test_relaxation_method.py
import pytest
import numpy as np
from ..implementation.relaxation_method import relaxation_method


def test_relaxation_constant():
    f = lambda x: 5.0
    initial_guess = 0.0
    root = relaxation_method(f, initial_guess)
    expected = 5.0
    assert np.isclose(root, expected, atol=1e-6)


def test_relaxation_linear():
    f = lambda x: 2.0 * x + 1.0
    initial_guess = 0.0
    root = relaxation_method(f, initial_guess)
    # Fixed point: x = 2x + 1 => x = -1
    expected = -1.0
    assert np.isclose(root, expected, atol=1e-6)


def test_relaxation_quadratic():
    f = lambda x: np.sqrt(4 + x)
    initial_guess = 0.0
    root = relaxation_method(f, initial_guess)
    # Fixed point: x = sqrt(4 + x) => x ≈ 2.5615528128
    expected = 2.5615528128
    assert np.isclose(root, expected, atol=1e-6)


def test_relaxation_sin():
    f = lambda x: np.sin(x)
    initial_guess = 2.0
    root = relaxation_method(f, initial_guess, tol=1e-10)
    # Fixed point near 0
    expected = 0.0
    assert np.isclose(root, expected, atol=1e-2)


def test_relaxation_non_convergent():
    f = lambda x: 1 - x
    initial_guess = 1000.0
    root = relaxation_method(f, initial_guess, tol=1e-6, max_iterations=100)
    # Should oscillate between 1 and 0, not converge to a fixed point
    # Since the method returns after max_iterations, we check it's not close to any fixed point
    assert not np.isclose(root, 0.0, atol=1e-6)
    assert not np.isclose(root, 1.0, atol=1e-6)


def test_relaxation_exact_fixed_point():
    f = lambda x: 3.0
    initial_guess = 10.0
    root = relaxation_method(f, initial_guess)
    expected = 3.0
    assert np.isclose(root, expected, atol=1e-6)


def test_relaxation_close_to_fixed_point():
    f = lambda x: x - 0.1 * (x ** 3 - x - 2)
    initial_guess = 1.5
    root = relaxation_method(f, initial_guess, omega=0.5, tol=1e-10)
    expected = 1.5213797068045676  # Approximate root of x^3 - x - 2 = 0
    assert np.isclose(root, expected, atol=1e-6)


def test_relaxation_negative_fixed_point():
    f = lambda x: -2.0
    initial_guess = 1.0
    root = relaxation_method(f, initial_guess)
    expected = -2.0
    assert np.isclose(root, expected, atol=1e-6)


def test_relaxation_high_precision():
    f = lambda x: x / 2 + 1
    initial_guess = 0.0
    root = relaxation_method(f, initial_guess, tol=1e-12)
    # Fixed point: x = x/2 + 1 => x = 2
    expected = 2.0
    assert np.isclose(root, expected, atol=1e-12)


def test_relaxation_initial_guess():
    f = lambda x: x ** 2 - 2
    initial_guess = 1.5
    root = relaxation_method(f, initial_guess)
    # Fixed points: x = 2 and x = -1
    assert not np.isclose(root, 0.0, atol=1e-6)
    assert np.isclose(root, 2.0, atol=1e-6) or np.isclose(root, -1.0, atol=1e-6)


def test_relaxation_fractional_fixed_point():
    f = lambda x: 1.5
    initial_guess = 0.0
    root = relaxation_method(f, initial_guess)
    expected = 1.5
    assert np.isclose(root, expected, atol=1e-6)


def test_relaxation_large_number_iterations():
    f = lambda x: x
    initial_guess = 100.0
    root = relaxation_method(f, initial_guess, tol=1e-12, max_iterations=100000)
    expected = 100.0
    assert np.isclose(root, expected, atol=1e-12)


def test_relaxation_omega_adjustment():
    f = lambda x: 0.5 * x + 1
    initial_guess = 0.0
    root = relaxation_method(f, initial_guess)
    # Fixed point: x = 0.5x + 1 => x = 2
    expected = 2.0
    assert np.isclose(root, expected, atol=1e-6)
