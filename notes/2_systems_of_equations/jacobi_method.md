## Jacobi Method

The Jacobi method is an iterative algorithm for determining the solutions of a diagonally dominant system of linear equations.

## Key Concepts

- Each diagonal element is solved for, and an approximate value is plugged in.
- The process is then iterated until it converges.

## Mathematical Formulation

For a system of equations Ax = b, where A is the coefficient matrix and b is the constant vector, the Jacobi method forms an iterative process to solve for x.

The system can be expressed as: 

Dx = -(L + U)x + b,

where D is the diagonal matrix of A, L is the strict lower triangular matrix of A, and U is the strict upper triangular matrix of A.

## Algorithm Steps

1. Choose an initial approximation to the solution.
2. For each row i, compute the updated x_i value as follows:

x_i^(new) = (b_i - Σ(j ≠ i)A_ij*x_j^(old)) / A_ii

3. Repeat step 2 until convergence is achieved.

## Example

Consider the system of equations 2x - y = 5, x + 3y = 7.

1. Choose an initial approximation, say x^(0) = 0, y^(0) = 0.
2. Update x and y using the Jacobi method.
3. Repeat step 2 until the values of x and y do not change significantly.

## Advantages

- Simplicity of the algorithm.
- It can be applied to any matrix with non-zero elements on the diagonals.

## Limitations

- It requires the matrix to be diagonally dominant or else the method may not converge.
- The rate of convergence can be slow.
