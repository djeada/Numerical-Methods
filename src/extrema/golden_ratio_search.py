from scipy.constants import golden_ratio as phi


def f(x):
    return x + np.exp(-2 * x) - 1


def golden_ratio_search(f, x1=1, x4=4, num_iter=100, espilon=1e-8):

    x2 = x4 - (x4 - x1) / phi
    x3 = xi + (x4 - x1) / phi
    for i in range(num_iter):
        if f(x2) < f(x3):
            x4, x3 = x3, x2
            x2 = x4 - (x4 - x1) / phi
        else:
            x1, x2 = x2, x3
            x3 = x1 + (x4 - x1) / phi

        if abs(x3 - x2) < epsilon:
            x = (x2 + x3) / 2
            print("x = {} after {} iterations".format(x, i + 1))
            return x

    raise ValueError("FAILURE")
