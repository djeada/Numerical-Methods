"""
Fit a third order polynomial to fit a curve to the given data point:

A(-9, -2)
B(-5, 3)
C(-2.5, 0)
D(4, 5)
F(7, 11)
"""
import numpy as np
import matplotlib.pyplot as plt
import scipy.interpolate


# Define the data
x = np.array([-9, -5, -2.5, 4, 7])
y = np.array([-2, 3, 0, 5, 11])

# Plot the raw data
plt.scatter(x, y, s=200, marker="P", color="black", label="Raw data")
plt.xlabel("x")
plt.ylabel("y")

# Create the domain
x_domain = np.linspace(1.1 * min(x), 1.1 * max(x), 100)

# Create the model and show the predictions for djeada implementation

# Create the model and show the predictions for numpy implementation
model = np.poly1d(np.polyfit(x, y, 3))
y_prediction = model(x_domain)
plt.plot(x_domain, y_prediction, label="Polynomial regression numpy")

# Add a legend and show the plot
plt.legend(loc="best")
plt.show()

