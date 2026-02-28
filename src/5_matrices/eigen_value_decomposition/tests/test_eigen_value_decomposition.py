# test_eigen_value_decomposition.py
import pytest
import numpy as np
from ..implementation.eigen_value_decomposition import (
    eigen_decomposition_full,
    eigen_decomposition_real_full,
)


def test_eigen_decomposition_identity():
    A = np.eye(3)
    P, D, P_inv = eigen_decomposition_full(A)
    assert np.allclose(P @ D @ P_inv, A)
    assert np.allclose(D, np.eye(3))
    assert np.allclose(P, np.eye(3))
    assert np.allclose(P_inv, np.eye(3))


def test_eigen_decomposition_diagonal():
    A = np.diag([1, 2, 3])
    P, D, P_inv = eigen_decomposition_full(A)
    assert np.allclose(P @ D @ P_inv, A)
    assert np.allclose(D, A)
    assert np.allclose(P, np.eye(3))
    assert np.allclose(P_inv, np.eye(3))


def test_eigen_decomposition_symmetric():
    A = np.array([[2, 1], [1, 2]], dtype=float)
    P, D, P_inv = eigen_decomposition_real_full(A)
    reconstructed = P @ D @ P_inv
    assert np.allclose(reconstructed, A)
    expected_eigenvalues = np.array([1, 3])
    assert np.allclose(np.sort(np.diag(D)), np.sort(expected_eigenvalues))
    assert np.allclose(P_inv, P.T)


def test_eigen_decomposition_non_symmetric():
    A = np.array([[0, 1], [-2, -3]], dtype=float)
    P, D, P_inv = eigen_decomposition_full(A)
    reconstructed = P @ D @ P_inv
    assert np.allclose(reconstructed, A)
    expected_eigenvalues = np.array([-1, -2])
    assert np.allclose(np.sort(D.diagonal()), np.sort(expected_eigenvalues))


def test_eigen_decomposition_complex():
    A = np.array([[0, -1], [1, 0]], dtype=float)
    P, D, P_inv = eigen_decomposition_full(A)
    reconstructed = P @ D @ P_inv
    assert np.allclose(reconstructed, A)
    expected_eigenvalues = np.array([1j, -1j])
    assert np.allclose(D.diagonal(), expected_eigenvalues)


def test_eigen_decomposition_real_non_symmetric():
    A = np.array([[1, 2], [3, 4]], dtype=float)
    with pytest.raises(ValueError):
        eigen_decomposition_real_full(A)


def test_eigen_decomposition_large_matrix():
    np.random.seed(0)
    A = np.random.rand(10, 10)
    P, D, P_inv = eigen_decomposition_full(A)
    reconstructed = P @ D @ P_inv
    assert np.allclose(reconstructed, A, atol=1e-6)


def test_eigen_decomposition_singular_matrix():
    A = np.array([[2, 4], [1, 2]], dtype=float)
    P, D, P_inv = eigen_decomposition_full(A)
    reconstructed = P @ D @ P_inv
    assert np.allclose(reconstructed, A)
    expected_eigenvalues = np.array([0, 4])
    assert np.allclose(np.sort(D.diagonal()), np.sort(expected_eigenvalues))


def test_eigen_decomposition_real_eigenvalues():
    A = np.array([[6, 0], [0, 1]], dtype=float)
    P, D, P_inv = eigen_decomposition_real_full(A)
    reconstructed = P @ D @ P_inv
    assert np.allclose(reconstructed, A)
    expected_eigenvalues = np.array([1, 6])
    assert np.allclose(np.sort(D.diagonal()), np.sort(expected_eigenvalues))


def test_eigen_decomposition_zero_matrix():
    A = np.zeros((3, 3))
    P, D, P_inv = eigen_decomposition_full(A)
    reconstructed = P @ D @ P_inv
    assert np.allclose(reconstructed, A)
    assert np.allclose(D, np.zeros((3, 3)))
    assert np.allclose(P @ P_inv, np.eye(3))


def test_eigen_decomposition_2x2_simple():
    A = np.array([[3, 1], [0, 2]], dtype=float)
    P, D, P_inv = eigen_decomposition_full(A)
    reconstructed = P @ D @ P_inv
    assert np.allclose(reconstructed, A)
    expected_eigenvalues = np.array([2, 3])
    assert np.allclose(np.sort(np.real(D.diagonal())), np.sort(expected_eigenvalues))


def test_eigen_decomposition_real_3x3():
    A = np.array([[2, -1, 0], [-1, 2, -1], [0, -1, 2]], dtype=float)
    P, D, P_inv = eigen_decomposition_real_full(A)
    reconstructed = P @ D @ P_inv
    assert np.allclose(reconstructed, A)
    assert np.allclose(P @ P.T, np.eye(3), atol=1e-10)


def test_eigen_decomposition_real_large_symmetric():
    np.random.seed(42)
    M = np.random.rand(5, 5)
    A = M + M.T
    P, D, P_inv = eigen_decomposition_real_full(A)
    reconstructed = P @ D @ P_inv
    assert np.allclose(reconstructed, A, atol=1e-8)


def test_eigen_decomposition_negative_eigenvalues():
    A = np.array([[-2, 0], [0, -3]], dtype=float)
    P, D, P_inv = eigen_decomposition_full(A)
    reconstructed = P @ D @ P_inv
    assert np.allclose(reconstructed, A)
    assert np.allclose(np.sort(D.diagonal()), np.array([-3, -2]))


def test_eigen_decomposition_full_preserves_eigenvalues():
    np.random.seed(7)
    A = np.random.rand(4, 4)
    P, D, P_inv = eigen_decomposition_full(A)
    computed_evals = np.sort_complex(D.diagonal())
    expected_evals = np.sort_complex(np.linalg.eigvals(A))
    assert np.allclose(computed_evals, expected_evals, atol=1e-8)
