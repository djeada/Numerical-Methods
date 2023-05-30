## Eigenvalue Decomposition (EVD)

Eigenvalue Decomposition, also known as Eigendecomposition, is a method of factorization for square matrices that represents them in terms of their eigenvalues and eigenvectors.

## Key Concepts

- Eigendecomposition decomposes a matrix into a canonical form, whereby the matrix is represented in terms of its eigenvalues and eigenvectors. 
- Only diagonalizable matrices can be factorized in this way.

## Mathematical Formulation

Given a square matrix A, it can be factorized as:

A = PDP⁻¹

where:

- D is a diagonal matrix whose entries are the eigenvalues of A,
- P is a matrix whose columns are the corresponding eigenvectors of A,
- P⁻¹ is the inverse of the matrix P.

The diagonal matrix D is such that the entry in the i-th row and i-th column is the eigenvalue corresponding to the i-th eigenvector (the i-th column of P).

## Algorithm Steps

1. Find the eigenvalues of the matrix.
2. For each eigenvalue, find the corresponding eigenvector.
3. Form the matrix P from the eigenvectors and the matrix D from the eigenvalues.

## Example

Consider a 2x2 matrix A. The eigendecomposition of A results in matrices P and D such that A = PDP⁻¹.

## Advantages

- The decomposed form can make many matrix calculations easier and more stable.
- Useful in the development of certain matrix algorithms.

## Limitations

- Not all matrices are diagonalizable and thus not all matrices can be decomposed in this manner.
- Computationally expensive for large matrices.
