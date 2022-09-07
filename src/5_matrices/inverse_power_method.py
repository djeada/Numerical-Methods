import numpy as np


def inverse_power_method(a, x, num_iter=10):
    """
    returns the smallest eigenvalue and coressponding eigenvector    
    """

    def normalize(vec):
        return abs(vec).max(), vec / vec.max()

    lambda_1 = None
    a_inv = np.linalg.inv(a)

    for i in range(num_iter):
        x = np.dot(a_inv, x)
        lambda_1, x = normalize(x)

    return lambda_1, x
