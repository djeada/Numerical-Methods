import numpy as np
import matplotlib.pyplot as plt
from multiple_linear_regression import multiple_linear_regression


def generate_data(n):
    x_1 = np.random.uniform(low=0.0, high=100.0, size=n)
    x_2 = np.random.uniform(low=0.0, high=300.0, size=n)
    y = np.random.uniform(low=-80, high=80, size=n)

    x_1.sort()
    x_2.sort()
    y.sort()

    x = np.column_stack((x_1, x_2))

    return x, y


def generate_z_plane(x, y):

    a, b = multiple_linear_regression(x, y)

    def fun(val_1, val_2):
        return a + b[0] * val_1 + b[1] * val_2

    x_1 = np.linspace(min(x[:, 0]), max(x[:, 0]))
    x_2 = np.linspace(min(x[:, 1]), max(x[:, 1]))
    X_1, X_2 = np.meshgrid(x_1, x_2)

    Z = np.array(fun(np.ravel(X_1), np.ravel(X_2))).reshape(X_1.shape)

    return X_1, X_2, Z


def main():

    n = 100
    x, y = generate_data(n)
    X_1, X_2, Z = generate_z_plane(x, y)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")
    ax.plot_surface(X_1, X_2, Z, color="cyan")
    ax.scatter(x[:, 0], x[:, 1], y, c="g")
    ax.set_xlabel("x_1")
    ax.set_ylabel("x_2")
    ax.set_zlabel("y")
    plt.title("Data in 3D")

    plt.show()


if __name__ == "__main__":
    main()
