# test_regression_methods_comparison.py
import pytest
import numpy as np
from ..implementation.regression_methods_comparison import (
    compute_metrics,
    compare_methods,
    rank_methods,
    cross_validate_methods,
    polynomial_fit_predict,
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
        "method_a": {
            "rmse": 0.5,
            "mae": 0.4,
            "r_squared": 0.9,
            "max_error": 0.8,
            "rss": 1.0,
        },
        "method_b": {
            "rmse": 0.1,
            "mae": 0.1,
            "r_squared": 0.99,
            "max_error": 0.2,
            "rss": 0.1,
        },
        "method_c": {
            "rmse": 0.3,
            "mae": 0.2,
            "r_squared": 0.95,
            "max_error": 0.5,
            "rss": 0.5,
        },
    }
    ranked = rank_methods(results, metric="rmse")
    assert ranked[0][0] == "method_b"
    assert ranked[1][0] == "method_c"
    assert ranked[2][0] == "method_a"


def test_rank_methods_by_r_squared():
    results = {
        "method_a": {
            "rmse": 0.5,
            "mae": 0.4,
            "r_squared": 0.9,
            "max_error": 0.8,
            "rss": 1.0,
        },
        "method_b": {
            "rmse": 0.1,
            "mae": 0.1,
            "r_squared": 0.99,
            "max_error": 0.2,
            "rss": 0.1,
        },
    }
    ranked = rank_methods(results, metric="r_squared")
    assert ranked[0][0] == "method_b"
    assert ranked[1][0] == "method_a"


def test_rank_methods_empty_results():
    with pytest.raises(ValueError):
        rank_methods({}, metric="rmse")


def test_rank_methods_unknown_metric():
    results = {
        "method_a": {
            "rmse": 0.5,
            "mae": 0.4,
            "r_squared": 0.9,
            "max_error": 0.8,
            "rss": 1.0,
        },
    }
    with pytest.raises(ValueError):
        rank_methods(results, metric="unknown")


def test_compute_metrics_r_squared_exact_value():
    y_true = np.array([1.0, 2.0, 3.0, 4.0])
    y_pred = np.array([1.0, 2.0, 3.0, 5.0])
    metrics = compute_metrics(y_true, y_pred)
    # rss = 1, tss = 5
    assert metrics["r_squared"] == pytest.approx(0.8, abs=1e-12)


def test_compute_metrics_constant_target():
    y_true = np.array([2.0, 2.0, 2.0])
    assert compute_metrics(y_true, y_true.copy())["r_squared"] == 1.0
    assert compute_metrics(y_true, y_true + 1.0)["r_squared"] == 0.0


def _noisy_quadratic():
    rng = np.random.default_rng(3)
    x = np.linspace(-1, 1, 24)
    y = 1 + 2 * x - 3 * x**2 + rng.normal(0, 0.3, x.size)
    return x, y


def test_training_ranking_prefers_overfit_but_cv_does_not():
    x, y = _noisy_quadratic()

    def train_fit(deg):
        return lambda xt, yt: np.polyval(np.polyfit(xt, yt, deg), xt)

    train = compare_methods(x, y, {"deg2": train_fit(2), "deg9": train_fit(9)})
    assert rank_methods(train, "rmse")[0][0] == "deg9"

    cv = cross_validate_methods(
        x,
        y,
        {"deg2": polynomial_fit_predict(2), "deg9": polynomial_fit_predict(9)},
        n_folds=6,
        seed=0,
    )
    assert rank_methods(cv, "rmse")[0][0] == "deg2"
    assert cv["deg9"]["rmse"] > cv["deg2"]["rmse"]


def test_cross_validate_methods_uses_only_held_out_points():
    x = np.arange(10.0)
    y = x**2
    seen = []

    def spy(x_train, y_train, x_eval):
        assert not np.intersect1d(x_train, x_eval).size
        seen.append(x_eval.copy())
        return np.zeros_like(x_eval)

    res = cross_validate_methods(x, y, {"spy": spy}, n_folds=5)
    assert np.array_equal(np.sort(np.concatenate(seen)), x)
    assert res["spy"]["rss"] == pytest.approx(float(np.sum(y**2)))


def test_cross_validate_methods_exact_model_has_zero_error_and_loo():
    x = np.linspace(0, 4, 8)
    y = 2 * x + 1
    res = cross_validate_methods(x, y, {"line": polynomial_fit_predict(1)}, n_folds=100)
    assert res["line"]["rmse"] == pytest.approx(0.0, abs=1e-9)


def test_cross_validate_methods_validation():
    x = np.array([0.0, 1.0, 2.0, 3.0])
    m = {"line": polynomial_fit_predict(1)}
    with pytest.raises(ValueError):
        cross_validate_methods(x, x[:3], m)
    with pytest.raises(ValueError):
        cross_validate_methods(x[:2], x[:2], m)
    with pytest.raises(ValueError):
        cross_validate_methods(x, x, {})
    with pytest.raises(ValueError):
        cross_validate_methods(x, x, m, n_folds=1)
    with pytest.raises(ValueError):
        polynomial_fit_predict(-1)
