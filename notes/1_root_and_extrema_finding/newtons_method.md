## Newton's Method in Numerical Methods

- Newton's method, also known as Newton-Raphson method, is used for finding successively better approximations to the roots of a real-valued function.
- It's an open method that requires only a single initial approximation to the root.
- It's a very efficient method when it converges, but there's no guarantee of convergence.

## Mathematical Formulation

The formula for Newton's method is $x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}$, where $f'(x_n)$ is the derivative of the function $f$ at the point $x_n$.

## Algorithm Steps

1. Start with an initial approximation $x_0$ to the root.
2. Calculate $x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}$.
3. Repeat step 2 for a given number of iterations $n$ or until a satisfactory approximation for the root is obtained.

## Example

Consider a function $f(x) = x^2 - 4$.

We start with an initial approximation $x_0 = 3$.

1. Compute $x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)} = 3 - \frac{(3^2 - 4)}{2*3} = 2.333$.
2. Compute $x_{n+1} = 2.333 - \frac{(2.333^2 - 4)}{2*2.333} = 2.059$.
3. Continue this process until a satisfactory approximation of the root is obtained or the maximum number of iterations is reached.

In this case, we would find that $x = 2$ is a root of the function $f(x) = x^2 - 4$.

## Advantages

- Newton's method is very fast when it converges.
- It has quadratic convergence, meaning it roughly doubles the number of correct digits at each step.
- It only requires a single starting point.

## Limitations

- It requires the evaluation of the derivative $f'(x)$.
- There's no guarantee of convergence. It may not converge if the initial approximation is too far from the root.
- It may fail or converge to the wrong root if the function or its derivative has discontinuities.
- It can be trapped by local minima or maxima because it uses the derivative to guide its search.
