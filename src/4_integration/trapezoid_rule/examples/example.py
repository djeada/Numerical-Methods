import numpy as np
import matplotlib.pyplot as plt
from trapezoid_rule import trapezoid_rule


def f(x):
    return x * np.sin(x)


a = 0
b = np.pi
n = 20

result = trapezoid_rule(a, b, f, n)
print(result)

x = np.linspace(a - 1, b + 1)
y = f(x)

# Create the plot
fig, ax = plt.subplots()
ax.plot(x, y, "blue", linewidth=2)
ax.set_ylim(bottom=0)
ax.spines.right.set_visible(False)
ax.spines.top.set_visible(False)
fig.text(0.9, 0.05, "$x$")
fig.text(0.1, 0.9, "$y$")

# Draw the trapezoids
dx = (b - a) / n
for point in np.linspace(a, b - dx, n):
    xs = [point, point, point + dx, point + dx]
    ys = [0, f(point), f(point + dx), 0]
    plt.fill(xs, ys, "lightgray", edgecolor="black")

plt.legend(["f(x) = x*sin(x)"])
plt.show()
