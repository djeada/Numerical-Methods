# Linear Systems of Equations

A *linear system of equations* is a collection of one or more linear equations involving the same set of variables. Such systems arise in diverse areas such as engineering, economics, physics, and computer science. The main goal is to find values of the variables that simultaneously satisfy all equations.

When working with linear systems, representing the equations in *matrix form* proves to be highly efficient. This matrix-based representation underpins a variety of numerical methods—such as Gaussian elimination, LU decomposition, and iterative techniques—used for both small and large-scale problems.

## Mathematical formulation

A general linear system with $n$ variables $x_1, x_2, \ldots, x_n$ can be expressed as:

$$
\begin{cases}
  a_{11}x_1 + a_{12}x_2 + \cdots + a_{1n}x_n = b_1, \\
  a_{21}x_1 + a_{22}x_2 + \cdots + a_{2n}x_n = b_2, \\
  \quad\vdots \\
  a_{n1}x_1 + a_{n2}x_2 + \cdots + a_{nn}x_n = b_n.
\end{cases}
$$

We can rewrite this collection of equations succinctly as:

$$
\mathbf{A} \mathbf{x} = \mathbf{b},
$$

where

$$
\mathbf{A} = \begin{bmatrix}
a_{11} & a_{12} & \ldots & a_{1n} \\
a_{21} & a_{22} & \ldots & a_{2n} \\
\vdots & \vdots & \ddots & \vdots \\
a_{n1} & a_{n2} & \ldots & a_{nn}
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

## Criteria for a unique solution

A system $\mathbf{A}\mathbf{x} = \mathbf{b}$ of $n$ linear equations in $n$ unknowns has a *unique* solution if and only if any one (and thus all) of the following equivalent conditions holds:

I. **Non-zero determinant**:

$$
\det(\mathbf{A}) \neq 0
$$

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

## Rank, residuals, and sensitivity

For a general $m\times n$ system, consistency requires $\operatorname{rank}(A)=\operatorname{rank}([A\mid\mathbf{b}])$. A consistent system has a unique solution exactly when this rank is $n$; otherwise it has free variables. If the ranks differ, there is no exact solution, and a [least-squares approximation](../6_regression/least_squares.md) may be appropriate.

For a nonsingular square matrix, define the residual of an approximation $\widehat{\mathbf{x}}$ as $\mathbf{r}=\mathbf{b}-A\widehat{\mathbf{x}}$. Since $A\mathbf{x}=\mathbf{b}$,

$$
\mathbf{x}-\widehat{\mathbf{x}}=A^{-1}\mathbf{r}.
$$

For a compatible induced matrix norm and nonzero $\mathbf{b}$, this implies

$$
\frac{\|\mathbf{x}-\widehat{\mathbf{x}}\|}{\|\mathbf{x}\|}\leq\kappa(A)\frac{\|\mathbf{r}\|}{\|\mathbf{b}\|},\qquad \kappa(A)=\|A\|\|A^{-1}\|.
$$

The **condition number** describes sensitivity of the mathematical problem, whereas **stability** describes how an algorithm propagates rounding. Pivoting improves elimination stability but does not change an ill-conditioned problem into a well-conditioned one. A small residual therefore needs to be interpreted with the condition number and the accuracy of the input data.

For a dense square system, pivoted LU is a standard direct approach. SPD systems admit Cholesky factorization; large sparse systems often benefit from iterative methods and preconditioners. The expression $\mathbf{x}=A^{-1}\mathbf{b}$ is a theoretical identity, while factorization is usually the practical way to compute the solution.

### Why row operations preserve the solution

Swapping equations, multiplying an equation by a nonzero scalar, and adding a multiple of one equation to another are reversible operations. Applying any of them to the whole augmented system therefore keeps exactly the same solutions. This is the common reason Gaussian elimination and the triangular solves following LU are valid. An operation on the coefficient row alone would instead change the problem, which is why the right-hand side must be updated with it.

## Example

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

For this example the solution is $(x,y,z)=(1,-2,-2)$. Substitution gives $3-4+2=1$, $2+4-8=-2$, and $-1-1+2=0$, checking all three equations independently of the chosen solver.

## Advantages

- Matrix methods, such as Gaussian elimination, provide a *systematic framework* for solving linear systems, making both theoretical understanding and practical implementation more straightforward.
- Representing a system of equations as $\mathbf{A}\mathbf{x} = \mathbf{b}$ creates a *compact representation* that reduces complexity, especially for systems involving many equations and variables.
- Computational efficiency benefits from *scalability*, as many matrix-based algorithms have predictable complexities, and optimized libraries like BLAS and LAPACK are designed to utilize modern hardware capabilities.
- Properties of the system can be analyzed using *matrix insights*, such as the determinant to assess solution existence or uniqueness, or matrix decompositions (e.g., LU, QR, SVD) to reveal structure and enhance solving methods.

## Limitations

- When the matrix $\mathbf{A}$ is *singular* or nearly singular, solutions may not exist, may be infinite, or may be numerically unstable due to amplified computational errors.
- Solving large systems can be computationally expensive since direct methods like Gaussian elimination scale with $O(n^3)$, and dense matrices increase memory requirements significantly.
- *Ill-conditioned* matrices amplify small changes in $\mathbf A$ or $\mathbf b$ into larger changes in the solution. Pivoting controls arithmetic error growth, and iterative refinement can improve a computed residual, but neither removes sensitivity to uncertainty already present in the supplied data.
- Sparse systems can be inefficiently handled if treated as dense, leading to unnecessary computational and memory overhead unless *specialized sparse techniques* are employed.
