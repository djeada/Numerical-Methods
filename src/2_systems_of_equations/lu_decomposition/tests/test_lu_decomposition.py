# test_lu_decomposition.py
import pytest
import numpy as np
from ..implementation.lu_decomposition import lu_decomposition, solve_lu

def test_lu_decomposition_identity():
    A = np.eye(3)
    P, L, U = lu_decomposition(A)
    assert np.allclose(P @ L @ U, A)
    assert np.allclose(L, np.eye(3))
    assert np.allclose(U, np.eye(3))
    assert np.allclose(P, np.eye(3))

def test_lu_decomposition_diagonal():
    A = np.diag([2, 3, 4])
    P, L, U = lu_decomposition(A)
    assert np.allclose(P @ L @ U, A)
    assert np.allclose(L, np.eye(3))
    assert np.allclose(U, A)
    assert np.allclose(P, np.eye(3))

def test_lu_decomposition_random():
    np.random.seed(0)
    A = np.random.rand(4, 4)
    P, L, U = lu_decomposition(A)
    assert np.allclose(P @ L @ U, A, atol=1e-8)
    assert np.allclose(L @ U, P.T @ A, atol=1e-8)

def test_lu_decomposition_singular():
    A = np.array([[1, 2], [2, 4]], dtype=float)
    with pytest.raises(ValueError):
        lu_decomposition(A)

def test_lu_decomposition_non_square():
    A = np.array([[1, 2, 3], [4, 5, 6]], dtype=float)
    b = np.array([7, 8], dtype=float)
    with pytest.raises(ValueError):
        lu_decomposition(A)

def test_solve_lu_simple():
    A = np.array([[3, 2], [1, 2]], dtype=float)
    b = np.array([5, 5], dtype=float)
    P, L, U = lu_decomposition(A)
    x = solve_lu(P, L, U, b)
    expected = np.linalg.solve(A, b)
    assert np.allclose(x, expected)

def test_solve_lu_complex():
    A = np.array([[2, -1, 0], [1, 3, 1], [0, -1, 1]], dtype=float)
    b = np.array([1, 7, 3], dtype=float)
    P, L, U = lu_decomposition(A)
    x = solve_lu(P, L, U, b)
    expected = np.linalg.solve(A, b)
    assert np.allclose(x, expected, atol=1e-8)

def test_solve_lu_large_matrix():
    np.random.seed(1)
    A = np.random.rand(5, 5) + 5 * np.eye(5)
    b = np.random.rand(5)
    P, L, U = lu_decomposition(A)
    x = solve_lu(P, L, U, b)
    expected = np.linalg.solve(A, b)
    assert np.allclose(x, expected, atol=1e-8)

def test_solve_lu_zero_vector():
    A = np.array([[1, 2], [3, 4]], dtype=float)
    b = np.array([0, 0], dtype=float)
    P, L, U = lu_decomposition(A)
    x = solve_lu(P, L, U, b)
    expected = np.array([0, 0], dtype=float)
    assert np.allclose(x, expected)

def test_solve_lu_fractional():
    A = np.array([[0.5, 0.2], [0.1, 0.3]], dtype=float)
    b = np.array([1.1, 0.7], dtype=float)
    P, L, U = lu_decomposition(A)
    x = solve_lu(P, L, U, b)
    expected = np.linalg.solve(A, b)
    assert np.allclose(x, expected, atol=1e-8)

def test_solve_lu_negative_values():
    A = np.array([[2, -1], [-3, 4]], dtype=float)
    b = np.array([1, -2], dtype=float)
    P, L, U = lu_decomposition(A)
    x = solve_lu(P, L, U, b)
    expected = np.linalg.solve(A, b)
    assert np.allclose(x, expected, atol=1e-8)

def test_solve_lu_single_element():
    A = np.array([[5]], dtype=float)
    b = np.array([10], dtype=float)
    P, L, U = lu_decomposition(A)
    x = solve_lu(P, L, U, b)
    expected = np.array([2], dtype=float)
    assert np.allclose(x, expected)

def test_solve_lu_non_dominant():
    A = np.array([[1, 3], [2, 1]], dtype=float)
    b = np.array([5, 5], dtype=float)
    P, L, U = lu_decomposition(A)
    x = solve_lu(P, L, U, b)
    expected = np.linalg.solve(A, b)
    assert np.allclose(x, expected, atol=1e-8)

def test_lu_decomposition_with_integer_inputs():
    A = np.array([[2, 1], [5, 7]], dtype=int)
    b = np.array([11, 13], dtype=int)
    P, L, U = lu_decomposition(A)
    x = solve_lu(P, L, U, b)
    expected = np.linalg.solve(A.astype(float), b.astype(float))
    assert np.allclose(x, expected, atol=1e-8)

def test_solve_lu_multiple_solutions():
    A = np.array([[1, 2], [2, 4]], dtype=float)
    b = np.array([3, 6], dtype=float)
    with pytest.raises(ValueError):
        P, L, U = lu_decomposition(A)
        solve_lu(P, L, U, b)

def test_solve_lu_no_solution():
    A = np.array([[1, 2], [2, 4]], dtype=float)
    b = np.array([3, 5], dtype=float)
    with pytest.raises(ValueError):
        P, L, U = lu_decomposition(A)
        solve_lu(P, L, U, b)
