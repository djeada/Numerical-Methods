import numpy as np
import matplotlib.pyplot as plt
from algorithm import gradient_descent

def f(x, y):
    return np.sin(x) * np.sin(y)


def dfdx(x, y):
    return np.cos(x) * np.sin(y)


def dfdy(x, y):
    return np.cos(y) * np.sin(x)


def gradient_f(f, xy, num_iter=100, espilon=1e-8):
    x, y = xy
    return np.array([dfdx(x, y), dfdy(x, y)])

x_range = y_range = np.linspace(-np.pi, np.pi, 101)
x, y = np.meshgrid(x_range, y_range)
x2, y2 = x[5::10, 5::10], y[5::10, 5::10]

plt.figure(figsize=(8, 6))
plt.imshow(
    f(x, y), origin="lower", extent=(-np.pi, np.pi, -np.pi, np.pi), cmap="coolwarm"
)
plt.colorbar()
plt.quiver(x2, y2, gradient_descent.dfdx(x2, y2), gradient_descent.dfdy(x2, y2), pivot="middle")
plt.show()

print(gradient_descent(f))
