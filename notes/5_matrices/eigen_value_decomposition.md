## Introduction

Eigenvalue Decomposition (EVD), also known as Eigendecomposition, is a fundamental operation in linear algebra that breaks down a square matrix into a simpler form defined by its eigenvalues and eigenvectors. This decomposition provides deep insights into the properties and structure of a matrix, enabling simplifications in numerous computations such as matrix powers, transformations, and the solution of systems of linear equations. In many applications — from vibration analysis in engineering to principal component analysis in data science — EVD plays a critical role.

The key idea is that certain square matrices can be represented as a product of a matrix of their eigenvectors and a diagonal matrix of their eigenvalues. This diagonalization separates the scaling factors (eigenvalues) from the directions of transformations (eigenvectors) encoded by the original matrix.

*(PLOT 1: A conceptual plot illustrating how an original linear transformation represented by $A$ can be decomposed into simpler operations based on eigen-directions and eigen-scales.)*

## Mathematical Formulation

Consider an $n \times n$ matrix $A$. The Eigenvalue Decomposition of $A$ is given by:

$$A = P D P^{-1},$$
where:

I. **Eigenvalues ($\lambda_i$)**:  

The eigenvalues of $A$ are the roots of the characteristic polynomial:

$$\det(A - \lambda I) = 0.$$

If we solve this polynomial equation and find $n$ eigenvalues (not necessarily distinct), we denote them as $\lambda_1, \lambda_2, \ldots, \lambda_n$.

II. **Eigenvectors ($v_i$)**:  

For each eigenvalue $\lambda_i$, we find the corresponding eigenvector $v_i$ by solving:

$$(A - \lambda_i I) v_i = 0.$$

Each eigenvector $v_i$ is a nonzero vector associated with the eigenvalue $\lambda_i$.

III. **Eigenvector Matrix ($P$) and Eigenvalue Matrix ($D$)**:
Once we have the set of eigenvalues and eigenvectors:
- Construct $D$ as a diagonal matrix whose diagonal entries are the eigenvalues:

 $$D = \begin{bmatrix}

 \lambda_1 & 0 & \cdots & 0 \\

 0 & \lambda_2 & \cdots & 0 \\

 \vdots & \vdots & \ddots & \vdots \\

 0 & 0 & \cdots & \lambda_n

 \end{bmatrix}.$$
- Construct $P$ such that its columns are the eigenvectors $v_1, v_2, \ldots, v_n$:

 $$P = \begin{bmatrix}

 | & | &  & | \\
 v_1 & v_2 & \cdots & v_n \\
 | & | &  & |
 \end{bmatrix}.$$

If $A$ is diagonalizable, and if the $v_i$ are chosen to be linearly independent, then $P$ is invertible and $A = P D P^{-1}$.

*(PLOT 2: A schematic showing how eigenvectors form the columns of $P$ and how $D$ is a simple diagonal matrix with eigenvalues.)*

## Derivation

The derivation of EVD follows naturally from the definition of eigenvalues and eigenvectors. For each eigenvalue $\lambda_i$, we have:

$$A v_i = \lambda_i v_i.$$

If we gather all eigenvectors into the matrix $P$ and consider how $A$ acts on the columns of $P$:

$$A [v_1 \, v_2 \, \cdots \, v_n] = [A v_1 \, A v_2 \, \cdots \, A v_n] = [\lambda_1 v_1 \, \lambda_2 v_2 \, \cdots \, \lambda_n v_n] = P D.$$

If $P$ is invertible, we can write:

$$A = P D P^{-1}.$$

Not every matrix is guaranteed to have a full set of $n$ linearly independent eigenvectors. If it does, the matrix is said to be diagonalizable, and the above decomposition is possible. If not, the matrix cannot be decomposed purely into this form.

*(PLOT 3: A flow diagram showing the steps from defining eigenvalues and eigenvectors to assembling $P$ and $D$ and confirming $A = PDP^{-1}$.)*

## Algorithm Steps

