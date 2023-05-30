## Secant Method in Numerical Methods

- The Secant Method is an iterative method used to find the roots of a function.
- It does not require the function to be differentiable, and it often converges more quickly than other methods like the bisection method.

## Mathematical Formulation

The secant method is based on the approximation of the derivative of the function by the finite difference of the function values at two points. Given two initial points $x_0$ and $x_1$, the method uses the iterative formula:

$$x_{n+1} = x_n - f(x_n)\frac{x_n - x_{n-1}}{f(x_n) - f(x_{n-1})}$$

## Algorithm Steps

1. **Initialization**: Choose two initial approximations $x_0$ and $x_1$.

2. **Update**: Compute the next point $x_{n+1}$ using the secant method formula.

3. **Convergence Check**: Repeat step 2 until the absolute difference between $x_{n+1}$ and $x_n$ is less than a pre-defined tolerance, or until a maximum number of iterations is reached.

## Example

Let's consider the function $f(x) = x^2 - 4$, and we want to find its root. We start with initial guesses $x_0 = 0$ and $x_1 = 1$.

1. **Initialization**: Start with $x_0 = 0$ and $x_1 = 1$.

2. **Update**: Calculate $x_2$ using the secant method formula. We get $x_2 = 1 - (1^2 - 4) * \frac{1 - 0}{1^2 - 4 - 0} = 2$.

3. **Repeat**: Using $x_1$ and $x_2$ as the new points, repeat step 2. The update gives us $x_3 = 2 - (2^2 - 4) * \frac{2 - 1}{2^2 - 4 - 1} = 2$.

4. **Convergence**: Since $x_3 = x_2$, we have found a root of the function: $x = 2$.

## Advantages

- The secant method often converges more quickly than the bisection method and the false position method.
- It does not require the function to be differentiable.

## Limitations

- It's not guaranteed to converge.
- It can converge to a root different from the expected one if the function has multiple roots.
- It requires two initial points, and the choice of these points can significantly influence the convergence of the method.
