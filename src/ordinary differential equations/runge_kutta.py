import numpy as np
import matplotlib.pyplot as plt

# y' = u
# u' = -y

"""
y'' + y = 0

y(0) = 0 and y'(0) = 1/pi
"""


def F(y, u, x):
    return -y


a = 0
b = 2 * np.pi
N = 100
h = (b - a) / N

xpoints = np.arange(a, b, h)
ypoints = []
upoints = []

y = 0.0
u = 1.0 / np.pi

for x in xpoints:
    ypoints.append(y)
    upoints.append(u)

    m1 = h * u
    k1 = h * F(y, u, x)  # (x, v, t)

    m2 = h * (u + 0.5 * k1)
    k2 = h * F(y + 0.5 * m1, u + 0.5 * k1, x + 0.5 * h)

    m3 = h * (u + 0.5 * k2)
    k3 = h * F(y + 0.5 * m2, u + 0.5 * k2, x + 0.5 * h)

    m4 = h * (u + k3)
    k4 = h * F(y + m3, u + k3, x + h)

    y += (m1 + 2 * m2 + 2 * m3 + m4) / 6
    u += (k1 + 2 * k2 + 2 * k3 + k4) / 6

plt.plot(xpoints, ypoints)
# plt.xlim([0,4])
# plt.xlim([0,4])
plt.show()
