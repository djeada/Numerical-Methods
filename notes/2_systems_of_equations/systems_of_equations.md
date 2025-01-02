## Linear Systems of Equations

Linear systems of equations can be represented in a matrix form, which enables the use of a variety of numerical methods for solving them. 

### Mathematical Formulation

A linear system can be written as a set of equations:

$$
\begin{eqnarray*}
  A_{11}x_1 + A_{12}x_2 + \ldots + A_{1n}x_n = b_1 \\
  A_{21}x_1 + A_{22}x_2 + \ldots + A_{2n}x_n = b_2 \\
  \vdots \\
  A_{n1}x_1 + A_{n2}x_2 + \ldots + A_{nn}x_n = b_n
\end{eqnarray*} 
$$

This system of equations can be rewritten in a compact matrix form as Ax = b, where:

$$
A = \begin{bmatrix}
  A_{11} & A_{12} & \ldots & A_{1n} \\
  A_{21} & A_{22} & \ldots & A_{2n} \\
  \vdots & \vdots & \ddots & \vdots \\
  A_{n1} & A_{n2} & \ldots & A_{nn}
\end{bmatrix},
\quad
x = \begin{bmatrix}
  x_1 \\
  x_2 \\
  \vdots \\
  x_n
\end{bmatrix},
\quad
b = \begin{bmatrix}
  b_1 \\
  b_2 \\
  \vdots \\
  b_n
\end{bmatrix}
$$

### Criteria for a Unique Solution

A system of equations has a unique solution if and only if:

- The determinant of A is not zero, i.e., det(A) ≠ 0, implying A is non-singular.
- The matrix A is invertible.
- The columns of A are linearly independent.
- The rows of A are linearly independent.

### Example

Consider the system of equations: 

$$
\begin{eqnarray*}
  3x + 2y - z = 1 \\
  2x - 2y + 4z = -2 \\
  -x + 0.5y - z = 0
\end{eqnarray*}
$$

This can be represented as a matrix equation: Ax = b, where A, x, and b are defined as follows:

$$
A = \begin{bmatrix}
  3 & 2 & -1 \\
  2 & -2 & 4 \\
  -1 & 0.5 & -1
\end{bmatrix},
\quad
x = \begin{bmatrix}
  x \\
  y \\
  z
\end{bmatrix},
\quad
b = \begin{bmatrix}
  1 \\
  -2 \\
  0
\end{bmatrix}
$$

The system can be solved using various matrix methods such as the Gaussian elimination method, which involves transforming the matrix A into its row echelon form and then performing back substitution to solve for x.

### Advantages

- Matrix methods provide a **systematic approach** to solving systems of equations, which makes them straightforward to automate in computer algorithms.
- The **compact representation** of systems using matrices is especially useful when dealing with many variables and equations.
- These methods allow for **scalability**, as they are adaptable to both small and large systems, leveraging computational tools and libraries.
- Matrix methods offer **insight into system properties**, such as determinant calculations, linear independence, and transformations.

### Limitations

- When the matrix is **singular or nearly singular**, the system may not have a unique solution, potentially leading to no solution or infinitely many solutions.
- Solving **large systems** using direct matrix methods can be computationally expensive, often requiring significant time and memory resources.
- Ill-conditioned matrices can cause **numerical instability**, where small changes in inputs result in large errors in the solution.
- Representing and solving **sparse systems** using dense matrix techniques can be inefficient unless specialized sparse matrix methods are employed.
