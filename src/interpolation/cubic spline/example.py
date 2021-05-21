import numpy as np
import matplotlib.pyplot as plt
from cubic_spline import cubic_spline

x = np.array([0, 1, 2, 3])
y = np.array([0, -1, 4, 3])

result_function = cubic_spline(x, y)

x_new = np.arange(0, 5, 0.1)
y_new = np.array([result_function(i) for i in x_new])

fig = plt.figure(figsize=(10, 8))
plt.plot(x_new, y_new, "b", x, y, "ro")
plt.title("Cubic Spline")
plt.grid()
plt.xlabel("x")
plt.ylabel("y")
plt.show()
