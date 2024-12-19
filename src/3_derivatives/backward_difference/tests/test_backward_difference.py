# test_backward_difference.py
import pytest
import numpy as np
from ..implementation.backward_difference import backward_difference, backward_difference_gradient

def test_backward_difference_constant():
    f = lambda x: 5.0
    x = 2.0
    result = backward_difference(f, x)
    expected = 0.0
    assert np.isclose(result, expected, rtol=1e-6)

def test_backward_difference_linear():
    f = lambda x: 2.0 * x + 3.0
    x = 1.0
    result = backward_difference(f, x)
    expected = 2.0
    assert np.isclose(result, expected, rtol=1e-6)

def test_backward_difference_quadratic():
    f = lambda x: x**2
    x = 3.0
    result = backward_difference(f, x)
    expected = 6.0
    assert np.isclose(result, expected, rtol=1e-6)

def test_backward_difference_sin():
    f = np.sin
    x = np.pi / 4
    result = backward_difference(f, x)
    expected = np.cos(x)
    assert np.isclose(result, expected, rtol=1e-6)

def test_backward_difference_h_small():
    f = lambda x: x**3
    x = 2.0
    h = 1e-8
    result = backward_difference(f, x, h)
    expected = 12.0
    assert np.isclose(result, expected, rtol=1e-4)

def test_backward_difference_gradient_constant():
    f = lambda x: 5.0
    x = np.array([1.0, 2.0, 3.0])
    result = backward_difference_gradient(f, x)
    expected = np.array([0.0, 0.0, 0.0])
    assert np.allclose(result, expected, rtol=1e-6)

def test_backward_difference_gradient_linear():
    f = lambda x: 2.0 * x[0] + 3.0 * x[1]
    x = np.array([1.0, 2.0])
    result = backward_difference_gradient(f, x)
    expected = np.array([2.0, 3.0])
    assert np.allclose(result, expected, rtol=1e-6)

def test_backward_difference_gradient_quadratic():
    def f(x):
        return x[0]**2 + 3 * x[1]**2

    x = np.array([2.0, 3.0])
    result = backward_difference_gradient(f, x)
    expected = np.array([4.0, 18.0])
    assert np.allclose(result, expected, rtol=1e-6)

def test_backward_difference_gradient_sin():
    def f(x):
        return np.sin(x[0]) + np.cos(x[1])

    x = np.array([np.pi / 3, np.pi / 6])
    result = backward_difference_gradient(f, x)
    expected = np.array([np.cos(x[0]), -np.sin(x[1])])
    assert np.allclose(result, expected, rtol=1e-6)

def test_backward_difference_gradient_mixed():
    def f(x):
        return x[0] * x[1] + x[2]**3

    x = np.array([1.0, 2.0, 3.0])
    result = backward_difference_gradient(f, x)
    expected = np.array([2.0, 1.0, 27.0])
    assert np.allclose(result, expected, rtol=1e-6)

def test_backward_difference_gradient_high_dimensions():
    def f(x):
        return np.sum(x**2)

    x = np.random.rand(10)
    result = backward_difference_gradient(f, x)
    expected = 2 * x
    assert np.allclose(result, expected, rtol=1e-6)

def test_backward_difference_gradient_zero_vector():
    def f(x):
        return np.dot(x, x)

    x = np.zeros(5)
    result = backward_difference_gradient(f, x)
    expected = np.zeros(5)
    assert np.allclose(result, expected, rtol=1e-6)

def test_backward_difference_gradient_single_element():
    def f(x):
        return x[0]**2

    x = np.array([3.0])
    result = backward_difference_gradient(f, x)
    expected = np.array([6.0])
    assert np.allclose(result, expected, rtol=1e-6)

def test_backward_difference_gradient_non_differentiable():
    def f(x):
        return np.abs(x[0])

    x = np.array([0.0])
    result = backward_difference_gradient(f, x, h=1e-5)
    expected = 0.0
    assert np.isclose(result, expected, rtol=1e-3)

def test_backward_difference_gradient_complex_function():
    def f(x):
        return np.exp(x[0] * x[1])

    x = np.array([1.0, 2.0])
    result = backward_difference_gradient(f, x)
    expected = np.array([2.0 * np.exp(2.0), 1.0 * np.exp(2.0)])
    assert np.allclose(result, expected, rtol=1e-6)

def test_backward_difference_gradient_negative_values():
    def f(x):
        return x[0]**3 - x[1]**2

    x = np.array([-1.0, -2.0])
    result = backward_difference_gradient(f, x)
    expected = np.array([-3.0, -4.0])
    assert np.allclose(result, expected, rtol=1e-6)

def test_backward_difference_gradient_high_precision():
    def f(x):
        return x[0]**4 + x[1]**4

    x = np.array([1.0, 1.0])
    result = backward_difference_gradient(f, x, h=1e-10)
    expected = np.array([4.0, 4.0])
    assert np.allclose(result, expected, rtol=1e-8)
