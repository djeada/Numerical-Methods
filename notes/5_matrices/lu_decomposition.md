
## LU Decomposition

LU Decomposition, also known as LU factorization, refers to the factorization of a square matrix into two matrices – a lower triangular matrix (L) and an upper triangular matrix (U). 

## Key Concepts

- The main idea of LU decomposition is to represent a matrix as the product of a lower triangular matrix and an upper triangular matrix.
- In the decomposition, `A = LU`, where A is the square matrix to be factorized, L is the lower triangular matrix, and U is the upper triangular matrix.

## Mathematical Formulation

The goal is to *decompose* a matrix so that it is computationally cheaper to calculate the solution of the following equation:

$$A\boldsymbol{x}^{n+1} = \boldsymbol{b}(\boldsymbol{x}^n, \ldots)$$

The matrix $A$ get's decomposed into to other matrices $L$ and $U$:

$$ A = LU $$

$L$ is a lower-triangular matrix and $U$ is an upper-triangular matrix. 
These matrices conatin all the infomration needed for the Gaussian elimination.

$$ A\boldsymbol{x} = \boldsymbol{b} \iff (LU)\boldsymbol{x} = \boldsymbol{b} \iff  L(U\boldsymbol{x}) = \boldsymbol{b} $$

We introduce a new notation for the $U$ and $x$ product:

$$\boldsymbol{c}=U\boldsymbol{x}$$

We can then rewrite the previous equation in the following way:

$$ L\boldsymbol{c} = \boldsymbol{b} $$

Since $L$ is in lower-triangular form we can quickly solve the above eqaution.

The last step is this equation:

$$ U\boldsymbol{x} = \boldsymbol{c} $$

## Algorithm Steps

1. Given a square matrix A, the objective is to find an upper triangular matrix U and a lower triangular matrix L such that their product equals A.
2. Iterate over each row in A.
3. For each row `i`, calculate each `u[i,j]` for `j>i` and each `l[i,j]` for `j<i`.
4. Use the equations `l[i,j] = a[i,j] - Σ(l[i,k]*u[k,j])` for `k=1` to `j-1` and `u[i,j] = (a[i,j] - Σ(l[i,k]*u[k,j]))/l[j,j]` for `k=1` to `i-1`.
5. After you get L and U, you can use forward and backward substitution to solve a system of equations `Ax = b`.

## Example

Let's consider the system of linear equations:

2x + 3y - 4z = 1
3x - 3y + 2z = -2
-2x + 6y - z = 3

markdown


This can be represented as a matrix equation `Ax = b`, where `A` is the matrix of coefficients, `x` is the vector of variables, and `b` is the right-hand side. LU Decomposition can be applied on `A` to solve for `x`.

## Advantages

- LU Decomposition is efficient and numerically stable, especially for solving systems of linear equations.
- Can be used for finding the determinant and inverse of a matrix more easily.

## Limitations

- Only applicable for square matrices.
- Not all matrices can be LU decomposed. A is LU decomposable if and only if all its leading principal minors are non-zero.

