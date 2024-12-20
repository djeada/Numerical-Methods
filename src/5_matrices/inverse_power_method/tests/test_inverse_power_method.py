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
    # Set initial guess aligned with [1, 0, 0] to target eigenvalue 1
    x0 = np.array([1, 0, 0], dtype=float)
    eigenvalue, eigenvector = inverse_power_method(A, x0=x0)
    expected_eigenvalue = 1.0
    expected_eigenvector = np.array([1, 0, 0], dtype=float)
    assert np.isclose(eigenvalue, expected_eigenvalue, atol=1e-6), f"Expected eigenvalue {expected_eigenvalue}, got {eigenvalue}"
    # Check if eigenvectors are proportional (allowing sign difference)
    assert np.allclose(eigenvector, expected_eigenvector, atol=1e-6) or np.allclose(eigenvector, -expected_eigenvector, atol=1e-6), "Eigenvector does not match expected direction."

def test_inverse_power_method_symmetric():
    A = np.array([[2, 1], [1, 2]], dtype=float)
    eigenvalue, eigenvector = inverse_power_method(A)
    expected_eigenvalue = 1.0
    expected_eigenvector = np.array([-1, 1])/np.sqrt(2)
    assert np.isclose(eigenvalue, expected_eigenvalue)
    assert np.allclose(np.abs(eigenvector), np.abs(expected_eigenvector), atol=1e-5)


def test_inverse_power_method_non_symmetric():
    A = np.array([[0, 1], [-2, -3]], dtype=float)
    eigenvalue, eigenvector = inverse_power_method(A)
    expected_eigenvalues = np.linalg.eigvals(A)
    smallest_eigenvalue = min(expected_eigenvalues, key=lambda x: np.abs(x))
    assert np.isclose(eigenvalue, smallest_eigenvalue)
    expected_eigenvector = np.linalg.eig(A)[1][:, np.argmin(np.abs(expected_eigenvalues))]
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
    A = np.array([[1, 1], [0, 1]], dtype=float)
    with pytest.raises(ValueError):
        inverse_power_method(A, tol=1e-12, max_iterations=10)


def test_inverse_power_method_initial_guess():
    A = np.array([[3, 2], [2, 3]], dtype=float)
    # Set initial guess aligned with [1, -1] to target eigenvalue 1
    x0 = np.array([1, -1], dtype=float)
    eigenvalue, eigenvector = inverse_power_method(A, x0=x0)
    expected_eigenvalue = 1.0
    expected_eigenvector = np.array([1, -1]) / np.sqrt(2)
    assert np.isclose(eigenvalue, expected_eigenvalue, atol=1e-6), f"Expected eigenvalue {expected_eigenvalue}, got {eigenvalue}"
    # Check proportionality
    assert np.allclose(eigenvector, expected_eigenvector, atol=1e-6) or np.allclose(eigenvector, -expected_eigenvector, atol=1e-6), "Eigenvector does not match expected direction."


def test_inverse_power_method_shift():
    A = np.array([[4, 1], [2, 3]], dtype=float)
    shift = 1.0
    eigenvalue, eigenvector = inverse_power_method(A, shift=shift)
    expected_eigenvalue = 2.0
    assert np.isclose(eigenvalue, expected_eigenvalue, atol=1e-4)





def test_inverse_power_method_negative_eigenvalue():
    A = np.array([[-2, 0], [0, -3]], dtype=float)
    # Set shift near -inf to target eigenvalue -3
    shift = 0.0  # Since all eigenvalues are negative, shift=0 targets the smallest in magnitude, which is -2
    # To target -3, set shift slightly larger than -3, e.g., shift= -2.5
    shift = -2.5
    # Set initial guess aligned with [0,1] to target eigenvalue -3
    x0 = np.array([0, 1], dtype=float)
    eigenvalue, eigenvector = inverse_power_method(A, shift=shift, x0=x0)
    expected_eigenvalue = -3.0
    expected_eigenvector = np.array([0, 1], dtype=float)
    assert np.isclose(eigenvalue, expected_eigenvalue, atol=1e-6), f"Expected eigenvalue {expected_eigenvalue}, got {eigenvalue}"
    # Check proportionality
    assert np.allclose(eigenvector, expected_eigenvector, atol=1e-6) or np.allclose(eigenvector, -expected_eigenvector, atol=1e-6), "Eigenvector does not match expected direction."


def test_inverse_power_method_complex_eigenvalues():
    A = np.array([[0, -1], [1, 0]], dtype=float)
    with pytest.raises(ValueError):
        inverse_power_method(A)


def test_inverse_power_method_high_dimensions():
    A = 11 * np.eye(10)
    x0 = np.random.rand(10)
    eigenvalue, eigenvector = inverse_power_method(A, x0=x0, max_iterations=10000)
    assert np.allclose(A @ eigenvector, eigenvalue * eigenvector, atol=1e-6)
