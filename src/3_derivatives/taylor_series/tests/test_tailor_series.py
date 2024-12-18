import pytest
import math
from implementation.taylor_series import taylor_series

def test_taylor_series_exp():
    def exp_derivatives(k: int) -> float:
        return math.exp(0)
    approx = taylor_series(math.exp, 0, 10, 1, exp_derivatives)
    expected = math.exp(1)
    assert math.isclose(approx, expected, rel_tol=1e-9)

def test_taylor_series_sin():
    def sin_derivatives(k: int) -> float:
        derivatives = [0, 1, 0, -1]
        return derivatives[k % 4]
    approx = taylor_series(math.sin, 0, 10, math.pi / 2, sin_derivatives)
    expected = math.sin(math.pi / 2)
    assert math.isclose(approx, expected, rel_tol=1e-6)

def test_taylor_series_cos():
    def cos_derivatives(k: int) -> float:
        derivatives = [1, 0, -1, 0]
        return derivatives[k % 4]
    approx = taylor_series(math.cos, 0, 10, 0, cos_derivatives)
    expected = math.cos(0)
    assert math.isclose(approx, expected, rel_tol=1e-9)

def test_taylor_series_ln():
    def ln_derivatives(k: int) -> float:
        if k == 0:
            return math.log(1)
        return (-1) ** (k -1) * (k -1)! if k > 0 else 0
    with pytest.raises(OverflowError):
        taylor_series(math.log, 1, 100, 2, ln_derivatives)

def test_taylor_series_error():
    def linear_derivatives(k: int) -> float:
        return 1.0 if k == 1 else 0.0
    approx = taylor_series(lambda x: x, 0, 2, 5, linear_derivatives)
    expected = 5.0
    assert math.isclose(approx, expected, rel_tol=1e-9)

def test_taylor_series_zero_terms():
    def any_derivatives(k: int) -> float:
        return 0.0
    approx = taylor_series(math.exp, 0, 0, 1, any_derivatives)
    expected = 0.0
    assert math.isclose(approx, expected, rel_tol=1e-9)

def test_taylor_series_negative_x():
    def exp_derivatives(k: int) -> float:
        return math.exp(0)
    approx = taylor_series(math.exp, 0, 10, -1, exp_derivatives)
    expected = math.exp(-1)
    assert math.isclose(approx, expected, rel_tol=1e-9)

def test_taylor_series_high_terms():
    def exp_derivatives(k: int) -> float:
        return math.exp(0)
    approx = taylor_series(math.exp, 0, 20, 1, exp_derivatives)
    expected = math.exp(1)
    assert math.isclose(approx, expected, rel_tol=1e-12)
