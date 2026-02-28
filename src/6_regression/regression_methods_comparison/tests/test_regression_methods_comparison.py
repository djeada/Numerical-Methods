# test_regression_methods_comparison.py
import pytest
import numpy as np
from ..implementation.regression_methods_comparison import (
    compute_metrics,
    compare_methods,
    rank_methods,
)


def test_compute_metrics_perfect_fit():
    y_true = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
    y_pred = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
    metrics = compute_metrics(y_true, y_pred)
    assert metrics["rmse"] == pytest.approx(0.0, abs=1e-10)
    assert metrics["mae"] == pytest.approx(0.0, abs=1e-10)
    assert metrics["r_squared"] == pytest.approx(1.0, abs=1e-10)
    assert metrics["max_error"] == pytest.approx(0.0, abs=1e-10)
    assert metrics["rss"] == pytest.approx(0.0, abs=1e-10)


def test_compute_metrics_known_values():
    y_true = np.array([1.0, 2.0, 3.0])
    y_pred = np.array([1.1, 1.9, 3.2])
    metrics = compute_metrics(y_true, y_pred)
    residuals = y_true - y_pred
    expected_rss = float(np.sum(residuals**2))
    expected_rmse = float(np.sqrt(expected_rss / 3))
    expected_mae = float(np.mean(np.abs(residuals)))
    assert metrics["rmse"] == pytest.approx(expected_rmse, abs=1e-10)
    assert metrics["mae"] == pytest.approx(expected_mae, abs=1e-10)
    assert metrics["rss"] == pytest.approx(expected_rss, abs=1e-10)


def test_compute_metrics_r_squared():
    y_true = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
    y_pred = np.array([1.1, 2.1, 2.9, 3.9, 5.1])
    metrics = compute_metrics(y_true, y_pred)
    assert 0.0 < metrics["r_squared"] < 1.0


def test_compute_metrics_shape_mismatch():
    y_true = np.array([1.0, 2.0, 3.0])
    y_pred = np.array([1.0, 2.0])
    with pytest.raises(ValueError):
        compute_metrics(y_true, y_pred)


def test_compute_metrics_empty_arrays():
    y_true = np.array([])
    y_pred = np.array([])
    with pytest.raises(ValueError):
        compute_metrics(y_true, y_pred)


def test_compare_methods_linear():
    x = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
    y = np.array([2.0, 4.0, 6.0, 8.0, 10.0])

    def perfect_method(x_data, y_data):
        return y_data.copy()

    def offset_method(x_data, y_data):
        return y_data + 0.1

    methods = {"perfect": perfect_method, "offset": offset_method}
    results = compare_methods(x, y, methods)

    assert "perfect" in results
    assert "offset" in results
    assert results["perfect"]["rmse"] < results["offset"]["rmse"]


def test_compare_methods_mismatched_data():
    x = np.array([1.0, 2.0, 3.0])
    y = np.array([1.0, 2.0])
    methods = {"dummy": lambda x, y: y}
    with pytest.raises(ValueError):
        compare_methods(x, y, methods)


def test_compare_methods_too_few_points():
    x = np.array([1.0])
    y = np.array([1.0])
    methods = {"dummy": lambda x, y: y}
    with pytest.raises(ValueError):
        compare_methods(x, y, methods)


def test_compare_methods_empty_methods():
    x = np.array([1.0, 2.0])
    y = np.array([1.0, 2.0])
    with pytest.raises(ValueError):
        compare_methods(x, y, {})


def test_rank_methods_by_rmse():
    results = {
        "method_a": {"rmse": 0.5, "mae": 0.4, "r_squared": 0.9, "max_error": 0.8, "rss": 1.0},
        "method_b": {"rmse": 0.1, "mae": 0.1, "r_squared": 0.99, "max_error": 0.2, "rss": 0.1},
        "method_c": {"rmse": 0.3, "mae": 0.2, "r_squared": 0.95, "max_error": 0.5, "rss": 0.5},
    }
    ranked = rank_methods(results, metric="rmse")
    assert ranked[0][0] == "method_b"
    assert ranked[1][0] == "method_c"
    assert ranked[2][0] == "method_a"


def test_rank_methods_by_r_squared():
    results = {
        "method_a": {"rmse": 0.5, "mae": 0.4, "r_squared": 0.9, "max_error": 0.8, "rss": 1.0},
        "method_b": {"rmse": 0.1, "mae": 0.1, "r_squared": 0.99, "max_error": 0.2, "rss": 0.1},
    }
    ranked = rank_methods(results, metric="r_squared")
    assert ranked[0][0] == "method_b"
    assert ranked[1][0] == "method_a"


def test_rank_methods_empty_results():
    with pytest.raises(ValueError):
        rank_methods({}, metric="rmse")


def test_rank_methods_unknown_metric():
    results = {
        "method_a": {"rmse": 0.5, "mae": 0.4, "r_squared": 0.9, "max_error": 0.8, "rss": 1.0},
    }
    with pytest.raises(ValueError):
        rank_methods(results, metric="unknown")
