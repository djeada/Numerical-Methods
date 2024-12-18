import numpy as np
import matplotlib.pyplot as plt

# Generate more example data: Input (X) and Output (Y) with noise
np.random.seed(42)
x = np.linspace(1, 10, 20)  # 20 evenly spaced feature values
y = 0.5 * x + 2 + np.random.normal(0, 0.5, size=len(x))  # Linear relation with noise

# Step 1: Add intercept term to X (column of ones)
X = np.vstack([np.ones(len(x)), x]).T  # Design matrix

# Step 2: Compute the Normal Equation: beta = (X^T X)^(-1) X^T Y
XT_X = X.T @ X  # X transpose multiplied by X
XT_Y = X.T @ y  # X transpose multiplied by Y
beta = np.linalg.inv(XT_X) @ XT_Y  # Solving for beta

# Step 3: Define the regression line
x_fit = np.linspace(min(x), max(x), 100)  # Smooth range for plotting
y_fit = beta[0] + beta[1] * x_fit  # Fitted line

# Step 4: Visualization
plt.figure(figsize=(8, 6))
plt.scatter(x, y, color='red', label='Data Points')  # Original data points
plt.plot(x_fit, y_fit, color='blue', label=f'Fitted Line: y = {beta[0]:.2f} + {beta[1]:.2f}x')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Least Squares Regression - Fitted Line')
plt.legend()
plt.grid(True)
plt.show()

# Display the regression coefficients
print(f"Regression Coefficients: Intercept = {beta[0]:.2f}, Slope = {beta[1]:.2f}")
