import pytest
import numpy as np
from ..implementation.inverse_matrix import inverse_matrix, solve_inverse_matrix


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
    A_inv = inverse_matrix(A)
    x_expected = np.linalg.solve(A, b)
    x = solve_inverse_matrix(A, b)
    assert np.allclose(x, x_expected)


def test_inverse_matrix_3x3():
    A = np.array([[1, 2, 3], [0, 1, 4], [5, 6, 0]], dtype=float)
    A_inv = inverse_matrix(A)
    assert np.allclose(A @ A_inv, np.eye(3), atol=1e-10)
    assert np.allclose(A_inv @ A, np.eye(3), atol=1e-10)


def test_inverse_matrix_4x4():
    A = np.array([[2, 1, 1, 0], [4, 3, 3, 1], [8, 7, 9, 5], [6, 7, 9, 8]], dtype=float)
    A_inv = inverse_matrix(A)
    assert np.allclose(A @ A_inv, np.eye(4), atol=1e-8)


def test_inverse_matrix_diagonal():
    A = np.diag([2.0, 5.0, 10.0])
    A_inv = inverse_matrix(A)
    expected = np.diag([0.5, 0.2, 0.1])
    assert np.allclose(A_inv, expected)


def test_inverse_matrix_symmetric():
    A = np.array([[4, 2], [2, 3]], dtype=float)
    A_inv = inverse_matrix(A)
    assert np.allclose(A @ A_inv, np.eye(2), atol=1e-10)
    assert np.allclose(A_inv, A_inv.T, atol=1e-10)


def test_inverse_matrix_negative_values():
    A = np.array([[-1, 2], [3, -4]], dtype=float)
    A_inv = inverse_matrix(A)
    assert np.allclose(A @ A_inv, np.eye(2), atol=1e-10)


def test_inverse_matrix_double_inverse():
    A = np.array([[1, 2], [3, 5]], dtype=float)
    A_inv = inverse_matrix(A)
    A_inv_inv = inverse_matrix(A_inv)
    assert np.allclose(A_inv_inv, A, atol=1e-10)


def test_solve_inverse_matrix_3x3():
    A = np.array([[1, 2, 3], [0, 1, 4], [5, 6, 0]], dtype=float)
    b = np.array([1, 2, 3], dtype=float)
    x = solve_inverse_matrix(A, b)
    assert np.allclose(A @ x, b, atol=1e-10)


def test_solve_inverse_matrix_identity():
    A = np.eye(3)
    b = np.array([1.0, 2.0, 3.0])
    x = solve_inverse_matrix(A, b)
    assert np.allclose(x, b)


def test_solve_inverse_matrix_diagonal():
    A = np.diag([2.0, 4.0, 8.0])
    b = np.array([6.0, 12.0, 24.0])
    x = solve_inverse_matrix(A, b)
    expected = np.array([3.0, 3.0, 3.0])
    assert np.allclose(x, expected)
