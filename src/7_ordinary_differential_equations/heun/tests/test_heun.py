# test_heun_solver.py
import pytest
import numpy as np
from ..implementation.heun import heun_method

def test_heun_method_linear_ode():
    f = lambda t, y: y
    t0 = 0.0
    y0 = np.array([1.0])
    t_end = 1.0
    h = 0.1
    t, y = heun_method(f, t0, y0, t_end, h)
    expected = np.exp(t)
    assert np.allclose(y.flatten(), expected, atol=0.1)

def test_heun_method_constant_ode():
    f = lambda t, y: np.array([2.0])
    t0 = 0.0
    y0 = np.array([0.0])
    t_end = 1.0
    h = 0.2
    t, y = heun_method(f, t0, y0, t_end, h)
    expected = 2.0 * t
    assert np.allclose(y.flatten(), expected, atol=0.1)

def test_heun_method_system_ode():
    def f(t, y):
        dy1 = y[1]
        dy2 = -y[0]
        return np.array([dy1, dy2])
    
    t0 = 0.0
    y0 = np.array([0.0, 1.0])
    t_end = 2 * np.pi
    h = 0.1
    t, y = heun_method(f, t0, y0, t_end, h)
    expected_y1 = np.sin(t)
    expected_y2 = np.cos(t)
    assert np.allclose(y[:,0], expected_y1, atol=0.1)
    assert np.allclose(y[:,1], expected_y2, atol=0.1)

def test_heun_method_zero_step_size():
    f = lambda t, y: y
    t0 = 0.0
    y0 = np.array([1.0])
    t_end = 1.0
    h = 0.0
    with pytest.raises(ValueError):
        heun_method(f, t0, y0, t_end, h)

def test_heun_method_negative_step_size():
    f = lambda t, y: y
    t0 = 0.0
    y0 = np.array([1.0])
    t_end = 1.0
    h = -0.1
    with pytest.raises(ValueError):
        heun_method(f, t0, y0, t_end, h)

def test_heun_method_t_end_less_than_t0():
    f = lambda t, y: y
    t0 = 1.0
    y0 = np.array([1.0])
    t_end = 0.0
    h = 0.1
    with pytest.raises(ValueError):
        heun_method(f, t0, y0, t_end, h)

def test_heun_method_single_step():
    f = lambda t, y: np.array([3.0])
    t0 = 0.0
    y0 = np.array([2.0])
    t_end = 0.1
    h = 0.1
    t, y = heun_method(f, t0, y0, t_end, h)
    expected_y = np.array([2.0, 2.0 + (3.0 + 3.0)/2 * 0.1])
    assert np.allclose(y, expected_y, atol=0.3)

def test_heun_method_multiple_steps():
    f = lambda t, y: np.array([t])
    t0 = 0.0
    y0 = np.array([0.0])
    t_end = 1.0
    h = 0.25
    t, y = heun_method(f, t0, y0, t_end, h)
    expected_y = np.array([0.0, 0.0 + (0.0 + 0.25)/2 * 0.25, 
                           (0.0625) + (0.25 + 0.5)/2 * 0.25,
                           (0.15625) + (0.5 + 0.75)/2 * 0.25,
                           (0.3125) + (0.75 + 1.0)/2 * 0.25])
    assert np.allclose(y.flatten(), expected_y, atol=0.1)

def test_heun_method_high_precision():
    f = lambda t, y: y
    t0 = 0.0
    y0 = np.array([1.0])
    t_end = 1.0
    h = 0.01
    t, y = heun_method(f, t0, y0, t_end, h)
    expected = np.exp(t)
    assert np.allclose(y.flatten(), expected, atol=0.05)

def test_heun_method_large_steps():
    f = lambda t, y: y
    t0 = 0.0
    y0 = np.array([1.0])
    t_end = 1.0
    h = 0.5
    t, y = heun_method(f, t0, y0, t_end, h)
    expected = np.array([1.0, np.exp(0.5), np.exp(1.0)])
    assert np.allclose(y.flatten(), expected, atol=0.1)

@pytest.mark.skip()
def test_heun_method_vector_valued_ode():
    def f(t, y):
        return np.array([y[0] + y[1], y[0] - y[1]])

    t0 = 0.0
    y0 = np.array([1.0, 0.0])
    t_end = 1.0
    h = 0.1
    t, y = heun_method(f, t0, y0, t_end, h)
    expected_y1 = np.exp(t) + np.exp(-t)
    expected_y2 = np.exp(t) - np.exp(-t)

    assert np.allclose(y[:, 0], expected_y1, atol=0.3), "y1 does not match expected values"
    assert np.allclose(y[:, 1], expected_y2, atol=0.3), "y2 does not match expected values"
def test_heun_method_non_linear_ode():
    def f(t, y):
        return np.array([y[0]**2])
    
    t0 = 0.0
    y0 = np.array([1.0])
    t_end = 0.5
    h = 0.1
    t, y = heun_method(f, t0, y0, t_end, h)
    expected = 1 / (1 - t)
    assert np.allclose(y.flatten(), expected, atol=0.1)

def test_heun_method_high_dimension():
    def f(t, y):
        return np.array([y[1], -y[0]])
    
    t0 = 0.0
    y0 = np.array([0.0, 1.0])
    t_end = 2 * np.pi
    h = 0.1
    t, y = heun_method(f, t0, y0, t_end, h)
    expected_y1 = np.sin(t)
    expected_y2 = np.cos(t)
    assert np.allclose(y[:,0], expected_y1, atol=0.1)
    assert np.allclose(y[:,1], expected_y2, atol=0.1)

def test_heun_method_non_convergent():
    def f(t, y):
        return np.array([1 - y[0]])
    
    t0 = 0.0
    y0 = np.array([0.0])
    t_end = 1.0
    h = 0.1
    # Heun's method is explicit and should converge for this simple ODE
    t, y = heun_method(f, t0, y0, t_end, h)
    expected = 1 - np.exp(-t)
    assert np.allclose(y.flatten(), expected, atol=1e-2)
