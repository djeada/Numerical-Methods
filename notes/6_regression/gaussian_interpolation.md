## Gauss Central-Difference Interpolation

Gauss's forward and backward formulas construct a polynomial through equally spaced data, starting near the middle of the table. This note uses “Gaussian interpolation” to mean these **Gauss central-difference formulas**, not interpolation with a Gaussian radial basis function.

The construction is [Newton polynomial interpolation](newton_polynomial.md) with a different node order. When all nodes are included, Gauss, Newton, and Lagrange forms give the same polynomial in exact arithmetic. A central ordering can be convenient when using a small subset of nearby nodes; it does not guarantee smaller error than another method.

### Inputs and Goal

**Inputs:** $n+1$ values $(x_i,y_i)$ with $x_i=x_0+ih$, constant $h>0$, and a query $x_*$ in $[x_0,x_n]$. **Goal:** evaluate the polynomial interpolant at $x_*$, either using all nodes or an explicitly chosen lower order $k$.

Check that nodes are distinct and equally spaced. For unequal spacing, use divided differences directly.

Define the ordinary forward-difference table by

$$
\Delta^0y_i=y_i,
\qquad\Delta^ky_i=\Delta^{k-1}y_{i+1}-\Delta^{k-1}y_i,
\quad 0\le i\le n-k.
$$

For a reference node $x_m$, let $t=(x_*-x_m)/h$. The word “central” describes the order in which the table is used; the table entries themselves are forward differences.

### Derivation from Newton's Formula

For $k+1$ consecutive equally spaced nodes,

$$
f[x_b,\ldots,x_{b+k}]=\frac{\Delta^ky_b}{k!h^k}.
$$

Divided differences do not depend on the ordering of those nodes. In Newton's formula, each degree-$k$ term multiplies this coefficient by the $k$ factors belonging to the previously included nodes. Each factor is $h(t-j)$, where $j$ is that node's offset from $m$. The powers of $h$ cancel.

**Forward ordering:** $m,m+1,m-1,m+2,m-2,\ldots$.

For example, the first three Newton products are $ht$, $h^2t(t-1)$, and $h^3t(t-1)(t+1)$. This gives

$$
\begin{aligned}
P(x_*)={}&y_m+t\Delta y_m
+\frac{t(t-1)}{2!}\Delta^2y_{m-1}\\
&+\frac{(t+1)t(t-1)}{3!}\Delta^3y_{m-1}
+\frac{(t+1)t(t-1)(t-2)}{4!}\Delta^4y_{m-2}+\cdots.
\end{aligned}
$$

**Backward ordering:** $m,m-1,m+1,m-2,m+2,\ldots$.

The first products instead use $ht$, $h^2t(t+1)$, and $h^3t(t+1)(t-1)$:

$$
\begin{aligned}
P(x_*)={}&y_m+t\Delta y_{m-1}
+\frac{(t+1)t}{2!}\Delta^2y_{m-1}\\
&+\frac{(t+1)t(t-1)}{3!}\Delta^3y_{m-2}
+\frac{(t+2)(t+1)t(t-1)}{4!}\Delta^4y_{m-2}+\cdots.
\end{aligned}
$$

Only include terms for which the required table entry exists. For order $k\ge1$, the general term is $c_k(t)\Delta^ky_{b_k}$:

| Form | Base index $b_k$ | Coefficient $c_k(t)$ |
| --- | --- | --- |
| Forward | $m-\lfloor k/2\rfloor$ | $\displaystyle\frac{1}{k!}\prod_{j=-\lfloor(k-1)/2\rfloor}^{\lfloor k/2\rfloor}(t-j)$ |
| Backward | $m-\lceil k/2\rceil$ | $\displaystyle\frac{1}{k!}\prod_{j=-\lfloor k/2\rfloor}^{\lfloor(k-1)/2\rfloor}(t-j)$ |

The index check is $0\le b_k$ and $b_k+k\le n$.

### Choosing the Central Row Correctly

To use **all** $n+1$ nodes, choose

$$
m_F=\lfloor n/2\rfloor\quad\text{for forward},
\qquad m_B=\lceil n/2\rceil\quad\text{for backward}.
$$

These are the same for an odd number of observations, but different for an even number. For four nodes indexed $0,1,2,3$, forward starts at 1 and visits $1,2,0,3$; backward starts at 2 and visits $2,1,3,0$. Starting backward at 1 would request a nonexistent node $-1$ before reaching all observations.

