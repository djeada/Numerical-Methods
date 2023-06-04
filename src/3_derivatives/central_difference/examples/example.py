"""
Calculate the derivative of f(x) = cos(x) at PI/3.
"""
import numpy as np
import matplotlib.pyplot as plt
from central_difference import central_difference


def function(x):
    return np.cos(x)


def exact_derivative(x):
    return -np.sin(x)


point = np.pi / 3


computed_derivative_history = list()
step = point / 2

for _ in range(100):
    computed_derivative = central_difference(function, point, step)
    computed_derivative_history.append(computed_derivative)
    step /= 2

exact_result = exact_derivative(point)
error_history = np.array(
    [
        abs(exact_result - computed_derivative)
        for computed_derivative in computed_derivative_history
    ]
)
best_computed_result = computed_derivative_history[np.argmin(error_history)]

print("")
print(f"Exact derivative of cos(x) at point {point:.3f} is {exact_result:.7f}")
print(
    f"The derivative of cos(x) at point {point:.3f} computed using central differencing is {best_computed_result:.7f}"
)
print("")

plt.plot(np.linspace(0, error_history.size, error_history.size), error_history)
plt.xlabel("Iteration")
plt.ylabel("Absolute Error")
plt.show()
