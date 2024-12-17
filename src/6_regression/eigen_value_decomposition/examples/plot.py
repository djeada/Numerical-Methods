import numpy as np
import matplotlib.pyplot as plt
from numpy.linalg import eig, inv

def eigen_decomposition_visualize(A):
    """
    Performs and visualizes the Eigenvalue Decomposition (EVD) of a square matrix A.

    Parameters:
        A (ndarray): A square numpy matrix.
    """
    # Compute eigenvalues and eigenvectors
    eigenvalues, eigenvectors = eig(A)
    D = np.diag(eigenvalues)  # Diagonal matrix D
    P = eigenvectors          # Matrix P with eigenvectors as columns
    P_inv = inv(P)            # Inverse of P

    # Verify decomposition A = P D P^{-1}
    A_reconstructed = P @ D @ P_inv

    # Print results
    print("Original Matrix A:")
    print(A)
    print("\nEigenvalues (D):")
    print(D)
    print("\nEigenvectors (P):")
    print(P)
    print("\nReconstructed A (P D P^{-1}):")
    print(A_reconstructed)

    # Plotting: Eigenvectors, Eigenvalues, and Reconstruction
    fig, axs = plt.subplots(1, 3, figsize=(18, 6))

    # Plot 1: Original Matrix A Transformation (Conceptual)
    axs[0].set_title("Original Matrix A")
    axs[0].imshow(A, cmap='viridis')
    axs[0].axis('off')
    axs[0].set_xlabel('A transformation')

    # Plot 2: Eigenvectors and Eigenvalues
    axs[1].set_title("Eigenvectors (P) and Eigenvalues (D)")
    axs[1].imshow(D, cmap='coolwarm')
    axs[1].set_xlabel('Diagonal Eigenvalues (D)')

    # Plot 3: Reconstructed A
    axs[2].set_title("Reconstructed Matrix A")
    axs[2].imshow(A_reconstructed, cmap='viridis')
    axs[2].axis('off')
    axs[2].set_xlabel('A = P D P^{-1}')

    plt.tight_layout()
    plt.show()

# Example Matrix A
A = np.array([[4, 1],
              [2, 3]])

# Perform and visualize Eigenvalue Decomposition
eigen_decomposition_visualize(A)
