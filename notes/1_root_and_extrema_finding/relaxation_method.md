## Relaxation Method

- The relaxation method, or successive over-relaxation method, is an iterative method used for solving linear system of equations.
- It can converge faster than the basic iterative methods such as Jacobi's or Gauss-Seidel methods.

## Mathematical Formulation

Given a system of linear equations of the form $Ax = b$, where $A$ is the matrix of coefficients, $x$ is the vector of variables, and $b$ is the constant vector, the system can be rewritten in the form $x = Tx + c$, where $T$ and $c$ depend on $A$ and $b$. The relaxation method modifies the basic iterative method by introducing a relaxation parameter $\omega$:

$$x_{n+1} = (1-\omega)x_n + \omega(Tx_n + c)$$

## Algorithm Steps

1. **Initialization**: Start with an initial guess $x_0$.

2. **Update**: Compute the next point $x_{n+1}$ using the relaxation method update rule: $x_{n+1} = (1-\omega)x_n + \omega(Tx_n + c)$.

3. **Convergence Check**: Repeat step 2 until the difference between $x_{n+1}$ and $x_n$ is less than a pre-defined tolerance or maximum iterations have been reached.

## Example

Suppose we have a system of equations as follows:

$$3x - y = 1$$
$$x + 2y = 4$$

We can write this system in matrix form as:

$$\begin{bmatrix} 3 & -1 \\ 1 & 2 \end{bmatrix} \begin{bmatrix} x \\ y \end{bmatrix} = \begin{bmatrix} 1 \\ 4 \end{bmatrix}$$

The iterative form of the system is then:

$$\begin{bmatrix} x \\ y \end{bmatrix} = \begin{bmatrix} 1 + \frac{1}{3}y \\ 2 - \frac{1}{2}x \end{bmatrix}$$

We start with an initial guess of $x_0 = (0, 0)$. We then use the relaxation method with $\omega = 1.25$ to find the solution. 

## Advantages

- The relaxation method can converge faster than the basic iterative methods for a suitable choice of the relaxation parameter.

## Limitations

- The method can diverge if the relaxation parameter is not chosen properly.
- It can only be used for linear systems of equations.
- It requires the system of equations to have a unique solution, and that the matrix of coefficients is diagonally dominant or symmetric and positive-definite.
