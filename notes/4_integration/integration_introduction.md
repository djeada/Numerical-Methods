# Integration in Calculus

Integration accumulates a quantity over an interval. It can recover total change from a known rate of change, measure area, and express solutions of differential equations. For example, integrating velocity over time gives displacement, including the sign of the motion.

A definite integral is a signed accumulation: portions of the graph below the horizontal axis contribute negatively. When the function is nonnegative, the integral equals the geometric area under its graph. Integrating $|f(x)|$ gives the total unsigned area instead.

In numerical work, an antiderivative may be unavailable, the function may be expensive to evaluate, or only discrete measurements may be known. Numerical integration estimates the accumulation from those available values; its accuracy depends on how the samples represent the function between them.

## Numerical integration (or quadrature)

- Numerical integration, often referred to as quadrature, is a method used to approximate the integral of a function using finite sums.
- It is often used when it may be impossible to integrate some functions analytically, or when the formula for the function is unknown, for instance, when data from an experiment is available.
- The function is evaluated at a set of points and these values are used to estimate the integral's value.
- Composite quadrature divides the interval into smaller pieces and adds an approximation from each piece. This follows the additivity of the exact integral:

$$
\int_a^b f(x)\,dx=\int_a^c f(x)\,dx+\int_c^b f(x)\,dx,
$$

where $c$ lies between $a$ and $b$.

## Numerical methods for integration

1. **Rectangle Rule (or midpoint rule):** This method approximates the area under the curve as a series of rectangles. For example, if we have a function $f(x) = x^2$, and we want to approximate the integral over the interval $[1, 2]$ with a step size $h = 0.1$, using the rectangle rule, we get:

$$
\int_{1}^{2} x^2 dx \approx \sum_{i=1}^{10} h \cdot f(1 + 0.1(i - 0.5))
$$

2. **trapezoidal rule:** This method approximates the area under the curve as a series of trapezoids, which typically provides a better approximation compared to the left or right rectangle rule. An example application would be the same function $f(x) = x^2$, the integral can be approximated as:

$$
\int_{1}^{2} x^2 dx \approx \sum_{i=1}^{10} \frac{h}{2}
(f(1 + 0.1(i - 1)) + f(1 + 0.1i))
$$

3. **Simpson's rule:** This method approximates the area under the curve as a series of parabolic segments. It is typically more accurate than both the rectangle and trapezoidal rules. Let's consider an example where we want to approximate the same integral, using Simpson's rule, it would look like:

$$
\int_{1}^{2} x^2 dx \approx \frac{h}{3}
(f(1) + 4\sum_{i=1}^{5} f(1 + 0.2i - 0.1) + 2\sum_{i=1}^{4} f(1 + 0.2i) + f(2))
$$

4. **Monte Carlo Integration:** This method uses random sampling to estimate the integral, which can be especially useful for higher-dimensional integrals. An example of this could be estimating the integral of a complex multi-variable function over a specific region.

## Error estimation and convergence of numerical integration methods

- Each of the methods for numerical integration has its own rate of convergence, which determines how quickly the numerical approximation approaches the exact value. For instance, the trapezoidal rule converges as $O(h^2)$, Simpson's rule converges as $O(h^4)$, etc., where $h$ is the step size.

## A common grid and a concrete comparison

Let $x_i=a+ih$, $h=(b-a)/n$, and let $I=\int_a^b f(x)\,dx$ denote the exact integral. A quadrature approximation $Q_n$ is a weighted sum of sampled values. The number of subintervals is $n$; endpoint-based rules usually sample $n+1$ grid points, while the midpoint rule samples $n$ interior points.

| Rule | Samples for the composite rule | Smoothness for the usual error bound | Global error order |
| --- | --- | --- | --- |
| Midpoint | $n$ midpoints | Bounded continuous second derivative | $O(h^2)$ |
| Trapezoidal | $n+1$ endpoints | Bounded continuous second derivative | $O(h^2)$ |
| Simpson | $n+1$ endpoints, with even $n$ | Bounded continuous fourth derivative | $O(h^4)$ |
| Monte Carlo | $N$ independent random points | Integrability for a law of large numbers; finite variance for a standard error | Root mean square error $O(N^{-1/2})$ |

For the examples above, $I=\int_1^2x^2\,dx=7/3$. With $n=10$ and $h=0.1$, the midpoint rule gives $2.3325$, the trapezoidal rule gives $2.335$, and Simpson's rule gives $7/3$ exactly in exact arithmetic. The signed errors $I-Q_n$ are respectively $1/1200$, $-1/600$, and zero. This makes the shared example a direct comparison rather than three unrelated formulas.

## Estimating error by refinement

Suppose $Q_h=I+ch^p+o(h^p)$ on a sequence of uniform grids and that the leading asymptotic term dominates. Then

$$
I-Q_{h/2}\approx\frac{Q_{h/2}-Q_h}{2^p-1}.
$$

Use $p=2$ for midpoint or trapezoidal quadrature and $p=4$ for Simpson's rule. This estimate requires the stated smoothness and does not certify accuracy when the grid misses a narrow peak, singularity, or oscillation. Split known discontinuities or singular points into separate intervals and use a method suited to each piece. If only fixed data are available, refinement may require a new measurement rather than another function call.

## Advantages of numerical integration

- Numerical integration can handle a wide range of functions, including ones where analytical integration is difficult or impossible.
- These methods can also handle functions that are only known at certain discrete points, such as data obtained from experiments or observations.

## Limitations of numerical integration

- Numerical integration is only an approximation and can introduce errors. The approximation is more accurate for a larger number of points, but it may require more computational resources.
- The accuracy of the approximation also depends on the behavior of the function. If the function is rapidly changing, discontinuous, or noisy, the approximation may not be very accurate.
- Numerical methods require the function to be known or evaluated at certain points. If the function is expensive to evaluate, or if it is only known at a few points, numerical integration may not be practical.
- Different methods have different strengths and weaknesses. While Simpson's rule is generally more accurate than the Trapezoid Rule for smooth functions, it may perform worse for functions with discontinuities or sharp turns.
