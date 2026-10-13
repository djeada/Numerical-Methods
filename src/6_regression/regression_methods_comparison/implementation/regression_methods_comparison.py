import numpy as np
from typing import Dict, List, Tuple, Callable


def compute_metrics(y_true: np.ndarray, y_pred: np.ndarray) -> Dict[str, float]:
    if y_true.shape != y_pred.shape:
        raise ValueError("y_true and y_pred must have the same shape.")
    if len(y_true) == 0:
        raise ValueError("Arrays must not be empty.")

    residuals = y_true - y_pred
    rss = float(np.sum(residuals**2))
    tss = float(np.sum((y_true - np.mean(y_true)) ** 2))
    n = len(y_true)

    rmse = float(np.sqrt(rss / n))
    mae = float(np.mean(np.abs(residuals)))
    if tss > 0:
        r_squared = 1.0 - rss / tss
    else:
        # Constant y_true: R^2 is undefined; report 1.0 only for an exact fit.
        r_squared = 1.0 if rss == 0 else 0.0
    max_error = float(np.max(np.abs(residuals)))

    return {
        "rmse": rmse,
        "mae": mae,
        "r_squared": r_squared,
        "max_error": max_error,
        "rss": rss,
    }


def compare_methods(
    x_data: np.ndarray,
    y_data: np.ndarray,
    methods: Dict[str, Callable[[np.ndarray, np.ndarray], np.ndarray]],
) -> Dict[str, Dict[str, float]]:
    """Score each method by its error on the data it was fitted to.

    These are *training* metrics: a more flexible model can always match the
    training points at least as well, so ranking by them favours overfitting.
    Use :func:`cross_validate_methods` for a held-out comparison.
    """
    if x_data.shape[0] != y_data.shape[0]:
        raise ValueError("X and Y vectors must have equal number of elements.")
    if x_data.shape[0] < 2:
        raise ValueError("At least 2 data points are required.")
    if len(methods) == 0:
        raise ValueError("At least one method must be provided.")

    results = {}
    for name, method in methods.items():
        y_pred = method(x_data, y_data)
        results[name] = compute_metrics(y_data, y_pred)

    return results


def rank_methods(
    results: Dict[str, Dict[str, float]],
    metric: str = "rmse",
) -> List[Tuple[str, float]]:
    """Sort ``(name, value)`` pairs best first for the chosen metric.

    Works on the output of either :func:`compare_methods` (training error)
    or :func:`cross_validate_methods` (held-out error).
    """
    if len(results) == 0:
        raise ValueError("Results dictionary must not be empty.")
    if metric not in ("rmse", "mae", "r_squared", "max_error", "rss"):
        raise ValueError(f"Unknown metric: {metric}")

    items = [(name, metrics[metric]) for name, metrics in results.items()]

    if metric == "r_squared":
        items.sort(key=lambda x: x[1], reverse=True)
    else:
        items.sort(key=lambda x: x[1])

    return items


def polynomial_fit_predict(
    degree: int,
) -> Callable[[np.ndarray, np.ndarray, np.ndarray], np.ndarray]:
    """Return a ``fit_predict(x_train, y_train, x_eval)`` for a polynomial fit."""
    if degree < 0:
        raise ValueError("Degree must be non-negative.")

    def fit_predict(
        x_train: np.ndarray, y_train: np.ndarray, x_eval: np.ndarray
    ) -> np.ndarray:
        coeffs = np.polyfit(x_train, y_train, degree)
        return np.polyval(coeffs, x_eval)

    return fit_predict


def cross_validate_methods(
    x_data: np.ndarray,
    y_data: np.ndarray,
    methods: Dict[str, Callable[[np.ndarray, np.ndarray, np.ndarray], np.ndarray]],
    n_folds: int = 5,
    seed: int = 0,
) -> Dict[str, Dict[str, float]]:
    """K-fold cross-validated metrics, based on held-out predictions only.

    Unlike :func:`compare_methods`, which scores each method on the very
    points it was fitted to (so a more flexible model always looks at least
    as good), every point here is predicted by a model that never saw it.

    ``methods`` maps a name to ``fit_predict(x_train, y_train, x_eval)``,
    which fits on the training part and returns predictions at ``x_eval``.
    The out-of-fold predictions of all folds are pooled and scored with
    :func:`compute_metrics`; the result has the same layout as
    :func:`compare_methods`, so it can be passed to :func:`rank_methods`.

    ``n_folds`` is clipped to the number of points (leave-one-out). Folds are
    a seeded random partition, identical for every method.
    """
    if x_data.shape[0] != y_data.shape[0]:
        raise ValueError("X and Y vectors must have equal number of elements.")
    if x_data.shape[0] < 3:
        raise ValueError("At least 3 data points are required for cross-validation.")
    if len(methods) == 0:
        raise ValueError("At least one method must be provided.")
    if n_folds < 2:
        raise ValueError("n_folds must be at least 2.")

    n = x_data.shape[0]
    n_folds = min(n_folds, n)
    order = np.random.default_rng(seed).permutation(n)
    folds = np.array_split(order, n_folds)

    results = {}
    for name, fit_predict in methods.items():
        y_pred = np.empty(n, dtype=float)
        for held_out in folds:
            train = np.ones(n, dtype=bool)
            train[held_out] = False
            y_pred[held_out] = fit_predict(
                x_data[train], y_data[train], x_data[held_out]
            )
        results[name] = compute_metrics(y_data.astype(float), y_pred)

    return results
