# test_partial_differential_equations.py
import pytest
import numpy as np
from ..implementation.partial_differential_equations import (
    heat_equation_explicit,
    heat_equation_implicit,
    wave_equation_explicit,
    laplace_equation_2d,
)


def test_heat_explicit_constant_initial():
    x = np.linspace(0, 1, 11)
    u0 = np.zeros(len(x))
    t, x_out, u = heat_equation_explicit(u0, x, t_end=0.1, dt=0.001, alpha=0.01)
    assert np.allclose(u[-1], 0.0, atol=1e-10)


def test_heat_explicit_sine_initial():
    x = np.linspace(0, 1, 51)
    u0 = np.sin(np.pi * x)
    alpha = 0.01
    dt = 0.0001
    t_end = 0.1
    t, x_out, u = heat_equation_explicit(u0, x, t_end=t_end, dt=dt, alpha=alpha)
    expected = np.exp(-alpha * np.pi**2 * t_end) * np.sin(np.pi * x)
    assert np.allclose(u[-1], expected, atol=0.05)


def test_heat_explicit_preserves_boundary():
    x = np.linspace(0, 1, 21)
    u0 = np.sin(np.pi * x)
    t, x_out, u = heat_equation_explicit(
        u0, x, t_end=0.01, dt=0.0001, alpha=0.01, bc_left=0.0, bc_right=0.0
    )
    assert np.allclose(u[:, 0], 0.0, atol=1e-10)
    assert np.allclose(u[:, -1], 0.0, atol=1e-10)


def test_heat_explicit_stability_violation():
    x = np.linspace(0, 1, 11)
    u0 = np.sin(np.pi * x)
    with pytest.raises(ValueError):
        heat_equation_explicit(u0, x, t_end=0.1, dt=0.1, alpha=1.0)


def test_heat_explicit_invalid_dt():
    x = np.linspace(0, 1, 11)
    u0 = np.zeros(len(x))
    with pytest.raises(ValueError):
        heat_equation_explicit(u0, x, t_end=0.1, dt=0.0, alpha=0.01)


def test_heat_explicit_invalid_t_end():
    x = np.linspace(0, 1, 11)
    u0 = np.zeros(len(x))
    with pytest.raises(ValueError):
        heat_equation_explicit(u0, x, t_end=-0.1, dt=0.001, alpha=0.01)


def test_heat_explicit_invalid_alpha():
    x = np.linspace(0, 1, 11)
    u0 = np.zeros(len(x))
    with pytest.raises(ValueError):
        heat_equation_explicit(u0, x, t_end=0.1, dt=0.001, alpha=-0.01)


def test_heat_explicit_grid_too_small():
    x = np.linspace(0, 1, 2)
    u0 = np.zeros(2)
    with pytest.raises(ValueError):
        heat_equation_explicit(u0, x, t_end=0.1, dt=0.001, alpha=0.01)


def test_heat_explicit_mismatched_u0():
    x = np.linspace(0, 1, 11)
    u0 = np.zeros(5)
    with pytest.raises(ValueError):
        heat_equation_explicit(u0, x, t_end=0.1, dt=0.001, alpha=0.01)


def test_heat_implicit_constant_initial():
    x = np.linspace(0, 1, 11)
    u0 = np.zeros(len(x))
    t, x_out, u = heat_equation_implicit(u0, x, t_end=0.1, dt=0.001, alpha=0.01)
    assert np.allclose(u[-1], 0.0, atol=1e-10)


def test_heat_implicit_sine_initial():
    x = np.linspace(0, 1, 51)
    u0 = np.sin(np.pi * x)
    alpha = 0.01
    dt = 0.001
    t_end = 0.1
    t, x_out, u = heat_equation_implicit(u0, x, t_end=t_end, dt=dt, alpha=alpha)
    expected = np.exp(-alpha * np.pi**2 * t_end) * np.sin(np.pi * x)
    assert np.allclose(u[-1], expected, atol=0.05)


def test_heat_implicit_preserves_boundary():
    x = np.linspace(0, 1, 21)
    u0 = np.sin(np.pi * x)
    t, x_out, u = heat_equation_implicit(
        u0, x, t_end=0.01, dt=0.001, alpha=0.01, bc_left=0.0, bc_right=0.0
    )
    assert np.allclose(u[:, 0], 0.0, atol=1e-10)
    assert np.allclose(u[:, -1], 0.0, atol=1e-10)


def test_heat_implicit_no_stability_limit():
    x = np.linspace(0, 1, 11)
    u0 = np.sin(np.pi * x)
    t, x_out, u = heat_equation_implicit(u0, x, t_end=0.1, dt=0.1, alpha=1.0)
    assert u.shape[0] > 1
    assert np.isfinite(u).all()


