"""Generate the Gaussian RBF figures used by gaussian_interpolation.md."""
from pathlib import Path

import numpy as np

from svg_plot_utils import PALETTE, line_chart

OUT = Path(__file__).with_name("plots")


def gaussian_basis(queries, centers, epsilon):
    """Evaluate unweighted Gaussian basis functions, one column per center."""
    return np.exp(-(epsilon * (queries[:, None] - centers[None, :])) ** 2)


def main():
    centers = np.array([0., 1., 2., 3.])
    values = np.array([0., 1., .2, 1.2])
    # Include the centers exactly so every unit peak is represented in the SVG.
    x = np.unique(np.concatenate((np.linspace(-.5, 3.5, 801), centers)))
    epsilon = 1.2
    basis = gaussian_basis(x, centers, epsilon)
    peaks = [
        {"x": [c], "y": [1.], "color": PALETTE[j]}
        for j, c in enumerate(centers)
    ]
    line_chart(
        OUT / "gaussian_rbf_basis_functions.svg",
        "Gaussian RBFs at the data sites (epsilon = 1.2)", "x", "basis value",
        [{"x": x, "y": basis[:, j], "label": f"center {c:g}"}
         for j, c in enumerate(centers)],
        peaks + [{"x": centers, "y": np.zeros_like(centers),
                  "label": "data sites (not data values)", "color": "#111827"}],
        max_points=None, legend_below=True,
    )

    series = []
    for epsilon in [.5, 1., 2.]:
        matrix = gaussian_basis(centers, centers, epsilon)
        weights = np.linalg.solve(matrix, values)
        series.append({
            "x": x, "y": gaussian_basis(x, centers, epsilon) @ weights,
            "label": f"epsilon={epsilon:g}, cond={np.linalg.cond(matrix):.1e}",
        })
    line_chart(
        OUT / "gaussian_rbf_shape_parameter.svg",
        "Shape parameter changes curve and conditioning", "x", "s(x)",
        series, [{"x": centers, "y": values, "label": "data"}],
        max_points=None, legend_below=True,
    )


if __name__ == "__main__":
    main()
