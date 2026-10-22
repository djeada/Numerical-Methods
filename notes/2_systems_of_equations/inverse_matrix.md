# Matrix Inverse

The inverse of a square matrix $A$ is denoted by $A^{-1}$. When it exists, it is the unique matrix whose product with $A$, on either side, is the identity matrix $I$. Mathematically, this is expressed as:

$$
AA^{-1} = A^{-1}A = I
$$

Not all matrices have an inverse. Only square matrices (those with the same number of rows and columns) are eligible to have an inverse, and even then, some do not. A matrix has an inverse if and only if it is non-singular, i.e., its determinant is not zero.

## Mathematical formulation

For an invertible square matrix $A$ of order $n$, the adjugate formula expresses the inverse as:

$$
A^{-1} = \frac{1}{\det(A)}\operatorname{adj}(A)
$$

Here $\det(A)$ is the determinant of $A$, and $\operatorname{adj}(A)$ is its adjugate.

The adjugate is the transpose of the cofactor matrix $C$. Its entries are $c_{ij}=(-1)^{i+j}\det(M_{ij})$, where $M_{ij}$ is the submatrix obtained by deleting row $i$ and column $j$ of $A$. The determinant $\det(M_{ij})$ is the corresponding minor.

## Using the inverse to solve matrix equations

For an invertible coefficient matrix, the inverse gives an algebraic expression for the solution of the following system:

$$
A\boldsymbol{x} = \boldsymbol{b}
$$

Multiply both sides on the left by $A^{-1}$, preserving the order of matrix multiplication:

$$
\implies A^{-1}A\boldsymbol{x} = A^{-1}\boldsymbol{b}
$$

$$
\implies I\boldsymbol{x} = A^{-1}\boldsymbol{b}
$$

$$
\implies \boldsymbol{x} = A^{-1}\boldsymbol{b}
$$

### Why the adjugate formula works

Cofactor expansion along row $i$ gives $\sum_k a_{ik}c_{ik}=\det(A)$. If the cofactors come from a different row $j\ne i$, the same sum is the determinant of a matrix with two equal rows, and is therefore zero. Thus

$$
(A\operatorname{adj}(A))_{ij}=\sum_k a_{ik}c_{jk}=\det(A)\delta_{ij},
$$

where $\delta_{ij}$ is $1$ for $i=j$ and $0$ otherwise. Dividing by the nonzero determinant proves the inverse formula.

There is also a computational interpretation: column $j$ of $A^{-1}$ solves $A\mathbf{z}_j=\mathbf{e}_j$, where $\mathbf{e}_j$ is column $j$ of the identity. Gauss–Jordan elimination solves all these right-hand sides together by transforming $[A\mid I]$ to $[I\mid A^{-1}]$. Alternatively, an LU factorization can be reused for the $n$ columns.

When the goal is only $A\mathbf{x}=\mathbf{b}$, solve that system with the factors directly. Forming all columns of $A^{-1}$ computes more information than the solve needs and can destroy sparsity. The adjugate expression is useful for proofs and small examples; determinant size alone is not a reliable numerical conditioning test because it changes strongly under scaling.

## Algorithm steps

**Implementation note:** the formula above (cofactors and adjugate) is shown for theory and for small hand calculations. It is far too expensive and numerically poor for general use, so the code in this repository computes the inverse by **Gauss-Jordan elimination with partial pivoting**: it row-reduces the augmented matrix $[A \mid I]$ to $[I \mid A^{-1}]$ and raises an error if a pivot is (numerically) zero, i.e. $A$ is singular. The steps below describe the adjugate method.

Finding the inverse of a matrix with the adjugate formula is a multi-step process:

1. Check if the matrix is invertible. A matrix is invertible if it is square (has the same number of rows and columns) and its determinant is not zero. If the matrix is not invertible, stop here, the matrix does not have an inverse.
2. Calculate the matrix of minors. The minor of each element in the matrix is the determinant of the matrix formed by removing the row and column of that element from the original matrix.
3. Form the matrix of cofactors. Multiply each minor by $(-1)^{i+j}$, where $i$ and $j$ are its row and column indices. This alternating sign pattern converts the minors into cofactors.
4. Calculate the adjugate of the matrix. The adjugate is simply the transpose of the cofactor matrix.
5. Finally, the inverse of the original matrix is the adjugate divided by the determinant of the original matrix.

