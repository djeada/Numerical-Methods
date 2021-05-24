import numpy as np


def f(x):
    return x + np.exp(-2 * x) - 1


def binary_search(f, x1=-1, x2=1, num_iter=100, espilon=1e-8):

    for i in range(num_iter):
        xm = (x1 + x2) / 2
        if np.sign(f(xm)) == np.sign(f(x1)):
            x1 = xm
        else:
            x2 = xm
        if x2 - x1 < epsilon:
            print("x = {} after {} iterations".format(xm, i + 1))
            return xm

    raise ValueError("FAILURE")
