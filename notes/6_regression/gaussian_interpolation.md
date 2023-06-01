# Gaussian Interpolation

Gaussian interpolation, named after Carl Friedrich Gauss, is a method used in numerical analysis to interpolate a smooth function on a given interval using orthogonal polynomials, specifically, the Legendre polynomials. This method is unique because it does not interpolate the function at equally spaced points, but rather at the roots of the Legendre polynomials.

## Mathematical Formulation

Gaussian interpolation uses orthogonal polynomials, and for interpolation on the interval $[-1, 1]$, Legendre polynomials $P_n(x)$ are used. 

Given $n+1$ distinct points $(x_0, y_0), (x_1, y_1), ..., (x_n, y_n)$, the goal of Gaussian interpolation is to find a polynomial $P(x)$ of degree $n$, such that $P(x_i) = y_i$. 

The polynomial $P(x)$ in the Lagrange form is given by:

$$P(x) = \sum_{i=0}^{n} y_i L_i(x)$$

Here $L_i(x)$ is the $i$-th Lagrange polynomial given by:

$$L_i(x) = \prod_{j=0, j\neq i}^{n} \frac{x - x_j}{x_i - x_j}$$

However, in Gaussian interpolation, the $x_i$ values are not arbitrary but are chosen as the roots of the Legendre polynomials.

## Derivation

The Gaussian interpolation relies heavily on the properties of Legendre polynomials, which are solutions to Legendre's differential equation:

$$(1 - x^2)y'' - 2xy' + n(n+1)y = 0$$

The $n$th degree Legendre polynomial, $P_n(x)$, can be derived using Rodrigues' formula:

$$P_n(x) = \frac{1}{2^n n!}\frac{d^n}{dx^n}(x^2 - 1)^n$$

The roots of these polynomials, $x_0, x_1, ..., x_{n}$, are used as the nodes of interpolation in Gaussian interpolation.

The Lagrange form of an interpolating polynomial is given by:

$$P(x) = \sum_{i=0}^{n} y_i L_i(x)$$

where $y_i$ are the function values at the nodes and $L_i(x)$ are the Lagrange basis polynomials, defined as:

$$L_i(x) = \prod_{j=0, j\neq i}^{n} \frac{x - x_j}{x_i - x_j}$$

In the Gaussian interpolation, we choose $x_i$ to be the roots of the Legendre polynomials, which are the solutions to the equation $P_n(x_i) = 0$.

Now, the goal is to find these roots. Since Legendre polynomials have the property that they are orthogonal with respect to the weight function $w(x) = 1$ on the interval $[-1, 1]$, we can use this property to find the roots. The orthogonality condition is:

$$\int_{-1}^{1} P_m(x) P_n(x) dx = 0 \quad \text{for } m \neq n$$

and non-zero for $m = n$. This orthogonality property can be used to numerically calculate the roots of the Legendre polynomials using techniques such as the Newton-Raphson method.

Once we have the roots $x_i$, we can substitute these into our Lagrange form of the polynomial to obtain the Gaussian interpolation of the function.

## Algorithm Steps

For Gaussian interpolation, we follow a set of structured steps to obtain the interpolated values:

1. **Choose the number of data points**: Decide on the number of points, $n$, you want to use for the interpolation. This number will be the degree of the polynomial we'll use for interpolation.

2. **Calculate the Legendre Polynomial**: Calculate or retrieve the $n$-th degree Legendre polynomial $P_n(x)$. 

3. **Find the Roots of the Legendre Polynomial**: These roots, known as the Legendre points or the Gauss points, will serve as the $x$-values at which we'll evaluate our function.

4. **Evaluate the Function at the Gauss Points**: For each Gauss point $x_i$, evaluate the function $f(x_i)$ to get the corresponding $y_i$.

5. **Construct the Lagrange Basis Polynomials**: For each $x_i$, construct the corresponding Lagrange basis polynomial $L_i(x)$ using the Gauss points.

6. **Interpolate the Function**: Use the Lagrange basis polynomials to interpolate the function. This will be a weighted sum of the basis polynomials, where the weights are the function values at the Gauss points: $$f(x) \approx \sum_{i=1}^n f(x_i) L_i(x)$$

7. **Evaluate the Interpolated Function**: Evaluate this approximate function at the points where you want to interpolate the function values.

## Example

Suppose we have three points A(-1, 0), B(0, 1), and C(1, 0). We want to interpolate the value at the point D(0.5, ?).

Here are the steps we need to follow to apply the Gaussian interpolation.

1. **Choose the number of data points**: We have three points (n=2) for the interpolation.

2. **Calculate the Legendre Polynomial**: The second-degree Legendre polynomial $P_2(x) = \frac{1}{2}(3x^2 - 1)$.

3. **Find the Roots of the Legendre Polynomial**: The roots of $P_2(x)$ are $x_1 = -\sqrt{\frac{1}{3}}$, $x_2 = \sqrt{\frac{1}{3}}$.

4. **Evaluate the Function at the Gauss Points**: Evaluate the function at the Gauss points. $f(x_1) = 0$, $f(x_2) = 0$.

5. **Construct the Lagrange Basis Polynomials**: For each Gauss point, construct the Lagrange basis polynomial.

$$L_1(x) = \frac{x - x_2}{x_1-x_2} = \frac{x - \sqrt{\frac{1}{3}}}{-\sqrt{\frac{1}{3}} - \sqrt{\frac{1}{3}}} = -\sqrt{3}x + 1$$

$$L_2(x) = \frac{x - x_1}{x_2-x_1} = \frac{x + \sqrt{\frac{1}{3}}}{\sqrt{\frac{1}{3}} + \sqrt{\frac{1}{3}}} = \sqrt{3}x + 1$$

6. **Interpolate the Function**: Use the Lagrange basis polynomials to interpolate the function.

$$f(x) \approx \sum_{i=1}^2 f(x_i) L_i(x) = 0 \cdot L_1(x) + 1 \cdot L_2(x) = \sqrt{3}x + 1$$

7. **Evaluate the Interpolated Function**: Evaluate this function at D(0.5, ?).

$$f(0.5) = \sqrt{3} * 0.5 + 1 = 1.8660...$$

So, the interpolated value at the point D(0.5, ?) is approximately 1.866. 

## Advantages

1. Gaussian interpolation can provide excellent accuracy

2. Compared to other methods, Gaussian interpolation can achieve a higher level of precision with fewer points. This is because it optimizes the choice of points, unlike methods such as Newton-Cotes formulas where the points are evenly spaced.

## Limitations

1. Gaussian interpolation requires the roots of the Legendre polynomials, which might not be straightforward to calculate. They are typically tabulated for practical use. This could be seen as a disadvantage compared to simpler methods like linear or polynomial interpolation.

2. Gaussian interpolation assumes that the function is well-behaved, i.e., it is differentiable and does not have sharp peaks or discontinuities. For functions that do not satisfy these conditions, the interpolation error could be significant.
