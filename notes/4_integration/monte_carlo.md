## Monte Carlo Integration

- Monte Carlo integration is a technique for numerical integration using random numbers. 
- It's particularly useful for high-dimensional integrals.

## Mathematical Formulation

Monte Carlo integration works by estimating the value of an integral as the average of function values at randomly chosen points within the integration domain.

The integral of a function $f(x)$ over a domain $D$ is approximated as:

$$
\int_D f(x) dx \approx \frac{V}{N} \sum_{i=1}^{N} f(x_i)
$$

where:
- $V$ is the volume of the integration domain,
- $N$ is the number of random points,
- $x_i$ are the random points in the domain $D$.

## Algorithm Steps

1. Define the integration domain $D$ and the function $f(x)$.
2. Generate $N$ random points within the domain.
3. Compute the function value at each of these points.
4. Calculate the sum of these function values and divide by $N$ to get the average.
5. Multiply the average by the volume of the domain $V$ to get the integral estimate.

## Example

Consider the function $f(x) = x^2$ over the interval [0, 1]. 

1. The volume of the integration domain is $V = 1 - 0 = 1$.
2. Generate $N = 1000$ random points in the interval [0, 1].
3. Compute the function value at each of these points and sum these up.
4. Divide the sum by $N$ to get the average.
5. Multiply the average by $V$ to get the integral estimate. This gives an approximation of $\int_0^1 x^2 dx$.

Note: Monte Carlo integration is based on random numbers, so the result will vary each time it's run. However, with a large number of points $N$, the result will converge to the true value of the integral.

## Advantages

- Monte Carlo integration is straightforward and easy to implement.
- It can be used for high-dimensional integrals, where other numerical integration methods become impractical.

## Limitations

- The accuracy of Monte Carlo integration depends on the number of random points used. Too few points can lead to an inaccurate estimate.
- It can be slow compared to other methods for low-dimensional integrals.
- The result can be different each time it's run due to the random nature of the method.
