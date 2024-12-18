import pytest
import numpy as np
from implementation.inverse_matrix import inverse_matrix, solve_inverse_matrix

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
