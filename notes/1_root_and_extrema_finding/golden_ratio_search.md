## Golden Ratio Search 

- The Golden Ratio Search method is a bracketing method used for finding the minimum or maximum of a function.
- The method uses the properties of the golden ratio, a mathematical constant, to eliminate the need for derivative information.
- It can be applied to unimodal functions where there is a single highest or lowest point in a given interval [a, b].

## Mathematical Formulation

The method uses the golden ratio, φ = (1 + sqrt(5)) / 2 ≈ 1.618, to divide the search interval. 

Two points, x1 and x2, are selected within the interval such that they divide the interval into a golden ratio: x2 - a = b - x1 = φ * (b - a).

The function values at x1 and x2, f(x1) and f(x2), are evaluated and compared to find the direction of the search.

## Algorithm Steps

1. Start with initial $a$ and $b$.
2. Calculate two points, $x1 = b - frac{1}{phi}(b - a)$ and $x2 = a + frac{1}{phi}(b - a)$.
3. Evaluate the function at $x1$ and $x2$.
4. If $f(x1) < f(x2)$, the minimum lies in the interval [a, x2], so replace $b$ with $x2$.
5. If $f(x1) > f(x2)$, the minimum lies in the interval [x1, b], so replace $a$ with $x1$.
6. Repeat the steps from 2 to 5 for a given number of iterations $n$ or until a satisfactory approximation for the minimum is obtained.

## Example

Consider a function $f(x) = x^2$.

We start with an initial bracket $a = -2$ and $b = 2$.

1. Compute $x1 = 2 - frac{1}{phi}(2 - -2) = -0.472$ and $x2 = -2 + frac{1}{phi}(2 - -2) = 0.472$.
2. Compute $f(x1) = (-0.472)^2 = 0.2225$ and $f(x2) = (0.472)^2 = 0.2225$.
3. Because $f(x1) = f(x2)$, we can pick any of the intervals [-2, 0.472] or [-0.472, 2]. Let's pick [-2, 0.472] for simplicity, so we set $b = 0.472$.
4. Repeating the steps, we find new $x1$ and $x2$ and new function values, and adjust the interval accordingly.
5. This process continues until we have a satisfactory approximation of the minimum or we reach the maximum number of iterations.

In this case, we would find that $x = 0$ is the minimum of the function $f(x) = x^2$.

## Advantages

- The method is guaranteed to converge to a minimum if one exists in the interval.
- It doesn't require derivative information.
- The method is efficient as it reduces the search interval by a constant proportion at each step.

## Limitations

- It can only be applied to unimodal functions.
- The method requires a good initial bracket [a, b] to ensure convergence to the desired minimum.
- It might converge slowly for flat, plateau-like functions.
