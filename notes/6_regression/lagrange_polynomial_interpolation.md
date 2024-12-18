## Lagrange Polynomial Interpolation

Lagrange Polynomial Interpolation is a widely used technique for determining a polynomial that passes exactly through a given set of data points. Suppose we have a set of $(n+1)$ data points $(x_0, y_0), (x_1, y_1), \ldots, (x_n, y_n)$ where all $x_i$ are distinct. The aim is to find a polynomial $L(x)$ of degree at most $n$ such that:

$$L(x_i) = y_i, \quad \text{for} \; i=0,1,\ldots,n.$$

Instead of solving a system of linear equations (as would be required if we used a general polynomial form), Lagrange interpolation provides a direct formula for the interpolating polynomial in terms of **Lagrange basis polynomials**. This approach is conceptually straightforward and does not require forming and solving large linear systems.

**Conceptual Illustration**:

Imagine that you have three points $(x_0, y_0), (x_1, y_1), (x_2, y_2)$. The Lagrange form builds a polynomial that goes exactly through these points. Each Lagrange basis polynomial $P_i(x)$ is constructed to be zero at all $x_j$ except $x_i$. By taking a suitable linear combination of these basis polynomials with weights given by $y_i$, we get an interpolating polynomial $L(x)$.

![Lagrange Polynomial Plot](https://user-images.githubusercontent.com/37275728/188961030-379f428f-a0c4-403a-a6bd-e4a5393f38e0.png)

The Lagrange polynomial passing through all these points is unique and matches every given data point exactly.

### Mathematical Formulation

Given $(n+1)$ distinct points $(x_0, y_0), (x_1, y_1), \ldots, (x_n, y_n)$, the Lagrange interpolation polynomial is constructed as follows:

I. **Lagrange Basis Polynomials:**

For each $i$ in $\{0,1,\ldots,n\}$, define the $i$-th Lagrange basis polynomial $P_i(x)$ by:

$$P_i(x) = \prod_{\substack{j=0 \\ j \neq i}}^{n} \frac{x - x_j}{x_i - x_j}.$$

Notice that $P_i(x_k) = \delta_{ik}$, where $\delta_{ik}$ is the Kronecker delta. In other words:

$$P_i(x_k) =
\begin{cases}
1 & \text{if } i=k,\\[6pt]
0 & \text{if } i \neq k.
\end{cases}$$

II. **Lagrange Interpolating Polynomial:**

Once we have the $P_i(x)$, the interpolating polynomial $L(x)$ is given by:

$$L(x) = \sum_{i=0}^{n} y_i P_i(x).$$

By construction, $L(x_j) = y_j$ for all $j$. The degree of $L(x)$ is at most $n$.

### Derivation

Starting from the requirement that $L(x)$ matches all data points:

$$L(x_i) = y_i \quad \text{for } i=0,1,\ldots,n.$$

Consider polynomials $P_i(x)$ defined as:

$$P_i(x) = \prod_{\substack{j=0 \\ j \neq i}}^{n} \frac{x - x_j}{x_i - x_j}.$$

This construction ensures that for each fixed $i$:

- When $x = x_i$, the numerator in $P_i(x)$ contains all factors $(x_i - x_j)$ for $j \neq i$, which exactly cancel with the denominator $(x_i - x_j)$. Thus, $P_i(x_i)=1$.
- For $x = x_k$ with $k \neq i$, the factor $(x_k - x_k)$ in the numerator makes $P_i(x_k)=0$.

Hence $P_i(x)$ acts like a "selector" polynomial that equals 1 at $x_i$ and 0 at every other $x_j$.

To construct $L(x)$ that passes through all points, we form:

$$L(x) = \sum_{i=0}^{n} y_i P_i(x).$$

Evaluating at $x = x_k$:

$$L(x_k) = \sum_{i=0}^{n} y_i P_i(x_k) = y_k,$$

since $P_k(x_k)=1$ and $P_i(x_k)=0$ for $i \neq k$.

### Algorithm Steps

I. **Input**: 

A set of $(n+1)$ points $(x_i,y_i)$ with all $x_i$ distinct.

II. **Initialization**:

Set $L(x)=0$.

III. **Compute Lagrange Basis Polynomials**:

For each $i=0,1,\ldots,n$:

- Initialize $P_i(x)=1$.
- For each $j=0,1,\ldots,n$ with $j \neq i$:

$$P_i(x) = P_i(x) \cdot \frac{x - x_j}{x_i - x_j}.$$

IV. **Form the Interpolating Polynomial**:

Compute:

$$L(x) = \sum_{i=0}^{n} y_i P_i(x).$$

**Result**:

The polynomial $L(x)$ is the desired Lagrange interpolating polynomial. To interpolate at any $x$, just evaluate $L(x)$.

### Example

**Given Points**:

Let’s consider three points:

$$A(-1,1), \quad B(2,3), \quad C(3,5).$$

We have $n=2$ (since there are 3 points), and thus the polynomial $L(x)$ will be of degree at most 2.

**Compute $P_0(x)$** for the point $A(-1, 1)$:

$$P_0(x) = \frac{(x - x_1)(x - x_2)}{(x_0-x_1)(x_0-x_2)} = \frac{(x - 2)(x - 3)}{(-1 -2)(-1 -3)} = \frac{(x - 2)(x - 3)}{(-3)(-4)} = \frac{(x - 2)(x - 3)}{12}.$$

**Compute $P_1(x)$** for the point $B(2,3)$:

$$P_1(x) = \frac{(x - x_0)(x - x_2)}{(x_1 - x_0)(x_1 - x_2)} = \frac{(x +1)(x - 3)}{(2 + 1)(2 - 3)} = \frac{(x+1)(x - 3)}{3 \cdot (-1)} = -\frac{(x+1)(x-3)}{3}.$$

**Compute $P_2(x)$** for the point $C(3,5)$:

$$P_2(x) = \frac{(x - x_0)(x - x_1)}{(x_2 - x_0)(x_2 - x_1)} = \frac{(x +1)(x - 2)}{(3 + 1)(3 - 2)} = \frac{(x+1)(x - 2)}{4}.$$

Now, plug these into $L(x)$:

$$L(x) = y_0 P_0(x) + y_1 P_1(x) + y_2 P_2(x)$$

Substitute $(y_0, y_1, y_2) = (1,3,5)$:

$$L(x) = 1 \cdot \frac{(x - 2)(x - 3)}{12} + 3 \cdot \left(-\frac{(x+1)(x - 3)}{3}\right) + 5 \cdot \frac{(x+1)(x-2)}{4}.$$

This polynomial will exactly fit the three given points.

### Advantages

I. **Exact Fit:**  

The Lagrange interpolation polynomial passes through all given data points exactly. There is no approximation error at these nodes.

II. **No Linear System Needed:**  

Unlike other polynomial interpolation techniques that require solving a system of equations, Lagrange interpolation provides a direct formula.

III. **Simplicity of Form:**  

The formula for the interpolating polynomial is explicit and easy to implement.

IV. **Flexibility:**  

Works for any set of points with distinct $x_i$.

### Limitations

I. **Runge’s Phenomenon:**  

For a large number of interpolation points, Lagrange interpolation may cause oscillations between the points, especially if the points are unevenly spaced.

II. **Recalculation for Added Points:**  

If a new point is added, the entire polynomial must be recomputed from scratch, unlike some other forms (e.g., Newton’s divided differences) that allow incremental updates more easily.

III. **Computational Cost:**  

Evaluating Lagrange polynomials directly can be computationally intensive for large $n$ due to the product terms, though this can be mitigated with more efficient evaluation strategies.
