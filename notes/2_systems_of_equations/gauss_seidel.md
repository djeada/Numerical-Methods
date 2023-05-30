## Gauss-Seidel Method

The Gauss-Seidel method is an iterative technique for solving a square system of n linear equations with unknown x.

## Key Concepts

- The method is an improvement over the Jacobi method, as it uses updated values as soon as they are available.
- It converges faster than the Jacobi method.

## Mathematical Formulation

For a given system of linear equations Ax = b, where A is the coefficient matrix and b is the constant vector, the Gauss-Seidel method seeks to solve for the vector x.

The system can be written as: 

x = Lx + b,

where L is the lower triangular part of A.

## Algorithm Steps

1. Choose an initial approximation to the solution.
2. For each row i, update x_i as follows:

x_i^(k+1) = (b_i - Σ(j ≠ i)A_ij*x_j^(k)) / A_ii

3. Repeat step 2 until convergence is achieved.

## Example

Consider the system of equations 5x - y = 6, 7x + 8y = 20.

1. Choose an initial approximation, say x^(0) = 0, y^(0) = 0.
2. Update x and y as per the formula.
3. Repeat step 2 until the values of x and y do not change significantly.

## Advantages

- Faster convergence than the Jacobi method.
- Can be used when A is a sparse matrix or when memory is limited.

## Limitations

- Only converges when the coefficient matrix A is either diagonally dominant, or symmetric and positive definite.
- Convergence can be slow for certain types of matrices.
