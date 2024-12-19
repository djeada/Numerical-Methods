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
