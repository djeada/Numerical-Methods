# test_inverse_power_method.py
import pytest
import numpy as np
from ..implementation.inverse_power_method import inverse_power_method


def test_inverse_power_method_identity():
    A = np.eye(3)
    eigenvalue, eigenvector = inverse_power_method(A)
    assert np.isclose(eigenvalue, 1.0, atol=1e-5)
    assert np.isclose(np.linalg.norm(eigenvector), 1.0, atol=1e-5)
    assert np.isclose(eigenvalue, np.dot(eigenvector, A @ eigenvector), atol=1e-5)


def test_inverse_power_method_diagonal():
    A = np.diag([1, 3, 2])
    # Shift 0 targets the eigenvalue of smallest magnitude (1); the initial
    # guess has components along every eigenvector.
    x0 = np.array([1, 1, 1], dtype=float)
    eigenvalue, eigenvector = inverse_power_method(A, x0=x0)
    expected_eigenvalue = 1.0
    expected_eigenvector = np.array([1, 0, 0], dtype=float)
    assert np.isclose(
        eigenvalue, expected_eigenvalue, atol=1e-6
    ), f"Expected eigenvalue {expected_eigenvalue}, got {eigenvalue}"
    # Check if eigenvectors are proportional (allowing sign difference)
    assert np.allclose(eigenvector, expected_eigenvector, atol=1e-3) or np.allclose(
        eigenvector, -expected_eigenvector, atol=1e-3
    ), "Eigenvector does not match expected direction."


def test_inverse_power_method_symmetric():
    A = np.array([[2, 1], [1, 2]], dtype=float)
    eigenvalue, eigenvector = inverse_power_method(A)
    expected_eigenvalue = 1.0
    expected_eigenvector = np.array([-1, 1]) / np.sqrt(2)
    assert np.isclose(eigenvalue, expected_eigenvalue)
    assert np.allclose(np.abs(eigenvector), np.abs(expected_eigenvector), atol=1e-5)


def test_inverse_power_method_non_symmetric():
    A = np.array([[0, 1], [-2, -3]], dtype=float)
    eigenvalue, eigenvector = inverse_power_method(A)
    expected_eigenvalues = np.linalg.eigvals(A)
    smallest_eigenvalue = min(expected_eigenvalues, key=lambda x: np.abs(x))
    assert np.isclose(eigenvalue, smallest_eigenvalue)
    expected_eigenvector = np.linalg.eig(A)[1][
        :, np.argmin(np.abs(expected_eigenvalues))
    ]
    assert np.allclose(np.abs(eigenvector), np.abs(expected_eigenvector))


def test_inverse_power_method_singular_matrix():
    A = np.array([[2, 4], [1, 2]], dtype=float)
    with pytest.raises(ValueError):
        inverse_power_method(A)


def test_inverse_power_method_zero_matrix():
    A = np.zeros((3, 3))
    with pytest.raises(ValueError):
        inverse_power_method(A)


def test_inverse_power_method_rank_deficient():
    A = np.array([[1, 2, 3], [2, 4, 6], [3, 6, 9]], dtype=float)
    with pytest.raises(ValueError, match="singular"):
        inverse_power_method(A)


def test_inverse_power_method_single_element():
    A = np.array([[5]], dtype=float)
    eigenvalue, eigenvector = inverse_power_method(A)
    assert np.isclose(eigenvalue, 5.0)
    assert np.isclose(eigenvector, 1.0)


def test_inverse_power_method_random_matrix():
    np.random.seed(0)
    A = np.random.rand(4, 4) + 4 * np.eye(4)  # Ensure it's invertible
    eigenvalue, eigenvector = inverse_power_method(A)
    expected_eigenvalues = np.linalg.eigvals(A)
    smallest_eigenvalue = min(expected_eigenvalues, key=lambda x: np.abs(x))
    assert np.isclose(eigenvalue, smallest_eigenvalue, atol=1e-6)


def test_inverse_power_method_convergence():
    A = np.array([[4, 1], [2, 3]], dtype=float)
    eigenvalue, eigenvector = inverse_power_method(A)
    expected_eigenvalue = 2.0
    assert np.isclose(eigenvalue, expected_eigenvalue, atol=1e-4)


