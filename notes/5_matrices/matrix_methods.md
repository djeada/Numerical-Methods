# Matrix Methods

Matrices organize numbers into rows and columns and represent linear transformations, systems of equations, and collections of data. Their dimensions determine which operations are defined, while their structure determines which numerical methods are appropriate. In applied mathematics and engineering, the same matrix notation can describe a geometric transformation, a coupled physical model, a high-dimensional calculation, or a local optimization step. This note introduces the basic operations and the factorizations used throughout the repository. The central numerical idea is to use a matrix's structure: triangular factors simplify solves, orthogonal factors preserve lengths, and singular values expose rank and sensitivity. These representations make large calculations systematic without requiring every task to be reduced to an explicit inverse.

## Representation of matrices

A matrix is denoted by an uppercase letter, while its elements are commonly denoted by the corresponding lowercase letter with subscripts indicating row and column position. For instance, a generic 3×3 matrix $A$ might look like this:

$$
A = \begin{bmatrix}
a_{11} & a_{12} & a_{13} \\
a_{21} & a_{22} & a_{23} \\
a_{31} & a_{32} & a_{33}
\end{bmatrix}
$$

One way to visualize a 3×3 matrix is with a diagram that shows the rows and columns:

| Position | Column 1 | Column 2 | Column 3 |
| --- | --- | --- | --- |
| Row 1 | $a_{11}$ | $a_{12}$ | $a_{13}$ |
| Row 2 | $a_{21}$ | $a_{22}$ | $a_{23}$ |
| Row 3 | $a_{31}$ | $a_{32}$ | $a_{33}$ |

Rows are horizontal sequences of elements, and columns are vertical sequences. This basic structure underpins all matrix-based numerical methods, from simple multiplication to more advanced decompositions.

## Common matrix operations

Matrix operations include addition, multiplication, inversion, and determinant calculation. Each plays an important role in numerical algorithms.

### Matrix addition

When adding two matrices $A$ and $B$ of the same dimension, you add each element in $A$ to the corresponding element in $B$. This is expressed by:

$$
C = A + B \quad \Longrightarrow \quad c_{ij} = a_{ij} + b_{ij}
$$

### Scalar multiplication

In scalar multiplication, you multiply every element of a matrix by the same scalar:

$$
C = kA \quad \Longrightarrow \quad c_{ij} = k \cdot a_{ij}
$$

### Matrix multiplication

Multiplying two matrices of appropriate dimensions involves taking the dot product of each row of the first matrix with each column of the second. If $A$ is an $(m \times n)$ matrix and $B$ is an $(n \times p)$ matrix, then their product $C = AB$ is an $(m \times p)$ matrix where:

$$
c_{ij} = \sum_{k=1}^{n} a_{ik} \, b_{kj}
$$

A sketch for a 3×2 times 2×3 multiplication might look like this:

$$
\underbrace{\begin{bmatrix}a_{11}&a_{12}\\a_{21}&a_{22}\\a_{31}&a_{32}\end{bmatrix}}_{A:\,3\times2}
\underbrace{\begin{bmatrix}b_{11}&b_{12}&b_{13}\\b_{21}&b_{22}&b_{23}\end{bmatrix}}_{B:\,2\times3}
=\underbrace{\begin{bmatrix}c_{11}&c_{12}&c_{13}\\c_{21}&c_{22}&c_{23}\\c_{31}&c_{32}&c_{33}\end{bmatrix}}_{C:\,3\times3}.
$$

For example, $c_{23}=a_{21}b_{13}+a_{22}b_{23}$. The shared inner dimension determines the summation, and the outer dimensions determine the shape of the result. Matrix multiplication generally does not commute: $AB$ and $BA$ can have different sizes, or different values when both are defined.

### Matrix inversion

An invertible matrix $A$ of dimension $n \times n$ has an inverse $A^{-1}$ such that:

$$
A \, A^{-1} = A^{-1} \, A = I_n
$$

where $I_n$ is the $n \times n$ identity matrix. Not all matrices possess an inverse. Those that do not can be called singular or degenerate.

### Determinant

The determinant of a square matrix $A$ is a scalar value that provides information about certain properties of $A$, such as whether $A$ is invertible. For a 3×3 matrix:

$$
\det(A) = a_{11}(a_{22}a_{33} - a_{23}a_{32}) - a_{12}(a_{21}a_{33} - a_{23}a_{31}) +
a_{13}(a_{21}a_{32} - a_{22}a_{31})
$$

A non-zero determinant indicates that $A$ is invertible, while a zero determinant means that $A$ is singular.

## Matrix decompositions

Matrix decompositions break a matrix into products of simpler or special-purpose matrices. They help solve complicated problems systematically.

### LU decomposition

LU decomposition (or factorization) writes a square matrix $A$ as the product of a lower triangular matrix $L$ and an upper triangular matrix $U$. Symbolically:

$$
A = L \, U
$$

Matrix $L$ has all 1s on the main diagonal and zero entries above the diagonal, while $U$ has zeros below the diagonal. A complete $3\times3$ factorization has the following shape:

