## Simpson's Rule

- Simpson's Rule is a technique in numerical integration, utilized for approximating definite integrals.
- This method treats the region under the function's graph as a succession of parabolic segments, typically offering a more precise approximation than the Midpoint Rule (using rectangles) or the Trapezoidal Rule (using trapezoids).

## Mathematical Formulation

The foundation of Simpson's Rule lies in the concept of estimating the integral of a function $f(x)$ over a specified interval $[a, b]$ by the area beneath a quadratic polynomial. This polynomial passes through the points $(a, f(a))$, $((a+b)/2, f((a+b)/2))$, and $(b, f(b))$.

Here is the formula to approximate the integral of $f(x)$ from $a$ to $b$ using Simpson's Rule:

$$
\frac{b - a}{6} [f(a) + 4f(\frac{a+b}{2}) + f(b)]
$$

The diagram below visualizes the concept:

![simpson](https://user-images.githubusercontent.com/37275728/188944644-e3f47dbf-ba97-472f-8891-7e12906566d3.png)

Let $h$ represent half the width of the interval, i.e., $h = \frac{b-a}{2}$.

The approximation can be expressed as follows:

$$\int_a^b f(x)dx \approx \frac{h}{3} \sum_{k=1}^{N/2} \{f(x_{2k-2})+4f(x_{2k-1})+f(x_{2k})\}$$

## Algorithm Steps

1. Partition the interval $[a, b]$ into an even number of subintervals.
2. Calculate the function values at the end points and the mid points of each subinterval.
3. Apply Simpson's Rule formula to each subinterval.
4. Aggregate the results of each subinterval to derive the total integral approximation.

## Example

Consider the function $f(x) = x^2$.

1. Choose $a = 0$ and $b = 2$, and split this interval into 2 equal subintervals.
2. Calculate the function values at $x = 0$, $x = 1$, and $x = 2$. Thus, $f(0) = 0$, $f(1) = 1$, and $f(2) = 4$.
3. Apply the Simpson's Rule formula to the entire interval: $\frac{b - a}{6} [f(a) + 4f(\frac{a+b}{2}) + f(b)] = \frac{1}{3} [f(0) + 4f(1) + f(2)] = \frac{1}{3} [0 + 4*1 + 4] = \frac{8}{3}$.
4. Since this example contains only one subinterval, the total integral approximation is $\frac{8}{3}$.

## Advantages

- Compared to the Rectangle and Trapezoidal rules, Simpson's Rule often yields a more accurate approximation for a wide variety of functions.
- The method is straightforward to understand and easy to implement.

## Limitations

- Simpson's Rule mandates an even number of intervals, which may not always be convenient.
- For functions that are poorly approximated by parabolas over the chosen intervals, the accuracy of Simpson's Rule may falter.
- Similar to other numerical methods, Simpson's Rule is an approximation technique and can introduce errors, particularly if the function displays rapid changes.