def test_inverse_power_method_non_convergent():
    # Defective matrix (single Jordan block): the iterates approach the only
    # eigenvector sublinearly, so even with the default tolerance and iteration
    # budget the eigenvalue estimate does not settle.
    A = np.array([[1, 1], [0, 1]], dtype=float)
    x0 = np.array([1, 1], dtype=float)
    with pytest.raises(ValueError, match="did not converge"):
        inverse_power_method(A, x0=x0)


def test_inverse_power_method_max_iterations_exhausted():
    # A well-conditioned problem still fails when given too few iterations.
    A = np.array([[4, 1], [2, 3]], dtype=float)
    x0 = np.array([1, 0], dtype=float)
    with pytest.raises(ValueError, match="did not converge"):
        inverse_power_method(A, x0=x0, tol=1e-14, max_iterations=2)


def test_inverse_power_method_initial_guess():
    A = np.array([[3, 2], [2, 3]], dtype=float)
    # Eigenvalues are 1 (vector [1, -1]) and 5; x0 is not an eigenvector.
    x0 = np.array([1, 0], dtype=float)
    eigenvalue, eigenvector = inverse_power_method(A, x0=x0)
    expected_eigenvalue = 1.0
    expected_eigenvector = np.array([1, -1]) / np.sqrt(2)
    assert np.isclose(
        eigenvalue, expected_eigenvalue, atol=1e-6
    ), f"Expected eigenvalue {expected_eigenvalue}, got {eigenvalue}"
    # Check proportionality
    assert np.allclose(eigenvector, expected_eigenvector, atol=1e-6) or np.allclose(
        eigenvector, -expected_eigenvector, atol=1e-6
    ), "Eigenvector does not match expected direction."


def test_inverse_power_method_shift():
    A = np.array([[4, 1], [2, 3]], dtype=float)
    shift = 1.0
    eigenvalue, eigenvector = inverse_power_method(A, shift=shift)
    expected_eigenvalue = 2.0
    assert np.isclose(eigenvalue, expected_eigenvalue, atol=1e-4)


def test_inverse_power_method_negative_eigenvalue():
    A = np.array([[-2, 0], [0, -3]], dtype=float)
    # With shift=0 the method would find -2 (closest to 0). A shift of -2.8 is
    # closer to -3 than to -2, so inverse iteration converges to -3 even though
    # the initial guess has a component along both eigenvectors.
    shift = -2.8
    x0 = np.array([1, 1], dtype=float)
    eigenvalue, eigenvector = inverse_power_method(A, shift=shift, x0=x0)
    expected_eigenvalue = -3.0
    expected_eigenvector = np.array([0, 1], dtype=float)
    assert np.isclose(
        eigenvalue, expected_eigenvalue, atol=1e-6
    ), f"Expected eigenvalue {expected_eigenvalue}, got {eigenvalue}"
    # Check proportionality
    assert np.allclose(eigenvector, expected_eigenvector, atol=1e-3) or np.allclose(
        eigenvector, -expected_eigenvector, atol=1e-3
    ), "Eigenvector does not match expected direction."


def test_inverse_power_method_complex_eigenvalues():
    A = np.array([[0, -1], [1, 0]], dtype=float)
    with pytest.raises(ValueError):
        inverse_power_method(A)


def test_inverse_power_method_high_dimensions():
    A = 11 * np.eye(10)
    x0 = np.random.rand(10)
    eigenvalue, eigenvector = inverse_power_method(A, x0=x0, max_iterations=10000)
    assert np.allclose(A @ eigenvector, eigenvalue * eigenvector, atol=1e-6)


def test_inverse_power_method_equidistant_eigenvalues():
    # Eigenvalues 1 and -1 are equally close to shift 0, so inverse iteration has
    # no dominant direction; the Rayleigh quotient settles on a non-eigenvalue
    # (-0.6) which must not be reported as converged.
    A = np.diag([1.0, -1.0])
    x0 = np.array([1.0, 2.0])
    with pytest.raises(ValueError, match="did not converge"):
        inverse_power_method(A, x0=x0)
