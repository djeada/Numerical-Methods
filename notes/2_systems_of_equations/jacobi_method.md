## Jacobi Method

The Jacobi method is an iterative technique for finding the solutions to a diagonally dominant system of linear equations.

## Key Concepts

- The algorithm iteratively solves each diagonal element and replaces it with an approximate value.
- This procedure is repeated until convergence, i.e., until the change in values becomes negligibly small.

## Mathematical Formulation

Consider a system of equations represented as $Ax = b$, where $A$ is the coefficient matrix, and $b$ is the constant vector. The Jacobi method uses an iterative process to solve for the unknown vector $x$.

The system can be decomposed as follows:

$$
Ax = Dx - (L + U)x = b
$$

where $D$ represents the diagonal matrix of $A$, $L$ is the strict lower triangular matrix of $A$, and $U$ is the strict upper triangular matrix of $A$.

## Algorithm Steps

1. Start with an initial approximation to the solution vector.
2. For each row $i$, compute the updated $x_i$ value with this formula:

$$
x_i^{(new)} = \frac{(b_i - \sum_{j ≠ i}A_{ij}x_j^{(old)})}{A_{ii}}
$$

3. Iterate step 2 until the values of $x$ converge, i.e., changes in values are below a defined tolerance level.

## Example

Let's consider the system of linear equations: 

$$
\begin{align*}
2x - y &= 5 \\
x + 3y &= 7
\end{align*}
$$

Step 1: Let's choose an initial approximation, for example $x^{(0)} = 0$ and $y^{(0)} = 0$.

Step 2: Compute the new values using the Jacobi method. For this system, the update equations are:

$$
x^{(new)} = \frac{1}{2}(5 + y^{(old)})
$$

and

$$
y^{(new)} = \frac{1}{3}(7 - x^{(old)})
$$

Substitute $x^{(0)}$ and $y^{(0)}$ into the equations, we get $x^{(1)} = 2.5$ and $y^{(1)} = 2.33$.

Step 3: Repeat step 2 using $x^{(1)}$ and $y^{(1)}$ until the difference between the new and old values is below a defined tolerance level.

## Advantages

- The Jacobi method is straightforward to understand and implement.
- It can be applied to any matrix that has non-zero elements on the diagonals.

## Limitations

- The Jacobi method requires the coefficient matrix $A$ to be diagonally dominant; otherwise, the method may fail to converge.
- The rate of convergence can be slow, depending on the nature of the system of equations.
