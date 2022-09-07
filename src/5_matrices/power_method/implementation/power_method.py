import numpy as np


def power_method(a, x, num_iter=10):
    """
    return eigenvalue and coressponding eigenvector    
    """

    def normalize(vec):
        return abs(vec).max(), vec / vec.max()

    lambda_1 = None

    for i in range(num_iter):
        x = np.dot(a, x)
        lambda_1, x = normalize(x)

    return lambda_1, x
