import numpy as np
import matplotlib.pyplot as plt
from least_squares import least_squares

x = np.linspace(0, 10)
y = np.random.normal(x, 0.5)

beta = least_squares(x, y)

y_computed = np.array([beta[0]]) * x + np.array([beta[1]])

plt.figure(figsize=(10, 8))
plt.plot(x, y, "b.")
plt.plot(
    x,
    y_computed,
    "r",
    label="y = {}*x + {}".format(round(beta[0], 2), round(beta[1], 2)),
)
plt.xlabel("x")
plt.ylabel("y")
plt.legend(loc="upper left")
plt.show()
