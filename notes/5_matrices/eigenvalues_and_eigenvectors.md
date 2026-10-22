# Eigenvalues and Eigenvectors

An eigenvector identifies a direction that a square matrix preserves under multiplication, while its eigenvalue records the scaling along that direction. The scaling may include a sign change or, over the complex numbers, a phase change. These concepts connect matrix transformations to vibration modes, geometric transformations in computer graphics, and directions of variation in machine learning. They also form the starting point for eigendecomposition and iterative eigenvalue algorithms.

## Definitions

An **eigenvector** of a square matrix $A$ is a non-zero vector $v$ that, when multiplied by $A$, results in a scaled version of $v$. The scalar factor is the **eigenvalue** corresponding to that eigenvector. In mathematical terms, this relationship is described as:

$$
A v = \lambda v
$$

where:

- $A$ is a square matrix,
- $v$ is an eigenvector of $A$,
- $\lambda$ is the corresponding eigenvalue.

## Procedure for finding eigenvalues and eigenvectors

1. **Eigenvalues**: Eigenvalues are calculated by solving the characteristic equation, formulated as $\det(A - \lambda I) = 0$. Here, $I$ is the identity matrix of the same dimension as $A$, and $\det(\cdot)$ denotes the determinant. The roots of this equation yield the eigenvalues.

2. **Eigenvectors**: Upon finding each eigenvalue, its corresponding eigenvectors are obtained by substituting the eigenvalue into the equation $(A - \lambda I)v = 0$, followed by computing the null space.

## Why the characteristic equation appears

Rearranging $Av=\lambda v$ gives $(A-\lambda I)v=0$. A homogeneous square system has a nonzero solution exactly when its matrix is singular, hence the condition $\det(A-\lambda I)=0$. The zero vector is excluded because it satisfies this equation for every scalar and therefore identifies no particular eigenvalue.

Eigenvectors are directions: if $v$ is an eigenvector, so is every nonzero multiple of $v$. Normalizing to $\|v\|_2=1$ removes its arbitrary length, but its sign, or complex phase, remains arbitrary. Two answers with opposite signs may therefore describe the same eigenvector.

For any computed eigenpair $(\widehat\lambda,\widehat v)$, inspect the residual $r=A\widehat v-\widehat\lambda\widehat v$. In the example, $A[1,-2]^\top=[2,-4]^\top=2[1,-2]^\top$ and $A[1,1]^\top=[5,5]^\top=5[1,1]^\top$. Trace and determinant give additional checks: $2+5=\operatorname{tr}(A)=7$ and $2\cdot5=\det(A)=10$.

A real symmetric matrix always has real eigenvalues and an orthonormal eigenvector basis. General real matrices can have complex conjugate pairs, as the rotation matrix $\begin{bmatrix}0&-1\\1&0\end{bmatrix}$ demonstrates with eigenvalues $\pm i$. See [eigendecomposition](eigen_value_decomposition.md) for the additional condition needed to build a complete eigenvector basis.

## Example

Consider a 2x2 matrix:

$$
A = \begin{bmatrix} 4 & 1 \\
2 & 3 \\ \end{bmatrix}
$$

1. Solve the characteristic equation $\det(A - \lambda I) = 0$, which gives $\lambda^2 - 7\lambda + 10 = 0$. The roots of this equation are $\lambda_1 = 2$ and $\lambda_2 = 5$, representing the eigenvalues.

2. To find the corresponding eigenvectors:

   - For $\lambda_1 = 2$, solve the equation $(A - 2I)v = 0$, which yields the eigenvector $v_1=[1,-2]^\top$.
   - For $\lambda_2 = 5$, solve the equation $(A - 5I)v = 0$, which yields the eigenvector $v_2=[1,1]^\top$.

## Applications

- Eigenvalues and eigenvectors are used in PCA for dimensionality reduction, enabling data to be represented in fewer dimensions without significant loss of information.
- They are employed in solving systems of linear differential equations, providing a simplified approach to understanding dynamic systems.
- In quantum mechanics, eigenvalues and eigenvectors of operators correspond to physically measurable quantities and their associated states, respectively.

## Limitations

- Eigenvalues and eigenvectors are defined only for square matrices. A real matrix may have complex eigenvalues, and not every square matrix has a full set of linearly independent eigenvectors (defective matrices).
- For large matrices, the computation of eigenvalues and eigenvectors can be computationally demanding (about $O(n^3)$ operations for a dense $n \times n$ matrix), potentially slowing down analyses or algorithm implementations.
- Forming the characteristic polynomial and solving for its roots, as in the hand calculation above, is numerically unreliable for larger matrices, especially with repeated eigenvalues; library routines use methods such as the QR algorithm instead.