$$
A=\begin{bmatrix}a&b&c\\d&e&f\\g&h&i\end{bmatrix}
=\begin{bmatrix}1&0&0\\l_{21}&1&0\\l_{31}&l_{32}&1\end{bmatrix}
\begin{bmatrix}u_{11}&u_{12}&u_{13}\\0&u_{22}&u_{23}\\0&0&u_{33}\end{bmatrix}.
$$

This unpivoted form assumes suitable nonzero pivots. With row pivoting, use $PA=LU$, where $P$ records the row swaps; the right-hand side of a solve must be permuted in the same way.

This method is a cornerstone for solving systems of linear equations of the form $Ax = b$, because once $A$ is decomposed into $L$ and $U$, forward and backward substitutions become more efficient.

### Singular value decomposition (SVD)

SVD factorizes any $m \times n$ matrix $A$ (whether square or rectangular) into three matrices:

$$
A = U \, \Sigma \, V^T
$$

Matrix $U$ is an orthogonal (or unitary in the complex case) $m \times m$ matrix, $\Sigma$ is an $m \times n$ diagonal matrix (with nonnegative real numbers on the diagonal), and $V$ is an $n \times n$ orthogonal (or unitary) matrix. The superscript $T$ indicates the transpose. SVD highlights the underlying structure of $A$, making it valuable in data compression, noise reduction, and feature extraction.

### QR decomposition

QR decomposition takes a matrix $A$ of size $m \times n$ (often $m \geq n$) and expresses it as:

$$
A = Q \, R
$$

Matrix $Q$ is $m \times m$ and orthogonal, which means $Q^T Q = I$. Matrix $R$ is $m \times n$ and upper triangular. This decomposition appears in algorithms for solving least squares problems and eigenvalue calculations. Its ability to transform a matrix into an upper-triangular form via orthogonal operations simplifies numerical analyses, since orthogonal transformations are known for preserving numerical stability.

## The power method

The power method is an iterative approach for finding the eigenvalue of largest magnitude (the dominant eigenvalue) and the associated eigenvector of a square matrix $A$. You start with an initial vector $x^{(0)}$ and repeatedly apply the matrix to this vector, normalizing each time:

$$
x^{(k+1)} = \frac{A \, x^{(k)}}{\|A \, x^{(k)}\|}
$$

Under suitable conditions, $x^{(k)}$ converges to the eigenvector corresponding to the dominant eigenvalue of $A$. Numerically, the eigenvalue can be approximated by the Rayleigh quotient:

$$
\lambda_{\text{approx}} = \frac{(x^{(k)})^T \, A \, x^{(k)}}{(x^{(k)})^T \, x^{(k)}}
$$

## Choosing a decomposition

| Goal or structure | Useful factorization | Key reason |
| --- | --- | --- |
| General square linear solve | Pivoted LU, $PA=LU$ | Reuse triangular solves for new right-hand sides |
| Symmetric positive definite solve | Cholesky, $A=LL^\top$ | Exploits symmetry and positive definiteness |
| Full-column-rank least squares | QR, $A=QR$ | Avoids explicitly forming $A^\top A$ |
| Rank estimation or a minimum-norm solution | SVD, $A=U\Sigma V^\top$ | Exposes singular values and null spaces |
| Symmetric eigenvalue problem | Orthogonal eigendecomposition | Separates orthogonal modes and real eigenvalues |

The displayed transpose formulas assume real matrices. In complex arithmetic, use conjugate transposes and unitary matrices. A full QR factorization has the dimensions given above; for $m\geq n$, an economy QR uses $Q\in\mathbb R^{m\times n}$ and $R\in\mathbb R^{n\times n}$ instead.

Matrix dimensions establish whether an operation is defined; conditioning establishes whether its result is sensitive to input errors. For example, a nonzero determinant proves invertibility in exact arithmetic but does not measure numerical reliability. For an invertible matrix, $\kappa_2(A)=\sigma_{\max}/\sigma_{\min}$ measures this sensitivity. Factorizations help compute a stable answer to the supplied problem, but cannot recover accuracy already lost through uncertain data.

## Applications

- Matrices are employed in 3D graphics to execute transformations like translation, scaling, and rotation.
- In physics, matrices find utility in various fields such as quantum mechanics, optics, and electrical circuitry.
- In machine learning, matrices find usage in various algorithms, including linear regression, Principal Component Analysis (PCA), and more.

## Limitations

- Not all matrices are invertible. Those that lack an inverse are termed as singular or degenerate matrices. This poses challenges in numerous matrix methods where the inverse of a matrix is required.
- Many matrix decomposition methods like LU decomposition, Cholesky decomposition, or QR decomposition, require the matrix to fulfill certain conditions. For instance, LU decomposition without pivoting requires every leading principal submatrix to be non-singular (with row pivoting, $PA = LU$ exists for every square matrix), and Cholesky decomposition requires a symmetric positive definite matrix. Such requirements limit the applicability of these methods.
- Matrix methods may not always be the most computationally efficient way to solve a given problem, especially for very large matrices. For such cases, iterative methods or approximation methods might be more suitable.
- Some matrix problems are sensitive because of ill-conditioning, and some algorithms are susceptible to rounding errors. This means small changes in the input can result in large changes in the output, which can lead to significant errors.
- Most matrix methods assume that the matrix elements are real or complex numbers. However, in some applications (like in computer graphics), the matrix elements can be more complicated objects, which makes these methods less applicable.
