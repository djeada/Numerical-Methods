# test_euler_solver.py
import pytest
import numpy as np
from ..implementation.euler import euler_method

def test_euler_method_linear_ode():
    f = lambda t, y: y
    t0 = 0.0
    y0 = np.array([1.0])
    t_end = 1.0
    h = 0.1
    t, y = euler_method(f, t0, y0, t_end, h)
    expected = np.exp(t)
    assert np.allclose(y.flatten(), expected, atol=0.3)

def test_euler_method_constant_ode():
    f = lambda t, y: np.array([2.0])
    t0 = 0.0
    y0 = np.array([0.0])
    t_end = 1.0
    h = 0.2
    t, y = euler_method(f, t0, y0, t_end, h)
    expected = 2.0 * t
    assert np.allclose(y.flatten(), expected, atol=0.1)

def test_euler_method_system_ode():
    def f(t, y):
        dy1 = y[1]
        dy2 = -y[0]
        return np.array([dy1, dy2])
    
    t0 = 0.0
    y0 = np.array([0.0, 1.0])
    t_end = 2 * np.pi
    h = 0.1
    t, y = euler_method(f, t0, y0, t_end, h)
    expected_y1 = np.sin(t)
    expected_y2 = np.cos(t)
    assert np.allclose(y[:,0], expected_y1, atol=0.5)
    assert np.allclose(y[:,1], expected_y2, atol=0.5)

def test_euler_method_zero_step_size():
    f = lambda t, y: y
    t0 = 0.0
    y0 = np.array([1.0])
    t_end = 1.0
    h = 0.0
    with pytest.raises(ValueError):
        euler_method(f, t0, y0, t_end, h)

def test_euler_method_negative_step_size():
    f = lambda t, y: y
    t0 = 0.0
    y0 = np.array([1.0])
    t_end = 1.0
    h = -0.1
    with pytest.raises(ValueError):
        euler_method(f, t0, y0, t_end, h)

def test_euler_method_t_end_less_than_t0():
    f = lambda t, y: y
    t0 = 1.0
    y0 = np.array([1.0])
    t_end = 0.0
    h = 0.1
    with pytest.raises(ValueError):
        euler_method(f, t0, y0, t_end, h)

def test_euler_method_single_step():
    f = lambda t, y: np.array([3.0])
    t0 = 0.0
    y0 = np.array([2.0])
    t_end = 0.1
    h = 0.1
    t, y = euler_method(f, t0, y0, t_end, h)
    expected_y = np.array([2.0, 2.0 + 3.0 * 0.1])
    assert np.allclose(y, expected_y, atol=0.3)

def test_euler_method_multiple_steps():
    f = lambda t, y: np.array([t])
    t0 = 0.0
    y0 = np.array([0.0])
    t_end = 1.0
    h = 0.25
    t, y = euler_method(f, t0, y0, t_end, h)
    expected_y = np.array([0.0, 0.0 + 0.0*0.25, 0.0 + 0.25*0.25, 0.0 + 0.5*0.25, 0.0 + 0.75*0.25])
    assert np.allclose(y.flatten(), expected_y, atol=0.3)

def test_euler_method_high_precision():
    f = lambda t, y: y
    t0 = 0.0
    y0 = np.array([1.0])
    t_end = 1.0
    h = 0.01
    t, y = euler_method(f, t0, y0, t_end, h)
    expected = np.exp(t)
    assert np.allclose(y.flatten(), expected, atol=0.05)

def test_euler_method_large_steps():
    f = lambda t, y: y
    t0 = 0.0
    y0 = np.array([1.0])
    t_end = 1.0
    h = 0.5
    t, y = euler_method(f, t0, y0, t_end, h)
    expected = np.array([1.0, 1.0 + 1.0 * 0.5, (1.0 + 0.5) + (1.0 + 0.5) * 0.5])
    assert np.allclose(y.flatten(), expected, atol=0.1)

def test_euler_method_vector_valued_ode():
    def f(t, y):
        return np.array([y[0] + y[1], y[0] - y[1]])
    
    t0 = 0.0
    y0 = np.array([1.0, 0.0])
    t_end = 1.0
    h = 0.1
    t, y = euler_method(f, t0, y0, t_end, h)
    # Analytical solution can be compared approximately
    expected_y = np.array([1.0, 0.0])
    for i in range(1, len(t)):
        expected_y = expected_y + h * f(t[i-1], expected_y)
        assert np.allclose(y[i], expected_y, atol=1e-2)

def test_euler_method_non_linear_ode():
    def f(t, y):
        return np.array([y[0]**2])
    
    t0 = 0.0
    y0 = np.array([1.0])
    t_end = 0.5
    h = 0.1
    t, y = euler_method(f, t0, y0, t_end, h)
    expected = np.array([1.0, 1.0 + 1.0**2 * 0.1, 1.1 + 1.1**2 * 0.1, 1.21 + 1.21**2 * 0.1, 1.331 + 1.331**2 * 0.1, 1.4641 + 1.4641**2 * 0.1])
    assert np.allclose(y.flatten(), expected, atol=0.5)

def test_euler_method_high_dimension():
    def f(t, y):
        return np.array([y[1], -y[0]])
    
    t0 = 0.0
    y0 = np.array([0.0, 1.0])
    t_end = 2 * np.pi
    h = 0.1
    t, y = euler_method(f, t0, y0, t_end, h)
    expected_y1 = np.sin(t)
    expected_y2 = np.cos(t)
    assert np.allclose(y[:,0], expected_y1, atol=0.5)
    assert np.allclose(y[:,1], expected_y2, atol=0.5)
