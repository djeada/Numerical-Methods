## Singular Value Decomposition (SVD)

Singular Value Decomposition, often abbreviated as SVD, is a powerful factorization method in linear algebra for rectangular matrices. 

## Key Concepts

- SVD provides a way to transform correlated variables into a set of uncorrelated ones that better expose the various relationships among the original data items.
- It is widely used in signal processing and statistics.

## Mathematical Formulation

SVD is the factorization of a real or complex matrix, with many useful applications in signal processing and statistics. For a given m × n matrix M, there exists a factorization such that:

M = UΣV*

where:

- U is an m × m unitary matrix,
- Σ is an m × n rectangular diagonal matrix with non-negative real numbers, and
- V* (the conjugate transpose of V) is an n × n unitary matrix. 
- The diagonal entries Σ[i,i] of Σ are known as the singular values of M.

## Algorithm Steps

1. Determine the eigenvalues and eigenvectors of M*M and MM*.
2. The singular values are the square roots of eigenvalues from step 1.
3. Form the matrices U and V from the eigenvectors.
4. Form the diagonal matrix of singular values.

## Example

Consider a 3x3 matrix A. SVD decomposes A into matrices U, Σ, and V* such that A = UΣV*.

## Advantages

- Provides optimal low-rank approximations, which are useful in applications like compression and denoising.
- Used in machine learning algorithms, like principal component analysis (PCA) and least squares linear regression.

## Limitations

- Computationally intensive for large matrices.
- The presence of zero or very small singular values can lead to numerical instability.
