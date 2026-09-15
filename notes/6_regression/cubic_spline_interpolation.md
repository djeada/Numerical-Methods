## Cubic Spline Interpolation

A cubic spline joins low-degree polynomial pieces into one interpolating curve. Adjacent pieces have matching values, first derivatives, and second derivatives at their shared nodes. This gives a smooth curve without using one high-degree polynomial over the whole interval.

Smoothness does not guarantee monotonicity or prevent overshoot. Endpoint conditions are part of the model and can affect the entire curve.

### Inputs and Goal

**Inputs:** at least two finite data pairs with strictly increasing nodes, a query $x_*$, and two endpoint conditions. **Goal:** build the piecewise cubic interpolant and evaluate the segment containing $x_*$. Equal spacing is not required.

This note derives the natural spline, whose endpoint second derivatives vanish. Clamped splines instead prescribe endpoint slopes; periodic and not-a-knot conditions define other splines. A natural condition does not mean the endpoint slope is zero.

### Mathematical Formulation

We start with a set of $n+1$ data points:

$$
(x_0, y_0), (x_1, y_1), \ldots, (x_n, y_n)
$$

with $x_0 < x_1 < \cdots < x_n$.

A **cubic spline** is a function $S(x)$ defined piecewise on each interval $[x_i, x_{i+1}]$, $i = 0, 1, \ldots, n-1$:

$$
S_i(x) = a_i + b_i(x - x_i) + c_i(x - x_i)^2 + d_i(x - x_i)^3
$$

where $a_i, b_i, c_i, d_i$ are the unknown coefficients for the cubic polynomial on the interval $[x_i, x_{i+1}]$.

**Key Requirements:**

I. **Interpolation Condition:**

Each segment must pass through the given data points:

$$
S_i(x_i) = y_i, \quad S_i(x_{i+1}) = y_{i+1}.
$$

II. **Continuity of the Spline:**

The function $S(x)$ must be continuous at the interior points:

$$
S_i(x_{i+1}) = S_{i+1}(x_{i+1}).
$$

III. **Continuity of First Derivative:**

The first derivatives of adjacent segments must match:

$$
S_i'(x_{i+1}) = S_{i+1}'(x_{i+1}).
$$

IV. **Continuity of Second Derivative:**

Similarly, the second derivatives must also be continuous:

$$
S_i''(x_{i+1}) = S_{i+1}''(x_{i+1}).
$$

V. **Boundary Conditions:**

For a **natural cubic spline**, the second derivatives at the boundaries are set to zero:

$$
S_0''(x_0) = 0, \quad S_{n-1}''(x_n) = 0.
$$

For $n$ intervals there are $4n$ coefficients: the $2n$ endpoint interpolation conditions, $2(n-1)$ derivative matching conditions, and two boundary conditions determine them. Function continuity is already implied by matching the shared data values; it is not an extra independent condition.

### Derivation of the Coefficients

I. **Step Sizes and Secant Slopes:**

Let the spacing between consecutive points be:

$$
h_i = x_{i+1} - x_i, \quad i=0,1,\ldots,n-1
$$

II. **Formulation in Terms of Second Derivatives:**

Let $M_i = S''(x_i)$. If we can determine $M_i$ for all $i$, we can write each piece $S_i(x)$ as:

$$
\begin{aligned}
S_i(x) ={}& M_{i}\frac{(x_{i+1}-x)^3}{6h_i} + M_{i+1}\frac{(x - x_i)^3}{6h_i} \\
&+ \left(y_i - \frac{M_i h_i^2}{6}\right)\frac{x_{i+1}-x}{h_i} \\
&+ \left(y_{i+1} - \frac{M_{i+1}h_i^2}{6}\right)\frac{x - x_i}{h_i}.
\end{aligned}
$$

This form matches the endpoint values and prescribed endpoint second derivatives of each piece. The system below enforces first-derivative continuity, and the endpoint choices impose the boundary conditions.

III. **System of Equations for $M_i$:**

Requiring continuity of the first derivative at each interior knot ($S_{i-1}'(x_i) = S_i'(x_i)$) and substituting the second-derivative form from step II yields a tridiagonal system for the unknown $M_i$. For natural splines the boundary values are:

