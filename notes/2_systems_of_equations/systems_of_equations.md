## Linear Systems of Equations

A *linear system of equations* is a collection of one or more linear equations involving the same set of variables. Such systems arise in diverse areas such as engineering, economics, physics, and computer science. The overarching goal is to find values of the variables that simultaneously satisfy all equations.

When working with linear systems, representing the equations in *matrix form* proves to be highly efficient. This matrix-based representation underpins a variety of numerical methods—such as Gaussian elimination, LU decomposition, and iterative techniques—used for both small and large-scale problems.

### Mathematical Formulation

A general linear system with $n$ variables $x_1, x_2, \ldots, x_n$ can be expressed as:

$$
\begin{cases}
A_{11}x_1 + A_{12}x_2 + \cdots + A_{1n}x_n = b_1, \\
A_{21}x_1 + A_{22}x_2 + \cdots + A_{2n}x_n = b_2, \\
\quad\;\;\;\vdots \\
A_{n1}x_1 + A_{n2}x_2 + \cdots + A_{nn}x_n = b_n.
\end{cases}
$$

We can rewrite this collection of equations succinctly as:

$$
\mathbf{A} \mathbf{x} = \mathbf{b},
$$

where

$$
\mathbf{A} = \begin{bmatrix}
A_{11} & A_{12} & \ldots & A_{1n} \\
A_{21} & A_{22} & \ldots & A_{2n} \\
\vdots & \vdots & \ddots & \vdots \\
A_{n1} & A_{n2} & \ldots & A_{nn}
\end{bmatrix},
\quad
\mathbf{x} = \begin{bmatrix}
x_1 \\
x_2 \\
\vdots \\
x_n
\end{bmatrix},
\quad
\mathbf{b} = \begin{bmatrix}
b_1 \\
b_2 \\
\vdots \\
b_n
\end{bmatrix}.
$$

In this form:

- $\mathbf{A}$ (an $n \times n$ matrix) contains the coefficients of the variables.
- $\mathbf{x}$ (an $n \times 1$ column vector) represents the unknowns of the system.
- $\mathbf{b}$ (an $n \times 1$ column vector) contains the constant terms from the right-hand side of each equation.

Expressing the system in matrix form allows us to apply well-studied algebraic procedures and computational routines to solve for $\mathbf{x}$.

### Criteria for a Unique Solution

A system $\mathbf{A}\mathbf{x} = \mathbf{b}$ of $n$ linear equations in $n$ unknowns has a *unique* solution if and only if any one (and thus all) of the following equivalent conditions holds:

I. **Non-zero determinant**: 

$$\det(\mathbf{A}) \neq 0$$  

A non-zero determinant indicates that the matrix $\mathbf{A}$ is *invertible*.

II. **Invertibility of $\mathbf{A}$**: 

There exists an inverse matrix $\mathbf{A}^{-1}$ such that  

$$
\mathbf{x} = \mathbf{A}^{-1}\mathbf{b}.
$$

III. **Linear independence of columns**: 

The columns of $\mathbf{A}$ are linearly independent vectors in $\mathbb{R}^n$. In practical terms, no column can be written as a linear combination of the other columns.

IV. **Linear independence of rows**: 

Similarly, the rows of $\mathbf{A}$ are also linearly independent. No row can be expressed as a linear combination of the other rows.

If any of these criteria fail (e.g., $\det(\mathbf{A}) = 0$), the system does not have a unique solution: it may either have *no solution* (inconsistent system) or *infinitely many solutions* (underdetermined system).

### Example

Consider the following system of three linear equations in three unknowns $x, y, z$:

$$
\begin{cases}
3x + 2y - z = 1, \\
2x - 2y + 4z = -2, \\
-x + 0.5y - z = 0.
\end{cases}
$$

We can represent it in matrix form $\mathbf{A}\mathbf{x} = \mathbf{b}$ as:

$$
\mathbf{A} = \begin{bmatrix}
3 & 2 & -1 \\
2 & -2 & 4 \\
-1 & 0.5 & -1
\end{bmatrix},
\quad
\mathbf{x} = \begin{bmatrix}
x \\
y \\
z
\end{bmatrix},
\quad
\mathbf{b} = \begin{bmatrix}
1 \\
-2 \\
0
\end{bmatrix}.
$$

To solve this system, one may use:

- Transform $\mathbf{A}$ into an upper-triangular (or row-echelon) form via elementary row operations, then perform back-substitution to determine $x, y, z$.
- Factor $\mathbf{A}$ into a product of a lower-triangular matrix $\mathbf{L}$ and an upper-triangular matrix $\mathbf{U}$. Then solve two simpler triangular systems.
- Compute $\mathbf{A}^{-1}$ and multiply both sides of $\mathbf{A}\mathbf{x} = \mathbf{b}$ by $\mathbf{A}^{-1}$.

Each approach exploits the structure of linear systems to systematically isolate the solution for $\mathbf{x}$.
### Advantages

- Matrix methods, such as Gaussian elimination, provide a *systematic framework* for solving linear systems, making both theoretical understanding and practical implementation more straightforward.
- Representing a system of equations as $\mathbf{A}\mathbf{x} = \mathbf{b}$ creates a *compact representation* that reduces complexity, especially for systems involving many equations and variables.
- Computational efficiency benefits from *scalability*, as many matrix-based algorithms have predictable complexities, and optimized libraries like BLAS and LAPACK are designed to utilize modern hardware capabilities.
- Properties of the system can be analyzed using *matrix insights*, such as the determinant to assess solution existence or uniqueness, or matrix decompositions (e.g., LU, QR, SVD) to reveal structure and enhance solving methods.

### Limitations

- When the matrix $\mathbf{A}$ is *singular* or nearly singular, solutions may not exist, may be infinite, or may be numerically unstable due to amplified computational errors.
- Solving large systems can be computationally expensive since direct methods like Gaussian elimination scale with $O(n^3)$, and dense matrices increase memory requirements significantly.
- Numerical instability can arise from *ill-conditioned* matrices where small changes in $\mathbf{A}$ or $\mathbf{b}$ lead to large deviations in the solution, requiring techniques like pivoting or iterative refinement to mitigate errors.
- Sparse systems can be inefficiently handled if treated as dense, leading to unnecessary computational and memory overhead unless *specialized sparse techniques* are employed.
