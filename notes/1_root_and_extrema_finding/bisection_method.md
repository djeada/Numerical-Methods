## Bisection Method

- The bisection method is a bracketing method used for finding a root of a function.
- It is simple, reliable, but comparatively slow, especially for functions that are steep or nearly linear.
- The function should be continuous, and the initial interval [a, b] should contain exactly one root.

## Mathematical Formulation

The main principle behind the method is that the function changes sign across a root. Therefore, if $f(a)f(b) < 0$, we can be certain that a root exists in the interval [a, b].

The midpoint of [a, b] is computed as $c = \frac{a+b}{2}$. Then, $f(c)$ is evaluated.

## Algorithm Steps

1. Start with initial $a$ and $b$ such that $f(a)f(b) < 0$.
2. Calculate the midpoint $c = \frac{a+b}{2}$.
3. If $f(a)f(c) < 0$, then the root lies in the interval [a, c], so replace $b$ with $c$.
4. If $f(c)f(b) < 0$, then the root lies in the interval [c, b], so replace $a$ with $c$.
5. Repeat the steps from 2 to 4 for a given number of iterations $n$ or until a satisfactory approximation for the root is obtained.

## Example

Consider a continuous function $f(x) = x^2 - 4$.

We start with an initial bracket $a = 0$ and $b = 5$, for which $f(a)f(b) = (-4)(1) < 0$.

1. Compute $c = \frac{a+b}{2} = 2.5$.
2. Compute $f(c) = (2.5)^2 - 4 = 2.25$.
3. Because $f(a)f(c) = (-4)(2.25) < 0$, the root is in the interval [0, 2.5]. So, we set $b = 2.5$.
4. Repeating the steps, we find $c = 1.25$ and $f(c) = -2.4375$. This time, $f(c)f(b) = (2.25)(-2.4375) < 0$, so the root is in the interval [1.25, 2.5]. So, we set $a = 1.25$.
5. Repeating the steps again, we find $c = 1.875$ and $f(c) = -0.234375$.
6. This process continues until we have a satisfactory approximation of the root or we reach the maximum number of iterations.

In this case, we would find that $x = 2$ is a root of the function $f(x) = x^2 - 4$.

## Advantages

- The method is guaranteed to converge to a root if one exists in the interval.
- It's a simple method and easy to understand/implement.

## Limitations

- The method can be relatively slow, especially for functions that are steep or nearly linear.
- The method requires that a root is bracketed and only finds one root in the given bracket. If there are multiple roots, this method can't find them unless each is bracketed separately.
- It's not suitable for complex functions or when the derivative information is available, in which cases other methods like Newton-Raphson may be more efficient.
