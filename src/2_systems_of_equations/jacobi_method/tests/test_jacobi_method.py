# test_jacobi_method.py
import pytest
import numpy as np
from ..implementation.jacobi_method import jacobi_method


def test_jacobi_identity():
    A = np.eye(3)
    b = np.array([1, 2, 3], dtype=float)
    x = jacobi_method(A, b)
    expected = b
    assert np.allclose(x, expected)


def test_jacobi_diagonal():
    A = np.diag([2, 3, 4])
    b = np.array([4, 9, 16], dtype=float)
    x = jacobi_method(A, b)
    expected = np.array([2, 3, 4], dtype=float)
    assert np.allclose(x, expected)


def test_jacobi_symmetric_positive_definite():
    A = np.array([[4, 1, 2], [1, 3, 1], [2, 1, 3]], dtype=float)
    b = np.array([4, 5, 6], dtype=float)
    x = jacobi_method(A, b)
    expected = np.linalg.solve(A, b)
    assert np.allclose(x, expected, atol=1e-8)


def test_jacobi_non_diagonally_dominant():
    A = np.array([[1, 2], [3, 4]], dtype=float)
    b = np.array([5, 11], dtype=float)
    with pytest.raises(ValueError):
        jacobi_method(A, b, max_iterations=10)


def test_jacobi_convergence():
    A = np.array([[5, -2, 3], [-3, 9, 1], [2, -1, -7]], dtype=float)
    b = np.array([-1, 2, 3], dtype=float)
    x = jacobi_method(A, b)
    expected = np.linalg.solve(A, b)
    assert np.allclose(x, expected, atol=1e-6)


def test_jacobi_zero_diagonal():
    A = np.array([[0, 1], [1, 2]], dtype=float)
    b = np.array([1, 2], dtype=float)
    with pytest.raises(ValueError):
        jacobi_method(A, b)


def test_jacobi_large_system():
    np.random.seed(0)
    A = np.random.rand(10, 10) + 10 * np.eye(10)
    b = np.random.rand(10)
    x = jacobi_method(A, b)
    expected = np.linalg.solve(A, b)
    assert np.allclose(x, expected, atol=1e-8)


def test_jacobi_single_variable():
    A = np.array([[5]], dtype=float)
    b = np.array([10], dtype=float)
    x = jacobi_method(A, b)
    expected = np.array([2], dtype=float)
    assert np.allclose(x, expected)


def test_jacobi_multiple_iterations():
    A = np.array([[3, 1], [1, 2]], dtype=float)
    b = np.array([9, 8], dtype=float)
    x = jacobi_method(A, b, epsilon=1e-10, max_iterations=1000)
    expected = np.linalg.solve(A, b)
    assert np.allclose(x, expected, atol=1e-10)


def test_jacobi_no_initial_guess():
    A = np.array([[4, 1], [2, 3]], dtype=float)
    b = np.array([1, 2], dtype=float)
    x = jacobi_method(A, b)
    expected = np.linalg.solve(A, b)
    assert np.allclose(x, expected, atol=1e-8)


def test_jacobi_with_initial_guess():
    A = np.array([[4, 1], [2, 3]], dtype=float)
    b = np.array([1, 2], dtype=float)
    x0 = np.array([0, 0], dtype=float)
    x = jacobi_method(A, b, x0=x0)
    expected = np.linalg.solve(A, b)
    assert np.allclose(x, expected, atol=1e-8)


def test_jacobi_non_square():
    A = np.array([[1, 2, 3], [4, 5, 6]], dtype=float)
    b = np.array([7, 8], dtype=float)
    with pytest.raises(ValueError):
        jacobi_method(A, b)


def test_jacobi_no_solution():
    A = np.array([[1, 2], [2, 4]], dtype=float)
    b = np.array([3, 7], dtype=float)
    with pytest.raises(ValueError):
        jacobi_method(A, b, max_iterations=100)


def test_jacobi_zero_vector():
    A = np.array([[2, 1], [1, 3]], dtype=float)
    b = np.array([0, 0], dtype=float)
    x = jacobi_method(A, b)
    expected = np.array([0, 0], dtype=float)
    assert np.allclose(x, expected)


def test_jacobi_negative_values():
    A = np.array([[5, -2], [-1, 3]], dtype=float)
    b = np.array([7, 4], dtype=float)
    x = jacobi_method(A, b)
    expected = np.linalg.solve(A, b)
    assert np.allclose(x, expected, atol=1e-8)


def test_jacobi_fractional():
    A = np.array([[0.5, 0.2], [0.1, 0.3]], dtype=float)
    b = np.array([1.1, 0.7], dtype=float)
    x = jacobi_method(A, b)
    expected = np.linalg.solve(A, b)
    assert np.allclose(x, expected, atol=1e-8)


def test_jacobi_high_precision():
    A = np.array([[10, 1], [2, 10]], dtype=float)
    b = np.array([11, 12], dtype=float)
    x = jacobi_method(A, b, epsilon=1e-12, max_iterations=1000)
    expected = np.linalg.solve(A, b)
    assert np.allclose(x, expected, atol=1e-12)


def test_jacobi_non_convergent():
    A = np.array([[1, 2], [3, 4]], dtype=float)
    b = np.array([5, 6], dtype=float)
    with pytest.raises(ValueError):
        jacobi_method(A, b, epsilon=1e-10, max_iterations=50)
