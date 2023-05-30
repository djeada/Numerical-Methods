## Gaussian Interpolation

Gaussian interpolation is a numerical method used to approximate values between two points in a dataset. 

## Key Concepts

- Gaussian interpolation utilizes the Gauss-Legendre Quadrature which integrates a function using the Legendre polynomials, yielding an exact result for polynomials of degree 2n-1 or less.
- The weights and abscissas used for the Gaussian Quadrature are derived from the roots of the Legendre polynomials.

## Mathematical Formulation

The formula for Gauss-Legendre Quadrature is:

$$∫_a^b f(x) dx ≈ ∑_{i=1}^n w_i*f(x_i)$$

Where w_i are the weights, x_i are the abscissas (roots of the Legendre polynomials) and f(x) is the function being integrated.
Algorithm Steps

    Select a number of points n for the approximation.
    Determine the abscissas x_i and weights w_i for the selected number of points. These are typically pre-computed and can be found in tables or calculated using a method such as the Bonnet recursion formula.
    Calculate the function values f(x_i).
    Compute the weighted sum of the function values.

Example

Suppose you want to approximate the integral of the function f(x) = x^2 over the interval [0,1] using Gaussian Quadrature with n=2.
Advantages

    Gaussian Quadrature gives exact results for polynomials of degree 2n-1 or less, where n is the number of points used.
    It generally has a higher accuracy per degree than methods like the Trapezoidal Rule or Simpson's Rule.

Limitations

    The Gauss-Legendre Quadrature method can only be used to integrate functions over the interval [-1,1]. For functions defined on other intervals, a change of variables must be used.
    The method requires knowledge of the function in question in order to determine the function values at the abscissas.
