## Matrices and Matrix Methods in Numerical Methods

- Matrices are fundamental in the field of numerical methods for solving linear systems, performing transformations, and more.
- Matrix methods involve algorithms for matrix manipulations and solve various computational problems.

## Key Concepts

- A **matrix** is a two-dimensional data structure where numbers are arranged into rows and columns.
- **Matrix multiplication** involves multiplying two matrices together to produce a third matrix.
- **Matrix inversion** involves finding a matrix that, when multiplied with the original matrix, gives an identity matrix.
- **Determinants** are a special number that can be calculated from a square matrix.

## Matrix Methods 

- **LU Decomposition**: This method decomposes a matrix into a product of a lower triangular matrix (L) and an upper triangular matrix (U). It simplifies solving systems of linear equations.

-  **Singular Value Decomposition (SVD)**: A powerful method that decomposes a matrix into the product of three matrices: U, Σ, and V^T. U and V are orthogonal matrices, and Σ is a diagonal matrix. SVD is used in a wide range of applications, including machine learning, image compression, and signal processing.

- **QR Decomposition**: It is another matrix factorization method where a matrix A is decomposed into a product of an orthogonal matrix Q and upper triangular matrix R. This method is widely used in the numerical solution of linear least squares problems.

- **Power Method**: It is an iterative method that computes the largest eigenvalue and the corresponding eigenvector of a matrix. This method is commonly used in Google's PageRank algorithm and other applications involving network analysis.

## Example

- SVD Example: Consider a matrix A = [[4, 11], [2, 1]]. The singular value decomposition of A results in matrices U, Σ, and V such that A = U * Σ * V^T.

- QR Decomposition Example: For a square matrix A = [[12, -51, 4], [6, 167, -68], [-4, 24, -41]], the QR decomposition results in an orthogonal matrix Q and an upper triangular matrix R.

- Power Method Example: Consider a square matrix A = [[2, 1], [1, 3]]. The power method will give the largest eigenvalue and its corresponding eigenvector.

## Applications

- Matrices are used in 3D graphics to perform transformations such as translation, scaling, rotation.
- In physics, matrices are used in quantum mechanics, optics, and electrical circuitry.
- In machine learning, matrices are used in various algorithms, including linear regression, PCA, and more.

## Caveats

- Not all matrices have an inverse. Those that do not are called singular or degenerate.
- The Gauss-Seidel method may not converge for all systems of linear equations.
- LU decomposition does not work for all square matrices. The matrix must be square and not singular.
