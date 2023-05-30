## Trapezoidal Rule 

- The Trapezoidal Rule is a numerical integration technique used for approximating definite integrals.
- This method estimates the area under the function's curve by constructing a series of trapezoids and summing their areas.

## Mathematical Formulation

The Trapezoidal Rule operates by assuming the region under the graph of the function as a trapezoid, then calculating its area.

Given a function $f(x)$ defined over an interval $[a, b]$, the approximation of the integral using the Trapezoidal Rule is expressed as:

$$
\frac{b - a}{2} [f(a) + f(b)]
$$
$$I = \sum_{i=0}^{n-1} \frac{f(x_{i+1}) + f(x_{i})}{2} h$$

![trapezoid](https://user-images.githubusercontent.com/37275728/188944637-3e912cfb-f8f2-40f4-b664-c4e5cf81a64f.png)

Let $h$ represent the width of the interval, i.e., $h = \frac{b-a}{N -1}$, where $N$ is the number of points.

The total area (or the integral) can be approximated as:

$$\int_a^b f(x)dx \approx h\sum_{k=1}^{N} \frac{f(x_{k-1})+f(x_k)}{2}$$

## Algorithm Steps

1. Partition the interval $[a, b]$ into several subintervals.
2. Calculate the function values at the end points of each subinterval.
3. Apply the Trapezoidal Rule formula to each subinterval.
4. Aggregate the results from each subinterval to derive the total integral approximation.

## Example

Take the function $f(x) = x^2$ for instance.

1. Choose $a = 0$ and $b = 2$, and split this interval into 2 equal subintervals.
2. Compute the function values at $x = 0$, $x = 1$, and $x = 2$. Thus, $f(0) = 0$, $f(1) = 1$, and $f(2) = 4$.
3. Apply the Trapezoidal Rule formula to the interval [0, 1]: $\frac{b - a}{2} [f(a) + f(b)] = \frac{1 - 0}{2} [f(0) + f(1)] = 0.5 * (0 + 1) = 0.5$.
4. Similarly, apply the formula to the interval [1, 2]: $\frac{b - a}{2} [f(a) + f(b)] = \frac{2 - 1}{2} [f(1) + f(2)] = 0.5 * (1 + 4) = 2.5$.
5. The total integral approximation is the sum of these values, i.e., $0.5 + 2.5 = 3$.

## Advantages

- The Trapezoidal Rule is straightforward to understand and easy to implement.
- For a wide array of functions, it delivers a more accurate approximation than the Rectangle Rule.

## Limitations

- For functions exhibiting rapid changes or high curvature, the accuracy of the Trapezoidal Rule may be insufficient.
- Like all numerical methods, it is an approximation technique and can introduce errors, particularly with complex or rapidly changing functions.
- To achieve high precision, a large number of intervals might be required, which could escalate computational demands.
