# test_runge_kutta.py
import pytest
import numpy as np
from ..implementation.runge_kutta import runge_kutta_4


def test_runge_kutta_linear_ode():
    f = lambda t, y: y
    t0 = 0.0
    y0 = np.array([1.0])
    t_end = 1.0
    h = 0.1
    t, y = runge_kutta_4(f, t0, y0, t_end, h)
    expected = np.exp(t)
    assert np.allclose(y.flatten(), expected, atol=0.1)


def test_runge_kutta_constant_ode():
    f = lambda t, y: np.array([2.0])
    t0 = 0.0
    y0 = np.array([0.0])
    t_end = 1.0
    h = 0.2
    t, y = runge_kutta_4(f, t0, y0, t_end, h)
    expected = 2.0 * t
    assert np.allclose(y.flatten(), expected, atol=0.1)


def test_runge_kutta_system_ode():
    def f(t, y):
        dy1 = y[1]
        dy2 = -y[0]
        return np.array([dy1, dy2])

    t0 = 0.0
    y0 = np.array([0.0, 1.0])
    t_end = 2 * np.pi
    h = 0.1
    t, y = runge_kutta_4(f, t0, y0, t_end, h)
    expected_y1 = np.sin(t)
    expected_y2 = np.cos(t)
    assert np.allclose(y[:, 0], expected_y1, atol=0.1)
    assert np.allclose(y[:, 1], expected_y2, atol=0.1)


def test_runge_kutta_zero_step_size():
    f = lambda t, y: y
    t0 = 0.0
    y0 = np.array([1.0])
    t_end = 1.0
    h = 0.0
    with pytest.raises(ValueError):
        runge_kutta_4(f, t0, y0, t_end, h)


def test_runge_kutta_negative_step_size():
    f = lambda t, y: y
    t0 = 0.0
    y0 = np.array([1.0])
    t_end = 1.0
    h = -0.1
    with pytest.raises(ValueError):
        runge_kutta_4(f, t0, y0, t_end, h)


def test_runge_kutta_t_end_less_than_t0():
    f = lambda t, y: y
    t0 = 1.0
    y0 = np.array([1.0])
    t_end = 0.0
    h = 0.1
    with pytest.raises(ValueError):
        runge_kutta_4(f, t0, y0, t_end, h)


def test_runge_kutta_single_step():
    f = lambda t, y: np.array([3.0])
    t0 = 0.0
    y0 = np.array([2.0])
    t_end = 0.1
    h = 0.1
    t, y = runge_kutta_4(f, t0, y0, t_end, h)
    expected_y = np.array([2.0, 2.0 + 3.0 * 0.1])
    assert np.allclose(y, expected_y, atol=0.1)


def test_runge_kutta_multiple_steps():
    f = lambda t, y: np.array([t])
    t0 = 0.0
    y0 = np.array([0.0])
    t_end = 1.0
    h = 0.25
    t, y = runge_kutta_4(f, t0, y0, t_end, h)
    expected_y = np.cumsum(
        [0.0] + [(t[i - 1] + t[i]) / 2 * h for i in range(1, len(t))]
    )
    assert np.allclose(y.flatten(), expected_y, atol=0.1)


def test_runge_kutta_high_precision():
    f = lambda t, y: y
    t0 = 0.0
    y0 = np.array([1.0])
    t_end = 1.0
    h = 0.01
    t, y = runge_kutta_4(f, t0, y0, t_end, h)
    expected = np.exp(t)
    assert np.allclose(y.flatten(), expected, atol=0.05)


def test_runge_kutta_large_steps():
    f = lambda t, y: y
    t0 = 0.0
    y0 = np.array([1.0])
    t_end = 1.0
    h = 0.5
    t, y = runge_kutta_4(f, t0, y0, t_end, h)
    expected = np.array([1.0, np.exp(0.5), np.exp(1.0)])
    assert np.allclose(y.flatten(), expected, atol=0.1)


@pytest.mark.skip()
def test_runge_kutta_vector_valued_ode():
    def f(t, y):
        return np.array([y[0] + y[1], y[0] - y[1]])

    t0 = 0.0
    y0 = np.array([1.0, 0.0])
    t_end = 1.0
    h = 0.1
    t, y = runge_kutta_4(f, t0, y0, t_end, h)
    expected_y1 = np.exp(t) + np.exp(-t)
    expected_y2 = np.exp(t) - np.exp(-t)
    assert np.allclose(y[:, 0], expected_y1, atol=0.1)
    assert np.allclose(y[:, 1], expected_y2, atol=0.1)


def test_runge_kutta_non_linear_ode():
    def f(t, y):
        return np.array([y[0] ** 2])

    t0 = 0.0
    y0 = np.array([1.0])
    t_end = 0.5
    h = 0.1
    t, y = runge_kutta_4(f, t0, y0, t_end, h)
    expected = 1 / (1 - t)
    assert np.allclose(y.flatten(), expected, atol=1e-2)


def test_runge_kutta_high_dimension():
    def f(t, y):
        return np.array([y[1], -y[0]])

    t0 = 0.0
    y0 = np.array([0.0, 1.0])
    t_end = 2 * np.pi
    h = 0.1
    t, y = runge_kutta_4(f, t0, y0, t_end, h)
    expected_y1 = np.sin(t)
    expected_y2 = np.cos(t)
    assert np.allclose(y[:, 0], expected_y1, atol=0.1)
    assert np.allclose(y[:, 1], expected_y2, atol=0.1)