def test_heat_implicit_invalid_dt():
    x = np.linspace(0, 1, 11)
    u0 = np.zeros(len(x))
    with pytest.raises(ValueError):
        heat_equation_implicit(u0, x, t_end=0.1, dt=-0.001, alpha=0.01)


def test_wave_explicit_zero_initial():
    x = np.linspace(0, 1, 21)
    u0 = np.zeros(len(x))
    v0 = np.zeros(len(x))
    t, x_out, u = wave_equation_explicit(u0, v0, x, t_end=0.1, dt=0.001, c=1.0)
    assert np.allclose(u[-1], 0.0, atol=1e-10)


def test_wave_explicit_preserves_boundary():
    x = np.linspace(0, 1, 51)
    u0 = np.sin(np.pi * x)
    v0 = np.zeros(len(x))
    dx = x[1] - x[0]
    c = 1.0
    dt = 0.5 * dx / c
    t, x_out, u = wave_equation_explicit(
        u0, v0, x, t_end=0.1, dt=dt, c=c, bc_left=0.0, bc_right=0.0
    )
    assert np.allclose(u[:, 0], 0.0, atol=1e-10)
    assert np.allclose(u[:, -1], 0.0, atol=1e-10)


def test_wave_explicit_cfl_violation():
    x = np.linspace(0, 1, 11)
    u0 = np.sin(np.pi * x)
    v0 = np.zeros(len(x))
    with pytest.raises(ValueError):
        wave_equation_explicit(u0, v0, x, t_end=0.1, dt=0.5, c=1.0)


def test_wave_explicit_invalid_dt():
    x = np.linspace(0, 1, 11)
    u0 = np.zeros(len(x))
    v0 = np.zeros(len(x))
    with pytest.raises(ValueError):
        wave_equation_explicit(u0, v0, x, t_end=0.1, dt=0.0, c=1.0)


def test_wave_explicit_invalid_c():
    x = np.linspace(0, 1, 11)
    u0 = np.zeros(len(x))
    v0 = np.zeros(len(x))
    with pytest.raises(ValueError):
        wave_equation_explicit(u0, v0, x, t_end=0.1, dt=0.001, c=-1.0)


def test_wave_explicit_mismatched_v0():
    x = np.linspace(0, 1, 11)
    u0 = np.zeros(len(x))
    v0 = np.zeros(5)
    with pytest.raises(ValueError):
        wave_equation_explicit(u0, v0, x, t_end=0.1, dt=0.001, c=1.0)


def test_laplace_2d_constant_boundary():
    def bc(X, Y):
        u = np.zeros_like(X)
        u[0, :] = 1.0
        u[-1, :] = 1.0
        u[:, 0] = 1.0
        u[:, -1] = 1.0
        return u

    x, y, u = laplace_equation_2d(11, 11, (0, 1), (0, 1), bc)
    assert np.allclose(u[1:-1, 1:-1], 1.0, atol=1e-4)


def test_laplace_2d_zero_boundary():
    def bc(X, Y):
        return np.zeros_like(X)

    x, y, u = laplace_equation_2d(11, 11, (0, 1), (0, 1), bc)
    assert np.allclose(u, 0.0, atol=1e-10)


def test_laplace_2d_invalid_grid():
    def bc(X, Y):
        return np.zeros_like(X)

    with pytest.raises(ValueError):
        laplace_equation_2d(2, 2, (0, 1), (0, 1), bc)


def test_laplace_2d_invalid_tol():
    def bc(X, Y):
        return np.zeros_like(X)

    with pytest.raises(ValueError):
        laplace_equation_2d(5, 5, (0, 1), (0, 1), bc, tol=-1e-6)


def test_laplace_2d_invalid_max_iter():
    def bc(X, Y):
        return np.zeros_like(X)

    with pytest.raises(ValueError):
        laplace_equation_2d(5, 5, (0, 1), (0, 1), bc, max_iter=0)


def test_laplace_2d_top_boundary_only():
    def bc(X, Y):
        u = np.zeros_like(X)
        u[-1, :] = 100.0
        return u

    x, y, u = laplace_equation_2d(21, 21, (0, 1), (0, 1), bc, tol=1e-6)
    assert u[-1, 5] == pytest.approx(100.0, abs=1e-10)
    assert u[0, 5] == pytest.approx(0.0, abs=1e-10)
    assert u[10, 5] > 0.0
    assert u[10, 5] < 100.0
