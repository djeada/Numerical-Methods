import numpy as np


def least_squares(x, y):
    a = np.array([np.array((elem, 1.0)) for elem in x])
    y = y[:, np.newaxis]

    result = np.linalg.inv(np.dot(a.T, a))
    result = np.dot(result, a.T)
    result = np.dot(result, y)

    return result[0][0], result[1][0]
