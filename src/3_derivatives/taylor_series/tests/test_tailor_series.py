import pytest
import math
import numpy as np
from ..implementation.taylor_series import taylor_series


def test_taylor_series_exp():
    def exp_derivatives(k: np.ndarray) -> np.ndarray:
        return np.ones_like(k, dtype=float)  # The derivative of exp(0) is always 1

    approx = taylor_series(math.exp, 0, 10, 1, exp_derivatives)
    expected = math.exp(1)
    assert math.isclose(approx, expected, rel_tol=1e-3)


def test_taylor_series_sin():
    def sin_derivatives(k: np.ndarray) -> np.ndarray:
        return np.array([0, 1, 0, -1])[k % 4]

    approx = taylor_series(math.sin, 0, 10, math.pi / 2, sin_derivatives)
    expected = math.sin(math.pi / 2)
    assert math.isclose(approx, expected, rel_tol=1e-3)


def test_taylor_series_cos():
    def cos_derivatives(k: np.ndarray) -> np.ndarray:
        return np.array([1, 0, -1, 0])[k % 4]

    approx = taylor_series(math.cos, 0, 10, 0, cos_derivatives)
    expected = math.cos(0)
    assert math.isclose(approx, expected, rel_tol=1e-3)


def test_taylor_series_ln():
    def ln_derivatives(k: np.ndarray) -> np.ndarray:
        result = np.zeros_like(k, dtype=float)
        result[k > 0] = (-1) ** (k[k > 0] - 1) / k[k > 0]
        return result

    with pytest.warns(RuntimeWarning, match="divide by zero encountered in divide"):
        taylor_series(math.log, 1, 100, 2, ln_derivatives)


def test_taylor_series_error():
    def linear_derivatives(k: np.ndarray) -> np.ndarray:
        result = np.zeros_like(k, dtype=float)
        result[k == 1] = 1.0
        return result

    approx = taylor_series(lambda x: x, 0, 2, 5, linear_derivatives)
    expected = 5.0
    assert math.isclose(approx, expected, rel_tol=1e-3)


def test_taylor_series_zero_terms():
    def any_derivatives(k: np.ndarray) -> np.ndarray:
        return np.zeros_like(k, dtype=float)

    approx = taylor_series(math.exp, 0, 0, 1, any_derivatives)
    expected = 0.0
    assert math.isclose(approx, expected, rel_tol=1e-3)


def test_taylor_series_negative_x():
    def exp_derivatives(k: np.ndarray) -> np.ndarray:
        return np.ones_like(k, dtype=float)  # The derivative of exp(0) is always 1

    approx = taylor_series(math.exp, 0, 10, -1, exp_derivatives)
    expected = math.exp(-1)
    assert math.isclose(approx, expected, rel_tol=1e-3)


def test_taylor_series_high_terms():
    def exp_derivatives(k: np.ndarray) -> np.ndarray:
        return np.ones_like(k, dtype=float)  # The derivative of exp(0) is always 1

    approx = taylor_series(math.exp, 0, 20, 1, exp_derivatives)
    expected = math.exp(1)
    assert math.isclose(approx, expected, rel_tol=1e-12)


def test_taylor_series_polynomial():
    def poly_derivatives(k: np.ndarray) -> np.ndarray:
        # f(x) = 3x^2 + 2x + 1, expanded at a=0
        # f(0)=1, f'(0)=2, f''(0)=6, rest are 0
        result = np.zeros_like(k, dtype=float)
        result[k == 0] = 1.0
        result[k == 1] = 2.0
        result[k == 2] = 6.0
        return result

    approx = taylor_series(lambda x: 3 * x**2 + 2 * x + 1, 0, 5, 2, poly_derivatives)
    expected = 3 * 4 + 2 * 2 + 1
    assert math.isclose(approx, expected, rel_tol=1e-3)


def test_taylor_series_exp_negative_center():
    def exp_at_1_derivatives(k: np.ndarray) -> np.ndarray:
        return np.full_like(k, math.e, dtype=float)

    approx = taylor_series(math.exp, 1, 15, 0, exp_at_1_derivatives)
    expected = math.exp(0)
    assert math.isclose(approx, expected, rel_tol=1e-3)


def test_taylor_series_cos_at_pi():
    def cos_at_pi_derivatives(k: np.ndarray) -> np.ndarray:
        # cos derivatives at pi: -1, 0, 1, 0, -1, 0, 1, 0, ...
        return np.array([-1, 0, 1, 0])[k % 4]

    approx = taylor_series(math.cos, math.pi, 15, math.pi / 2, cos_at_pi_derivatives)
    expected = math.cos(math.pi / 2)
    assert math.isclose(approx, expected, abs_tol=1e-3)


def test_taylor_series_sin_at_zero():
    def sin_derivatives(k: np.ndarray) -> np.ndarray:
        return np.array([0, 1, 0, -1])[k % 4]

    approx = taylor_series(math.sin, 0, 15, 1, sin_derivatives)
    expected = math.sin(1)
    assert math.isclose(approx, expected, rel_tol=1e-6)


def test_taylor_series_constant_function():
    def const_derivatives(k: np.ndarray) -> np.ndarray:
        result = np.zeros_like(k, dtype=float)
        result[k == 0] = 7.0
        return result

    approx = taylor_series(lambda x: 7.0, 0, 5, 100, const_derivatives)
    expected = 7.0
    assert math.isclose(approx, expected, rel_tol=1e-10)


def test_taylor_series_single_term():
    def exp_derivatives(k: np.ndarray) -> np.ndarray:
        return np.ones_like(k, dtype=float)

    approx = taylor_series(math.exp, 0, 1, 0, exp_derivatives)
    expected = 1.0
    assert math.isclose(approx, expected, rel_tol=1e-10)
