## Simpson's method

![simpson](https://user-images.githubusercontent.com/37275728/188944644-e3f47dbf-ba97-472f-8891-7e12906566d3.png)

$h = \frac{b-a}{2}$

$$\int_a^b f(x)dx \approx \frac{h}{3} \sum_{k=1}^{N/2} \{f(x_{2k-2})+4f(x_{2k-1})+f(x_{2k}))\}$$


## Simpson's Rule

- Simpson's Rule is a numerical method used for approximating definite integrals.
- This method approximates the region under the graph of a function as a series of parabolic segments, which typically provides a more accurate approximation than methods using rectangles (Midpoint Rule) or trapezoids (Trapezoidal Rule).

## Mathematical Formulation

Simpson's Rule is based on the idea of approximating the integral of a function $f(x)$ over an interval $[a, b]$ by the area under a quadratic polynomial that passes through the points $(a, f(a))$, $((a+b)/2, f((a+b)/2))$, and $(b, f(b))$. 

The approximation of the integral of $f(x)$ from $a$ to $b$ is given by:

$$
\frac{b - a}{6} [f(a) + 4f(\frac{a+b}{2}) + f(b)]
$$

## Algorithm Steps

1. Divide the interval $[a, b]$ into an even number of subintervals.
2. Compute the function values at the end points and mid points of each subinterval.
3. Apply the formula of Simpson's rule to each subinterval.
4. Sum up the results of each subinterval to obtain the total integral approximation.

## Example

Let's consider a function $f(x) = x^2$.

1. Choose a = 0 and b = 2 and divide this interval into 2 equal subintervals.
2. Compute the function values at x = 0, x = 1, and x = 2. So, f(0) = 0, f(1) = 1, f(2) = 4.
3. Apply Simpson's rule formula to the interval: $\frac{b - a}{6} [f(a) + 4f(\frac{a+b}{2}) + f(b)]$ = $\frac{1}{3} [f(0) + 4f(1) + f(2)] = \frac{1}{3} [0 + 4*1 + 4] = \frac{8}{3}$
4. Since there is only one subinterval in this example, the total integral approximation is $\frac{8}{3}$.

## Advantages

- Simpson's Rule provides a more accurate approximation for many functions compared to the Rectangle and Trapezoidal rules.
- It is simple to understand and implement.

## Limitations

- Simpson's Rule requires that the number of intervals be even.
- It might not be accurate for functions that are not well-approximated by parabolas over the chosen intervals.
- Like other numerical methods, it is an approximation method and can introduce errors, especially if the function is rapidly changing.
