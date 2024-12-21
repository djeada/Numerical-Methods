# test_trapezoid_rule.py
import pytest
import numpy as np
from ..implementation.trapezoid_rule import trapezoid_rule, trapezoid_rule_multidim


def test_trapezoid_rule_constant():
    f = lambda x: 5.0
    a, b, n = 0.0, 10.0, 100
    result = trapezoid_rule(f, a, b, n)
    expected = 5.0 * (b - a)
    assert np.isclose(result, expected, rtol=1e-3)


def test_trapezoid_rule_linear():
    f = lambda x: 2.0 * x + 3.0
    a, b, n = 0.0, 5.0, 100
    result = trapezoid_rule(f, a, b, n)
    expected = 2.0 * (b ** 2 - a ** 2) / 2 + 3.0 * (b - a)
    assert np.isclose(result, expected, rtol=1e-3)


def test_trapezoid_rule_quadratic():
    f = lambda x: x ** 2
    a, b, n = 0.0, 3.0, 100
    result = trapezoid_rule(f, a, b, n)
    expected = (b ** 3 - a ** 3) / 3
    assert np.isclose(result, expected, rtol=1e-3)


def test_trapezoid_rule_sin():
    f = np.sin
    a, b, n = 0.0, np.pi, 100
    result = trapezoid_rule(f, a, b, n)
    expected = 2.0
    assert np.isclose(result, expected, rtol=1e-3)


def test_trapezoid_rule_zero_intervals():
    f = lambda x: x
    a, b, n = 0.0, 1.0, 0
    with pytest.raises(ValueError):
        trapezoid_rule(f, a, b, n)


def test_trapezoid_rule_single_interval():
    f = lambda x: x
    a, b, n = 0.0, 2.0, 1
    result = trapezoid_rule(f, a, b, n)
    expected = 2.0 * 1.0
    assert np.isclose(result, expected, rtol=1e-3)


def test_trapezoid_rule_negative_bounds():
    f = lambda x: x ** 2
    a, b, n = -1.0, 1.0, 100
    result = trapezoid_rule(f, a, b, n)
    expected = 2.0 / 3
    assert np.isclose(result, expected, rtol=1e-3)


def test_trapezoid_rule_large_n():
    f = lambda x: np.exp(x)
    a, b, n = 0.0, 1.0, 100000
    result = trapezoid_rule(f, a, b, n)
    expected = np.exp(1) - 1
    assert np.isclose(result, expected, rtol=1e-3)


def test_trapezoid_rule_multidim_constant():
    f = lambda x: 4.0
    bounds = [(0.0, 1.0), (0.0, 1.0)]
    n = 100
    result = trapezoid_rule_multidim(f, bounds, n)
    expected = 4.0 * 1.0 * 1.0
    assert np.isclose(result, expected, rtol=1e-3)


def test_trapezoid_rule_multidim_linear():
    f = lambda x: x[:, 0] + x[:, 1]
    bounds = [(0.0, 2.0), (0.0, 3.0)]
    n = 1000
    result = trapezoid_rule_multidim(f, bounds, n)
    expected = 15
    assert np.isclose(result, expected, rtol=1e-4)


def test_trapezoid_rule_multidim_quadratic():
    f = lambda x: x[:, 0] ** 2 + x[:, 1] ** 2
    bounds = [(0.0, 1.0), (0.0, 1.0)]
    n = 1000
    result = trapezoid_rule_multidim(f, bounds, n)
    expected = 1 / 3 + 1 / 3
    assert np.isclose(result, expected, rtol=1e-4)


def test_trapezoid_rule_multidim_sin():
    f = lambda x: np.sin(x[:, 0]) * np.sin(x[:, 1])
    bounds = [(0.0, np.pi), (0.0, np.pi)]
    n = 1000
    result = trapezoid_rule_multidim(f, bounds, n)
    expected = 4.0
    assert np.isclose(result, expected, rtol=1e-3)


def test_trapezoid_rule_multidim_zero_intervals():
    f = lambda x: x[:, 0]
    bounds = [(0.0, 1.0), (0.0, 1.0)]
    n = 0
    with pytest.raises(ValueError):
        trapezoid_rule_multidim(f, bounds, n)


def test_trapezoid_rule_multidim_single_interval():
    f = lambda x: x[:, 0] * x[:, 1]
    bounds = [(0.0, 2.0), (0.0, 3.0)]
    n = 1
    result = trapezoid_rule_multidim(f, bounds, n)
    expected = (1.0 * 1.5) * 2.0 * 3.0
    assert np.isclose(result, expected, rtol=1e-3)


def test_trapezoid_rule_multidim_large_n():
    f = lambda x: np.exp(x[:, 0] + x[:, 1])
    bounds = [(0.0, 1.0), (0.0, 1.0)]
    n = 100
    result = trapezoid_rule_multidim(f, bounds, n)
    expected = (np.exp(2) - np.exp(0)) / 2
    assert np.isclose(result, expected, rtol=0.2)