I. **Find Eigenvalues**:
- Form the characteristic polynomial $\det(A - \lambda I) = 0$.
- Solve for $\lambda$. This may be done analytically for small matrices or numerically for larger matrices.
II. **Find Eigenvectors**:
- For each eigenvalue $\lambda_i$, solve $(A - \lambda_i I)v_i = 0$.
- Ensure each eigenvector $v_i$ is normalized or scaled consistently.
III. **Form $P$ and $D$**:
- Construct $D$ as the diagonal matrix with eigenvalues on the diagonal.
- Construct $P$ with eigenvectors as columns.
IV. **Verify Invertibility of $P$**:
- If $P$ is invertible, then $A = P D P^{-1}$.
*(PLOT 4: A step-by-step illustration of computing eigenvalues, eigenvectors, and forming $P$ and $D$.)*

## Example

Let:

$$A = \begin{bmatrix}

4 & 1 \\

2 & 3

\end{bmatrix}.$$

I. **Find Eigenvalues**:  

The characteristic polynomial:

$$\det(A - \lambda I) = \det\begin{bmatrix}4 - \lambda & 1 \\ 2 & 3 - \lambda\end{bmatrix} = (4-\lambda)(3-\lambda) - 2 = 0.$$

Expanding:

$$(4-\lambda)(3-\lambda) - 2 = (12 -7\lambda + \lambda^2) - 2 = \lambda^2 -7\lambda +10=0.$$

Solve $\lambda^2 -7\lambda +10=0$:

The roots are $\lambda_1=5$ and $\lambda_2=2$.

II. **Find Eigenvectors**:

For $\lambda_1 = 5$:

$$(A - 5I)=\begin{bmatrix}-1 & 1 \\ 2 & -2\end{bmatrix}.$$

Solve $(A-5I)v=0$ leads to $v_1 = [1,1]^T$.

For $\lambda_2 = 2$:

$$(A - 2I)=\begin{bmatrix}2 & 1 \\ 2 & 1\end{bmatrix}.$$

Solve $(A-2I)v=0$ leads to $v_2 = [-1,2]^T$.

III. **Form $P$ and $D$**:

$$P = \begin{bmatrix}1 & -1 \\ 1 & 2\end{bmatrix}, \quad D = \begin{bmatrix}5 & 0 \\ 0 & 2\end{bmatrix}.$$

Thus:

$$A = P D P^{-1}.$$

*(PLOT 5: A geometric interpretation showing the directions defined by eigenvectors and scalings by eigenvalues for the given $A$.)*

## Advantages

I. **Simplification of Computations**:  

Once in the form $A = P D P^{-1}$, computing powers of $A$ or applying certain transformations becomes much simpler. For example, $A^k = P D^k P^{-1}$, and since $D$ is diagonal, raising it to a power is straightforward.

II. **Insights into Matrix Structure**:  

The eigendecomposition reveals the intrinsic "modes" of the linear transformation represented by $A$. Eigenvalues show how the transformation scales each eigen-direction, and eigenvectors show the directions of these fundamental modes.

III. **Numerical Stability in Some Computations**:  

Working with $D$ instead of $A$ can improve numerical stability and make some algorithms more efficient, particularly in areas like principal component analysis, spectral clustering, and other advanced data analysis tasks.

*(PLOT 6: A bar chart comparing computational effort for various matrix operations with and without using EVD.)*

## Limitations

I. **Not All Matrices Are Diagonalizable**:  

Some matrices cannot be broken down into a pure eigen decomposition if they do not have enough linearly independent eigenvectors. For such matrices, more generalized decompositions like the Jordan normal form are required.

II. **Computational Cost for Large Matrices**:  

Finding eigenvalues and eigenvectors for large matrices can be computationally expensive. Efficient numerical algorithms and approximations exist, but they may still be costly for very large systems.

III. **Complex Eigenvalues**:  

For real matrices, eigenvalues can be complex. While this is not a fundamental limitation, it means we must consider complex arithmetic when performing the decomposition, which may not be desired in some real-world applications.

*(PLOT 7: A plot illustrating eigenvalues in the complex plane, showing that real matrices can have complex eigenvalues and still be decomposed over the complex field.)*
