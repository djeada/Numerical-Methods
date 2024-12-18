## Cubic Spline

Cubic spline interpolation is a refined mathematical tool frequently used within numerical analysis. It's an approximation technique that employs piecewise cubic polynomials, collectively forming a cubic spline. These cubic polynomials are specifically engineered to pass through a defined set of data points, hence striking a balance between overly simple (like linear) and overly intricate (like high-degree polynomial) interpolations.

**Conceptual Illustration (Not Removing the Plot)**:

Imagine you have a set of points on a 2D plane. A cubic spline will "thread" through these points, forming a smooth curve that does not exhibit sudden bends or wiggles:

![Screenshot from 2022-09-07 21-24-04](https://user-images.githubusercontent.com/37275728/188960890-781f5947-1d8c-40bc-aba7-91728024eabe.png)

The spline is constructed from piecewise cubic segments that meet at the data points with continuous first and second derivatives, ensuring a visually natural and mathematically smooth interpolation.

### Mathematical Formulation

We start with a set of $n+1$ data points:

$$(x_0, y_0), (x_1, y_1), \ldots, (x_n, y_n)$$

with $x_0 < x_1 < \cdots < x_n$.

A **cubic spline** is a function $S(x)$ defined piecewise on each interval $[x_i, x_{i+1}]$, $i = 0, 1, \ldots, n-1$:

$$S_i(x) = a_i + b_i(x - x_i) + c_i(x - x_i)^2 + d_i(x - x_i)^3$$

where $a_i, b_i, c_i, d_i$ are the unknown coefficients for the cubic polynomial on the interval $[x_i, x_{i+1}]$.

**Key Requirements:**

I. **Interpolation Condition:**

Each segment must pass through the given data points:

$$S_i(x_i) = y_i, \quad S_i(x_{i+1}) = y_{i+1}.$$

II. **Continuity of the Spline:**

The function $S(x)$ must be continuous at the interior points:

$$S_i(x_{i+1}) = S_{i+1}(x_{i+1}).$$

III. **Continuity of First Derivative:**

The first derivatives of adjacent segments must match:

$$S_i'(x_{i+1}) = S_{i+1}'(x_{i+1}).$$

IV. **Continuity of Second Derivative:**

Similarly, the second derivatives must also be continuous:

$$S_i''(x_{i+1}) = S_{i+1}''(x_{i+1}).$$

V. **Boundary Conditions:**

For a **natural cubic spline**, the second derivatives at the boundaries are set to zero:

$$S_0''(x_0) = 0, \quad S_{n-1}''(x_n) = 0.$$

These conditions lead to a system of linear equations that determine the coefficients $a_i, b_i, c_i,$ and $d_i$.

### Derivation of the Coefficients

I. **Divided Differences and Step Sizes:**

Let the spacing between consecutive points be:

$$h_i = x_{i+1} - x_i, \quad i=0,1,\ldots,n-1$$

II. **Formulation in Terms of Second Derivatives:**

Let $M_i = S''(x_i)$. If we can determine $M_i$ for all $i$, we can write each piece $S_i(x)$ as:

$$S_i(x) = M_{i}\frac{(x_{i+1}-x)^3}{6h_i} + M_{i+1}\frac{(x - x_i)^3}{6h_i} 

+ \left(y_i - \frac{M_i h_i^2}{6}\right)\frac{x_{i+1}-x}{h_i} 

+ \left(y_{i+1} - \frac{M_{i+1}h_i^2}{6}\right)\frac{x - x_i}{h_i}.$$

This form ensures the correct boundary conditions and continuity of derivatives once $M_i$ are found.

III. **System of Equations for $M_i$:**

Using the conditions for continuity of first and second derivatives, one obtains a tridiagonal system of equations in terms of the unknown second derivatives $M_i$. For natural splines, we have:

$$M_0 = 0, \quad M_n = 0.$$

The remaining $M_i$'s (for $i=1,\ldots,n-1$) are found by solving this system:

$$\mu_i M_{i-1} + 2M_i + \lambda_i M_{i+1} = d_i,$$
where $\mu_i, \lambda_i, d_i$ depend on the data points and $h_i$.

IV. **Once $M_i$ are determined**, the coefficients $a_i, b_i, c_i, d_i$ of the cubic spline in the standard form:

$$S_i(x) = a_i + b_i(x - x_i) + c_i(x - x_i)^2 + d_i(x - x_i)^3$$

can be computed directly:

$$a_i = y_i$$

$$b_i = \frac{y_{i+1}-y_i}{h_i} - \frac{h_i}{3}(2M_i + M_{i+1})$$

$$c_i = M_i$$

$$d_i = \frac{M_{i+1} - M_i}{3h_i}.$$

### Algorithm Steps

I. **Data Preparation:**

- Sort the data points $(x_i,y_i)$ in ascending order by $x_i$.
- Compute $h_i = x_{i+1}-x_i$ for $i=0,\ldots,n-1$.

II. **Form the Equations:**

Set up the linear system to solve for the second derivatives $M_i$. For a natural spline:

$$M_0 = 0, \quad M_n = 0$$

For $i=1,\ldots,n-1$:

$$h_{i-1}M_{i-1} + 2(h_{i-1}+h_i)M_i + h_i M_{i+1} = 3\left(\frac{y_{i+1}-y_i}{h_i} - \frac{y_i - y_{i-1}}{h_{i-1}}\right)$$

III. **Solve the Tridiagonal System:**

Use an efficient method (like the Thomas algorithm) to solve for $M_1, M_2,\ldots,M_{n-1}$.

IV. **Calculate the Coefficients:**

With $M_i$ known, compute:

$$a_i = y_i, \quad b_i, \quad c_i = M_i, \quad d_i$$

as described above.

V. **Interpolation:**

For a given $x$, find the interval $[x_i, x_{i+1}]$ such that $x_i \leq x \leq x_{i+1}$ and evaluate:

$$S_i(x) = a_i + b_i(x - x_i) + c_i(x - x_i)^2 + d_i(x - x_i)^3$$

### Example

Consider three points: $(0,0), (1,0.5), (2,0)$.

- $h_0 = 1, h_1=1$.
- Boundary conditions: $M_0=M_2=0$.

We form the equation for $i=1$:

$$1 \cdot M_0 + 2(1+1)M_1 + 1 \cdot M_2 = 3((0-0.5)/1 - (0.5-0)/1) = 3(-0.5-0.5)= -3.$$

Since $M_0=M_2=0$:

$$4M_1 = -3 \implies M_1 = -0.75$$

Then:

$$a_0 = y_0=0, \quad c_0=M_0=0$$

$$b_0 = (y_1 - y_0)/h_0 - h_0(2M_0+M_1)/3 = 0.5/1 - (2\cdot 0 + (-0.75))/3 = 0.5 +0.25 =0.75$$

$$d_0 = (M_1 - M_0)/(3h_0)=(-0.75 -0)/3= -0.25$$

And similarly for $i=1$.

This gives piecewise polynomials smoothly interpolating the given points.

### Advantages

I. **Smoothness:**  

Produces smooth curves with continuous first and second derivatives.

II. **Controlled Behavior:**  

Avoids large oscillations that high-degree polynomial interpolation might introduce.

III. **Local Control:**  

Changing one data point affects only the neighboring spline segments, not the entire polynomial.

### Limitations

I. **Complexity:**  

Requires setting up and solving a linear system of equations, which is more involved than simpler interpolation methods.

II. **Computational Cost:**  

More computationally expensive than methods like linear interpolation, especially for very large data sets.

III. **Boundary Conditions Needed:**  

The behavior at the endpoints depends on chosen boundary conditions (natural, clamped, etc.), which must be specified.

- It can be computationally intense compared to more straightforward methods.
- It requires the resolution of a system of equations, which can become complex with a large number of control points.
