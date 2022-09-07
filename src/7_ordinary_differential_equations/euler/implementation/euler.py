import numpy as np

# x(t + h) = x(t) + hf(x,t)


def f(x, t):
    return x * np.cos(t)


h = 0.01
t_values = np.arange(0, 2 * np.pi, h)
x_values = []

x = 0

for t in t_values:
    x_values.append(x)
    x = x + h * f(x, t)

plt.plot(t_values, np.sin(t_values))
plt.plot(t_values, x_values, ".")
plt.axhline(c="k")
plt.show()
