import matplotlib.pyplot as plt
from cubic_spline import cubic_spline

test_x = [0, 1, 2, 3]
test_y = [0, 0.5, 2, 1.5]
spline = cubic_spline(test_x, test_y)

for i, x in enumerate(test_x):
    assert abs(test_y[i] - spline(x)) < 1e-8, f"Error at {x}, {test_y[i]}"

x_vals = [v / 10 for v in range(0, 50, 1)]
y_vals = [spline(y) for y in x_vals]

plt.plot(x_vals, y_vals)
plt.show()