$$
M_0 = 0, \quad M_n = 0.
$$

The remaining $M_i$'s (for $i=1,\ldots,n-1$) satisfy:

$$
h_{i-1}M_{i-1} + 2(h_{i-1}+h_i)M_i + h_i M_{i+1} = 6\left(\frac{y_{i+1}-y_i}{h_i} - \frac{y_i - y_{i-1}}{h_{i-1}}\right)
$$

IV. **Once $M_i$ are determined**, the coefficients $a_i, b_i, c_i, d_i$ of the cubic spline in the standard form:

$$
S_i(x) = a_i + b_i(x - x_i) + c_i(x - x_i)^2 + d_i(x - x_i)^3
$$

can be read off by expanding the second-derivative form from step II about $x = x_i$:

$$
a_i = y_i
$$

$$
b_i = \frac{y_{i+1}-y_i}{h_i} - \frac{h_i}{6}(2M_i + M_{i+1})
$$

$$
c_i = \frac{M_i}{2}
$$

$$
d_i = \frac{M_{i+1} - M_i}{6h_i}
$$

One can verify that $S_i''(x_i) = 2c_i = M_i$ and $S_i''(x_{i+1}) = 2c_i + 6d_i h_i = M_{i+1}$, confirming consistency with the definition $M_i = S''(x_i)$.

### Algorithm Steps

I. **Data Preparation:**

- Sort the data points $(x_i,y_i)$ in ascending order by $x_i$.
- Compute $h_i = x_{i+1}-x_i$ for $i=0,\ldots,n-1$.

II. **Form the Equations:**

Set up the linear system to solve for the second derivatives $M_i$. For a natural spline:

$$
M_0 = 0, \quad M_n = 0
$$

For $i=1,\ldots,n-1$:

$$
h_{i-1}M_{i-1} + 2(h_{i-1}+h_i)M_i + h_i M_{i+1} = 6\left(\frac{y_{i+1}-y_i}{h_i} - \frac{y_i - y_{i-1}}{h_{i-1}}\right)
$$

III. **Solve the Tridiagonal System:**

Use the Thomas algorithm (tridiagonal matrix algorithm) to solve for $M_1, M_2,\ldots,M_{n-1}$. Because the coefficient matrix is tridiagonal, the Thomas algorithm solves the system in $O(n)$ time using a single forward-elimination and back-substitution pass.

IV. **Calculate the Coefficients:**

With $M_i$ known, compute for each segment $i = 0, 1, \ldots, n-1$:

$$
a_i = y_i, \quad b_i = \frac{y_{i+1}-y_i}{h_i} - \frac{h_i}{6}(2M_i + M_{i+1}), \quad c_i = \frac{M_i}{2}, \quad d_i = \frac{M_{i+1}-M_i}{6h_i}
$$

V. **Interpolation:**

For a given $x$, find the interval $[x_i, x_{i+1}]$ such that $x_i \leq x \leq x_{i+1}$ and evaluate:

$$
S_i(x) = a_i + b_i(x - x_i) + c_i(x - x_i)^2 + d_i(x - x_i)^3
$$

### Example

**Inputs:** $(0,0),\;(1,0.5),\;(2,0)$, natural endpoint conditions, and query $x_*=0.5$. **Goal:** find both cubic pieces, verify their joins, and estimate the value at the query.

**Setup:**

- $h_0 = x_1 - x_0 = 1,\quad h_1 = x_2 - x_1 = 1$.
- Natural boundary conditions: $M_0 = 0,\; M_2 = 0$.

**Solving for $M_1$:**

The tridiagonal equation for $i=1$:

$$
h_0 M_0 + 2(h_0+h_1)M_1 + h_1 M_2 = 6\left(\frac{y_2-y_1}{h_1} - \frac{y_1-y_0}{h_0}\right)
$$

$$
1\cdot 0 + 2(1+1)M_1 + 1\cdot 0 = 6\left(\frac{0-0.5}{1} - \frac{0.5-0}{1}\right) = 6(-0.5 - 0.5) = -6
$$

