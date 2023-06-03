import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# define the true function
def f(x):
    return 2.5 * x + 1.3

# generate points using above function
np.random.seed(0) # for reproducibility
n_points = 10
X = np.linspace(0, 1, n_points)
y = f(X) + np.random.normal(0, 0.3, size=n_points) # add some noise

# fit a linear function to the data
def fit_func(x, a, b):
    return a * x + b

params, _ = curve_fit(fit_func, X, y)

# generate y-values for the best fit line
y_fit = params[0] * X + params[1]

plt.figure(figsize=(8, 6))

# plot the data points
plt.scatter(X, y, label='Data points')

# plot the best fit line
plt.plot(X, y_fit, 'r-', label='Best fit: a=%5.3f, b=%5.3f' % tuple(params))

# plot vertical lines to show errors
for xi, yi, y_fit_i in zip(X, y, y_fit):
    plt.plot([xi, xi], [yi, y_fit_i], color='gray', linestyle='--')

plt.xlabel('X')
plt.ylabel('y')
plt.title('Curve fitting')
plt.legend()
plt.show()
