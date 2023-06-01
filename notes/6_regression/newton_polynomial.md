## Newton's Polynomial

Newton's Polynomial, also known as Newton's Interpolation Formula, is a method used for polynomial interpolation. It estimates values based on nearby points using divided differences. Interpolating with the Newton Polynomial yields the same results as with the Lagrange Polynomial.

## Mathematical Formulation

The Newton's Polynomial is formulated as:

$$
P(x) = f[x_0] + f[x_0,x_1](x - x_0) + f[x_0,x_1,x_2](x - x_0)(x - x_1) + \ldots
$$

In this formula, `f[x_0,x_1,...,x_n]` represents the nth divided difference based on the points `x_0`, `x_1`, ..., `x_n`.

## Derivation

The polynomial is rewritten in the following form:

$$ P_N(x) = a_0 +(x-x_0)a_1 + (x-x_0)(x-x_1)a_2 + \cdots + (x-x_0)(x-x_1)\ldots(x-x_N)a_N,$$

For `N=3`:

$$
P_3(x) = a_0 +(x-x_0)a_1 + (x-x_0)(x-x_1)a_2 + (x-x_0)(x-x_1)(x-x_2)a_3
$$

We can further simplify this to:

$$
P_3(x) = a_0 +(x-x_0)[a_1 + (x-x_1)[a_2 + (x-x_2)a_3]]
$$

1. Substitute `x=x_0`: We have `P_3(x_0)=a_0`, and our interpolant `P_3(x)` evaluated at `x_0` must return `y_0`. Hence we can deduce:

$$a_0 = y_0$$

2. Substitute `x=x_1`: We get `P_3(x_1) = a_0 +(x_1-x_0)a_1 = y_0 +(x_1-x_0)a_1`. The left hand side of this equals `y_1`, and we know everything on the right hand side since we've already calculated that `a_0 = y_0`. We can then rearrange to find:

$$ a_1 = \frac{(y_1 - y_0)}{(x_1-x_0)}$$

3. Substituting `x=x_2` gives:

$$ y_2 = P_3(x_2) = a_0 +(x_2-x_0)[a_1 + (x_2-x_1)a_2] = y_0 + (x_2-x_0)\left[ \frac{(y_1 - y_0)}{(x_1-x_0)} + (x_2-x_1)a_2\right] $$

$$ \implies a_2 = \frac{ \frac{(y_2 - y_0)}{(x_2-x_0)} - \frac{(y_1 - y_0)}{(x_1-x_0)}}{x_2-x_1} $$

For a general algorithm for this method, let's introduce the following [*divided difference*](https://en.wikipedia.org/wiki/Divided_differences) notation:

$$ \Delta y_i = \frac{y_i-y_0}{x_i-x_0}, \quad i=1,2,\ldots, N $$
$$ \Delta^2 y_i = \frac{\Delta y_i-\Delta y_1}{x_i-x_1}, \quad i=2, 3,\ldots, N $$
$$ \vdots $$
$$ \Delta^N y_N = \frac{\Delta^{N-1} y_N-\Delta^{N-1} y_{N-1}}{x_N-x_{N-1}} $$

The coefficients of the interpolating polynomial in the general case are given by:

$$a_0=y_0, \quad a_1 = \Delta y_1, \quad a_2 = \Delta^2 y_2, \quad \ldots \quad a_N = \Delta^N y_N$$

The Newton Polynomial evaluation process follows these steps:

1. Initialize the unknown array `a` with the data `y`, so that:
$$ a_0 = y_0, \quad a_1 = y_1, \quad a_2 = y_2, \ldots $$

2. Update `a` values without touching `a_0`:
$$ a_1 = \frac{(a_1 - a_0)}{(x_1-x_0)}, \quad a_2 = \frac{(a_2 - a_0)}{(x_2-x_0)}, \ldots $$

3. For the next steps, don't touch `a_1` and set:
$$ a_2 = \frac{(a_2 - a_1)}{(x_2-x_1)} $$
## Algorithm Steps

To construct the Newton's Polynomial, follow these steps:

1. **Prepare the data**: Given a set of points $(x_0, y_0), (x_1, y_1), ..., (x_n, y_n)$, ensure the data is ordered such that the x-values are in increasing order.

2. **Compute the divided differences table**: 

- Start with the given y-values as the first column of the table. This column corresponds to $f[x_i]$.
- Compute the subsequent columns using the formula:

$$
f[x_i, x_{i+1}, ..., x_{j}] = \frac{f[x_{i+1}, x_{i+2}, ..., x_{j}] - f[x_i, x_{i+1}, ..., x_{j-1}]}{x_j - x_i}
$$

- The topmost entry of each column gives the coefficient for the corresponding term in the Newton's polynomial.

3. **Construct the Newton's Polynomial**: 

- Start with the polynomial $P(x) = f[x_0]$.
- For each subsequent coefficient $f[x_0, x_1, ..., x_i]$, add the term $f[x_0, x_1, ..., x_i] \cdot (x - x_0) \cdot ... \cdot (x - x_{i-1})$ to the polynomial.

4. **Use the Newton's Polynomial for interpolation**: 

- To estimate a value at a point $x$, substitute $x$ into the Newton's polynomial and compute the result.

## Example

Let's illustrate this process with an example. Suppose we wish to interpolate a value at a point $x$ using the points (1, 2), (2, 3), (3, 5).

1. **Prepare the data**: Our points are already in order, so no additional preparation is needed.

2. **Compute the divided differences table**:

| x | f   | f, f   |
|---|-----|--------|
| 1 | 2   |        |
| 2 | 3   | 1      |
| 3 | 5   | 2      |

Here, the first column represents the y-values, the second column is the first-order divided differences, and so forth.

3. **Construct the Newton's Polynomial**: Using the coefficients from the divided differences table, the polynomial becomes:

$$
P(x) = 2 + 1 \cdot (x - 1) + 2 \cdot (x - 1) \cdot (x - 2)
$$

4. **Use the Newton's Polynomial for interpolation**: For example, to estimate the value at $x = 1.5$, we substitute $x = 1.5$ into the polynomial to get the estimate.

## Advantages

- It's a flexible method: adding an extra point doesn't require recalculating the entire interpolating polynomial.
- It yields a polynomial of minimum degree for a given dataset.

## Limitations

- Divided differences can become computationally intensive for a large number of points.
- Just like other interpolation methods, it might not give accurate results for extrapolation, or when the function is not well-behaved.
