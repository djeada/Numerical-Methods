# test_monte_carlo_integral.py
import pytest
import numpy as np
from ..implementation.monte_carlo_integral import (
    monte_carlo_integral,
    monte_carlo_integral_multidim,
)


def test_monte_carlo_integral_constant():
    f = lambda x: 5.0
    a, b = 0.0, 10.0
    result = monte_carlo_integral(f, a, b, num_samples=100000)
    expected = 5.0 * (b - a)
    assert np.isclose(result, expected, rtol=1e-2)


def test_monte_carlo_integral_linear():
    f = lambda x: 2.0 * x + 3.0
    a, b = 0.0, 5.0
    result = monte_carlo_integral(f, a, b, num_samples=100000)
    expected = 2.0 * (b ** 2 - a ** 2) / 2 + 3.0 * (b - a)
    assert np.isclose(result, expected, rtol=1e-2)


def test_monte_carlo_integral_quadratic():
    f = lambda x: x ** 2
    a, b = 0.0, 3.0
    result = monte_carlo_integral(f, a, b, num_samples=1000000)
    expected = (b ** 3 - a ** 3) / 3
    assert np.isclose(result, expected, rtol=0.1)


def test_monte_carlo_integral_sin():
    f = np.sin
    a, b = 0.0, np.pi
    result = monte_carlo_integral(f, a, b, num_samples=1000000)
    expected = 2.0
    assert np.isclose(result, expected, rtol=0.1)


def test_monte_carlo_integral_multidim_constant():
    f = lambda x: 4.0
    bounds = ((0.0, 1.0), (0.0, 1.0))
    result = monte_carlo_integral_multidim(f, bounds, num_samples=100000)
    expected = 4.0 * 1.0 * 1.0
    assert np.isclose(result, expected, rtol=1e-2)


def test_monte_carlo_integral_multidim_linear():
    f = lambda x: x[0] + x[1]
    bounds = ((0.0, 2.0), (0.0, 3.0))
    result = monte_carlo_integral_multidim(f, bounds, num_samples=1000000)
    expected = 15
    assert np.isclose(result, expected, rtol=0.1)


def test_monte_carlo_integral_multidim_quadratic():
    f = lambda x: x[0] ** 2 + x[1] ** 2
    bounds = ((0.0, 1.0), (0.0, 1.0))
    result = monte_carlo_integral_multidim(f, bounds, num_samples=1000000)
    expected = 1 / 3 + 1 / 3
    assert np.isclose(result, expected, rtol=0.1)


def test_monte_carlo_integral_multidim_sin():
    f = lambda x: np.sin(x[0]) * np.sin(x[1])
    bounds = ((0.0, np.pi), (0.0, np.pi))
    result = monte_carlo_integral_multidim(f, bounds, num_samples=1000000)
    expected = 4.0
    assert np.isclose(result, expected, rtol=1e-2)


def test_monte_carlo_integral_zero_samples():
    f = lambda x: x
    a, b = 0.0, 1.0
    with pytest.raises(ValueError):
        monte_carlo_integral(f, a, b, num_samples=0)


def test_monte_carlo_integral_multidim_zero_samples():
    f = lambda x: x[0]
    bounds = ((0.0, 1.0),)
    with pytest.raises(ValueError):
        monte_carlo_integral_multidim(f, bounds, num_samples=0)
