import numpy as np
import matplotlib.pyplot as plt
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import RBF, ConstantKernel as C


def gaussian_process_regression(data_x, data_y, target_x):
    """
    Perform Gaussian Process Regression on a given dataset.

    Parameters:
        data_x (numpy.ndarray): x values (1D array).
        data_y (numpy.ndarray): Corresponding y values.
        target_x (numpy.ndarray): The x values to predict.

    Returns:
        y_pred (numpy.ndarray): Predicted values at target_x.
        sigma (numpy.ndarray): Standard deviations of the predictions.
    """
    # Reshape data for sklearn
    X = np.atleast_2d(data_x).T
    target_X = np.atleast_2d(target_x).T

    # Define the kernel
    kernel = C(1.0, (1e-3, 1e3)) * RBF(1, (1e-2, 1e2))

    # Create and fit Gaussian Process Regressor
    gp = GaussianProcessRegressor(kernel=kernel, n_restarts_optimizer=10)
    gp.fit(X, data_y)

    # Predict on target points
    y_pred, sigma = gp.predict(target_X, return_std=True)
    return y_pred, sigma


def plot_gaussian_process(data_x, data_y, target_x):
    """
    Plot the Gaussian Process Regression results along with original data points.

    Parameters:
        data_x (numpy.ndarray): Original x values.
        data_y (numpy.ndarray): Original y values.
        target_x (numpy.ndarray): The x values to predict.
    """
    # Perform Gaussian Process Regression
    y_pred, sigma = gaussian_process_regression(data_x, data_y, target_x)

    # Plot results
    plt.figure(figsize=(10, 6))
    plt.plot(data_x, data_y, "o", label="Data points", markersize=8)
    plt.plot(target_x, y_pred, "b-", label="Prediction")
    plt.fill_between(
        target_x,
        y_pred - 1.96 * sigma,
        y_pred + 1.96 * sigma,
        alpha=0.2,
        color="gray",
        label="95% Confidence Interval",
    )
    plt.title("Gaussian Process Regression")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.legend()
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    # Example dataset
    data_x = np.array([0, 1, 2, 3, 4], dtype=float)
    data_y = np.array([2, 3.5, 5, 5.8, 6], dtype=float)

    # Target points to interpolate/predict
    target_x = np.linspace(0, 4, 100)

    # Perform and plot Gaussian Process Regression
    plot_gaussian_process(data_x, data_y, target_x)
