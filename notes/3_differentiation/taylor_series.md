## Taylor Series Expansion

- The Taylor series is a representation of a function as an infinite sum of terms.
- These terms are calculated from the values of the function's derivatives at a single point.

## Mathematical Formulation

The Taylor series of a function $f(x)$ about a point $a$ is given by:

$$f(x) = f(a) + f'(a)(x-a) + \frac{f''(a)}{2!}(x-a)^2 + \frac{f'''(a)}{3!}(x-a)^3 + \cdots$$

In general, the nth term of the series is:

$$\frac{f^{(n)}(a)}{n!}(x-a)^n$$

where $f^{(n)}(a)$ denotes the nth derivative of the function at the point $a$.

## Practical Use

Taylor series are used to approximate functions that are difficult to compute. The approximation becomes better as more terms are included in the series.

## Example

The Taylor series of the function $e^x$ around the point $a = 0$ is:

$$e^x = 1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \cdots$$

In this case, all the derivatives of the function $e^x$ are $e^x$, and $e^0 = 1$, so all the terms in the series are simple powers of $x$ divided by the factorial of the power.

## Advantages

- Taylor series provide a way to represent complex functions as infinite polynomials, which can be easier to work with.
- They provide a way to approximate functions near a point.

## Limitations

- The approximation is only valid near the point of expansion ($a$). The further away $x$ is from $a$, the worse the approximation may become.
- Not all functions can be represented as a Taylor series. The function must be infinitely differentiable at the point $a$.
- Even when a function can be represented as a Taylor series, the series may not converge to the function at all points.
