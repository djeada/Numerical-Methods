# test_least_squares.py
import pytest
import numpy as np
from ..implementation.least_squares import least_squares


def test_least_squares_simple():
    A = np.array([[1, 1], [1, 2], [2, 2]])
    b = np.array([4, 5, 6])
    x = least_squares(A, b)
    expected = np.linalg.lstsq(A, b, rcond=None)[0]
    assert np.allclose(x, expected, atol=1e-6)


def test_least_squares_overdetermined():
    A = np.array([
        [1, 1],
        [1, 2],
        [1, 3],
        [1, 4]
    ])
    b = np.array([2, 3, 4, 5])
    x = least_squares(A, b)
    expected = np.linalg.lstsq(A, b, rcond=None)[0]
    assert np.allclose(x, expected, atol=1e-6)


def test_least_squares_exact_solution():
    A = np.array([
        [2, 1],
        [1, -1]
    ])
    b = np.array([1, -1])
    x = least_squares(A, b)
    expected = np.linalg.lstsq(A, b, rcond=None)[0]
    assert np.allclose(x, expected, atol=1e-6)


def test_least_squares_singular():
    A = np.array([
        [1, 2],
        [2, 4],
        [3, 6]
    ])
    b = np.array([2, 4, 6])
    with pytest.raises(ValueError):
        least_squares(A, b)


def test_least_squares_non_square():
    A = np.array([[1, 2, 3], [4, 5, 6]])
    b = np.array([7, 8])
    with pytest.raises(ValueError):
        least_squares(A, b)


def test_least_squares_zero_vector():
    A = np.array([[1, 2], [3, 4]])
    b = np.array([0, 0])
    x = least_squares(A, b)
    expected = np.array([0, 0])
    assert np.allclose(x, expected, atol=1e-6)


def test_least_squares_large_matrix():
    np.random.seed(0)
    A = np.random.rand(100, 10)
    x_true = np.random.rand(10)
    b = A @ x_true + np.random.randn(100) * 0.01
    x_est = least_squares(A, b)
    assert np.allclose(x_est, x_true, atol=1e-2)


def test_least_squares_single_variable():
    A = np.array([[1], [2], [3]])
    b = np.array([2, 4, 6])
    x = least_squares(A, b)
    expected = np.array([2.0])
    assert np.allclose(x, expected, atol=1e-6)


def test_least_squares_negative_values():
    A = np.array([
        [1, -1],
        [-1, 1],
        [1, 1]
    ])
    b = np.array([0, 0, 2])
    x = least_squares(A, b)
    expected = np.linalg.lstsq(A, b, rcond=None)[0]
    assert np.allclose(x, expected, atol=1e-6)


def test_least_squares_fractional_solution():
    A = np.array([
        [0.5, 1.5],
        [1.0, 2.0],
        [1.5, 2.5]
    ])
    b = np.array([1.0, 2.0, 3.0])
    x = least_squares(A, b)
    expected = np.linalg.lstsq(A, b, rcond=None)[0]
    assert np.allclose(x, expected, atol=1e-6)


def test_least_squares_high_precision():
    A = np.array([
        [1.0000001, 1.0000002],
        [1.0000003, 1.0000004]
    ])
    b = np.array([2.0000003, 2.0000007])
    x = least_squares(A, b)
    expected = np.linalg.lstsq(A, b, rcond=None)[0]
    assert np.allclose(x, expected, atol=1e-8)


def test_least_squares_inconsistent_system():
    A = np.array([
        [1, 2],
        [2, 4],
        [3, 6]
    ])
    b = np.array([1, 2, 5])
    with pytest.raises(ValueError):
        least_squares(A, b)


def test_least_squares_zero_rows():
    A = np.array([
        [1, 2],
        [0, 0],
        [3, 4]
    ])
    b = np.array([5, 0, 11])
    with pytest.raises(ValueError):
        least_squares(A, b)


def test_least_squares_exact_match():
    A = np.array([
        [1, 0],
        [0, 1]
    ])
    b = np.array([3, 4])
    x = least_squares(A, b)
    expected = np.array([3, 4])
    assert np.allclose(x, expected, atol=1e-6)


def test_least_squares_multiple_answers():
    A = np.array([
        [1, 1],
        [2, 2]
    ])
    b = np.array([2, 4])
    with pytest.raises(ValueError):
        least_squares(A, b)


def test_least_squares_highly_correlated():
    A = np.array([
        [1, 1.0001],
        [2, 2.0002],
        [3, 3.0003]
    ])
    b = np.array([2.0001, 4.0002, 6.0003])
    x = least_squares(A, b)
    expected = np.linalg.lstsq(A, b, rcond=None)[0]
    assert np.allclose(x, expected, atol=1e-6)
