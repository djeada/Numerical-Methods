import numpy as np


def multiple_linear_regression(x, y):
    a = np.append(x, np.ones((len(x), 1)), axis=-1)
    y = y[:, np.newaxis]

    result = np.linalg.inv(np.dot(a.T, a))
    result = np.dot(result, a.T)
    result = np.dot(result, y)

    return result[-1][0], result[:-1]
