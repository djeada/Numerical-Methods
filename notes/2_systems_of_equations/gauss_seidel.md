## Gauss-Seidel Method

The Gauss-Seidel method is an iterative technique utilized for solving a system of 'n' linear equations with unknown variables, represented as a square system.

## Key Concepts

- The Gauss-Seidel method represents an enhancement over the Jacobi method because it immediately applies updated values as they become available.
- It offers a faster convergence rate compared to the Jacobi method.

## Mathematical Formulation

Given a system of linear equations in the form Ax = b, where 'A' is the coefficient matrix and 'b' is the constant vector, the Gauss-Seidel method aims to find the solution vector 'x'.

The system of equations can be rewritten as:

$$x = Lx + b$$

where 'L' denotes the lower triangular part of matrix 'A'.

## Algorithm Steps

1. Begin by choosing an initial approximation for the solution.
2. For each row 'i', update x_i in the following manner:

$$ x_i^(k+1) = (b_i - Σ(j ≠ i)A_ij*x_j^(k)) / A_ii$$

3. Repeat step 2 until the solution converges to a certain acceptable level of accuracy.

## Example

Consider a system of equations given by: 5x - y = 6, and 7x + 8y = 20.

1. Select an initial approximation, for instance, x^(0) = 0, y^(0) = 0.
2. Apply the Gauss-Seidel formula to update the values of 'x' and 'y'.
3. Repeat step 2 until the values of 'x' and 'y' stabilize within an acceptable range.

## Advantages

- The Gauss-Seidel method offers faster convergence compared to the Jacobi method.
- It's beneficial when 'A' is a sparse matrix or when memory resources are limited.

## Limitations

- The method converges only if the coefficient matrix 'A' is either diagonally dominant, or symmetric and positive definite.
- For certain types of matrices, convergence can be relatively slow.
