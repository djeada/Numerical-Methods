import numpy as np


def f(x):
    return x + np.exp(-2 * x) - 1


def dfdx(x):
    return 1 - 2 * np.exp(-2 * x)


def newton_raphson(f, x=1, num_iter=100, espilon=1e-8):

    for i in range(num_iter):
        x_last = x
        x -= f(x) / dfdx(x)

        if abs(x - x_last) < epsilon:
            print("x = {} after {} iterations".format(x, i + 1))
            return x

    raise ValueError("FAILURE")
