## Linear systems

A linear system can be represented by a linear function (straight line) that looks like this:

$$ f(x) = ax + b $$

A linear equation associated with a linear function is expressed as follows:

$$ f(x) = 0 $$

We are trying to figure out the solutions to the equation:

$$x=f(x)$$

Our goal will be to obtain a solution $x$ for this equation. For linear problems, the formula is $x = -b/a$. But the idea is that we may generalize useful insights from linear problems to nonlinear systems.

Nonlinear systems include at least one nonlinear element, that might one of the following:

- Powers: $x^2, x^3, \ldots $

- Roots, radicals and other non-integer polynomials: $ \sqrt{x}, x^{3/5}, x^{pi} \ldots $

- Trigonometric and other special functions: $\sin(x), \tan(x), \log(x), \ldots $

We call the solutions $x_0$

Iterations i:

$$x_i = f(x_{i-1}) $$
$$= f(x_0) + (x_{i-1}-x_0)f'(x_0) + ...$$

In each iteration $f(x_0) = x_0$

$$x_i - x_0 = (x_{i-1}-x_0)f'(x_0) + ... $$

$$\Delta x_i \approx \Delta x_{i-1} f'(x_0)$$

Does $$\Delta x_i $$ shrink?

Yes, only if $|f'(x_0)| < 1$

## Example

$$x = f(x) = 1 - e^{-2x}$$
$$f'(x) = -2e^{-2x}$$

OK:
$$f'(0.797) = -0.406$$

NOT OK:
$$f'(0) = -2$$
