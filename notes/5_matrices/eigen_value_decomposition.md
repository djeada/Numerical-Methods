## Eigenvalue Decomposition (EVD)

Eigenvalue Decomposition, or Eigendecomposition, is a method of factorizing square matrices into their eigenvalues and eigenvectors.

## Key Concepts

- Eigendecomposition breaks down a matrix into a canonical form, representing the matrix in terms of its eigenvalues and eigenvectors.
- Only diagonalizable matrices can undergo this form of factorization.

## Mathematical Formulation

Given a square matrix $A$, it can be factorized as:

$$A = PDP^{-1}$$

where:

- $D$ is a diagonal matrix containing the eigenvalues of $A$ on its diagonal. If $\lambda_1, \lambda_2, ..., \lambda_n$ are the eigenvalues of $A$, then $D$ is of the form:

$$
D = 
\begin{bmatrix}
\lambda_1 & 0 & 0 & \cdots & 0 \\
0 & \lambda_2 & 0 & \cdots & 0 \\
0 & 0 & \lambda_3 & \cdots & 0 \\
\vdots & \vdots & \vdots & \ddots & \vdots \\
0 & 0 & 0 & \cdots & \lambda_n
\end{bmatrix}
$$

- $P$ is a matrix composed of the corresponding eigenvectors of $A$ in its columns. If $v_1, v_2, ..., v_n$ are the column vectors representing the eigenvectors corresponding to the eigenvalues of $A$, then $P$ is of the form:

$$
P = 
\begin{bmatrix}
| & | & | & & | \\
v_1 & v_2 & v_3 & \cdots & v_n \\
| & | & | & & |
\end{bmatrix}
$$

- $P^{-1}$ is the inverse of the matrix $P$.

Eigenvalues $\lambda$ of a matrix $A$ are computed by solving the characteristic equation:

$$det(A - \lambda I) = 0$$

Here, $I$ denotes the identity matrix of the same dimension as $A$. The eigenvectors are then computed by solving the homogeneous system of linear equations:

$$(A - \lambda I)v = 0$$

for each eigenvalue $\lambda$, where $v$ is the corresponding eigenvector.

## Algorithm Steps

1. Compute the eigenvalues of the matrix $A$ by solving the characteristic equation.
2. For each eigenvalue, compute the corresponding eigenvector by solving the associated homogeneous system of linear equations.
3. Form the matrices $P$ and $D$ using the computed eigenvectors and eigenvalues.

## Example

Consider a 2x2 matrix $A$ given by:

$$
A = 
\begin{bmatrix}
4 & 1 \\
2 & 3
\end{bmatrix}
$$

1. Compute the eigenvalues of $A$:

Solve the characteristic equation $det(A - \lambda I) = 0$:

$$
det\left(\begin{bmatrix}
4-\lambda & 1 \\
2 & 3-\lambda
\end{bmatrix}\right) = 0
$$

which simplifies to $(4-\lambda)(3-\lambda) - 2 = 0$, giving the roots $\lambda_1 = 5$ and $\lambda_2 = 2$.

2. Compute the corresponding eigenvectors:

For $\lambda_1 = 5$, solve the system $(A - 5I)v = 0$:

$$
\begin{bmatrix}
-1 & 1 \\
2 & -2
\end{bmatrix}v = 0
$$

This gives $v_1 = [1, 1]$.

Similarly, for $\lambda_2 = 2$, solve the system $(A - 2I)v = 0$:

$$
\begin{bmatrix}
2 & 1 \\
2 & 1
\end{bmatrix}v = 0
$$

This gives $v_2 = [-1, 2]$.

3. Form the matrices $P$ and $D$:

$$
P = \begin{bmatrix}
1 & -1 \\
1 & 2
\end{bmatrix}
, \quad
D = \begin{bmatrix}
5 & 0 \\
0 & 2
\end{bmatrix}
$$

Thus, we have $A = PDP^{-1}$.

## Advantages

- The decomposed form simplifies many matrix computations and enhances numerical stability.
- It aids in the development of certain matrix algorithms.

## Limitations

- Not all matrices are diagonalizable, hence, not all matrices can be decomposed in this manner.
- Computation of EVD can be computationally expensive for large matrices.
