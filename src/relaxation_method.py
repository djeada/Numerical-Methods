import numpy as np


def f(x):
    return x + np.exp(-2 * x) - 1


def dfdx(x):
    return 1 - 2 * np.exp(-2 * x)


def relaxation_method(f, x=1, num_iter=100, espilon=1e-8):

    values = []
    for i in range(num_iter):
        values = f(x)
        x = f(x)

        if abs(x - values[-1]) < epsilon:
            print("x = {} after {} iterations".format(x, i + 1))
            return x

    raise ValueError("FAILURE")