A practical rule, also used by the repository implementation, is:

1. Compute $m_F=\lfloor n/2\rfloor$.
2. If $x_*\ge x_{m_F}$, use forward with $m=m_F$.
3. Otherwise use backward with $m=m_B$.
4. Recompute $t=(x_*-x_m)/h$ using the selected row.
5. Build the difference table and sum orders $0$ through $n$, or through a stated truncation order.

The sign rule is a convenience; either full-order form gives the same polynomial when indexed correctly.

### Worked Example: Five Observations

**Inputs:** the following table, spacing $h=1$, query $x_*=1.5$. **Goal:** compute both the cubic truncation and the full degree-at-most-four interpolant.

#### Step 1: Build the Difference Table

| $i$ | $x_i$ | $y_i$ | $\Delta y_i$ | $\Delta^2y_i$ | $\Delta^3y_i$ | $\Delta^4y_i$ |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 0 | 2.0 | 1.5 | 0.0 | -0.7 | 0.8 |
| 1 | 1 | 3.5 | 1.5 | -0.7 | 0.1 | |
| 2 | 2 | 5.0 | 0.8 | -0.6 | | |
| 3 | 3 | 5.8 | 0.2 | | | |
| 4 | 4 | 6.0 | | | | |

For example,

$$
\Delta y_2=5.8-5.0=0.8,
\quad\Delta^2y_1=0.8-1.5=-0.7,
$$

$$
\Delta^3y_0=-0.7-0=-0.7,
\quad\Delta^4y_0=0.1-(-0.7)=0.8.
$$

#### Step 2: Choose the Origin and Form

Here $n=4$, so $m_F=m_B=2$. Since $1.5<2$, use backward with

$$
t=\frac{1.5-2}{1}=-0.5.
$$

#### Step 3: Calculate Each Term

| Order | Substitution | Term | Running sum |
| --- | --- | --- | --- |
| 0 | $y_2$ | 5 | 5 |
| 1 | $(-0.5)(1.5)$ | -0.75 | 4.25 |
| 2 | $((0.5)(-0.5)/2)(-0.7)$ | 0.0875 | 4.3375 |
| 3 | $((0.5)(-0.5)(-1.5)/6)(-0.7)$ | -0.04375 | 4.29375 |
| 4 | $((1.5)(0.5)(-0.5)(-1.5)/24)(0.8)$ | 0.01875 | 4.3125 |

Thus the cubic truncation is $P_3(1.5)=4.29375$ and the full interpolant gives $P_4(1.5)=4.3125$. Keep all these digits until the final result; prematurely rounding terms obscures the sum.

#### Step 4: Verify Using an Independent Node Order

Newton's forward formula starting at $x_0=0$ uses $u=1.5$ and the top row of the table:

$$
\begin{aligned}
P_4(1.5)&=2+1.5(1.5)+\frac{1.5(0.5)}{2}(0)\\
&\quad+\frac{1.5(0.5)(-0.5)}{6}(-0.7)
+\frac{1.5(0.5)(-0.5)(-1.5)}{24}(0.8)\\
&=2+2.25+0+0.04375+0.01875=4.3125.
\end{aligned}
$$

Using only the two neighboring values gives a [linear estimate](linear_interpolation.md) of $(3.5+5)/2=4.25$. The difference $0.0625$ reflects the choice of interpolant. Without information about the underlying function, it does not establish which estimate is more accurate.

### Error, Cost, and Limitations

For a degree-$k$ interpolant using nodes $x_{i_0},\ldots,x_{i_k}$, if $f$ has a continuous $(k+1)$st derivative on an interval containing those nodes and the query,

$$
f(x_*)-P_k(x_*)=
\frac{f^{(k+1)}(\xi)}{(k+1)!}
\prod_{j=0}^k(x_*-x_{i_j})
$$

for some $\xi$ in that interval. A bound needs a bound on the derivative and on this product. Central ordering does not minimize the error for every function. A small next term alone is not a reliable stopping guarantee: later differences may be large even if an earlier one vanishes.

Building the full table takes $O(n^2)$ work and storage. Evaluation can take $O(n)$ work by updating the product and factorial incrementally. Repeated subtraction can amplify noise and roundoff in higher differences. As with any global polynomial on equally spaced nodes, high degree can cause oscillations. For many observations, consider a [piecewise cubic spline](cubic_spline_interpolation.md).
