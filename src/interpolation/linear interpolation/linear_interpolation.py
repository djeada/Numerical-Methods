import numpy as np


def linear_interpolation(x_data, y_data, point):
    if len(x_data) != len(y_data):
        raise Exception("X and Y vectors must have equal number of elements.")

    if x_data.size < 2:
        raise Exception("X and Y vectors have to contain at least 2 elements.")

    def _interpolate(x1, x2, y1, y2, point):
        return ((y2 - y1) * point + x2 * y1 - x1 * y2) / (x2 - x1)

    for index, x in np.ndenumerate(x_data[:-1]):
        i = index[0]
        if point >= x and point <= x_data[i + 1]:
            x1 = x
            x2 = x_data[i + 1]
            y1 = y_data[i]
            y2 = y_data[i + 1]
            return _interpolate(x1, x2, y1, y2, point)
