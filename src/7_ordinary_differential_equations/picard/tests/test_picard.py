# test_picard_solver.py
import pytest
import numpy as np
from ..implementation.picard import picard_method


def test_picard_method_linear_ode():
    f = lambda t, y: y
    t0 = 0.0
    y0 = np.array([1.0])
    t_end = 1.0
    h = 0.1
    t, y = picard_method(f, t0, y0, t_end, h, tol=1e-12)
    assert y.shape == (11,)
    # implicit midpoint on y' = y multiplies by (1 + h/2) / (1 - h/2) each step
    r = (1 + h / 2) / (1 - h / 2)
    assert np.allclose(y, r ** np.arange(11), rtol=0, atol=1e-10)
    # second-order error: observed 2.3e-3 at t = 1 (about h^2 * e / 12)
    assert np.allclose(y, np.exp(t), rtol=0, atol=2.4e-3)


def test_picard_method_constant_ode():
    f = lambda t, y: np.array([2.0])
    t0 = 0.0
    y0 = np.array([0.0])
    t_end = 1.0
    h = 0.2
    t, y = picard_method(f, t0, y0, t_end, h)
    expected = 2.0 * t
    assert np.allclose(y, expected, rtol=0, atol=1e-12)


def test_picard_method_system_ode():
    def f(t, y):
        dy1 = y[1]
        dy2 = -y[0]
        return np.array([dy1, dy2])

    t0 = 0.0
    y0 = np.array([0.0, 1.0])
    t_end = 2 * np.pi
    h = 0.1
    t, y = picard_method(f, t0, y0, t_end, h, tol=1e-12)
    assert y.shape == (len(t), 2)
    # second-order error: observed 5.2e-3 / 4.0e-3
    expected_y1 = np.sin(t)
    expected_y2 = np.cos(t)
    assert np.allclose(y[:, 0], expected_y1, rtol=0, atol=5.3e-3)
    assert np.allclose(y[:, 1], expected_y2, rtol=0, atol=4.1e-3)


def test_picard_method_zero_step_size():
    f = lambda t, y: y
    t0 = 0.0
    y0 = np.array([1.0])
    t_end = 1.0
    h = 0.0
    with pytest.raises(ValueError):
        picard_method(f, t0, y0, t_end, h)


def test_picard_method_negative_step_size():
    f = lambda t, y: y
    t0 = 0.0
    y0 = np.array([1.0])
    t_end = 1.0
    h = -0.1
    with pytest.raises(ValueError):
        picard_method(f, t0, y0, t_end, h)


def test_picard_method_t_end_less_than_t0():
    f = lambda t, y: y
    t0 = 1.0
    y0 = np.array([1.0])
    t_end = 0.0
    h = 0.1
    with pytest.raises(ValueError):
        picard_method(f, t0, y0, t_end, h)


def test_picard_method_single_step():
    f = lambda t, y: np.array([3.0])
    t0 = 0.0
    y0 = np.array([2.0])
    t_end = 0.1
    h = 0.1
    t, y = picard_method(f, t0, y0, t_end, h)
    expected_y = np.array([2.0, 2.0 + 3.0 * 0.1])
    assert np.allclose(y, expected_y, rtol=0, atol=1e-12)


def test_picard_method_multiple_steps():
    f = lambda t, y: np.array([t])
    t0 = 0.0
    y0 = np.array([0.0])
    t_end = 1.0
    h = 0.25
    t, y = picard_method(f, t0, y0, t_end, h)
    # the midpoint rule integrates y' = t exactly: y = t^2 / 2
    expected_y = np.array([t_i**2 / 2 for t_i in t])
    assert np.allclose(y, expected_y, rtol=0, atol=1e-12)


def test_picard_method_high_precision():
    f = lambda t, y: y
    t0 = 0.0
    y0 = np.array([1.0])
    t_end = 1.0
    h = 0.01
    t, y = picard_method(f, t0, y0, t_end, h, tol=1e-12)
    expected = np.exp(t)
    # second-order error: observed 2.2e-5, 100 times smaller than at h = 0.1
    assert np.allclose(y, expected, rtol=0, atol=2.3e-5)


def test_picard_method_large_steps():
    f = lambda t, y: y
    t0 = 0.0
    y0 = np.array([1.0])
    t_end = 1.0
    h = 0.5
    t, y = picard_method(f, t0, y0, t_end, h, tol=1e-12)
    # per step: y_{n+1} = y_n (1 + h/2) / (1 - h/2) = y_n * 5/3
    expected = np.array([1.0, 5.0 / 3.0, 25.0 / 9.0])
    assert np.allclose(y, expected, rtol=0, atol=1e-10)


