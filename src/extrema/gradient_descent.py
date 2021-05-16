import numpy as np
import matplotlib.pyplot as plt


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
plt.quiver(x2, y2, dfdx(x2, y2), dfdy(x2, y2), pivot="middle")
plt.show()


def gradient_descent(f, x1=0.1, x2=-0.1, gamma=1, num_iter=100, epsilon=1e-8):

    values = []
    x0 = np.array([x1, x2])
    for i in range(num_iter):
        values.append(x0)
        print(gradient_f(f, x0))
        x0 -= gamma * gradient_f(f, x0)

        if np.linalg.norm(x0 - values[-1]) < epsilon:
            x, y = x0[0], x0[1]
            print("x = {}, y = {} after {} iterations".format(x, y, i + 1))
            plt.figure(figsize=(8, 6))
            a, b = np.meshgrid(np.linspace(-np.pi, np.pi, 101), np.linspace(-np.pi, np.pi, 101))
            plt.imshow(
                f(a, b), origin="lower", extent=(-np.pi, np.pi, -np.pi, np.pi), cmap="coolwarm"
            )
            plt.colorbar()
            plt.quiver(x, y, dfdx(x, y), dfdy(x, y), pivot="middle")
            values = np.array(values)
            plt.plot(values[:,0], values[:,1], "yo")
            plt.show()
            return x, y

    raise ValueError("FAILURE")


print(gradient_descent(f))


