"""Tests for Gaussian RBF interpolation (not Gauss finite differences)."""

import numpy as np
import pytest

from ..implementation.gaussian_rbf import (
    GaussianRBFInterpolator,
    gaussian_rbf_interpolation,
)


def test_notes_example_coefficients_and_query():
    interpolator = GaussianRBFInterpolator([0, 1, 2], [0, 0.5, 0], epsilon=1)
    np.testing.assert_allclose(
        interpolator.weights,
        [-0.24602546, 0.68101542, -0.24602546],
        atol=1e-8,
    )
    assert interpolator(0.5) == pytest.approx(0.312839627750878, abs=1e-12)
    assert gaussian_rbf_interpolation([0, 1, 2], [0, 0.5, 0], 0.5) == pytest.approx(
        0.312839627750878, abs=1e-12
    )


@pytest.mark.parametrize(
    "nodes, values",
    [
        ([0, 1, 2], [0, 0.5, 0]),
        ([3, -2, 0.25, 1.5], [4, -1, 2, 0]),
        ([0, 0.2, 1.7, 5], [2, -3, 1, 4]),
    ],
)
def test_interpolates_distinct_unsorted_and_unequally_spaced_nodes(nodes, values):
    interpolator = GaussianRBFInterpolator(nodes, values, epsilon=0.9)
    np.testing.assert_allclose(interpolator(nodes), values, rtol=1e-10, atol=1e-10)


def test_single_node_is_valid():
    interpolator = GaussianRBFInterpolator([2], [5], epsilon=2)
    assert interpolator(2) == pytest.approx(5)
    assert interpolator(3) == pytest.approx(5 * np.exp(-4))


def test_scalar_and_array_queries_preserve_shape():
    interpolator = GaussianRBFInterpolator([0, 1, 2], [0, 0.5, 0])
    assert isinstance(interpolator(0.5), float)
    query = np.array([[0, 0.5], [1, 2]])
    result = interpolator(query)
    assert isinstance(result, np.ndarray)
    assert result.shape == query.shape
    np.testing.assert_allclose(result, [[0, interpolator(0.5)], [0.5, 0]], atol=1e-12)


def test_shape_parameter_changes_non_node_value():
    narrow = GaussianRBFInterpolator([0, 1, 2], [0, 0.5, 0], epsilon=2)
    broad = GaussianRBFInterpolator([0, 1, 2], [0, 0.5, 0], epsilon=0.5)
    assert not np.isclose(narrow(0.5), broad(0.5))
    np.testing.assert_allclose(narrow([0, 1, 2]), [0, 0.5, 0], atol=1e-12)
    np.testing.assert_allclose(broad([0, 1, 2]), [0, 0.5, 0], atol=1e-12)


def test_extrapolation_uses_gaussian_tail():
    interpolator = GaussianRBFInterpolator([0, 1], [1, 2])
    assert abs(interpolator(100)) < 1e-100


@pytest.mark.parametrize("epsilon", [0, -1, np.nan, np.inf, -np.inf])
def test_invalid_shape_parameter(epsilon):
    with pytest.raises(ValueError, match="epsilon"):
        GaussianRBFInterpolator([0, 1], [1, 2], epsilon=epsilon)


@pytest.mark.parametrize(
    "nodes, values, message",
    [
        ([], [], "At least one"),
        ([0, 1], [1], "equal lengths"),
        ([0, 0], [1, 2], "distinct"),
        ([0, np.nan], [1, 2], "finite"),
        ([0, 1], [1, np.inf], "finite"),
        ([[0, 1]], [1, 2], "one-dimensional"),
        ([0, 1], [[1, 2]], "one-dimensional"),
    ],
)
def test_invalid_data(nodes, values, message):
    with pytest.raises(ValueError, match=message):
        GaussianRBFInterpolator(nodes, values)


@pytest.mark.parametrize("query", [np.nan, np.inf, [0, -np.inf]])
def test_invalid_query(query):
    with pytest.raises(ValueError, match="Query points"):
        GaussianRBFInterpolator([0, 1], [1, 2])(query)


def test_solves_system_without_explicit_inverse(monkeypatch):
    def forbidden_inverse(*args, **kwargs):
        raise AssertionError("Do not explicitly invert the kernel matrix")

    monkeypatch.setattr(np.linalg, "inv", forbidden_inverse)
    interpolator = GaussianRBFInterpolator([0, 1, 2], [0, 0.5, 0])
    np.testing.assert_allclose(interpolator([0, 1, 2]), [0, 0.5, 0], atol=1e-12)