def _linear_system_exact(t):
    # y' = [[1, 1], [1, -1]] y, y(0) = [1, 0]; A^2 = 2I, so exp(At) is closed form.
    s2 = np.sqrt(2.0)
    return np.cosh(s2 * t) + np.sinh(s2 * t) / s2, np.sinh(s2 * t) / s2


def test_picard_method_vector_valued_ode():
    def f(t, y):
        return np.array([y[0] + y[1], y[0] - y[1]])

    t0 = 0.0
    y0 = np.array([1.0, 0.0])
    t_end = 1.0
    h = 0.1
    t, y = picard_method(f, t0, y0, t_end, h, tol=1e-12)
    assert y.shape == (11, 2)
    expected_y1, expected_y2 = _linear_system_exact(t)
    # second-order error: observed 8.2e-3 / 3.6e-3
    assert np.allclose(y[:, 0], expected_y1, rtol=0, atol=8.3e-3)
    assert np.allclose(y[:, 1], expected_y2, rtol=0, atol=3.7e-3)


def test_picard_method_non_linear_ode():
    def f(t, y):
        return np.array([y[0] ** 2])

    t0 = 0.0
    y0 = np.array([1.0])
    t_end = 0.5
    h = 0.1
    t, y = picard_method(f, t0, y0, t_end, h, tol=1e-12)
    expected = 1 / (1 - t)
    # second-order error: observed 1.0e-2 near the blow-up at t = 1
    assert np.allclose(y, expected, rtol=0, atol=1.1e-2)


def test_picard_method_high_dimension():
    def f(t, y):
        return np.array([y[1], -y[0]])

    t0 = 0.0
    y0 = np.array([0.0, 1.0])
    t_end = 2 * np.pi
    h = 0.01
    t, y = picard_method(f, t0, y0, t_end, h, tol=1e-12)
    expected_y1 = np.sin(t)
    expected_y2 = np.cos(t)
    # second-order error: 100 times smaller than at h = 0.1 (5.2e-3 / 4.0e-3)
    assert np.allclose(y[:, 0], expected_y1, rtol=0, atol=5.3e-5)
    assert np.allclose(y[:, 1], expected_y2, rtol=0, atol=4.1e-5)


def test_picard_method_non_convergent():
    def f(t, y):
        return np.array([1 - y[0]])

    t0 = 0.0
    y0 = np.array([0.0])
    t_end = 1.0
    h = 0.1
    with pytest.raises(ValueError):
        picard_method(f, t0, y0, t_end, h, max_iterations=1)


def test_picard_method_second_order_convergence():
    # per-step implicit midpoint solve -> second-order accurate
    f = lambda t, y: y
    errs = []
    for h in (0.1, 0.05):
        t, y = picard_method(f, 0.0, np.array([1.0]), 1.0, h, tol=1e-12)
        errs.append(abs(y[-1] - np.e))
    assert np.log2(errs[0] / errs[1]) == pytest.approx(2.0, abs=0.2)


def test_picard_method_last_step_is_shortened():
    f = lambda t, y: np.array([1.0])
    t, y = picard_method(f, 0.0, np.array([0.0]), 1.0, 0.3)
    assert t[-1] == 1.0
    assert np.allclose(t, [0.0, 0.3, 0.6, 0.9, 1.0])
    assert np.allclose(np.diff(t)[:-1], 0.3)
    assert np.allclose(y, t, rtol=0, atol=1e-12)


def test_picard_method_last_step_value():
    # one step of 0.5 then one of 0.25: factors (1 + h/2) / (1 - h/2)
    f = lambda t, y: y
    t, y = picard_method(f, 0.0, np.array([1.0]), 0.75, 0.5, tol=1e-12)
    assert np.allclose(t, [0.0, 0.5, 0.75])
    r = lambda h: (1 + h / 2) / (1 - h / 2)
    assert np.allclose(y, [1.0, r(0.5), r(0.5) * r(0.25)], rtol=0, atol=1e-10)


def test_picard_method_step_count_with_float_ratio():
    f = lambda t, y: np.array([0.0])
    t, y = picard_method(f, 0.0, np.array([0.0]), 0.07, 0.01)
    assert len(t) == 8
    assert t[-1] == 0.07


def test_picard_method_t_end_equals_t0():
    f = lambda t, y: y
    t, y = picard_method(f, 1.0, np.array([2.0]), 1.0, 0.1)
    assert np.allclose(t, [1.0])
    assert y.shape == (1,)


def test_picard_method_output_shapes():
    t, y = picard_method(lambda t, y: -y, 0.0, np.array([1.0]), 1.0, 0.25)
    assert y.shape == (5,)
    f_vec = lambda t, y: np.array([y[1], -y[0]])
    t, y = picard_method(f_vec, 0.0, np.array([0.0, 1.0]), 1.0, 0.25)
    assert y.shape == (5, 2)
