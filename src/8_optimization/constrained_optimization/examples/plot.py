import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon


def linear_programming(c, A_ub, b_ub):
    """
    Solve a 2D linear program: minimize c^T x subject to A_ub @ x <= b_ub, x >= 0.
    Uses vertex enumeration for 2D problems.

    Parameters:
        c (numpy.ndarray): Objective coefficients (2,).
        A_ub (numpy.ndarray): Inequality constraint matrix (m x 2).
        b_ub (numpy.ndarray): Inequality constraint bounds (m,).

    Returns:
        x_opt (numpy.ndarray): Optimal solution.
        obj (float): Optimal objective value.
    """
    m = A_ub.shape[0]
    # Build all constraint lines: A_ub @ x = b_ub and x_i = 0
    A_all = np.vstack([A_ub, np.eye(2)])
    b_all = np.concatenate([b_ub, np.zeros(2)])
    n_lines = len(b_all)

    vertices = []
    for i in range(n_lines):
        for j in range(i + 1, n_lines):
            A_pair = np.array([A_all[i], A_all[j]])
            b_pair = np.array([b_all[i], b_all[j]])
            try:
                v = np.linalg.solve(A_pair, b_pair)
            except np.linalg.LinAlgError:
                continue
            # Check feasibility
            if np.all(A_ub @ v <= b_ub + 1e-10) and np.all(v >= -1e-10):
                vertices.append(v)

    if not vertices:
        raise ValueError("No feasible region found.")

    vertices = np.array(vertices)
    objectives = vertices @ c
    idx = np.argmin(objectives)
    return vertices[idx], objectives[idx]


if __name__ == "__main__":
    # Minimize c^T x subject to A_ub @ x <= b_ub, x >= 0
    c = np.array([-3, -5])  # minimize -3x - 5y (maximize 3x + 5y)
    A_ub = np.array([[1, 0], [0, 1], [1, 2]])
    b_ub = np.array([4, 6, 8])

    x_opt, obj = linear_programming(c, A_ub, b_ub)
    print(f"Optimal point: ({x_opt[0]:.4f}, {x_opt[1]:.4f})")
    print(f"Optimal value: {obj:.4f}")

    fig, ax = plt.subplots(figsize=(8, 7))

    # Plot constraint boundaries
    x_range = np.linspace(-0.5, 6, 400)
    ax.plot(x_range, np.full_like(x_range, 6), "r-", label="$y \\leq 6$")
    ax.axvline(x=4, color="g", linestyle="-", label="$x \\leq 4$")
    ax.plot(x_range, (8 - x_range) / 2, "b-", label="$x + 2y \\leq 8$")

    # Shade feasible region
    corners = [[0, 0], [4, 0], [4, 2], [0, 4]]
    polygon = Polygon(corners, alpha=0.2, color="skyblue", label="Feasible region")
    ax.add_patch(polygon)

    # Plot optimal point
    ax.plot(x_opt[0], x_opt[1], "r*", markersize=20, zorder=5, label="Optimal point")

    ax.set_xlim(-0.5, 6)
    ax.set_ylim(-0.5, 7)
    ax.set_xlabel("$x$", fontsize=14)
    ax.set_ylabel("$y$", fontsize=14)
    ax.set_title("Constrained Optimization: Linear Programming", fontsize=16)
    ax.legend(fontsize=11)
    ax.grid(True)
    plt.tight_layout()
    plt.show()
