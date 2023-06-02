## Gauss-Seidel Method

The Gauss-Seidel method is an iterative technique utilized for solving a system of 'n' linear equations with unknown variables, represented as a square system.

## Key Concepts

- The Gauss-Seidel method represents an enhancement over the Jacobi method because it immediately applies updated values as they become available.
- It offers a faster convergence rate compared to the Jacobi method.

## Mathematical Formulation

Given a system of linear equations in the form $Ax = b$, where 'A' is the coefficient matrix and 'b' is the constant vector, the Gauss-Seidel method aims to find the solution vector 'x'.

The system of equations can be rewritten as:

$$x = Lx + b,$$

where 'L' denotes the lower triangular part of matrix 'A'.

## Algorithm Steps

1. Begin with an initial approximation for the solution, typically a zero vector.
2. For each row 'i', calculate $x_i$ in the following manner:

    $$x_i^{(k+1)} = \frac{{b_i - \sum_{j \neq i} A_{ij}x_j^{(k)}}}{A_{ii}}$$

3. Continue iterating until the difference between the old and the updated solution is less than a predetermined tolerance level.

## Example

Consider the system of linear equations: 

$$
\begin{aligned}
5x - y &= 6,\\
7x + 8y &= 20.
\end{aligned}
$$

This can be written in matrix form as $Ax = b$, where:

$$
A = 
\begin{bmatrix}
5 & -1 \\
7 & 8 
\end{bmatrix}
, \quad
x = 
\begin{bmatrix}
x \\
y
\end{bmatrix}
, \quad
b = 
\begin{bmatrix}
6 \\
20
\end{bmatrix}
.
$$

1. Start with an initial approximation, say $x^{(0)} = 0$, $y^{(0)} = 0$.
2. Apply the Gauss-Seidel formula for each equation. For the first equation, we update $x$ using $x^{(1)} = \frac{6+y^{(0)}}{5} = 1.2$. Then, for the second equation, we update $y$ using the newly computed $x^{(1)}$: $y^{(1)} = \frac{20 - 7x^{(1)}}{8} = 1.45$.
3. Repeat step 2 until the values of 'x' and 'y' stabilize within an acceptable range. After a few iterations, the solution converges to $x \approx 1.04$ and $y \approx 1.60$.

## Advantages

- The Gauss-Seidel method offers faster convergence compared to the Jacobi method.
- It's beneficial when 'A' is a sparse matrix or when memory resources are limited.

## Limitations

- The method converges only if the coefficient matrix 'A' is either diagonally dominant, or symmetric and positive definite.
- For certain types of matrices, convergence can be relatively slow.
