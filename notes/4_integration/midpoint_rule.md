## Midpoint Rule

The region between the integral boundaries is divided into $n$ subintervals. 
At the midpoint of each subinterval, we evaluate the function $f(x)$. 
So, if our subinterval is defined by $x_{i}$ and $x_{i+1}$, our rectangle will have the following coordinates:

$A = (x_{i}, f(\frac{x_{i} + x_{i+1}}{2}))$

$B = (x_{i+1}, f(\frac{x_{i} + x_{i+1}}{2}))$

$C = (x_{i+1}, 0)$

$D = (x_{i}, 0)$

The areas of each of those rectangles are then calculated, and the integral approximation is just the sum of all those areas.

$$I = \sum_{i=0}^{n-1} f(\frac{x_{i} + x_{i+1}}{2}) h$$

![Screenshot from 2022-09-13 23-18-11](https://user-images.githubusercontent.com/37275728/190011101-dcc77f54-d47d-4f62-b699-9d1eec9ef109.png)


## Midpoint Rule

- The Midpoint Rule is a numerical method used for approximating definite integrals.
- It works by approximating the area under the function's graph as a series of rectangles, where the height of each rectangle is determined by the function's value at the midpoint of the corresponding subinterval.

## Mathematical Formulation

For a function $f(x)$ over an interval $[a, b]$, the approximation of the integral using the Midpoint Rule is given by:

$$
(b - a) f\left(\frac{a+b}{2}\right)
$$

## Algorithm Steps

1. Divide the interval $[a, b]$ into a number of subintervals.
2. For each subinterval, compute the function value at the midpoint.
3. Apply the Midpoint Rule formula to each subinterval.
4. Sum up the results from each subinterval to obtain the total integral approximation.

## Example

Consider the function $f(x) = x^2$.

1. Choose a = 0 and b = 2, and divide this interval into 2 equal subintervals.
2. Compute the function values at the midpoints, x = 0.5 and x = 1.5. So, f(0.5) = 0.25, f(1.5) = 2.25.
3. Apply the Midpoint Rule formula to the interval [0, 1]: $(b - a) f\left(\frac{a+b}{2}\right) = (1 - 0) f(0.5) = 1 * 0.25 = 0.25$.
4. Similarly, apply the formula to the interval [1, 2]: $(b - a) f\left(\frac{a+b}{2}\right) = (2 - 1) f(1.5) = 1 * 2.25 = 2.25$.
5. The total integral approximation is the sum of these values: $0.25 + 2.25 = 2.5$.

## Advantages

- The Midpoint Rule is simple and straightforward to implement.
- It often gives a more accurate result than the Trapezoidal Rule for the same number of subintervals.

## Limitations

- Like other numerical integration methods, the Midpoint Rule is an approximation and can introduce errors, especially if the function has a high curvature or rapid changes.
- It may require many subintervals to achieve a high degree of accuracy, increasing the computational load.
