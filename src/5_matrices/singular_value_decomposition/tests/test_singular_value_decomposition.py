# test_singular_value_decomposition.py
import pytest
import numpy as np
from ..implementation.singular_value_decomposition import (
    singular_value_decomposition,
    singular_value_decomposition_reduced,
)


def test_svd_identity():
    A = np.eye(3)
    U, S, Vt = singular_value_decomposition(A)
    reconstructed = U @ S @ Vt
    assert np.allclose(reconstructed, A)
    assert np.allclose(U, np.eye(3))
    assert np.allclose(Vt, np.eye(3))
    assert np.allclose(S, np.eye(3))


def test_svd_diagonal():
    A = np.diag([1, 2, 3])
    U, S, Vt = singular_value_decomposition(A)
    reconstructed = U @ S @ Vt
    assert np.allclose(reconstructed, A), "Reconstruction failed"
    assert np.allclose(U @ U.T, np.eye(U.shape[0])), "U is not orthonormal"


def test_svd_symmetric():
    A = np.array([[4, 0], [0, 3]], dtype=float)
    U, S, Vt = singular_value_decomposition(A)
    reconstructed = U @ S @ Vt
    assert np.allclose(reconstructed, A)
    assert np.allclose(U @ U.T, np.eye(U.shape[0]))
    assert np.allclose(Vt @ Vt.T, np.eye(Vt.shape[0]))


def test_svd_non_square():
    A = np.random.rand(4, 3)
    U, S, Vt = singular_value_decomposition(A)
    reconstructed = U @ S @ Vt
    assert np.allclose(reconstructed, A, atol=1e-6)
    assert U.shape == (4, 4)
    assert S.shape == (4, 3)
    assert Vt.shape == (3, 3)


def test_svd_reduced():

    A = np.random.rand(5, 3)

    U, S_matrix, Vt = singular_value_decomposition_reduced(A)

    reconstructed = U @ S_matrix @ Vt

    assert np.allclose(reconstructed, A, atol=1e-6), "Reconstruction failed"

    assert U.shape == (5, 3), "Incorrect U shape"

    assert S_matrix.shape == (3, 3), "Incorrect S shape"

    assert Vt.shape == (3, 3), "Incorrect Vt shape"

    assert np.allclose(U.T @ U, np.eye(U.shape[1]), atol=1e-6), "U is not orthonormal"


def test_svd_rank_deficient():
    A = np.array([[2, 4], [1, 2]], dtype=float)
    U, S, Vt = singular_value_decomposition(A)
    reconstructed = U @ S @ Vt
    assert np.allclose(reconstructed, A)
    assert np.count_nonzero(S) == 1


def test_svd_zero_matrix():
    A = np.zeros((3, 3))
    U, S, Vt = singular_value_decomposition(A)
    reconstructed = U @ S @ Vt
    assert np.allclose(reconstructed, A)
    assert np.allclose(S, np.zeros((3, 3)))
    assert np.allclose(U @ U.T, np.eye(3))
    assert np.allclose(Vt @ Vt.T, np.eye(3))


def test_svd_random_matrix():
    np.random.seed(0)
    A = np.random.rand(6, 4)
    U, S, Vt = singular_value_decomposition(A)
    reconstructed = U @ S @ Vt
    assert np.allclose(reconstructed, A, atol=1e-6)
    assert U.shape == (6, 6)
    assert S.shape == (6, 4)
    assert Vt.shape == (4, 4)
    assert np.allclose(U @ U.T, np.eye(6))
    assert np.allclose(Vt @ Vt.T, np.eye(4))


def test_svd_reduced_random_matrix():
    np.random.seed(1)
    A = np.random.rand(5, 5)
    U, S, Vt = singular_value_decomposition_reduced(A)
    reconstructed = U @ S @ Vt
    assert np.allclose(reconstructed, A, atol=1e-6)
    assert U.shape == (5, 5)
    assert S.shape == (5, 5)
    assert Vt.shape == (5, 5)
    assert np.allclose(U @ U.T, np.eye(5))
    assert np.allclose(Vt @ Vt.T, np.eye(5))


def test_svd_reduced_non_square():

    A = np.random.rand(3, 5)

    U, S_matrix, Vt = singular_value_decomposition_reduced(A)

    reconstructed = U @ S_matrix @ Vt

    assert np.allclose(reconstructed, A, atol=1e-6), "Reconstruction failed"

    assert U.shape == (3, 3), "Incorrect U shape"

    assert S_matrix.shape == (3, 3), "Incorrect S shape"

    assert Vt.shape == (3, 5), "Incorrect Vt shape"


def test_svd_reduced_rank_deficient():
    A = np.array([[1, 2, 3], [2, 4, 6], [3, 6, 9]], dtype=float)
    U, S, Vt = singular_value_decomposition_reduced(A)
    reconstructed = U @ S @ Vt
    assert np.allclose(reconstructed, A), "Reconstruction failed"
    non_zero_singular_values = np.sum(np.diag(S) > 1e-10)
    assert non_zero_singular_values == 1, "Incorrect number of non-zero singular values"
