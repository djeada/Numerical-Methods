import pytest
import numpy as np
from ..implementation.eigenvalues_and_eigenvectors import (
    find_eigenvalues,
    find_eigenvectors,
)


def test_eigen_decomposition_identity():
    A = np.eye(3)
    eigenvalues = find_eigenvalues(A)
    expected_eigenvalues = np.array([1, 1, 1])
    assert np.allclose(np.sort(eigenvalues), np.sort(expected_eigenvalues))
    eigenvectors = find_eigenvectors(A)
    expected_eigenvectors = np.eye(3)
    for i in range(3):
        assert np.allclose(
            np.abs(eigenvectors[:, i]), np.abs(expected_eigenvectors[:, i]), rtol=1e-3
        )


def test_eigen_decomposition_diagonal():
    A = np.diag([2, 3, 4])
    eigenvalues = find_eigenvalues(A)
    expected_eigenvalues = np.array([2, 3, 4])
    assert np.allclose(np.sort(eigenvalues), np.sort(expected_eigenvalues))
    eigenvectors = find_eigenvectors(A)
    expected_eigenvectors = np.eye(3)
    for i in range(3):
        assert np.allclose(
            np.sort(np.abs(eigenvectors[:, i])),
            np.sort(np.abs(expected_eigenvectors[:, i])),
            atol=0.5,
        )


def test_eigen_decomposition_symmetric():
    A = np.array([[2, 1], [1, 2]], dtype=float)
    eigenvalues = find_eigenvalues(A)
    expected_eigenvalues = np.array([3, 1])
    assert np.allclose(np.sort(eigenvalues), np.sort(expected_eigenvalues))
    eigenvectors = find_eigenvectors(A)
    expected_eigenvectors = np.array([[1, -1], [1, 1]]) / np.sqrt(2)
    for i in range(2):
        assert np.allclose(
            np.abs(eigenvectors[:, i]), np.abs(expected_eigenvectors[:, i])
        )


def test_eigen_decomposition_random():
    np.random.seed(0)
    A = np.random.rand(4, 4)
    eigenvalues = find_eigenvalues(A)
    expected_eigenvalues = np.linalg.eigvals(A)
    assert np.allclose(
        np.sort_complex(eigenvalues), np.sort_complex(expected_eigenvalues), atol=1e-3
    )
    eigenvectors = find_eigenvectors(A)
    expected_eigenvectors = np.linalg.eig(A)[1]
    for i in range(A.shape[0]):
        assert np.allclose(
            np.sort(np.abs(eigenvectors[:, i])),
            np.sort(np.abs(expected_eigenvectors[:, i])),
            atol=0.5,
        )


def test_eigen_decomposition_singular():
    A = np.array([[2, 4], [1, 2]], dtype=float)
    eigenvalues = find_eigenvalues(A)
    expected_eigenvalues = np.linalg.eigvals(A)
    assert np.allclose(np.sort(eigenvalues), np.sort(expected_eigenvalues), atol=1e-3)
    eigenvectors = find_eigenvectors(A)
    expected_eigenvectors = np.linalg.eig(A)[1]
    for i in range(2):
        assert np.allclose(
            np.abs(eigenvectors[:, i]), np.abs(expected_eigenvectors[:, i]), atol=1e-3
        )


def test_eigen_decomposition_zero_matrix():
    A = np.zeros((3, 3), dtype=float)
    eigenvalues = find_eigenvalues(A)
    expected_eigenvalues = np.array([0, 0, 0])
    assert np.allclose(np.sort(eigenvalues), np.sort(expected_eigenvalues))
    eigenvectors = find_eigenvectors(A)
    for i in range(3):
        assert not np.allclose(eigenvectors[:, i], 0)


def test_eigen_decomposition_non_square():
    A = np.array([[1, 2, 3], [4, 5, 6]], dtype=float)
    with pytest.raises(ValueError):
        find_eigenvalues(A)


def test_eigen_decomposition_complex_eigenvalues():
    A = np.array([[0, -1], [1, 0]], dtype=float)
    eigenvalues = find_eigenvalues(A)
    expected_eigenvalues = np.array([1j, -1j])
    assert np.allclose(
        np.sort_complex(eigenvalues), np.sort_complex(expected_eigenvalues)
    )
    eigenvectors = find_eigenvectors(A)
    expected_eigenvectors = np.linalg.eig(A)[1]
    for i in range(2):
        assert np.allclose(
            np.abs(eigenvectors[:, i]), np.abs(expected_eigenvectors[:, i]), atol=1e-3
        )


@pytest.mark.skip()
def test_eigen_decomposition_repeated_eigenvalues():
    A = np.array([[3, 0, 0], [0, 3, 0], [0, 0, 3]], dtype=float)
    eigenvalues = find_eigenvalues(A)
    expected_eigenvalues = np.array([3, 3, 3])
    assert np.allclose(np.sort(eigenvalues), np.sort(expected_eigenvalues))
    eigenvectors = find_eigenvectors(A)
    expected_eigenvectors = np.eye(3)
    for i in range(3):
        assert np.allclose(
            np.abs(eigenvectors[:, i]), np.abs(expected_eigenvectors[:, i]), rtol=1e-3
        )


def test_eigen_decomposition_large_matrix():
    np.random.seed(1)
    A = np.random.rand(5, 5)
    eigenvalues = find_eigenvalues(A)
    expected_eigenvalues = np.linalg.eigvals(A)
    assert np.allclose(
        np.sort_complex(eigenvalues), np.sort_complex(expected_eigenvalues), atol=1e-3
    )
    eigenvectors = find_eigenvectors(A)
    expected_eigenvectors = np.linalg.eig(A)[1]
    for i in range(5):
        assert np.allclose(
            np.sort(np.abs(eigenvectors[:, i])),
            np.sort(np.abs(expected_eigenvectors[:, i])),
            atol=0.5,
        )


def test_eigenvalues_negative_matrix():
    A = np.array([[-1, 0], [0, -2]], dtype=float)
    eigenvalues = find_eigenvalues(A)
    expected = np.array([-2, -1])
    assert np.allclose(np.sort(np.real(eigenvalues)), np.sort(expected))


def test_eigenvalues_upper_triangular():
    A = np.array([[1, 3, 5], [0, 2, 4], [0, 0, 3]], dtype=float)
    eigenvalues = find_eigenvalues(A)
    expected = np.array([1, 2, 3])
    assert np.allclose(np.sort(np.real(eigenvalues)), np.sort(expected), atol=1e-3)


def test_eigenvectors_diagonal():
    A = np.diag([5.0, 10.0])
    eigenvectors = find_eigenvectors(A)
    for i in range(2):
        v = eigenvectors[:, i]
        assert np.linalg.norm(v) > 0


def test_eigenvalues_1x1():
    A = np.array([[7.0]])
    eigenvalues = find_eigenvalues(A)
    assert np.allclose(eigenvalues, np.array([7.0]))


def test_eigenvectors_verify_equation():
    A = np.array([[4, 1], [2, 3]], dtype=float)
    eigenvalues = find_eigenvalues(A)
    eigenvectors = find_eigenvectors(A)
    for i in range(A.shape[0]):
        lam = eigenvalues[i]
        v = eigenvectors[:, i]
        if np.linalg.norm(v) > 1e-10:
            Av = A @ v
            lv = lam * v
            assert np.allclose(Av, lv, atol=0.5)
