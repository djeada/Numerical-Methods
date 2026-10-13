# test_gaussian_elimination.py
import pytest
import numpy as np
from ..implementation.gaussian_elimination import (
    gaussian_elimination,
    solve_gaussian_elimination,
)


def test_gaussian_elimination_identity():
    A = np.eye(3)
    b = np.array([1, 2, 3], dtype=float)
    x = gaussian_elimination(A, b)
    expected = b
    assert np.allclose(x, expected)


def test_gaussian_elimination_diagonal():
    A = np.diag([2, 3, 4])
    b = np.array([4, 9, 16], dtype=float)
    x = gaussian_elimination(A, b)
    expected = np.array([2, 3, 4], dtype=float)
    assert np.allclose(x, expected)


def test_gaussian_elimination_random():
    np.random.seed(0)
    A = np.random.rand(5, 5)
    b = np.random.rand(5)
    x = gaussian_elimination(A, b)
    expected = np.linalg.solve(A, b)
    assert np.allclose(x, expected, atol=1e-8)


def test_gaussian_elimination_singular():
    A = np.array([[1, 2], [2, 4]], dtype=float)
    b = np.array([3, 6], dtype=float)
    with pytest.raises(ValueError):
        gaussian_elimination(A, b)


def test_gaussian_elimination_non_square():
    A = np.array([[1, 2, 3], [4, 5, 6]], dtype=float)
    b = np.array([7, 8], dtype=float)
    with pytest.raises(ValueError):
        gaussian_elimination(A, b)


def test_gaussian_elimination_zero_vector():
    A = np.array([[1, 2], [3, 4]], dtype=float)
    b = np.array([0, 0], dtype=float)
    x = gaussian_elimination(A, b)
    expected = np.array([0, 0], dtype=float)
    assert np.allclose(x, expected)


def test_gaussian_elimination_large_matrix():
    np.random.seed(1)
    A = np.random.rand(10, 10)
    b = np.random.rand(10)
    x = gaussian_elimination(A, b)
    expected = np.linalg.solve(A, b)
    assert np.allclose(x, expected, atol=1e-8)


def test_gaussian_elimination_least_squares():
    A = np.array([[1, 1], [1, 1], [1, 1]], dtype=float)
    b = np.array([2, 2, 2], dtype=float)
    with pytest.raises(ValueError):
        gaussian_elimination(A, b)


def test_solve_gaussian_elimination_simple():
    A = np.array([[3, 2], [1, 2]], dtype=float)
    b = np.array([5, 5], dtype=float)
    x = solve_gaussian_elimination(A, b)
    expected = np.array([0, 2.5], dtype=float)
    assert np.allclose(x, expected, atol=1e-8)


def test_solve_gaussian_elimination_complex():
    A = np.array([[2, -1, 0], [1, 3, 1], [0, -1, 1]], dtype=float)
    b = np.array([1, 7, 3], dtype=float)
    x = solve_gaussian_elimination(A, b)
    expected = np.linalg.solve(A, b)
    assert np.allclose(x, expected, atol=1e-8)


def test_gaussian_elimination_fractional():
    A = np.array([[0.5, 2.5], [1.5, -0.5]], dtype=float)
    b = np.array([1.0, 0.0], dtype=float)
    x = gaussian_elimination(A, b)
    expected = np.linalg.solve(A, b)
    assert np.allclose(x, expected, atol=1e-8)


def test_gaussian_elimination_negative_values():
    A = np.array([[2, -1], [-3, 4]], dtype=float)
    b = np.array([1, -2], dtype=float)
    x = gaussian_elimination(A, b)
    expected = np.linalg.solve(A, b)
    assert np.allclose(x, expected, atol=1e-8)


def test_gaussian_elimination_decimal_precision():
    A = np.array([[1.0000001, 2.0000001], [3.0000001, 4.0000001]], dtype=float)
    b = np.array([5.0000001, 11.0000001], dtype=float)
    x = gaussian_elimination(A, b)
    expected = np.linalg.solve(A, b)
    assert np.allclose(x, expected, atol=1e-6)


def test_gaussian_elimination_with_integer_inputs():
    A = np.array([[2, 1], [5, 7]], dtype=int)
    b = np.array([11, 13], dtype=int)
    x = gaussian_elimination(A, b)
    expected = np.linalg.solve(A.astype(float), b.astype(float))
    assert np.allclose(x, expected, atol=1e-8)


def test_gaussian_elimination_with_float_inputs():
    A = np.array([[1.5, 2.5], [3.5, 4.5]], dtype=float)
    b = np.array([5.5, 11.5], dtype=float)
    x = gaussian_elimination(A, b)
    expected = np.linalg.solve(A, b)
    assert np.allclose(x, expected, atol=1e-8)


def test_solve_gaussian_elimination_multiple_solutions():
    A = np.array([[1, 2], [2, 4]], dtype=float)
    b = np.array([3, 6], dtype=float)
    with pytest.raises(ValueError):
        solve_gaussian_elimination(A, b)


def test_solve_gaussian_elimination_no_solution():
    A = np.array([[1, 2], [2, 4]], dtype=float)
    b = np.array([3, 5], dtype=float)
    with pytest.raises(ValueError):
        solve_gaussian_elimination(A, b)


def test_gaussian_elimination_small_scale_not_singular():
    A = 1e-10 * np.eye(2)
    b = np.array([1e-10, 2e-10])
    x = gaussian_elimination(A, b)
    assert np.allclose(x, [1.0, 2.0])


def test_gaussian_elimination_does_not_modify_inputs():
    A = np.array([[2.0, 1.0], [5.0, 7.0]])
    b = np.array([11.0, 13.0])
    A0, b0 = A.copy(), b.copy()
    gaussian_elimination(A, b)
    assert np.array_equal(A, A0) and np.array_equal(b, b0)
