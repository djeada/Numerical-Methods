## Introduction

Newton’s Polynomial, often referred to as Newton’s Interpolation Formula, is another classical approach to polynomial interpolation. Given a set of data points $(x_0,y_0),(x_1,y_1),\dots,(x_n,y_n)$ with distinct $x_i$ values, Newton’s method constructs an interpolating polynomial in a form that makes it easy to add additional data points without recomputing the entire polynomial. This form involves **divided differences**, which are incremental ratio measures that help build the polynomial step by step.

While the end result is equivalent to that of Lagrange interpolation, Newton’s form is particularly convenient when data points are added incrementally. The polynomial can be updated by incorporating a new divided difference term without completely starting over.

## Mathematical Formulation

A Newton interpolating polynomial for $n+1$ points $(x_i, y_i)$ can be written as:

$$P(x) = f[x_0] + f[x_0,x_1](x - x_0) + f[x_0,x_1,x_2](x - x_0)(x - x_1) + \cdots + f[x_0,x_1,\ldots,x_n] (x - x_0)(x - x_1)\cdots(x - x_{n-1}),$$
where $f[x_0,x_1,\ldots,x_k]$ represents the $k$-th order divided difference of the function $f$ evaluated at points $x_0, x_1, \ldots, x_k$.

**Divided Differences**: For a set of points $(x_i,y_i)$, the divided differences are defined recursively:

- **Zero-th order divided difference**:  

$$f[x_i] = y_i.$$

- **First order divided difference**:  

For $i \neq j$:

$$f[x_i,x_j] = \frac{f[x_j] - f[x_i]}{x_j - x_i}.$$

- **Higher order divided differences**:  

For $i < j < k$:

$$f[x_i,x_j,x_k] = \frac{f[x_j,x_k] - f[x_i,x_j]}{x_k - x_i},$$
and so forth for even higher orders.

## Derivation

Consider the cubic case for intuition (the process generalizes to higher degrees):

$$P_3(x) = a_0 + (x-x_0)a_1 + (x-x_0)(x-x_1)a_2 + (x-x_0)(x-x_1)(x-x_2)a_3.$$

I. **At $x=x_0$**:

$$P_3(x_0)=a_0 = y_0.$$

II. **At $x=x_1$**:

Substitute $x_1$ into $P_3(x)$:

$$y_1 = P_3(x_1) = a_0 + (x_1-x_0)a_1.$$

Since $a_0 = y_0$:

$$a_1 = \frac{y_1 - y_0}{x_1-x_0} = f[x_0,x_1].$$

III. **At $x=x_2$**:

Substitute $x_2$:

$$y_2 = P_3(x_2)= a_0 + (x_2-x_0)(a_1 + (x_2 - x_1)a_2).$$

Rearranging terms leads to:

$$a_2 = \frac{\frac{y_2 - y_0}{x_2 - x_0} - \frac{y_1 - y_0}{x_1 - x_0}}{x_2 - x_1} = f[x_0,x_1,x_2].$$

Similarly, higher order coefficients ($a_3, a_4, \ldots$) can be obtained, which correspond to higher order divided differences. In general:

$$a_k = f[x_0,x_1,\ldots,x_k].$$

## Algorithm Steps

I. **Data Preparation**:  

Given $(x_0,y_0), (x_1,y_1),\ldots,(x_n,y_n)$ sorted so that $x_0 < x_1 < \cdots < x_n$.

II. **Compute Divided Differences**:  
- Start by listing the $y$-values as the zeroth order divided differences.
- Compute the first order divided differences:

 $$f[x_i,x_{i+1}] = \frac{y_{i+1}-y_i}{x_{i+1}-x_i} \quad \text{for } i=0,\ldots,n-1.$$
- Use these to compute the second order divided differences, and so on, until you have $f[x_0,x_1,\ldots,x_n]$.

Usually, this is arranged in a **divided difference table**, where each column corresponds to divided differences of increasing order.

III. **Form the Newton Polynomial**:

Once you have all the divided differences:

$$P(x) = f[x_0] + f[x_0,x_1](x - x_0) + f[x_0,x_1,x_2](x-x_0)(x-x_1) + \cdots.$$

IV. **Use the Polynomial for Interpolation**:

Substitute the desired $x$-value into $P(x)$ to get the interpolated $y$-value.

## Example

Consider points $(1,2), (2,3), (3,5)$.

- Zeroth order differences (just $y$-values):

$$f[x_0]=2, \quad f[x_1]=3, \quad f[x_2]=5.$$

- First order differences:

$$f[x_0,x_1] = \frac{3-2}{2-1}=1, \quad f[x_1,x_2] = \frac{5-3}{3-2}=2.$$

- Second order difference:

$$f[x_0,x_1,x_2] = \frac{f[x_1,x_2] - f[x_0,x_1]}{x_2 - x_0} = \frac{2-1}{3-1}=\frac{1}{2}=0.5.$$

The Newton polynomial is:

$$P(x)=f[x_0] + f[x_0,x_1](x - x_0) + f[x_0,x_1,x_2](x - x_0)(x - x_1).$$

Substitute the values:

$$P(x)=2 + (1)(x - 1) + (0.5)(x - 1)(x - 2).$$

This matches exactly the polynomial you would get if you used Lagrange or any other method for these points.

## Advantages

- **Incremental Updating**:  

If a new data point $(x_{n+1},y_{n+1})$ is added, you can update the polynomial by computing a new set of divided differences without starting over from scratch.

- **Equivalent to Lagrange**:  

Newton’s polynomial produces the same interpolating polynomial as Lagrange interpolation or any other form of polynomial interpolation.

- **Structured Form**:  

The nested form of Newton’s polynomial:

$$P(x)=a_0 + (x - x_0)(a_1 + (x - x_1)(a_2 + \cdots )),$$
is often numerically more stable for evaluating and updating the polynomial.

## Limitations

- **Complexity for Large Data**:

As the number of data points grows large, the computation and maintenance of higher order divided differences can become computationally intensive.

- **Interpolation Issues**:

Like any polynomial interpolation, Newton’s polynomial can suffer from Runge’s phenomenon if the points are not well-distributed, causing oscillations in the polynomial approximation.
