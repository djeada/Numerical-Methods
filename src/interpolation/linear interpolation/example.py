import numpy as np
import matplotlib.pyplot as plt
from linear_interpolation import linear_interpolation


def main():
    x = np.array([-1, 4, 7])
    y = np.array([1, 5, 2])

    point_1 = 1
    point_2 = 4.5

    plt.figure(figsize=(10, 8))
    plt.plot(x, y)
    plt.plot(point_1, linear_interpolation(x, y, point_1), "go")
    plt.plot(point_2, linear_interpolation(x, y, point_2), "go")
    plt.title("Linear Interpolation at x_1 = {} and x_2 = {}".format(point_1, point_2))
    plt.xlabel("x")
    plt.ylabel("y")
    plt.show()


if __name__ == "__main__":
    main()
