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
    # y' = y: forward Euler gives exactly (1 + h)^n
    assert y.shape == (11,)
    assert np.allclose(y, (1 + h) ** np.arange(11), rtol=0, atol=1e-12)
    # global error bound (h / 2) * max|y''| * (e^t - 1) = (h / 2) * e * (e^t - 1)
    bound = 0.5 * h * np.e * (np.exp(t) - 1)
    assert np.all(np.abs(y - np.exp(t)) <= bound + 1e-12)


def test_euler_method_constant_ode():
    f = lambda t, y: np.array([2.0])
    t0 = 0.0
    y0 = np.array([0.0])
    t_end = 1.0
    h = 0.2
    t, y = euler_method(f, t0, y0, t_end, h)
    # a constant slope is integrated exactly
    expected = 2.0 * t
    assert np.allclose(y, expected, rtol=0, atol=1e-12)


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
    assert y.shape == (len(t), 2)
    # w = y2 + i*y1 satisfies w' = i*w, so Euler gives w_n = (1 + i*h)^n
    # (checked on the full steps; the last step is shortened)
    w = (1 + 1j * h) ** np.arange(len(t) - 1)
    assert np.allclose(y[:-1, 0], w.imag, rtol=0, atol=1e-12)
    assert np.allclose(y[:-1, 1], w.real, rtol=0, atol=1e-12)
    # first-order accuracy: error is 0.28 / 0.37 here and shrinks linearly in h
    assert np.allclose(y[:, 0], np.sin(t), rtol=0, atol=0.3)
    assert np.allclose(y[:, 1], np.cos(t), rtol=0, atol=0.4)


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
    assert np.allclose(y, expected_y, rtol=0, atol=1e-12)


def test_euler_method_multiple_steps():
    f = lambda t, y: np.array([t])
    t0 = 0.0
    y0 = np.array([0.0])
    t_end = 1.0
    h = 0.25
    t, y = euler_method(f, t0, y0, t_end, h)
    # y' = t: Euler uses the left-endpoint rule, so y_n = h^2 n (n - 1) / 2
    expected_y = np.array([0.0, 0.0, 0.0625, 0.1875, 0.375])
    assert np.allclose(y, expected_y, rtol=0, atol=1e-12)


def test_euler_method_high_precision():
    f = lambda t, y: y
    t0 = 0.0
    y0 = np.array([1.0])
    t_end = 1.0
    h = 0.01
    t, y = euler_method(f, t0, y0, t_end, h)
    expected = np.exp(t)
    # observed max error 1.35e-2 (about h * e / 2); ten times smaller than h = 0.1
    assert np.allclose(y, expected, rtol=0, atol=0.5 * h * np.e)


def test_euler_method_large_steps():
    f = lambda t, y: y
    t0 = 0.0
    y0 = np.array([1.0])
    t_end = 1.0
    h = 0.5
    t, y = euler_method(f, t0, y0, t_end, h)
    expected = np.array([1.0, 1.0 + 1.0 * 0.5, (1.0 + 0.5) + (1.0 + 0.5) * 0.5])
    assert np.allclose(y, expected, rtol=0, atol=1e-12)


def test_euler_method_vector_valued_ode():
    def f(t, y):
        return np.array([y[0] + y[1], y[0] - y[1]])

    t0 = 0.0
    y0 = np.array([1.0, 0.0])
    t_end = 1.0
    h = 0.1
    t, y = euler_method(f, t0, y0, t_end, h)
    assert y.shape == (11, 2)
    expected_y = np.array([1.0, 0.0])
    for i in range(1, len(t)):
        expected_y = expected_y + h * f(t[i - 1], expected_y)
        assert np.allclose(y[i], expected_y, rtol=0, atol=1e-12)


def test_euler_method_non_linear_ode():
    def f(t, y):
        return np.array([y[0] ** 2])

    t0 = 0.0
    y0 = np.array([1.0])
    t_end = 0.5
    h = 0.1
    t, y = euler_method(f, t0, y0, t_end, h)
    expected = [1.0]
    for _ in range(5):
        expected.append(expected[-1] + h * expected[-1] ** 2)
    expected = np.array(expected)
    # the Euler recurrence u_{n+1} = u_n + h u_n^2 is reproduced to rounding error
    assert np.allclose(y, expected, rtol=0, atol=1e-12)
    # first-order error against the exact solution 1 / (1 - t): about 0.2 here
    assert np.allclose(y, 1 / (1 - t), rtol=0, atol=0.21)


def test_euler_method_high_dimension():
    def f(t, y):
        return np.array([y[1], -y[0]])

    t0 = 0.0
    y0 = np.array([0.0, 1.0])
    t_end = 2 * np.pi
    h = 0.01
    t, y = euler_method(f, t0, y0, t_end, h)
    # error scales like h: 0.28 / 0.37 at h = 0.1 become about 0.03 / 0.04
    assert np.allclose(y[:, 0], np.sin(t), rtol=0, atol=0.035)
    assert np.allclose(y[:, 1], np.cos(t), rtol=0, atol=0.045)


def test_euler_method_first_order_convergence():
    f = lambda t, y: y
    errs = []
    for h in (0.1, 0.05):
        t, y = euler_method(f, 0.0, np.array([1.0]), 1.0, h)
        errs.append(abs(y[-1] - np.e))
    assert np.log2(errs[0] / errs[1]) == pytest.approx(1.0, abs=0.1)


def test_euler_method_step_count_with_float_ratio():
    f = lambda t, y: np.array([0.0])
    t, y = euler_method(f, 0.0, np.array([0.0]), 0.07, 0.01)
    assert len(t) == 8
    assert t[-1] == 0.07


def test_euler_method_last_step_is_shortened():
    # (t_end - t0) / h = 3.33...: three full steps and one of length 0.1
    f = lambda t, y: np.array([1.0])
    t, y = euler_method(f, 0.0, np.array([0.0]), 1.0, 0.3)
    assert t[-1] == 1.0
    assert np.allclose(t, [0.0, 0.3, 0.6, 0.9, 1.0])
    assert np.allclose(np.diff(t)[:-1], 0.3)
    # y' = 1 is integrated exactly, so y must equal t on the returned grid
    assert np.allclose(y, t, rtol=0, atol=1e-12)


def test_euler_method_last_step_value():
    # one full step of 0.5 then one of 0.25: 1 -> 1.5 -> 1.5 * 1.25
    f = lambda t, y: y
    t, y = euler_method(f, 0.0, np.array([1.0]), 0.75, 0.5)
    assert np.allclose(t, [0.0, 0.5, 0.75])
    assert np.allclose(y, [1.0, 1.5, 1.875], rtol=0, atol=1e-12)


def test_euler_method_t_end_equals_t0():
    f = lambda t, y: y
    t, y = euler_method(f, 1.0, np.array([2.0]), 1.0, 0.1)
    assert np.allclose(t, [1.0])
    assert y.shape == (1,)
    assert y[0] == 2.0


def test_euler_method_output_shapes():
    f_scalar = lambda t, y: -y
    t, y = euler_method(f_scalar, 0.0, np.array([1.0]), 1.0, 0.25)
    assert y.shape == (5,)
    f_vec = lambda t, y: np.array([y[1], -y[0]])
    t, y = euler_method(f_vec, 0.0, np.array([0.0, 1.0]), 1.0, 0.25)
    assert y.shape == (5, 2)
