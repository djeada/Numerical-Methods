## Singular Value Decomposition (SVD)

Singular Value Decomposition, or SVD, is a method of factorizing matrices, which generalizes the Eigendecomposition to non-square matrices.

## Key Concepts

- SVD provides a way to break down a matrix into simpler, meaningful pieces. 
- Every real matrix has a singular value decomposition, but the same is not true of the Eigenvalue Decomposition.

## Mathematical Formulation

Given an $m \times n$ matrix $A$, it can be factorized as:

$$A = U\Sigma V^{T}$$

where:

- $U$ is an $m \times m$ matrix formed by the eigenvectors of $AA^{T}$. If $u_1, u_2, ..., u_m$ are the column vectors representing the eigenvectors of $AA^{T}$, then $U$ is of the form:

$$
U = 
\begin{bmatrix}
| & | & & | \\
u_1 & u_2 & \cdots & u_m \\
| & | & & |
\end{bmatrix}
$$

- $\Sigma$ is an $m \times n$ diagonal matrix formed by the square roots of the eigenvalues of $AA^{T}$ (or equivalently, $A^{T}A$), sorted in decreasing order. If $\sigma_1, \sigma_2, ..., \sigma_p$ are the square roots of these eigenvalues ($p$ is the rank of matrix $A$), then $\Sigma$ is of the form:

$$
\Sigma = 
\begin{bmatrix}
\sigma_1 & 0 & \cdots & 0 & \cdots & 0 \\
0 & \sigma_2 & \cdots & 0 & \cdots & 0 \\
\vdots & \vdots & \ddots & \vdots & & \vdots \\
0 & 0 & \cdots & \sigma_p & \cdots & 0 \\
\vdots & \vdots & & \vdots & \ddots & \vdots \\
0 & 0 & \cdots & 0 & \cdots & 0
\end{bmatrix}
$$

- $V^{T}$ is an $n \times n$ matrix formed by the eigenvectors of $A^{T}A$. If $v_1, v_2, ..., v_n$ are the column vectors representing the eigenvectors of $A^{T}A$, then $V^{T}$ is of the form:

$$
V^{T} = 
\begin{bmatrix}
... & v_1^{T} & ... \\
... & v_2^{T} & ... \\
& \vdots & \\
... & v_n^{T} & ...
\end{bmatrix}
$$

## Algorithm Steps

1. Calculate $A^{T}A$ and $AA^{T}$.

2. Compute the eigenvalues and the corresponding eigenvectors of $A^{T}A$ and $AA^{T}$. The eigenvalues of both these matrices are the same, and they correspond to the squares of the singular values of $A$.

3. The eigenvectors corresponding to the non-zero eigenvalues of $A^{T}A$ form the columns of $V$ while the eigenvectors corresponding to the non-zero eigenvalues of $AA^{T}$ form the columns of $U$.

4. The singular values $\sigma_i$ are calculated as the square root of the eigenvalues from either $A^{T}A$ or $AA^{T}$, arranged in decreasing order on the diagonal of an $m \times n$ matrix $\Sigma$.

5. The matrix $V$ is obtained by arranging the eigenvectors corresponding to the eigenvalues of $A^{T}A$ as columns. 

6. The matrix $U$ is formed by arranging the eigenvectors corresponding to the eigenvalues of $AA^{T}$ as columns.

## Example

Consider a 2x2 matrix $A$ given by:

$$
A = 
\begin{bmatrix}
3 & 4 \\
2 & 1
\end{bmatrix}
$$

1. Compute the matrices $A^{T}A$ and $AA^{T}$:

$$
A^{T}A = 
\begin{bmatrix}
13 & 14 \\
14 & 17
\end{bmatrix}
, \quad
AA^{T} = 
\begin{bmatrix}
25 & 10 \\
10 & 5
\end{bmatrix}
$$

2. Compute the eigenvalues and corresponding eigenvectors of both $A^{T}A$ and $AA^{T}$.

For $A^{T}A$, the characteristic equation is $det(A^{T}A - \lambda I) = 0$, which gives:

$$
\begin{vmatrix}
13-\lambda & 14 \\
14 & 17-\lambda
\end{vmatrix} = 0
$$

Solving this equation yields the eigenvalues $\lambda_1 = 30$ and $\lambda_2 = 0$.

Next, compute the eigenvectors corresponding to these eigenvalues by solving $(A^{T}A - \lambda I)v = 0$. The corresponding eigenvectors are $v_1 = [\frac{1}{\sqrt{2}}, \frac{1}{\sqrt{2}}]$ for $\lambda_1$, and $v_2 = [-\frac{1}{\sqrt{2}}, \frac{1}{\sqrt{2}}]$ for $\lambda_2$.

Similarly, for $AA^{T}$, solving the characteristic equation yields the eigenvalues $\lambda_1 = 30$ and $\lambda_2 = 0$, with corresponding eigenvectors $u_1 = [\frac{2}{\sqrt{5}}, \frac{1}{\sqrt{5}}]$ for $\lambda_1$, and $u_2 = [-\frac{1}{\sqrt{5}}, \frac{2}{\sqrt{5}}]$ for $\lambda_2$.

3. Form the matrices $U$, $\Sigma$ and $V^{T}$:

$$
U = \begin{bmatrix}
\frac{2}{\sqrt{5}} & -\frac{1}{\sqrt{5}} \\
\frac{1}{\sqrt{5}} & \frac{2}{\sqrt{5}}
\end{bmatrix}
, \quad
\Sigma = \begin{bmatrix}
\sqrt{30} & 0 \\
0 & 0
\end{bmatrix}
, \quad
V^{T} = \begin{bmatrix}
\frac{1}{\sqrt{2}} & \frac{1}{\sqrt{2}} \\
-\frac{1}{\sqrt{2}} & \frac{1}{\sqrt{2}}
\end{bmatrix}
$$

Thus, we have $A = U\Sigma V^{T}$.

## Advantages

- SVD exists for any type of matrix (m x n), whereas Eigendecomposition only exists for square (n x n) matrices.
- SVD is used in a variety of applications such as signal processing, statistics, and solving linear equations.

## Limitations

- SVD computation is more complex than Eigendecomposition, especially for large matrices.
- Since the calculation of SVD involves finding eigenvalues and eigenvectors of $AA^T$ and $A^TA$, which could be large matrices, the computation can be costly.
