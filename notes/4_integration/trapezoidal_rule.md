## Trapeziod method

$$I = \sum_{i=0}^{n-1} \frac{f(x_{i+1}) + f(x_{i})}{2} h$$

![trapezoid](https://user-images.githubusercontent.com/37275728/188944637-3e912cfb-f8f2-40f4-b664-c4e5cf81a64f.png)

$h = \frac{b-a}{N -1}$

N - number of points

Total area (integral)

$$\int_a^b f(x)dx \approx h\sum_{k=1}^{N} \frac{f(x_{k-1})+f(x_k)}{2}$$


## Trapezoidal Rule 

- The Trapezoidal Rule is a numerical method used for approximating definite integrals.
- This method approximates the area under the function as a series of trapezoids.

## Mathematical Formulation

The Trapezoidal Rule works by approximating the region under the graph of the function as a trapezoid and calculating its area. 

For a function $f(x)$ over an interval $[a, b]$, the approximation of the integral by the Trapezoidal Rule is given by:

$$
\frac{b - a}{2} [f(a) + f(b)]
$$

## Algorithm Steps

1. Divide the interval $[a, b]$ into a number of subintervals.
2. Compute the function values at the end points of each subinterval.
3. Apply the formula of the Trapezoidal Rule to each subinterval.
4. Sum up the results of each subinterval to obtain the total integral approximation.

## Example

Consider a function $f(x) = x^2$.

1. Choose a = 0 and b = 2 and divide this interval into 2 equal subintervals.
2. Compute the function values at x = 0, x = 1, and x = 2. So, f(0) = 0, f(1) = 1, f(2) = 4.
3. Apply the Trapezoidal Rule formula to the interval [0, 1]: $\frac{b - a}{2} [f(a) + f(b)]$ = $\frac{1 - 0}{2} [f(0) + f(1)] = 0.5 * (0 + 1) = 0.5$.
4. Similarly, apply the formula to the interval [1, 2]: $\frac{2 - 1}{2} [f(1) + f(2)] = 0.5 * (1 + 4) = 2.5$.
5. The total integral approximation is the sum of these values: $0.5 + 2.5 = 3$.

## Advantages

- The Trapezoidal Rule is simple to understand and implement.
- It provides a more accurate approximation than the Rectangle Rule for many functions.

## Limitations

- It might not be accurate for functions that have rapid changes or high curvature.
- Like other numerical methods, it's an approximation method and can introduce errors, especially if the function is complex or rapidly changing.
- It might require many intervals to achieve high accuracy, which can increase the computational load.
