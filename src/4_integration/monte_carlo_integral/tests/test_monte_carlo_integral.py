# test_monte_carlo_integral.py
import pytest
import numpy as np
from ..implementation.monte_carlo_integral import (
    monte_carlo_integral,
    monte_carlo_integral_multidim,
)


def test_monte_carlo_integral_constant():
    f = lambda x: 5.0
    a, b = 0.0, 10.0
    result = monte_carlo_integral(f, a, b, num_samples=100000)
    expected = 5.0 * (b - a)
    assert np.isclose(result, expected, rtol=1e-12)


def test_monte_carlo_integral_linear():
    f = lambda x: 2.0 * x + 3.0
    a, b = 0.0, 5.0
    result = monte_carlo_integral(f, a, b, num_samples=100000)
    expected = 2.0 * (b**2 - a**2) / 2 + 3.0 * (b - a)
    assert np.isclose(result, expected, rtol=5e-3)


def test_monte_carlo_integral_quadratic():
    f = lambda x: x**2
    a, b = 0.0, 3.0
    result = monte_carlo_integral(f, a, b, num_samples=1000000)
    expected = (b**3 - a**3) / 3
    assert np.isclose(result, expected, rtol=4e-3)


def test_monte_carlo_integral_sin():
    f = np.sin
    a, b = 0.0, np.pi
    result = monte_carlo_integral(f, a, b, num_samples=1000000)
    expected = 2.0
    assert np.isclose(result, expected, rtol=2e-3)


def test_monte_carlo_integral_multidim_constant():
    f = lambda x: 4.0
    bounds = ((0.0, 1.0), (0.0, 1.0))
    result = monte_carlo_integral_multidim(f, bounds, num_samples=100000)
    expected = 4.0 * 1.0 * 1.0
    assert np.isclose(result, expected, rtol=1e-12)


def test_monte_carlo_integral_multidim_linear():
    f = lambda x: x[0] + x[1]
    bounds = ((0.0, 2.0), (0.0, 3.0))
    result = monte_carlo_integral_multidim(f, bounds, num_samples=1000000)
    expected = 15
    assert np.isclose(result, expected, rtol=2e-3)


def test_monte_carlo_integral_multidim_quadratic():
    f = lambda x: x[0] ** 2 + x[1] ** 2
    bounds = ((0.0, 1.0), (0.0, 1.0))
    result = monte_carlo_integral_multidim(f, bounds, num_samples=1000000)
    expected = 1 / 3 + 1 / 3
    assert np.isclose(result, expected, rtol=3e-3)


def test_monte_carlo_integral_multidim_sin():
    f = lambda x: np.sin(x[0]) * np.sin(x[1])
    bounds = ((0.0, np.pi), (0.0, np.pi))
    result = monte_carlo_integral_multidim(f, bounds, num_samples=1000000)
    expected = 4.0
    assert np.isclose(result, expected, rtol=3e-3)


def test_monte_carlo_integral_zero_samples():
    f = lambda x: x
    a, b = 0.0, 1.0
    with pytest.raises(ValueError):
        monte_carlo_integral(f, a, b, num_samples=0)


def test_monte_carlo_integral_multidim_zero_samples():
    f = lambda x: x[0]
    bounds = ((0.0, 1.0),)
    with pytest.raises(ValueError):
        monte_carlo_integral_multidim(f, bounds, num_samples=0)


def test_monte_carlo_integral_negative_bounds():
    f = lambda x: x**2
    a, b = -2.0, 2.0
    result = monte_carlo_integral(f, a, b, num_samples=1000000)
    expected = 2 * (2.0**3) / 3
    assert np.isclose(result, expected, rtol=4e-3)


def test_monte_carlo_integral_narrow_range():
    f = lambda x: 1.0
    a, b = 0.0, 0.01
    result = monte_carlo_integral(f, a, b, num_samples=10000)
    expected = 0.01
    assert np.isclose(result, expected, rtol=1e-12)


def test_monte_carlo_integral_exponential():
    f = lambda x: np.exp(x)
    a, b = 0.0, 1.0
    result = monte_carlo_integral(f, a, b, num_samples=1000000)
    expected = np.e - 1
    assert np.isclose(result, expected, rtol=1.5e-3)


def test_monte_carlo_integral_negative_samples():
    f = lambda x: x
    a, b = 0.0, 1.0
    with pytest.raises(ValueError):
        monte_carlo_integral(f, a, b, num_samples=-1)


def test_monte_carlo_integral_multidim_3d():
    f = lambda x: 1.0
    bounds = ((0.0, 1.0), (0.0, 1.0), (0.0, 1.0))
    result = monte_carlo_integral_multidim(f, bounds, num_samples=100000)
    expected = 1.0
    assert np.isclose(result, expected, rtol=1e-12)


# The standard error of the estimate is V * std(f) / sqrt(N); the tolerances
# above are about four standard errors for the fixed default seed.


def test_monte_carlo_integral_default_seed_is_deterministic():
    f = np.sin
    first = monte_carlo_integral(f, 0.0, np.pi, num_samples=1000)
    second = monte_carlo_integral(f, 0.0, np.pi, num_samples=1000)
    assert first == second
    assert first == monte_carlo_integral(f, 0.0, np.pi, num_samples=1000, seed=0)


def test_monte_carlo_integral_seed_changes_samples():
    f = np.sin
    r1 = monte_carlo_integral(f, 0.0, np.pi, num_samples=1000, seed=1)
    r2 = monte_carlo_integral(f, 0.0, np.pi, num_samples=1000, seed=2)
    assert r1 != r2
    # 1000 samples: std error = pi * std(sin) / sqrt(N) ~ 0.04; allow ~5 sigma.
    assert abs(r1 - 2.0) < 0.2
    assert abs(r2 - 2.0) < 0.2


def test_monte_carlo_integral_seed_none_is_valid():
    f = lambda x: x**2
    result = monte_carlo_integral(f, 0.0, 1.0, num_samples=100000, seed=None)
    # std error ~ 0.298 / sqrt(1e5) ~ 9.4e-4; allow ~6 sigma.
    assert abs(result - 1 / 3) < 6e-3


def test_monte_carlo_integral_multidim_seed():
    f = lambda x: x[0] + x[1]
    bounds = ((0.0, 1.0), (0.0, 1.0))
    a = monte_carlo_integral_multidim(f, bounds, num_samples=1000, seed=3)
    b = monte_carlo_integral_multidim(f, bounds, num_samples=1000, seed=3)
    c = monte_carlo_integral_multidim(f, bounds, num_samples=1000, seed=4)
    assert a == b
    assert a != c


def test_monte_carlo_integral_error_scales_as_inverse_sqrt_n():
    # Averaged over seeds, the RMS error should drop by about 10x for 100x samples.
    f = lambda x: x**2
    exact = 1 / 3

    def rms(n):
        errs = [monte_carlo_integral(f, 0.0, 1.0, n, seed=s) - exact for s in range(40)]
        return np.sqrt(np.mean(np.square(errs)))

    ratio = rms(1000) / rms(100000)
    assert 5.0 < ratio < 20.0
