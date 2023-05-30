## Midpoint Rule

- The Midpoint Rule is a robust numerical method for approximating definite integrals. It seeks to estimate the area under a curve by partitioning it into a collection of rectangles and then summing the areas of these rectangles.
- Unique to this method, the height of each rectangle is determined by the function's value at the midpoint of the corresponding subinterval, leading to a more accurate estimate of the area than other methods like the Trapezoidal Rule.

## Mathematical Formulation

For a function $f(x)$ defined over an interval $[a, b]$, the Midpoint Rule provides the following approximation for the integral:

$$
(b - a) f\left(\frac{a+b}{2}\right)
$$

The integral boundaries are divided into $n$ subintervals. Within each subinterval, defined by $x_{i}$ and $x_{i+1}$, the function $f(x)$ is evaluated at the midpoint. This gives rise to the coordinates of the rectangle:

- Upper left corner (A): $(x_{i}, f(\frac{x_{i} + x_{i+1}}{2}))$
- Upper right corner (B): $(x_{i+1}, f(\frac{x_{i} + x_{i+1}}{2}))$
- Lower right corner (C): $(x_{i+1}, 0)$
- Lower left corner (D): $(x_{i}, 0)$

The areas of these rectangles are then computed, and the integral approximation is obtained by summing these areas:

$$I = \sum_{i=0}^{n-1} f(\frac{x_{i} + x_{i+1}}{2}) h$$

This computation is visually represented as follows:

![Midpoint Rule Visualization](https://user-images.githubusercontent.com/37275728/190011101-dcc77f54-d47d-4f62-b699-9d1eec9ef109.png)

## Algorithm Steps

1. Partition the interval $[a, b]$ into several subintervals.
2. Evaluate the function value at the midpoint of each subinterval.
3. Apply the Midpoint Rule formula for every subinterval.
4. Aggregate the results from all subintervals to yield the total integral approximation.

## Example

Consider the function $f(x) = x^2$. 

- Choose a = 0 and b = 2, and partition this interval into 2 equal subintervals.
- Evaluate the function values at the midpoints, x = 0.5 and x = 1.5. This gives f(0.5) = 0.25, f(1.5) = 2.25.
- Apply the Midpoint Rule formula to the interval [0, 1]: $(1 - 0) f(0.5) = 1 * 0.25 = 0.25$.
- Similarly, apply the formula to the interval [1, 2]: $(2 - 1) f(1.5) = 1 * 2.25 = 2.25$.
- The total integral approximation is the sum of these values: $0.25 + 2.25 = 2.5$.

## Advantages

- The Midpoint Rule is an intuitive and efficient method to implement.
- Compared to the Trapezoidal Rule, the Midpoint Rule often provides a more accurate approximation for the same number of subintervals.

## Limitations

- Like all numerical integration methods, the Midpoint Rule can introduce errors. These errors are more likely with functions that exhibit high curvature or rapid changes.
- Achieving high accuracy may necessitate a large number of subintervals, which could increase computational demands.
