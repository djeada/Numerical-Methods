## Linear Systems of Equations

Linear systems of equations can be represented in a matrix form, which enables the use of a variety of numerical methods for solving them. 

## Mathematical Formulation

A linear system can be written as a set of equations:

$$
\begin{eqnarray*}
  A_{11}x_1 + A_{12}x_2 + \ldots + A_{1n}x_n &=& b_1 \\
  A_{21}x_1 + A_{22}x_2 + \ldots + A_{2n}x_n &=& b_2 \\
  \vdots \\
  A_{n1}x_1 + A_{n2}x_2 + \ldots + A_{nn}x_n &=& b_n
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

## Criteria for a Unique Solution

A system of equations has a unique solution if and only if:

- The determinant of A is not zero, i.e., det(A) ≠ 0, implying A is non-singular.
- The matrix A is invertible.
- The columns of A are linearly independent.
- The rows of A are linearly independent.

## Example

Consider the system of equations: 

$$
\begin{eqnarray*}
  3x + 2y - z &=& 1 \\
  2x - 2y + 4z &=& -2 \\
  -x + 0.5y - z &=& 0
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

## Advantages

- Matrix methods for solving systems of equations are systematic and can be easily implemented in computer programs.
- Matrix representation is compact and insightful, especially when dealing with systems of many variables.

## Limitations

- If the matrix is singular or nearly singular (i.e., det(A) is zero or close to zero), the system may have no solution or infinitely many solutions.
- Large systems of equations may be computationally expensive to solve using matrix methods.
