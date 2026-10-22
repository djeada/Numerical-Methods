# Eigenvalue Decomposition (EVD)

Eigenvalue decomposition, also called eigendecomposition, expresses a diagonalizable square matrix in a basis of its eigenvectors. In that basis, the transformation acts independently along each eigenvector by multiplying it by the corresponding eigenvalue. Changing back to the original coordinates gives the factorization $A=PDP^{-1}$. This separates the directions of the transformation from their scale factors and simplifies calculations such as matrix powers and linear differential equations. In applications including vibration analysis and principal component analysis, the factors describe modes or directions of variation. The key qualification is diagonalizability: a square matrix must have enough independent eigenvectors for the change of basis to be invertible.

The key idea is that certain square matrices can be represented as a product of a matrix of their eigenvectors and a diagonal matrix of their eigenvalues. This diagonalization separates the scaling factors (eigenvalues) from the directions of transformations (eigenvectors) encoded by the original matrix.

![Eigenvectors and eigenvalues in a matrix decomposition](https://github.com/user-attachments/assets/75c28eaf-d800-44cc-98cd-c0d9a9c5f14b)

## Mathematical formulation

Consider an $n \times n$ matrix $A$ that has $n$ linearly independent eigenvectors over the field being used. Its diagonal eigenvalue decomposition is:

$$
A = P D P^{-1},
$$
where:

I. **Eigenvalues ($\lambda_i$)**:

The eigenvalues of $A$ are the roots of the characteristic polynomial:

$$
\det(A - \lambda I) = 0.
$$

If we solve this polynomial equation and find $n$ eigenvalues (not necessarily distinct), we denote them as $\lambda_1, \lambda_2, \ldots, \lambda_n$.

II. **Eigenvectors ($v_i$)**:

For each eigenvalue $\lambda_i$, we find the corresponding eigenvector $v_i$ by solving:

$$
(A - \lambda_i I) v_i = 0.
$$

Each eigenvector $v_i$ is a nonzero vector associated with the eigenvalue $\lambda_i$.

III. **Eigenvector Matrix ($P$) and Eigenvalue Matrix ($D$)**:

Once we have the set of eigenvalues and eigenvectors:

Construct $D$ as a diagonal matrix whose diagonal entries are the eigenvalues:

$$
D = \begin{bmatrix}
\lambda_1 & 0 & \cdots & 0 \\
0 & \lambda_2 & \cdots & 0 \\
\vdots & \vdots & \ddots & \vdots \\
0 & 0 & \cdots & \lambda_n
\end{bmatrix}
$$

Construct $P$ such that its columns are the eigenvectors $v_1, v_2, \ldots, v_n$:

$$
P = \begin{bmatrix}
| & | &  & | \\
v_1 & v_2 & \cdots & v_n \\
| & | &  & |
\end{bmatrix}
$$

If $A$ is diagonalizable, and if the $v_i$ are chosen to be linearly independent, then $P$ is invertible and $A = P D P^{-1}$.

## Derivation

The derivation of EVD follows naturally from the definition of eigenvalues and eigenvectors. For each eigenvalue $\lambda_i$, we have:

$$
A v_i = \lambda_i v_i.
$$

If we gather all eigenvectors into the matrix $P$ and consider how $A$ acts on the columns of $P$:

$$
A
[v_1 \, v_2 \, \cdots \, v_n] = [A v_1 \, A v_2 \, \cdots \, A v_n] = [\lambda_1 v_1 \,
\lambda_2 v_2 \, \cdots \, \lambda_n v_n] = P D.
$$

If $P$ is invertible, we can write:

$$
A = P D P^{-1}.
$$

Not every matrix is guaranteed to have a full set of $n$ linearly independent eigenvectors. If it does, the matrix is said to be diagonalizable, and the above decomposition is possible. If not, the matrix cannot be decomposed purely into this form.

### When diagonalization exists

Distinct eigenvalues guarantee independent eigenvectors, but repeated eigenvalues need closer examination. The **algebraic multiplicity** of an eigenvalue counts its occurrences in the characteristic polynomial; its **geometric multiplicity** is the dimension of $\ker(A-\lambda I)$. Diagonalization is possible exactly when these multiplicities agree for every eigenvalue.

For example,

$$
J=\begin{bmatrix}1&1\\0&1\end{bmatrix}
$$

has eigenvalue $1$ twice, but $(J-I)v=0$ forces the second component to zero. Its eigenspace is only one-dimensional, so no invertible eigenvector matrix $P$ exists. In contrast, the identity matrix has the same repeated eigenvalue and a full eigenvector basis.

For a real symmetric matrix, the spectral theorem gives $A=QDQ^\top$ with orthonormal eigenvectors and real eigenvalues. For a complex normal matrix, the corresponding statement is $A=QDQ^*$, where $Q^*$ denotes the conjugate transpose. Orthogonality avoids amplification from an ill-conditioned change of basis. A general matrix still has a Schur decomposition with an orthogonal or unitary factor even if it is not diagonalizable; Jordan form is mainly a theoretical description because it is highly sensitive to perturbations.

For the example below, $\det P=3$ and

$$
P^{-1}=\frac13\begin{bmatrix}2&1\\-1&1\end{bmatrix}.
$$

Multiplying $PDP^{-1}$ reconstructs $\begin{bmatrix}4&1\\2&3\end{bmatrix}$, giving an explicit check of the decomposition. Computing $AP-PD$ is also a useful verification that avoids forming an inverse.

## Algorithm steps

**Step 1: Find eigenvalues.**

- Form the characteristic polynomial $\det(A - \lambda I) = 0$.
- Solve for $\lambda$. This may be done analytically for small matrices. For larger matrices, finding the roots of the characteristic polynomial is numerically ill-conditioned, so practical algorithms (such as the QR algorithm) compute eigenvalues without forming the polynomial.

**Step 2: Find eigenvectors.**

- For each eigenvalue $\lambda_i$, solve $(A - \lambda_i I)v_i = 0$.
- Ensure each eigenvector $v_i$ is normalized or scaled consistently.

**Step 3: Form $P$ and $D$.**

- Construct $D$ as the diagonal matrix with eigenvalues on the diagonal.
- Construct $P$ with eigenvectors as columns.

**Step 4: Verify invertibility of $P$.**

- If $P$ is invertible, then $A = P D P^{-1}$.

## Example

Let:

$$
A = \begin{bmatrix}
4 & 1 \\
2 & 3
\end{bmatrix}
$$

**Step 1: Find eigenvalues.**

The characteristic polynomial:

$$
\det(A - \lambda I) = \det\begin{bmatrix}4 - \lambda & 1 \\ 2 & 3 - \lambda\end{bmatrix} = (4-\lambda)(3-\lambda) - 2 = 0.
$$

Expanding:

$$
(4 - \lambda)(3 - \lambda) - 2 = (12 - 7\lambda + \lambda^2) - 2 = \lambda^2 -
7\lambda + 10 = 0.
$$

Solve $\lambda^2 -7\lambda +10=0$:

The roots are $\lambda_1=5$ and $\lambda_2=2$.

**Step 2: Find eigenvectors.**

For $\lambda_1 = 5$:

$$
(A - 5I)=\begin{bmatrix}-1 & 1 \\ 2 & -2\end{bmatrix}.
$$

Solve $(A-5I)v=0$ leads to $v_1 = [1,1]^T$.

For $\lambda_2 = 2$:

$$
(A - 2I)=\begin{bmatrix}2 & 1 \\ 2 & 1\end{bmatrix}
$$

Solve $(A-2I)v=0$ leads to $v_2 = [-1,2]^T$.

**Step 3: Form $P$ and $D$.**

$$
P = \begin{bmatrix}1 & -1 \\ 1 & 2\end{bmatrix}, \quad D = \begin{bmatrix}5 & 0 \\ 0 & 2\end{bmatrix}
$$

Thus:

$$
A = P D P^{-1}.
$$

## Advantages

I. **Simplification of Computations**:

Once in the form $A = P D P^{-1}$, computing powers of $A$ or applying certain transformations becomes much simpler. For example, $A^k = P D^k P^{-1}$, and since $D$ is diagonal, raising it to a power is straightforward.

II. **Insights into Matrix Structure**:

The eigendecomposition reveals the intrinsic "modes" of the linear transformation represented by $A$. Eigenvalues show how the transformation scales each eigen-direction, and eigenvectors show the directions of these fundamental modes.

III. **Efficiency and Stability for Symmetric Matrices**:

Working with $D$ instead of $A$ makes some computations much cheaper, particularly in areas like principal component analysis, spectral clustering, and other advanced data analysis tasks. For symmetric (or, more generally, normal) matrices the eigenvector matrix $P$ can be chosen orthogonal (unitary), so $P^{-1}=P^T$ in the real orthogonal case, or $P^{-1}=P^*$ in the complex unitary case. This makes the change of basis well-conditioned, although clustered eigenvalues can still make individual eigenvectors sensitive. For non-normal matrices $P$ can be ill-conditioned, and then $A = P D P^{-1}$ may be computed or used inaccurately; there, orthogonal decompositions such as the Schur form are preferred.

## Limitations

I. **Not All Matrices Are Diagonalizable**:

Some matrices cannot be broken down into a pure eigen decomposition if they do not have enough linearly independent eigenvectors. Jordan normal form supplies a theoretical description for such matrices, while Schur form supplies an orthogonal or unitary representation useful for numerical computation. A diagonal eigenvalue factorization itself is unavailable.

II. **Computational Cost for Large Matrices**:

Computing all eigenvalues and eigenvectors of a dense $n \times n$ matrix takes $O(n^3)$ operations (with a sizeable constant) and $O(n^2)$ memory, which becomes expensive for very large systems. Iterative methods such as the power method or Lanczos/Arnoldi iterations compute only a few eigenpairs more cheaply, especially for sparse matrices.

III. **Complex Eigenvalues**:

For real matrices, eigenvalues can be complex. While this is not a fundamental limitation, it means we must consider complex arithmetic when performing the decomposition, which may not be desired in some real-world applications.
