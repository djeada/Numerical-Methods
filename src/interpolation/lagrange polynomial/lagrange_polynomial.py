import numpy as np


def lagrange_polynomial(x_data, y_data):
    if x_data.size != y_data.size:
        raise Exception("X and Y vectors must have equal number of elements.")

    if x_data.size < 3:
        raise Exception("X and Y vectors have to contain at least 3 elements.")

    n = x_data.size

    def _interpolate(idx, point):
        _coeff = [
            (point - x_data[i]) / (x_data[idx] - x_data[i])
            for i in range(n)
            if i != idx
        ]

        return np.prod(_coeff, axis=0) * y_data[idx]

    def result_function(point):
        coeff = [_interpolate(idx, point) for idx in range(n)]
        return np.sum(coeff, axis=0)

    return result_function
