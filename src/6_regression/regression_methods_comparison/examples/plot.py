import numpy as np
import matplotlib.pyplot as plt
import sys
import os

cwd = os.getcwd()
root_path = os.path.abspath(os.path.join(cwd, os.pardir))
sys.path.append(root_path)

from implementation.regression_methods_comparison import compare_methods, rank_methods


def poly_fit_1(x, y):
    coeffs = np.polyfit(x, y, 1)
    return np.polyval(coeffs, x)


def poly_fit_2(x, y):
    coeffs = np.polyfit(x, y, 2)
    return np.polyval(coeffs, x)


def poly_fit_5(x, y):
    coeffs = np.polyfit(x, y, 5)
    return np.polyval(coeffs, x)


def main():
    np.random.seed(42)
    x_data = np.linspace(0, 5, 20)
    y_data = np.sin(x_data) + np.random.normal(0, 0.1, size=len(x_data))

    methods = {
        "Linear (deg 1)": poly_fit_1,
        "Quadratic (deg 2)": poly_fit_2,
        "Degree 5": poly_fit_5,
    }

    results = compare_methods(x_data, y_data, methods)
    ranking = rank_methods(results, metric="rmse")

    x_fine = np.linspace(0, 5, 200)

    fig, axes = plt.subplots(1, 2, figsize=(16, 6))

    ax1 = axes[0]
    ax1.scatter(x_data, y_data, color="black", s=60, zorder=5, label="Data")
    colors = ["blue", "green", "orange"]
    degrees = [1, 2, 5]
    for (name, _), color, deg in zip(methods.items(), colors, degrees):
        coeffs = np.polyfit(x_data, y_data, deg)
        y_fine = np.polyval(coeffs, x_fine)
        rmse = results[name]["rmse"]
        ax1.plot(x_fine, y_fine, color=color, label=f"{name} (RMSE={rmse:.4f})")
    ax1.plot(x_fine, np.sin(x_fine), "k--", alpha=0.3, label="sin(x)")
    ax1.set_xlabel("x")
    ax1.set_ylabel("y")
    ax1.set_title("Regression Methods Comparison")
    ax1.legend()
    ax1.grid(True)

    ax2 = axes[1]
    names = [name for name, _ in ranking]
    scores = [score for _, score in ranking]
    ax2.barh(names, scores, color=["green", "orange", "blue"])
    ax2.set_xlabel("RMSE")
    ax2.set_title("Method Ranking by RMSE")
    ax2.grid(True, axis="x")

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
