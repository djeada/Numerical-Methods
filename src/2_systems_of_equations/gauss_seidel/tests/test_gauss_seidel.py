import pytest
import numpy as np
from ..implementation.gauss_seidel import gauss_seidel


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
        gauss_seidel(A, b, max_iterations=5)


def test_gauss_seidel_max_iter_deprecated_alias():
    A = np.array([[1, 2], [3, 4]], dtype=float)
    b = np.array([5, 6], dtype=float)
    with pytest.warns(DeprecationWarning, match="max_iterations"):
        with pytest.raises(ValueError, match="did not converge"):
            gauss_seidel(A, b, max_iter=5)
    # The alias really is applied: one sweep is not enough, many are.
    A = np.array([[4, 1], [2, 3]], dtype=float)
    b = np.array([1, 2], dtype=float)
    with pytest.warns(DeprecationWarning):
        with pytest.raises(ValueError):
            gauss_seidel(A, b, max_iter=1)
    assert np.allclose(gauss_seidel(A, b, max_iterations=100), np.linalg.solve(A, b))


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
    A = np.array(
        [
            [10, -1, 2, 0],
            [-1, 11, -1, 3],
            [2, -1, 10, -1],
            [0, 3, -1, 8],
        ],
        dtype=float,
    )
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


def test_gauss_seidel_non_square():
    A = np.array([[1, 2, 3], [4, 5, 6]], dtype=float)
    b = np.array([7, 8], dtype=float)
    with pytest.raises(ValueError):
        gauss_seidel(A, b)


def test_gauss_seidel_zero_diagonal():
    A = np.array([[0, 1], [1, 2]], dtype=float)
    b = np.array([1, 2], dtype=float)
    with pytest.raises(ValueError):
        gauss_seidel(A, b)


def test_gauss_seidel_does_not_modify_x0():
    A = np.array([[4, 1], [2, 3]], dtype=float)
    b = np.array([1, 2], dtype=float)
    x0 = np.array([5.0, 5.0])
    gauss_seidel(A, b, x0=x0)
    assert np.array_equal(x0, [5.0, 5.0])


def test_gauss_seidel_converges_for_spd_where_jacobi_diverges():
    # SPD but not diagonally dominant: Gauss-Seidel is guaranteed to converge
    # for SPD matrices (Jacobi diverges on this one, see the Jacobi tests).
    A = np.full((3, 3), 0.9) + 0.1 * np.eye(3)
    b = np.array([1.0, 2.0, 3.0])
    x = gauss_seidel(A, b, epsilon=1e-10, max_iterations=10000)
    assert np.allclose(x, np.linalg.solve(A, b), atol=1e-6)
