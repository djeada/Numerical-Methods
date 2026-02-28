import pytest
import numpy as np
from ..implementation.gauss_seidel import (
    inverse_matrix,
    solve_inverse_matrix,
    gauss_seidel,
)


def test_inverse_matrix_identity():
    A = np.eye(3)
    A_inv = inverse_matrix(A)
    assert np.allclose(A_inv, np.eye(3))


def test_inverse_matrix_simple():
    A = np.array([[4, 7], [2, 6]], dtype=float)
    expected = np.linalg.inv(A)
    A_inv = inverse_matrix(A)
    assert np.allclose(A_inv, expected)


def test_inverse_matrix_singular():
    A = np.array([[1, 2], [2, 4]], dtype=float)
    with pytest.raises(Exception):
        inverse_matrix(A)


def test_solve_inverse_matrix():
    A = np.array([[3, 0], [0, 2]], dtype=float)
    b = np.array([9, 8], dtype=float)
    expected = np.linalg.solve(A, b)
    x = solve_inverse_matrix(A, b)
    assert np.allclose(x, expected)


def test_solve_inverse_matrix_large():
    A = np.random.rand(5, 5)
    b = np.random.rand(5)
    x_expected = np.linalg.solve(A, b)
    x = solve_inverse_matrix(A, b)
    assert np.allclose(x, x_expected)


def test_gauss_seidel_convergence():
    A = np.array([[4, 1], [2, 3]], dtype=float)
    b = np.array([1, 2], dtype=float)
    expected = np.linalg.solve(A, b)
    x = gauss_seidel(A, b)
    assert np.allclose(x, expected, atol=1e-6)


def test_gauss_seidel_no_convergence():
    A = np.array([[1, 2], [3, 4]], dtype=float)
    b = np.array([5, 6], dtype=float)
    with pytest.raises(ValueError):
        gauss_seidel(A, b, max_iter=5)


def test_gauss_seidel_with_initial_guess():
    A = np.array([[3, 1], [1, 2]], dtype=float)
    b = np.array([9, 8], dtype=float)
    x0 = np.array([0, 0], dtype=float)
    expected = np.linalg.solve(A, b)
    x = gauss_seidel(A, b, x0=x0)
    assert np.allclose(x, expected, atol=1e-6)


def test_gauss_seidel_high_precision():
    A = np.array([[10, 1], [1, 10]], dtype=float)
    b = np.array([11, 11], dtype=float)
    expected = np.linalg.solve(A, b)
    x = gauss_seidel(A, b, epsilon=1e-12)
    assert np.allclose(x, expected, atol=1e-10)


def test_gauss_seidel_3x3_diag_dominant():
    A = np.array([[10, 2, 1], [1, 10, 2], [2, 1, 10]], dtype=float)
    b = np.array([13, 13, 13], dtype=float)
    expected = np.linalg.solve(A, b)
    x = gauss_seidel(A, b)
    assert np.allclose(x, expected, atol=1e-6)


def test_gauss_seidel_identity_matrix():
    A = np.eye(3)
    b = np.array([1.0, 2.0, 3.0])
    x = gauss_seidel(A, b)
    assert np.allclose(x, b, atol=1e-6)


def test_gauss_seidel_large_diagonal():
    A = np.array([[100, 1], [1, 100]], dtype=float)
    b = np.array([101, 101], dtype=float)
    expected = np.linalg.solve(A, b)
    x = gauss_seidel(A, b)
    assert np.allclose(x, expected, atol=1e-6)


def test_gauss_seidel_4x4_system():
    A = np.array([
        [10, -1, 2, 0],
        [-1, 11, -1, 3],
        [2, -1, 10, -1],
        [0, 3, -1, 8],
    ], dtype=float)
    b = np.array([6, 25, -11, 15], dtype=float)
    expected = np.linalg.solve(A, b)
    x = gauss_seidel(A, b)
    assert np.allclose(x, expected, atol=1e-5)


def test_gauss_seidel_negative_rhs():
    A = np.array([[5, 1], [1, 5]], dtype=float)
    b = np.array([-4, -4], dtype=float)
    expected = np.linalg.solve(A, b)
    x = gauss_seidel(A, b)
    assert np.allclose(x, expected, atol=1e-6)


def test_inverse_matrix_3x3():
    A = np.array([[1, 2, 3], [0, 1, 4], [5, 6, 0]], dtype=float)
    A_inv = inverse_matrix(A)
    assert np.allclose(A @ A_inv, np.eye(3), atol=1e-10)
