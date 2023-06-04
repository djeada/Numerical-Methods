## Relaxation Method
- The relaxation method, also known as the fixed-point iteration method, is an iterative technique applied to discover the roots of nonlinear equations.
- It has the potential to converge faster than certain other methods such as the bisection method; however, convergence isn't always guaranteed.

## Mathematical Formulation

For a given function $f(x)$ with a root at $\alpha$, the function can be expressed in a different form $x = g(x)$, where $g(x)$ is a continuous and differentiable function satisfying $g(\alpha) = \alpha$. The fixed-point iteration method then iteratively applies the following rule:

$$x_{n+1} = g(x_n)$$

## Algorithm Steps

1. **Initialization**: Begin with an initial estimate $x_0$.

2. **Iteration**: Compute the next approximation $x_{n+1}$ by applying the fixed-point iteration formula: $x_{n+1} = g(x_n)$.

3. **Convergence Check**: Repeat step 2 until the absolute difference between successive approximations $x_{n+1}$ and $x_n$ falls below a predetermined tolerance or until the maximum number of iterations is reached.

## Example

Consider the equation $x^2 - 3x + 2 = 0$, the root of which we aim to find. This equation can be reformulated in the form $x = g(x) = \frac{x^2 + 2}{3}$.

Starting with an initial guess of $x_0 = 0$, we can apply the relaxation method to determine the solution.

## Advantages

- The relaxation method can converge more quickly than certain other methods such as the bisection method, especially with a suitable initial guess.
- It can handle nonlinear equations, which broadens its range of applicability.

## Limitations

- The relaxation method does not always guarantee convergence for every function or initial guess.
- It relies heavily on an accurate initial guess for efficient and assured convergence.
- The method also assumes the function under consideration to be continuous and differentiable.