## Example

Consider the following $2\times2$ matrix $A$ and compute its inverse step by step:

$$
A = \begin{bmatrix} 4 & 7 \\
2 & 6\\ \end{bmatrix}
$$

1. First, check if the matrix is invertible. The determinant is $\det(A)=4\cdot6-7\cdot2=10$, which is not zero, so the matrix is invertible.
2. The minor of 4 is the determinant of the matrix that results from removing the row and column of 4 from A, which is just 6. Similarly, the minor of 7 is 2, the minor of 2 is 7, and the minor of 6 is 4.
3. The cofactor matrix is obtained by multiplying each minor by $(-1)^{i+j}$. The off-diagonal entries get a minus sign, so the cofactor matrix is $\begin{bmatrix} 6 & -2 \\ -7 & 4 \end{bmatrix}$.
4. The adjugate of A is the transpose of the cofactor matrix, which is $\begin{bmatrix} 6 & -7 \\ -2 & 4 \end{bmatrix}$.
5. The inverse of A is the adjugate divided by the determinant, resulting in:

$$
A^{-1} = \frac{1}{10} \begin{bmatrix} 6 & -7 \\
-2 & 4\\ \end{bmatrix} = \begin{bmatrix} 0.6 & -0.7 \\
-0.2 & 0.4\\ \end{bmatrix}
$$

## Checking a computed inverse

For the worked matrix, multiplying in either order gives

$$
\begin{bmatrix}4&7\\2&6\end{bmatrix}
\begin{bmatrix}0.6&-0.7\\-0.2&0.4\end{bmatrix}
=\begin{bmatrix}1&0\\0&1\end{bmatrix}.
$$

In floating point arithmetic, inspect $\|A\widehat B-I\|$ and, when useful, $\|\widehat BA-I\|$ for the computed inverse $\widehat B$. These residuals check the defining identities. Their scale and the conditioning of $A$ still matter when interpreting the accuracy of individual inverse entries; a printed matrix that looks plausible is not itself a verification.

## Advantages

- The **inverse of a matrix** provides an analytical solution for systems of linear equations of the form $A \mathbf{x} = \mathbf{b}$, where $\mathbf{x} = A^{-1} \mathbf{b}$, offering a direct approach when the inverse is available.
- Matrix inversion is a **fundamental concept in linear algebra**, with applications ranging from solving systems of equations to transformations in geometry, optimization problems, and control systems.
- It enables the **characterization of matrix properties**, such as determining whether a matrix is singular (non-invertible) and finding relationships in systems represented by matrices.
- Inverse matrices are used in **statistical computations**, such as calculating the covariance matrix in multivariate analysis and solving normal equations in least squares problems.
- The computation of $A^{-1}$ can be performed **once and reused** for multiple right-hand sides $\mathbf{b}$, making it useful in scenarios where multiple systems need solving with the same matrix $A$.

## Limitations

- **Not all matrices are invertible.** A matrix must be square (having the same number of rows and columns) and non-singular (having a non-zero determinant) to possess an inverse.
- **Computational cost is high** for calculating matrix inverses directly. The process involves determinant calculations and can be computationally prohibitive for large matrices, with complexity on the order of $O(n^3)$ for typical methods like Gaussian elimination.
- Using the inverse to solve $A \mathbf{x} = \mathbf{b}$ is often **less efficient and less numerically stable** than solving the system directly with techniques like LU decomposition or iterative methods, especially for large or sparse systems.
- Small numerical errors in the computation of the inverse can **magnify errors in the solution**, particularly for ill-conditioned matrices, making direct inversion less desirable in sensitive applications.
- The process of inversion does not apply to **non-square or singular matrices,** and alternative approaches like pseudo-inverse computation or regularization methods must be employed for such cases.
