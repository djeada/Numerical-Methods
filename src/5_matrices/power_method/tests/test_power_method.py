
# test_power_method.py
import pytest
import numpy as np
from implementation.power_method import power_method

def test_power_method_identity():
    A = np.eye(3)
    eigenvalue, eigenvector = power_method(A)
    assert np.isclose(eigenvalue, 1.0)
    assert np.allclose(np.abs(eigenvector), np.ones(3)/np.sqrt(3))

def test_power_method_diagonal():
    A = np.diag([1, 3, 2])
    eigenvalue, eigenvector = power_method(A)
    assert np.isclose(eigenvalue, 3.0)
    assert np.allclose(eigenvector, np.array([0, 1, 0]))

def test_power_method_symmetric():
    A = np.array([[2, 1], [1, 2]], dtype=float)
    eigenvalue, eigenvector = power_method(A)
    expected_eigenvalue = 3.0
    expected_eigenvector = np.array([1, 1])/np.sqrt(2)
    assert np.isclose(eigenvalue, expected_eigenvalue)
    assert np.allclose(np.abs(eigenvector), np.abs(expected_eigenvector))

def test_power_method_non_symmetric():
    A = np.array([[0, 1], [-2, -3]], dtype=float)
    eigenvalue, eigenvector = power_method(A)
    expected_eigenvalues = np.linalg.eigvals(A)
    dominant_eigenvalue = max(expected_eigenvalues, key=lambda x: np.abs(x))
    assert np.isclose(eigenvalue, dominant_eigenvalue)
    expected_eigenvector = np.linalg.eig(A)[1][:, np.argmax(np.abs(expected_eigenvalues))]
    assert np.allclose(np.abs(eigenvector), np.abs(expected_eigenvector))

def test_power_method_singular_matrix():
    A = np.array([[2, 4], [1, 2]], dtype=float)
    eigenvalue, eigenvector = power_method(A)
    expected_eigenvalues = np.linalg.eigvals(A)
    dominant_eigenvalue = max(expected_eigenvalues, key=lambda x: np.abs(x))
    assert np.isclose(eigenvalue, dominant_eigenvalue)
    expected_eigenvector = np.linalg.eig(A)[1][:, np.argmax(np.abs(expected_eigenvalues))]
    assert np.allclose(np.abs(eigenvector), np.abs(expected_eigenvector))

def test_power_method_zero_matrix():
    A = np.zeros((3, 3))
    with pytest.raises(ValueError):
        power_method(A)

def test_power_method_rank_deficient():
    A = np.array([[1, 2, 3], [2, 4, 6], [3, 6, 9]], dtype=float)
    eigenvalue, eigenvector = power_method(A)
    assert np.isclose(eigenvalue, 14.0)
    expected_eigenvector = np.array([1, 2, 3])/np.sqrt(14)
    assert np.allclose(np.abs(eigenvector), np.abs(expected_eigenvector))

def test_power_method_single_element():
    A = np.array([[5]], dtype=float)
    eigenvalue, eigenvector = power_method(A)
    assert np.isclose(eigenvalue, 5.0)
    assert np.isclose(eigenvector, 1.0)

def test_power_method_random_matrix():
    np.random.seed(0)
    A = np.random.rand(4, 4)
    eigenvalue, eigenvector = power_method(A)
    expected_eigenvalue = max(np.linalg.eigvals(A), key=lambda x: np.abs(x))
    assert np.isclose(eigenvalue, expected_eigenvalue, atol=1e-6)

def test_power_method_convergence():
    A = np.array([[4, 1], [2, 3]], dtype=float)
    eigenvalue, eigenvector = power_method(A, tol=1e-10, max_iterations=1000)
    expected_eigenvalue = 5.0
    expected_eigenvector = np.array([1, 1])/np.sqrt(2)
    assert np.isclose(eigenvalue, expected_eigenvalue)
    assert np.allclose(np.abs(eigenvector), np.abs(expected_eigenvector))

def test_power_method_non_convergent():
    A = np.array([[1, 1], [0, 1]], dtype=float)
    with pytest.raises(ValueError):
        power_method(A, tol=1e-12, max_iterations=10)

def test_power_method_initial_guess():
    A = np.array([[3, 2], [2, 3]], dtype=float)
    x0 = np.array([1, 0], dtype=float)
    eigenvalue, eigenvector = power_method(A, x0=x0)
    expected_eigenvalue = 5.0
    expected_eigenvector = np.array([1, 1])/np.sqrt(2)
    assert np.isclose(eigenvalue, expected_eigenvalue)
    assert np.allclose(np.abs(eigenvector), np.abs(expected_eigenvector))

def test_power_method_negative_eigenvalue():
    A = np.array([[-2, 0], [0, -3]], dtype=float)
    eigenvalue, eigenvector = power_method(A)
    expected_eigenvalue = -2.0
    expected_eigenvector = np.array([1, 0])
    assert np.isclose(eigenvalue, expected_eigenvalue)
    assert np.allclose(np.abs(eigenvector), np.abs(expected_eigenvector))

def test_power_method_complex_eigenvalues():
    A = np.array([[0, -1], [1, 0]], dtype=float)
    with pytest.raises(ValueError):
        power_method(A)

def test_power_method_high_dimensions():
    np.random.seed(1)
    A = np.random.rand(10, 10)
    eigenvalue, eigenvector = power_method(A)
    expected_eigenvalue = max(np.linalg.eigvals(A), key=lambda x: np.abs(x))
    assert np.isclose(eigenvalue, expected_eigenvalue, atol=1e-6)
