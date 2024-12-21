# test_qr_method.py
import pytest
import numpy as np
from ..implementation.qr_method import (
    qr_decomposition,
    qr_algorithm,
    qr_algorithm_with_shifts,
)


def test_qr_decomposition_identity():
    A = np.eye(3)
    Q, R = qr_decomposition(A)
    assert np.allclose(Q @ R, A)
    assert np.allclose(Q, np.eye(3))
    assert np.allclose(R, np.eye(3))


def test_qr_decomposition_random():
    np.random.seed(0)
    A = np.random.rand(4, 4)
    Q, R = qr_decomposition(A)
    assert np.allclose(Q @ R, A, atol=1e-8)
    assert np.allclose(Q @ Q.T, np.eye(4), atol=1e-8)


def test_qr_algorithm_diagonal():
    A = np.diag([1, 2, 3])
    eigenvalues = qr_algorithm(A)
    expected = np.array([1, 2, 3])
    assert np.allclose(eigenvalues, expected, atol=1e-8)


def test_qr_algorithm_symmetric():
    A = np.array([[2, 1], [1, 2]], dtype=float)
    eigenvalues = qr_algorithm(A)
    expected = np.linalg.eigvalsh(A)
    assert np.allclose(np.sort(eigenvalues), np.sort(expected), atol=1e-8)


def test_qr_algorithm_non_symmetric():
    A = np.array([[0, 1], [-2, -3]], dtype=float)
    eigenvalues = qr_algorithm(A)
    expected = np.linalg.eigvals(A)
    assert np.allclose(np.sort(eigenvalues), np.sort(expected), atol=1e-6)


def test_qr_algorithm_with_shifts_diagonal():
    A = np.diag([4, 5, 6])
    eigenvalues = qr_algorithm_with_shifts(A)
    expected = np.array([4, 5, 6])
    assert np.allclose(eigenvalues, expected, atol=1e-8)


def test_qr_algorithm_with_shifts_symmetric():
    A = np.array([[3, 2], [2, 3]], dtype=float)
    eigenvalues = qr_algorithm_with_shifts(A)
    expected = np.linalg.eigvalsh(A)
    assert np.allclose(np.sort(eigenvalues), np.sort(expected), atol=1e-8)


def test_qr_algorithm_with_shifts_non_symmetric():
    A = np.array([[1, 2, 3], [0, 1, 4], [5, 6, 0]], dtype=float)
    eigenvalues = qr_algorithm_with_shifts(A)
    expected = np.linalg.eigvals(A)
    assert np.allclose(np.sort(eigenvalues), np.sort(expected), atol=1e-6)


def test_qr_algorithm_max_iterations():
    A = np.array([[1, 1], [0, 1]], dtype=float)
    with pytest.raises(ValueError):  # Correct error type
        qr_algorithm(A, max_iterations=1)


def test_qr_algorithm_with_shifts_max_iterations():
    A = np.array([[1, 1], [0, 1]], dtype=float)
    with pytest.raises(ValueError):  # Correct error type
        qr_algorithm_with_shifts(A, max_iterations=1)


def test_qr_algorithm_zero_matrix():
    A = np.zeros((3, 3))
    eigenvalues = qr_algorithm(A)
    expected = np.zeros(3)
    assert np.allclose(eigenvalues, expected, atol=1e-8)


def test_qr_algorithm_with_shifts_zero_matrix():
    A = np.zeros((4, 4))
    eigenvalues = qr_algorithm_with_shifts(A)
    expected = np.zeros(4)
    assert np.allclose(eigenvalues, expected, atol=1e-8)


def test_qr_algorithm_single_element():
    A = np.array([[5]], dtype=float)
    eigenvalues = qr_algorithm(A)
    expected = np.array([5])
    assert np.allclose(eigenvalues, expected, atol=1e-8)


def test_qr_algorithm_with_shifts_single_element():
    A = np.array([[7]], dtype=float)
    eigenvalues = qr_algorithm_with_shifts(A)
    expected = np.array([7])
    assert np.allclose(eigenvalues, expected, atol=1e-8)


def test_qr_algorithm_non_square():
    A = np.random.rand(3, 4)
    with pytest.raises(ValueError):
        qr_algorithm(A)


def test_qr_algorithm_with_shifts_non_square():
    A = np.random.rand(4, 5)
    with pytest.raises(ValueError):
        qr_algorithm_with_shifts(A)
