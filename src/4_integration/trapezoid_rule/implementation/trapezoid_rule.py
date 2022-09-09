import numpy as np


def trapezoid_rule(start_point, end_point, f, number_of_bins=10):

    result = 0.0
    bin_size = (end_point - start_point) / number_of_bins

    for i in range(number_of_bins):
        a = start_point + (bin_size * i)
        b = a + bin_size

        result += bin_size * (f(a) + f(b)) / 2

    return result

