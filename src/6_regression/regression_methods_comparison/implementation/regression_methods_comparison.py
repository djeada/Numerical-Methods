import numpy as np
from typing import Dict, List, Tuple, Callable


def compute_metrics(
    y_true: np.ndarray, y_pred: np.ndarray
) -> Dict[str, float]:
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
    r_squared = 1.0 - rss / tss if tss > 0 else 0.0
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
