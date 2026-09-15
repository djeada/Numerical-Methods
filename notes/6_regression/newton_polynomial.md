## Newton Polynomial Interpolation

Newton interpolation constructs a polynomial one term at a time. Its coefficients are divided differences, computed from the observed values and distances between nodes.

The new term added for each observation vanishes at all previously included nodes. This makes the form convenient when data arrive incrementally and allows efficient nested evaluation.

### Inputs and Goal

**Inputs:** $n+1$ finite pairs $(x_i,y_i)$ with distinct nodes and a query $x_*$. **Goal:** construct the degree-at-most-$n$ interpolating polynomial and evaluate it at $x_*$. Equal spacing is unnecessary. Sorting helps interpretation but is not required by divided differences.

This is an interpolation formula, not Newton’s iterative root-finding method. Compare the [Lagrange form](lagrange_polynomial_interpolation.md), which represents the same polynomial.

### Mathematical Formulation

A Newton interpolating polynomial for $n+1$ points $(x_i, y_i)$ can be written as:

$$
P(x) = f[x_0] + f[x_0,x_1](x - x_0) + f[x_0,x_1,x_2](x - x_0)(x - x_1) + \cdots + f[x_0,x_1,\ldots,x_n] (x - x_0)(x - x_1)\cdots(x - x_{n-1})
$$

where $f[x_0,x_1,\ldots,x_k]$ represents the $k$-th order divided difference of the function $f$ evaluated at points $x_0, x_1, \ldots, x_k$.

**Divided Differences**: For a set of points $(x_i,y_i)$, the divided differences are defined recursively:

**Zero-th order divided difference**:  

$$
f[x_i] = y_i
$$

**First order divided difference**:  

For $i \neq j$:

$$
f[x_i,x_j] = \frac{f[x_j] - f[x_i]}{x_j - x_i}
$$

**Higher order divided differences**:  

For $i < j < k$:

$$
f[x_i,x_j,x_k] = \frac{f[x_j,x_k] - f[x_i,x_j]}{x_k - x_i}
$$

In general, for $k\ge1$,

$$
f[x_i,\ldots,x_{i+k}] =
\frac{f[x_{i+1},\ldots,x_{i+k}]-f[x_i,\ldots,x_{i+k-1}]}{x_{i+k}-x_i}.
$$

### Derivation

Consider the cubic case for intuition (the process generalizes to higher degrees):

$$
P_3(x) = a_0 + (x-x_0)a_1 + (x-x_0)(x-x_1)a_2 + (x-x_0)(x-x_1)(x-x_2)a_3
$$

I. **At $x=x_0$**:

$$
P_3(x_0)=a_0 = y_0.
$$

II. **At $x=x_1$**:

Substitute $x_1$ into $P_3(x)$:

$$
y_1 = P_3(x_1) = a_0 + (x_1-x_0)a_1.
$$

Since $a_0 = y_0$:

$$
a_1 = \frac{y_1 - y_0}{x_1-x_0} = f[x_0,x_1]
$$

III. **At $x=x_2$**:

Substitute $x_2$:

$$
y_2 = P_3(x_2)= a_0 + (x_2-x_0)(a_1 + (x_2 - x_1)a_2)
$$

Rearranging terms leads to:

$$
a_2 = \frac{\frac{y_2 - y_0}{x_2 - x_0} - \frac{y_1 - y_0}{x_1 - x_0}}{x_2 - x_1} = f[x_0,x_1,x_2]
$$

Similarly, higher order coefficients ($a_3, a_4, \ldots$) can be obtained, which correspond to higher order divided differences. In general:

$$
a_k = f[x_0,x_1,\ldots,x_k]
$$

### Algorithm Steps

I. **Data Preparation**:  

Given $(x_0,y_0), (x_1,y_1),\ldots,(x_n,y_n)$ sorted so that $x_0 < x_1 < \cdots < x_n$.

II. **Compute Divided Differences**: 

- Start by listing the $y$-values as the zeroth order divided differences.
- Compute the first order divided differences:

$$
f[x_i,x_{i+1}] = \frac{y_{i+1}-y_i}{x_{i+1}-x_i} \quad \text{for } i=0 \ldots n-1
$$

- Use these to compute the second order divided differences, and so on, until you have $f[x_0,x_1,\ldots,x_n]$.

Usually, this is arranged in a **divided difference table**, where each column corresponds to divided differences of increasing order.

III. **Form the Newton Polynomial**:

Once you have all the divided differences:

$$
P(x) = f[x_0] + f[x_0,x_1](x - x_0) + f[x_0,x_1,x_2](x-x_0)(x-x_1) + \cdots
$$

IV. **Use the Polynomial for Interpolation**:

Substitute the desired $x$-value into $P(x)$ to get the interpolated $y$-value.

### Example

**Inputs:** $(1,2), (2,3), (3,5)$ and query $x_*=2.5$. **Goal:** construct the quadratic interpolant, evaluate it, and show how adding $(4,8)$ updates the calculation.

Zeroth order differences (just $y$-values):

$$
f[x_0]=2, \quad f[x_1]=3, \quad f[x_2]=5
$$

First order differences:

$$
f[x_0,x_1] = \frac{3-2}{2-1}=1, \quad f[x_1,x_2] = \frac{5-3}{3-2}=2
$$

Second order difference:

$$
f[x_0,x_1,x_2] = \frac{f[x_1,x_2] - f[x_0,x_1]}{x_2 - x_0} = \frac{2-1}{3-1}=\frac{1}{2}=0.5
$$

Arranging these results in a **divided difference table**:

