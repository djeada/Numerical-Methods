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
    assert y.shape == (11,)
    # fourth-order error: observed 2.1e-6 at t = 1
    assert np.allclose(y, expected, rtol=0, atol=2.2e-6)


def test_runge_kutta_constant_ode():
    f = lambda t, y: np.array([2.0])
    t0 = 0.0
    y0 = np.array([0.0])
    t_end = 1.0
    h = 0.2
    t, y = runge_kutta_4(f, t0, y0, t_end, h)
    expected = 2.0 * t
    assert np.allclose(y, expected, rtol=0, atol=1e-12)


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
    assert y.shape == (len(t), 2)
    # fourth-order error: observed 5.2e-6 / 4.1e-6
    expected_y1 = np.sin(t)
    expected_y2 = np.cos(t)
    assert np.allclose(y[:, 0], expected_y1, rtol=0, atol=5.5e-6)
    assert np.allclose(y[:, 1], expected_y2, rtol=0, atol=4.5e-6)


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
    assert np.allclose(y, expected_y, rtol=0, atol=1e-12)


def test_runge_kutta_multiple_steps():
    f = lambda t, y: np.array([t])
    t0 = 0.0
    y0 = np.array([0.0])
    t_end = 1.0
    h = 0.25
    t, y = runge_kutta_4(f, t0, y0, t_end, h)
    # RK4 is exact for polynomial solutions up to degree 4: y = t^2 / 2
    assert np.allclose(y, t**2 / 2, rtol=0, atol=1e-12)


def test_runge_kutta_high_precision():
    f = lambda t, y: y
    t0 = 0.0
    y0 = np.array([1.0])
    t_end = 1.0
    h = 0.01
    t, y = runge_kutta_4(f, t0, y0, t_end, h)
    expected = np.exp(t)
    # fourth-order error: observed 2.2e-10, 10^4 times smaller than at h = 0.1
    assert np.allclose(y, expected, rtol=0, atol=3e-10)


def test_runge_kutta_large_steps():
    f = lambda t, y: y
    t0 = 0.0
    y0 = np.array([1.0])
    t_end = 1.0
    h = 0.5
    t, y = runge_kutta_4(f, t0, y0, t_end, h)
    # R(0.5) = 1 + 1/2 + 1/8 + 1/48 + 1/384 is the per-step factor
    r = 1 + 0.5 + 0.125 + 1 / 48 + 1 / 384
    assert np.allclose(y, [1.0, r, r * r], rtol=0, atol=1e-12)
    # fourth-order error: observed 9.4e-4
    assert np.allclose(y, np.exp(t), rtol=0, atol=1e-3)


def _linear_system_exact(t):
    # y' = [[1, 1], [1, -1]] y, y(0) = [1, 0]; A^2 = 2I, so exp(At) is closed form.
    s2 = np.sqrt(2.0)
    return np.cosh(s2 * t) + np.sinh(s2 * t) / s2, np.sinh(s2 * t) / s2


def test_runge_kutta_vector_valued_ode():
    def f(t, y):
        return np.array([y[0] + y[1], y[0] - y[1]])

    t0 = 0.0
    y0 = np.array([1.0, 0.0])
    t_end = 1.0
    h = 0.1
    t, y = runge_kutta_4(f, t0, y0, t_end, h)
    assert y.shape == (11, 2)
    expected_y1, expected_y2 = _linear_system_exact(t)
    # fourth-order error: observed 1.5e-5 / 6.6e-6
    assert np.allclose(y[:, 0], expected_y1, rtol=0, atol=1.6e-5)
    assert np.allclose(y[:, 1], expected_y2, rtol=0, atol=7e-6)


def test_runge_kutta_non_linear_ode():
    def f(t, y):
        return np.array([y[0] ** 2])

    t0 = 0.0
    y0 = np.array([1.0])
    t_end = 0.5
    h = 0.1
    t, y = runge_kutta_4(f, t0, y0, t_end, h)
    expected = 1 / (1 - t)
    # fourth-order error: observed 3.7e-5 near the blow-up at t = 1
    assert np.allclose(y, expected, rtol=0, atol=4e-5)


def test_runge_kutta_high_dimension():
    def f(t, y):
        return np.array([y[1], -y[0]])

    t0 = 0.0
    y0 = np.array([0.0, 1.0])
    t_end = 2 * np.pi
    h = 0.05
    t, y = runge_kutta_4(f, t0, y0, t_end, h)
    expected_y1 = np.sin(t)
    expected_y2 = np.cos(t)
    # fourth-order error: about 16 times smaller than at h = 0.1 (5.2e-6)
    assert np.allclose(y[:, 0], expected_y1, rtol=0, atol=4e-7)
    assert np.allclose(y[:, 1], expected_y2, rtol=0, atol=3e-7)


def test_runge_kutta_fourth_order_convergence():
    f = lambda t, y: y
    errs = []
    for h in (0.1, 0.05):
        t, y = runge_kutta_4(f, 0.0, np.array([1.0]), 1.0, h)
        errs.append(abs(y[-1] - np.e))
    assert np.log2(errs[0] / errs[1]) == pytest.approx(4.0, abs=0.2)


def test_runge_kutta_step_count_with_float_ratio():
    f = lambda t, y: np.array([0.0])
    t, y = runge_kutta_4(f, 0.0, np.array([0.0]), 0.07, 0.01)
    assert len(t) == 8
    assert t[-1] == 0.07


def test_runge_kutta_last_step_is_shortened():
    f = lambda t, y: np.array([1.0])
    t, y = runge_kutta_4(f, 0.0, np.array([0.0]), 1.0, 0.3)
    assert t[-1] == 1.0
    assert np.allclose(t, [0.0, 0.3, 0.6, 0.9, 1.0])
    assert np.allclose(np.diff(t)[:-1], 0.3)
    assert np.allclose(y, t, rtol=0, atol=1e-12)


def test_runge_kutta_last_step_value():
    # one full step of 0.5 then one of 0.25, each multiplying by the RK4 factor
    f = lambda t, y: y
    t, y = runge_kutta_4(f, 0.0, np.array([1.0]), 0.75, 0.5)
    assert np.allclose(t, [0.0, 0.5, 0.75])
    r = lambda h: 1 + h + h**2 / 2 + h**3 / 6 + h**4 / 24
    assert np.allclose(y, [1.0, r(0.5), r(0.5) * r(0.25)], rtol=0, atol=1e-12)


def test_runge_kutta_t_end_equals_t0():
    f = lambda t, y: y
    t, y = runge_kutta_4(f, 1.0, np.array([2.0]), 1.0, 0.1)
    assert np.allclose(t, [1.0])
    assert y.shape == (1,)
    assert y[0] == 2.0

    t, y = runge_kutta_4(lambda t, y: y, 1.0, np.array([2.0, 3.0]), 1.0, 0.1)
    assert y.shape == (1, 2)


def test_runge_kutta_output_shapes():
    t, y = runge_kutta_4(lambda t, y: -y, 0.0, np.array([1.0]), 1.0, 0.25)
    assert y.shape == (5,)
    f_vec = lambda t, y: np.array([y[1], -y[0]])
    t, y = runge_kutta_4(f_vec, 0.0, np.array([0.0, 1.0]), 1.0, 0.25)
    assert y.shape == (5, 2)
