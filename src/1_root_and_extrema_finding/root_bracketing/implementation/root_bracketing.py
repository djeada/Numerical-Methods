import numpy as np

def root_bracketing(f, a, b, dx):
    x = np.linspace(a, b, int((b - a) / dx) + 1)
    y = f(x)
    for i in range(1, len(x)):
        if np.sign(y[i]) != np.sign(y[i - 1]):
            return x[i], x[i - 1]
