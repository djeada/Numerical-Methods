We have a set of $N$ data points $(x_i, y_i)$. 

We want to find the coeeficients of a polynomial of degree $N - 1$:
 
$$ P_N(x) := a_0 + a_1 x + a_2 x^2 + a_3 x^3 + \ldots + a_N x^N, $$


## Polynomial Interpolation

Polynomial interpolation is a method of estimating values between known data points. When graphical data contains a gap, but data is available on either side of the gap or at a few specific points within the gap, an estimate of values within the gap can be made by interpolation.

## Key Concepts

- The goal is to find a polynomial that passes exactly through a set of given points.
- It is based on the principle that there is one and only one polynomial of degree at most `n-1` passing through `n` distinct points.

## Mathematical Formulation

Given `n` points `(x0, y0), (x1, y1), ..., (xn-1, yn-1)`, the interpolation polynomial in the Lagrange form is a linear combination:

$$
L(x) = y0 * l0(x) + y1 * l1(x) + ... + yn-1 * ln-1(x)
$$

Where li(x) are Lagrange basis polynomials:

$$
li(x) = (x - x0) * ... * (x - xi-1) * (x - xi+1) * ... * (x - xn-1) / ((xi - x0) * ... * (xi - xi-1) * (xi - xi+1) * ... * (xi - xn-1))
$$

Algorithm Steps

    Given a set of points (x0, y0), (x1, y1), ..., (xn, yn), compute the Lagrange basis polynomials.
    Construct the Polynomial Interpolation using the Lagrange form.
    Use the Polynomial Interpolation for estimating values.

Example

If we have three points (1, 1), (2, 4), (3, 9) and we want to estimate the value at x=1.5, we can use polynomial interpolation to find a polynomial that passes through these points and then evaluate it at x=1.5.
Advantages

    Polynomial interpolation will always pass through the given points.
    It gives a simple mathematical formula for the estimated function.

Limitations

    For points that do not lie on a single polynomial, this method can give poor results.
    As the degree of the polynomial increases, the polynomial oscillates, especially at the ends (Runge's phenomenon).
