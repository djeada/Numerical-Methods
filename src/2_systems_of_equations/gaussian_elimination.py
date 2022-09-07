import numpy as np


def gaussian_elimination(a, b):

    n = len(a)
    m = n + 1

    for row, element in zip(a, b):
        row.append(element)
        if len(row) != m:
            raise ValueError("You have to provide a square matrix")

    for i in range(n):
        if a[i][i] == 0.0:
            raise ZeroDivisionError()

        for j in range(i + 1, n):
            ratio = a[j][i] / a[i][i]

            for k in range(m):
                a[j][k] -= ratio * a[i][k]

    x = np.zeros(n)
    x[-1] = a[n - 1][n] / a[n - 1][n - 1]

    for i in range(n - 2, -1, -1):
        x[i] = a[i][n]

        for j in range(i + 1, n):
            x[i] -= x[j] * a[i][j]

        x[i] /= a[i][i]

    return x


print(gaussian_elimination([[2, 1, -1], [-3, -1, 2], [-2, 1, 2]], [8, -11, -3]))