| $i$ | $x_i$ | $y_i$ | $f[x_i,x_{i+1}]$ | $f[x_i,x_{i+1},x_{i+2}]$ |
| --- | --- | --- | --- | --- |
| 0 | 1 | 2 | 1 | 0.5 |
| 1 | 2 | 3 | 2 | |
| 2 | 3 | 5 | | |

Each entry in a difference column is computed from consecutive entries in the previous column, divided by the span of its nodes. The first row supplies coefficients $2,1,0.5$.

The Newton polynomial is:

$$
P(x)=f[x_0] + f[x_0,x_1](x - x_0) + f[x_0,x_1,x_2](x - x_0)(x - x_1)
$$

Substitute the values:

$$
P(x)=2 + (1)(x - 1) + (0.5)(x - 1)(x - 2)
$$

**Verification at the data points**:

$$
P(1) = 2 + 1 \cdot (1-1) + 0.5 \cdot (1-1)(1-2) = 2 + 0 + 0 = 2 \checkmark
$$

$$
P(2) = 2 + 1 \cdot (2-1) + 0.5 \cdot (2-1)(2-2) = 2 + 1 + 0 = 3 \checkmark
$$

$$
P(3) = 2 + 1 \cdot (3-1) + 0.5 \cdot (3-1)(3-2) = 2 + 2 + 1 = 5 \checkmark
$$

**Evaluation at a query point** $x = 2.5$:

$$
P(2.5) = 2 + 1 \cdot (2.5 - 1) + 0.5 \cdot (2.5 - 1)(2.5 - 2) = 2 + 1.5 + 0.5 \cdot 1.5 \cdot 0.5 = 2 + 1.5 + 0.375 = 3.875
$$

**Nested (Horner) form** for more efficient evaluation:

$$
P(x) = 2 + (x - 1)\bigl[1 + 0.5\,(x - 2)\bigr]
$$

This rewrites the polynomial so that evaluation requires only $O(n)$ multiplications instead of $O(n^2)$, and corresponds to the general nested form $P(x) = a_0 + (x - x_0)(a_1 + (x - x_1)(a_2 + \cdots))$.

**Adding a fourth point incrementally**: Suppose we now add the point $(4,8)$. Compute one new divided difference at each order (a new diagonal in the table), retaining all existing entries:

$$
f[x_2,x_3] = \frac{8 - 5}{4 - 3} = 3
$$

$$
f[x_1,x_2,x_3] = \frac{f[x_2,x_3] - f[x_1,x_2]}{x_3 - x_1} = \frac{3 - 2}{4 - 2} = 0.5
$$

$$
f[x_0,x_1,x_2,x_3] = \frac{f[x_1,x_2,x_3] - f[x_0,x_1,x_2]}{x_3 - x_0} = \frac{0.5 - 0.5}{4 - 1} = 0
$$

The new term is $0 \cdot (x-1)(x-2)(x-3) = 0$, so the polynomial is unchanged. The cubic coefficient is zero, confirming the data fits a quadratic exactly.

This matches exactly the polynomial you would get if you used Lagrange or any other method for these points.

### Advantages

- When a new data point is added, you can perform **incremental** updating of the polynomial by computing a new set of divided differences without starting over from scratch.
- Newton’s form produces the same degree-at-most-$n$ polynomial as Lagrange interpolation on the same $n+1$ nodes. Piecewise linear and spline interpolants are generally different.
- The nested form of Newton’s polynomial, such as $P(x) = a_0 + (x - x_0)(a_1 + (x - x_1)(a_2 + \cdots ))$, avoids explicitly expanding powers and evaluates in $O(n)$ work. It does not eliminate sensitivity to node placement or rounding in divided differences.

### Error Bound

If the data points are sampled from a function $f \in C^{n+1}[a,b]$, the interpolation error at any point $x$ can be expressed using divided differences:

$$
f(x) - P(x) = f[x_0, x_1, \ldots, x_n, x] \prod_{i=0}^{n}(x - x_i)
$$

Since the $(n+1)$-th order divided difference of $f$ satisfies $f[x_0,\ldots,x_n,x] = \frac{f^{(n+1)}(\xi)}{(n+1)!}$ for some $\xi$ in the interval spanned by the points, this reduces to the standard remainder:

$$
f(x) - P(x) = \frac{f^{(n+1)}(\xi)}{(n+1)!}\prod_{i=0}^{n}(x - x_i)
$$

This connects divided differences directly to the interpolation error and shows that the error depends on both the smoothness of $f$ and how close $x$ is to the data points.

### Limitations

- As the number of data points grows large, the computation and maintenance of higher order divided differences can become **computationally** intensive.
- Like any polynomial interpolation, Newton’s polynomial can suffer from Runge’s **phenomenon** if the points are not well-distributed, causing oscillations in the polynomial approximation.
- Divided differences can become numerically **sensitive** when data points are closely spaced, since the denominator $x_j - x_i$ becomes small, amplifying rounding errors in floating-point arithmetic.

### Cost and Evaluation Checks

Building the full divided-difference table takes $O(n^2)$ work and storage; an in-place coefficient array reduces storage to $O(n)$. With the existing full table, adding one node takes $O(n)$ additional work. Evaluate in nested form starting with $v=a_n$ and applying $v=a_k+(x_*-x_k)v$ for $k=n-1,\ldots,0$.

Verify the polynomial at every input node. An out-of-range query is extrapolation and needs separate justification. The remainder above assumes an interval containing both the nodes and query; at a node the interpolation error is zero directly, without using a divided difference with a repeated argument.
