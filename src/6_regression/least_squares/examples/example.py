import numpy as np
import matplotlib.pyplot as plt
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), os.pardir))
from implementation.least_squares import least_squares


def main():
    np.random.seed(42)
    x = np.linspace(0, 10, 50)
    y = 2 + 0.5 * x + np.random.normal(0, 0.5, size=x.shape[0])
    X = np.column_stack((np.ones_like(x), x))

    beta = least_squares(X, y)

    y_computed = beta[0] + beta[1] * x

    plt.figure(figsize=(10, 8))
    plt.plot(x, y, "b.")
    plt.plot(
        x,
        y_computed,
        "r",
        label="y = {} + {}x".format(round(beta[0], 2), round(beta[1], 2)),
    )
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend(loc="upper left")
    plt.show()


if __name__ == "__main__":
    main()