$$
4M_1 = -6 \implies M_1 = -1.5
$$

**Segment 0** ($[x_0,x_1] = [0,1]$):

$$
a_0 = y_0 = 0
$$

$$
b_0 = \frac{y_1 - y_0}{h_0} - \frac{h_0}{6}(2M_0 + M_1) = \frac{0.5}{1} - \frac{1}{6}(0 + (-1.5)) = 0.5 + 0.25 = 0.75
$$

$$
c_0 = \frac{M_0}{2} = 0
$$

$$
d_0 = \frac{M_1 - M_0}{6h_0} = \frac{-1.5}{6} = -0.25
$$

$$
S_0(x) = 0.75x - 0.25x^3
$$

**Segment 1** ($[x_1,x_2] = [1,2]$):

$$
a_1 = y_1 = 0.5
$$

$$
b_1 = \frac{y_2 - y_1}{h_1} - \frac{h_1}{6}(2M_1 + M_2) = \frac{-0.5}{1} - \frac{1}{6}(2(-1.5)+0) = -0.5 + 0.5 = 0
$$

$$
c_1 = \frac{M_1}{2} = -0.75
$$

$$
d_1 = \frac{M_2 - M_1}{6h_1} = \frac{1.5}{6} = 0.25
$$

$$
S_1(x) = 0.5 - 0.75(x-1)^2 + 0.25(x-1)^3
$$

**Verification at the knots:**

| Check | Value |
|---|---|
| $S_0(0) = 0$ | $= y_0$ ✓ |
| $S_0(1) = 0.75 - 0.25 = 0.5$ | $= y_1$ ✓ |
| $S_1(1) = 0.5$ | $= y_1$ ✓ |
| $S_1(2) = 0.5 - 0.75 + 0.25 = 0$ | $= y_2$ ✓ |
| $S_0'(x) = 0.75 - 0.75x^2,\; S_0'(1) = 0$ | First derivative continuous ✓ |
| $S_1'(x) = -1.5(x-1)+0.75(x-1)^2,\; S_1'(1) = 0$ | ✓ |
| $S_0''(x) = -1.5x,\; S_0''(1) = -1.5$ | Second derivative continuous ✓ |
| $S_1''(x) = -1.5+1.5(x-1),\; S_1''(1) = -1.5$ | ✓ |

**Evaluating at a query point $x = 0.5$:**

Since $0.5 \in [0,1]$, we use $S_0$:

$$
S_0(0.5) = 0.75(0.5) - 0.25(0.5)^3 = 0.375 - 0.03125 = 0.34375
$$

### Advantages

- Splines ensure **smoothness** by producing curves with continuous first and second derivatives, leading to a natural and visually appealing fit.
- Low-degree pieces often reduce the large oscillations seen with a single high-degree polynomial, although overshoot remains possible.
- Evaluation uses only one cubic segment after solving for the coefficients. However, changing a data value can change all segments because the coefficient system is globally coupled.

### Limitations

- The method involves **complexity**, as it requires setting up and solving a linear system of equations, making it more complicated than simpler interpolation techniques.
- **Computational cost** is higher than methods like linear interpolation, particularly for large datasets with many control points.
- **Boundary conditions** must be specified (e.g., natural, clamped) to define the behavior at the endpoints, which can influence the overall fit of the spline.

### Boundary and Numerical Checks

For the example, $S_0''(0)=0$ and $S_1''(2)=-1.5+1.5=0$, verifying the natural conditions as well as the joins checked above. With only two nodes, there are no interior second derivatives to solve for; the natural spline reduces to the line through the two values.

Locate the segment by binary search in $O(\log n)$ work, then evaluate its cubic in constant work using nested multiplication. Queries outside the knot range require an explicit extrapolation policy. Cubic splines do not generally preserve monotonicity or positivity.

For an independent numerical comparison, use [SciPy's CubicSpline](https://docs.scipy.org/doc/scipy/reference/generated/scipy.interpolate.CubicSpline.html) with `bc_type="natural"`. Its default is `"not-a-knot"`, which defines a different interpolant.
