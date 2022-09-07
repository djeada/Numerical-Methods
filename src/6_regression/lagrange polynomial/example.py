import matplotlib.pyplot as plt
import numpy as np
from lagrange_polynomial import lagrange_polynomial


def main():
    x = np.array([-9, -5, -2.5, 4, 7])
    y = np.array([-2, 3, 0, 5, 11])

    result_function = lagrange_polynomial(x, y)

    x_new = np.arange(-10, 10, 0.1)
    y_new = np.array([result_function(i) for i in x_new])

    fig = plt.figure(figsize=(10, 8))
    plt.plot(x_new, y_new, "b", x, y, "ro")
    plt.title("Lagrange Polynomial")
    plt.grid()
    plt.xlabel("x")
    plt.ylabel("y")
    plt.show()


if __name__ == "__main__":
    main()
