## Golden Ratio Search 

The Golden Ratio Search is a bracketing method employed for finding the minimum or maximum of a function. This method leverages the properties of the golden ratio, a mathematical constant, negating the necessity for derivative information. It is applicable to unimodal functions, where a single highest or lowest point exists within a given interval [a, b].

## Mathematical Formulation

The Golden Ratio, denoted by $\phi$, is approximately 1.618 and is defined as $\phi = \frac{1 + \sqrt{5}}{2}$. The Golden Ratio Search uses this constant to partition the search interval. 

Two points, $x_1$ and $x_2$, are chosen within the interval [a, b] such that they partition the interval following the golden ratio: 

$$x_2 - a = b - x_1 = \phi * (b - a)$$

The function values at $x_1$ and $x_2$, $f(x_1)$ and $f(x_2)$, are evaluated and contrasted to ascertain the direction of the search.

## Algorithm Steps

1. Begin with the initial $a$ and $b$.
2. Compute the two points: $x_1 = b - \frac{1}{\phi}(b - a)$ and $x_2 = a + \frac{1}{\phi}(b - a)$.
3. Determine the function values at $x_1$ and $x_2$.
4. If $f(x_1) < f(x_2)$, the minimum is present within the interval [a, $x_2$], so replace $b$ with $x_2$.
5. If $f(x_1) > f(x_2)$, the minimum is present within the interval [$x_1$, b], so replace $a$ with $x_1$.
6. Repeat steps 2 to 5 for a given number of iterations $n$ or until a satisfactory approximation for the minimum is achieved.

## Example

Take a function $f(x) = x^2$.

Let's start with an initial bracket $a = -2$ and $b = 2$.

1. Compute $x_1 = 2 - \frac{1}{\phi}(2 - -2) = -0.472$ and $x_2 = -2 + \frac{1}{\phi}(2 - -2) = 0.472$.
2. Compute $f(x_1) = (-0.472)^2 = 0.2225$ and $f(x_2) = (0.472)^2 = 0.2225$.
3. Since $f(x_1) = f(x_2)$, we can select either interval [-2, 0.472] or [-0.472, 2]. Let's choose [-2, 0.472] for simplicity, setting $b = 0.472$.
4. Repeat the steps to find new values for $x_1$ and $x_2$, compute new function values, and adjust the interval accordingly.
5. This iterative process continues until we achieve a satisfactory approximation of the minimum or reach the maximum number of iterations.

In this scenario, we would find that $x = 0$ is the minimum of the function $f(x) = x^2$.

## Advantages

- This method ensures convergence to a minimum if one exists within the interval.
- Derivative information is not required.
- The Golden Ratio Search is efficient as it reduces the search interval by a constant proportion with each step.

## Limitations

- The method can only be applied to unimodal functions.
- A good initial bracket [a, b] is necessary to guarantee convergence to the desired minimum.
- For flat, plateau-like functions, the method might converge slowly.
