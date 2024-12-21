import numpy as np
import matplotlib.pyplot as plt
from numpy.linalg import norm


def power_method(A, max_iterations=100, tolerance=1e-6):
    """
    Power Method for finding the dominant eigenvalue and its associated eigenvector.

    Parameters:
        A (ndarray): Square numpy matrix.
        max_iterations (int): Maximum number of iterations.
        tolerance (float): Convergence threshold for the eigenvalue.

    Returns:
        dominant_eigenvalue (float): The largest eigenvalue in magnitude.
        dominant_eigenvector (ndarray): Corresponding eigenvector.
    """
    n = A.shape[0]
    x = np.random.rand(n)  # Initial random vector
    x = x / norm(x)  # Normalize the initial vector

    eigenvalues = []  # Track eigenvalue convergence

    for i in range(max_iterations):
        # Matrix-vector multiplication
        y = np.dot(A, x)
        # Estimate the dominant eigenvalue using the Rayleigh quotient
        eigenvalue = np.dot(x.T, y)
        eigenvalues.append(eigenvalue)

        # Normalize the resulting vector
        x_next = y / norm(y)

        # Check convergence
        if norm(x_next - x) < tolerance:
            print(f"Converged after {i+1} iterations.")
            break

        x = x_next

    dominant_eigenvalue = eigenvalue
    dominant_eigenvector = x

    # Plot convergence
    plt.figure(figsize=(8, 6))
    plt.plot(range(1, len(eigenvalues) + 1), eigenvalues, marker="o", linestyle="-")
    plt.title("Convergence of Dominant Eigenvalue")
    plt.xlabel("Iteration")
    plt.ylabel("Eigenvalue Estimate")
    plt.grid(True)
    plt.show()

    return dominant_eigenvalue, dominant_eigenvector


# Example Matrix A
A = np.array([[4, 1], [2, 3]])

# Perform Power Method for Dominant Eigenvalue and Eigenvector
eigenvalue, eigenvector = power_method(A)
print("\nDominant Eigenvalue (Power Method):", eigenvalue)
print("Dominant Eigenvector (Power Method):", eigenvector)
