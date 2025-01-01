## Midpoint Rule

The Midpoint Rule is a robust numerical method for approximating definite integrals. It seeks to estimate the area under a curve by partitioning it into a collection of rectangles and then summing the areas of these rectangles. This method is particularly useful when an antiderivative of the function is difficult or impossible to find analytically. By breaking the interval of integration into smaller segments, the Midpoint Rule allows for a piecewise approximation that can closely match the behavior of the actual function.

Unique to this method, the height of each rectangle is determined by the function's value at the midpoint of the corresponding subinterval. This approach often leads to a more accurate estimate of the area than other methods like the Trapezoidal Rule. By sampling the function at the midpoint, the Midpoint Rule effectively captures the average behavior of the function over each subinterval, reducing the potential for overestimation or underestimation that can occur when using endpoints or other sampling points.

### Mathematical Formulation

For a function $f(x)$ defined over an interval $[a, b]$, the Midpoint Rule provides an approximation for the integral by evaluating the function at specific points within each subinterval. The basic formula for a single subinterval is:

$$
(b - a) f\left(\frac{a+b}{2}\right)
$$

This formula calculates the area of a single rectangle whose width is the length of the interval $(b - a)$ and whose height is the function value at the midpoint $\frac{a+b}{2}$. To achieve a better approximation, the interval $[a, b]$ is divided into $n$ subintervals of equal width. The width of each subinterval, denoted by $h$, is given by:

$$
h = \frac{b - a}{n}
$$

Within each subinterval, defined by $x_{i}$ and $x_{i+1}$, the function $f(x)$ is evaluated at the midpoint $\frac{x_{i} + x_{i+1}}{2}$. This gives rise to the coordinates of the rectangle:

- ** $\left(x_{i}, f\left(\frac{x_{i} + x_{i+1}}{2}\right)\right)$
- ** $\left(x_{i+1}, f\left(\frac{x_{i} + x_{i+1}}{2}\right)\right)$
- ** $\left(x_{i+1}, 0\right)$
- ** $\left(x_{i}, 0\right)$

The area of each rectangle is then computed by multiplying the height $f\left(\frac{x_{i} + x_{i+1}}{2}\right)$ by the width $h$. The integral approximation is obtained by summing these areas across all subintervals:

$$
I = \sum_{i=0}^{n-1} f\left(\frac{x_{i} + x_{i+1}}{2}\right) h
$$

This summation provides an estimate of the total area under the curve $f(x)$ over the interval $[a, b]$. The graphical representation of this method helps visualize how the Midpoint Rule approximates the integral by stacking these rectangles side by side.

![Midpoint Rule Visualization](https://user-images.githubusercontent.com/37275728/190011101-dcc77f54-d47d-4f62-b699-9d1eec9ef109.png)

### Algorithm Steps

1. Begin by dividing the interval $[a, b]$ into $n$ equal subintervals. The choice of $n$ determines the number of rectangles used in the approximation and affects the accuracy of the result.
2. For each subinterval, calculate the midpoint $\frac{x_{i} + x_{i+1}}{2}$. Evaluate the function $f(x)$ at this midpoint to determine the height of the corresponding rectangle.
3. For each subinterval, multiply the function value at the midpoint by the width $h$ of the subinterval. This gives the area of the rectangle for that subinterval.
4. Sum the areas of all rectangles obtained from each subinterval. This total sum provides the approximate value of the definite integral over $[a, b]$.

### Example

Consider the function $f(x) = x^2$.

I. **Choose Interval and Subdivisions:** 

Let $a = 0$ and $b = 2$, and partition this interval into $n = 2$ equal subintervals. This results in subintervals $[0, 1]$ and $[1, 2]$, each with a width $h = 1$.

II. **Evaluate at Midpoints:** 

- For the first subinterval $[0, 1]$, the midpoint is $x = 0.5$. Evaluating the function gives $f(0.5) = (0.5)^2 = 0.25$.
- For the second subinterval $[1, 2]$, the midpoint is $x = 1.5$. Evaluating the function gives $f(1.5) = (1.5)^2 = 2.25$.

III. **Apply the Midpoint Rule Formula:**

- $(1 - 0) \times f(0.5) = 1 \times 0.25 = 0.25$.
- $(2 - 1) \times f(1.5) = 1 \times 2.25 = 2.25$.

IV. **Sum the Areas:** 

The total integral approximation is $0.25 + 2.25 = 2.5$.

The exact value of the integral $\int_{0}^{2} x^2 \, dx = \frac{8}{3} \approx 2.6667$. The Midpoint Rule provides an approximation of $2.5$, which is reasonably close to the exact value, especially considering the simplicity of the method and the small number of subintervals used.

### Advantages

- The Midpoint Rule is straightforward and **efficient** to implement, making it a popular choice for numerical integration, especially in educational settings and for simple applications.
- For functions that are reasonably smooth, the Midpoint Rule often provides a more **accurate** approximation than the Trapezoidal Rule when using the same number of subintervals.
- The Midpoint Rule can better handle certain function **behaviors**, such as oscillations or variations within subintervals, by averaging out fluctuations through midpoint evaluations.

### Limitations

- The Midpoint Rule can introduce **errors** when dealing with functions that exhibit high curvature or rapid changes within subintervals, as a single midpoint evaluation may not capture the function's behavior adequately.
- Achieving high accuracy with the Midpoint Rule often requires a large number of **subintervals**, increasing computational effort due to the necessity of more function evaluations and calculations.
- The Midpoint Rule is less effective for **discontinuous** functions, as the method assumes continuity over the interval of integration and may fail to provide meaningful approximations for functions with discontinuities or sharp corners.

