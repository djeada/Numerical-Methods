The phrase quadrature refers to the numerical calculation of a definite integral.

For the function $f(x)$, the integral over $[a,b]$ is defined as:

$$ I = \int_{a}^{b} f(x) dx $$

Why do we need numerical methods for integration:

* It may be impossible to integrate some functions analytically.
* We may not know the formula for the function we wish to integrate, and we may just have some data from an experiment.

The following is true for a point $c$ between $a$ and $b$:

$$ \int_{a}^{b} f(x) dx = \int_{a}^{c} f(x) dx + \int_{c}^{b} f(x)dx $$

This is the foundation for many numerical approaches; we divide the large interval into smaller intervals and add the results from each smaller piece.
