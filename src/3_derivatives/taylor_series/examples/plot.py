import numpy as np
import matplotlib.pyplot as plt
from math import factorial

def taylor_series_approximation(f, df, a, x_range, n_terms):
    """
    Compute the Taylor series approximation of a function up to a given number of terms.

    Parameters:
        f (callable): The function to approximate.
        df (list of callable): List of derivatives of the function.
        a (float): The point of expansion.
        x_range (numpy.ndarray): Range of x values for plotting.
        n_terms (int): Number of terms in the Taylor series.

    Returns:
        approx (numpy.ndarray): The approximated values of the function.
    """
    approximations = np.zeros((n_terms, len(x_range)))
    for n in range(n_terms):
        approximations[n] = (df[n](a) / factorial(n)) * (x_range - a)**n
    return approximations

def plot_taylor_series(f, df, a, x_range, n_terms):
    """
    Plot a function and its Taylor series approximations.

    Parameters:
        f (callable): The original function.
        df (list of callable): List of derivatives of the function.
        a (float): The point of expansion.
        x_range (numpy.ndarray): Range of x values for plotting.
        n_terms (int): Number of terms in the Taylor series.
    """
    y_true = f(x_range)
    approximations = taylor_series_approximation(f, df, a, x_range, n_terms)

    plt.figure(figsize=(10, 6))
    plt.plot(x_range, y_true, label=f'Original function $f(x)$', color='black', linewidth=2)

    partial_sum = np.zeros_like(x_range)
    for n in range(n_terms):
        partial_sum += approximations[n]
        plt.plot(x_range, partial_sum, label=f'Taylor series (n={n})')

    plt.axvline(x=a, color='red', linestyle='--', label=f'Expansion point $a={a}$')
    plt.title("Taylor Series Approximation")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    # Define the function and its derivatives
    f = lambda x: np.exp(x)
    df = [lambda x: np.exp(x),  # f'(x)
          lambda x: np.exp(x),  # f''(x)
          lambda x: np.exp(x),  # f'''(x)
          lambda x: np.exp(x)]  # Higher derivatives (all the same for exp)

    a = 0  # Point of expansion
    x_range = np.linspace(-2, 2, 400)  # Range of x values
    n_terms = 5  # Number of terms in the Taylor series

    # Plot the Taylor series approximation
    plot_taylor_series(f, df, a, x_range, n_terms)
