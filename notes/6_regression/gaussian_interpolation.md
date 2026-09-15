## Gaussian Radial Basis Function Interpolation

Gaussian radial basis function interpolation constructs a smooth interpolant as a weighted sum of Gaussian functions centered at the data nodes. Unlike cubic splines, which use different polynomial pieces on separate intervals, a Gaussian RBF interpolant is **global**: every basis function can contribute to the value at every query point.

The Gaussian kernel is infinitely differentiable, so the resulting interpolant is very smooth. However, smoothness does not guarantee monotonicity, positivity, or freedom from overshoot. The choice of the **shape parameter** strongly affects both the form of the interpolant and the numerical conditioning of the interpolation system.

### Inputs and Goal

**Inputs:** at least one finite data pair with distinct nodes, a positive shape parameter $\varepsilon$, and a query $x_*$. **Goal:** determine the Gaussian RBF weights so that the interpolant passes exactly through all data points, then evaluate the resulting global interpolant at $x_*$.

Equal spacing is not required. Unlike cubic splines, Gaussian RBF interpolation does not require endpoint boundary conditions.

### Mathematical Formulation

We start with a set of $n+1$ data points:

$$
(x_0,y_0),(x_1,y_1),\ldots,(x_n,y_n)
$$

with distinct nodes $x_i$.

A **radial basis function interpolant** has the form

$$
s(x)=\sum_{j=0}^{n}\lambda_j\phi(|x-x_j|)
$$

where:

* $\lambda_j$ are unknown coefficients or weights,
* $x_j$ are the centers of the radial basis functions,
* $\phi(r)$ is a function depending only on the distance $r$ from a center.

For the **Gaussian radial basis function**,

$$
\phi(r)=e^{-(\varepsilon r)^2}
$$

where

$$
\varepsilon>0
$$

is called the **shape parameter**.

Thus the interpolant is

$$
s(x)=\sum_{j=0}^{n}\lambda_j
e^{-\varepsilon^2(x-x_j)^2}.
$$

An alternative parameterization sometimes uses a Gaussian width $\sigma$:

$$
\phi(r)=e^{-r^2/(2\sigma^2)}.
$$

The two conventions are equivalent when

$$
\varepsilon=\frac{1}{\sqrt{2}\sigma}.
$$

A larger $\varepsilon$ produces narrower Gaussian basis functions, while a smaller $\varepsilon$ produces wider and flatter basis functions.

### Key Requirements

I. **Interpolation Condition:**

The interpolant must reproduce every given data value:

$$
s(x_i)=y_i,
\qquad i=0,1,\ldots,n.
$$

Substituting the Gaussian RBF representation gives

$$
\sum_{j=0}^{n}
\lambda_j e^{-\varepsilon^2(x_i-x_j)^2}
=
y_i.
$$

II. **Global Representation:**

There are no separate polynomial segments. The same expression

$$
s(x)=\sum_{j=0}^{n}\lambda_j
e^{-\varepsilon^2(x-x_j)^2}
$$

is used over the entire domain.

Consequently, changing one data value can generally change every coefficient and therefore affect the interpolant everywhere.

III. **Smoothness:**

Because each Gaussian

$$
e^{-\varepsilon^2(x-x_j)^2}
$$

is infinitely differentiable, the interpolant $s(x)$ is also infinitely differentiable.

In particular,

$$
s\in C^\infty.
$$

Unlike cubic splines, no explicit derivative-matching conditions are necessary because there are no piecewise joins.

IV. **No Boundary Conditions:**

Gaussian RBF interpolation does not require endpoint conditions such as natural, clamped, periodic, or not-a-knot conditions.

Instead, an important modeling choice is the shape parameter $\varepsilon$.

### Derivation of the Coefficients

I. **Choose the Gaussian Basis:**

For every center $x_j$, define

$$
\phi_j(x)
=
e^{-\varepsilon^2(x-x_j)^2}.
$$

Then

$$
s(x)=
\lambda_0\phi_0(x)
+\lambda_1\phi_1(x)
+\cdots+
\lambda_n\phi_n(x).
$$

II. **Apply the Interpolation Conditions:**

At $x=x_i$,

$$
s(x_i)=y_i.
$$

Therefore,

$$
\lambda_0e^{-\varepsilon^2(x_i-x_0)^2}
+
\lambda_1e^{-\varepsilon^2(x_i-x_1)^2}
+\cdots+
\lambda_ne^{-\varepsilon^2(x_i-x_n)^2}
=
y_i.
$$

Doing this for all $n+1$ data points produces $n+1$ linear equations for the $n+1$ unknown coefficients.

III. **Matrix Form:**

Define the interpolation matrix $A$ by

$$
A_{ij}
=
e^{-\varepsilon^2(x_i-x_j)^2},
\qquad i,j=0,1,\ldots,n.
$$

Then

$$
A
\begin{bmatrix}
\lambda_0\\
\lambda_1\\
\vdots\\
\lambda_n
\end{bmatrix}
=
\begin{bmatrix}
y_0\\
y_1\\
\vdots\\
y_n
\end{bmatrix}.
$$

In compact notation,

$$
A\boldsymbol{\lambda}
=
\mathbf y.
$$

The matrix is

$$
A=
\begin{bmatrix}
1 &
e^{-\varepsilon^2(x_0-x_1)^2} &
\cdots &
e^{-\varepsilon^2(x_0-x_n)^2}
\\
e^{-\varepsilon^2(x_1-x_0)^2} &
1 &
\cdots &
e^{-\varepsilon^2(x_1-x_n)^2}
\\
\vdots & \vdots & \ddots & \vdots
\\
e^{-\varepsilon^2(x_n-x_0)^2} &
e^{-\varepsilon^2(x_n-x_1)^2} &
\cdots &
1
\end{bmatrix}.
$$

Since

$$
(x_i-x_j)^2=(x_j-x_i)^2,
$$

the matrix is symmetric:

$$
A_{ij}=A_{ji}.
$$

For distinct nodes and $\varepsilon>0$, the Gaussian kernel is strictly positive definite. Therefore $A$ is positive definite and nonsingular in exact arithmetic, so the interpolation coefficients are uniquely determined.

IV. **Solve for the Weights:**

Solve

$$
\boldsymbol{\lambda}=A^{-1}\mathbf y.
$$

In numerical computation, the inverse should generally **not** be formed explicitly. Instead, solve the linear system directly, for example using Cholesky factorization because $A$ is symmetric positive definite.

Once the coefficients are known,

$$
s(x)
=
\sum_{j=0}^{n}
\lambda_j e^{-\varepsilon^2(x-x_j)^2}.
$$

### Algorithm Steps

I. **Data Preparation:**

* Store the data pairs $(x_i,y_i)$.
* Ensure all $x_i$ are distinct.
* Choose a positive shape parameter $\varepsilon$.
* Sorting the nodes is convenient in one dimension but is not mathematically required for the RBF formulation.

II. **Construct the Interpolation Matrix:**

For

$$
i,j=0,1,\ldots,n,
$$

compute

$$
A_{ij}
=
e^{-\varepsilon^2(x_i-x_j)^2}.
$$

The diagonal entries satisfy

$$
A_{ii}=1
$$

because

$$
e^{-\varepsilon^2(x_i-x_i)^2}=e^0=1.
$$

III. **Solve the Linear System:**

Solve

$$
A\boldsymbol{\lambda}=\mathbf y
$$

for

$$
\lambda_0,\lambda_1,\ldots,\lambda_n.
$$

A dense direct solver requires approximately $O(n^3)$ work for the initial solve and $O(n^2)$ memory. Because the Gaussian interpolation matrix is symmetric positive definite, Cholesky factorization is a natural direct method.

IV. **Evaluate the Interpolant:**

For a query $x_*$, compute

$$
s(x_*)
=
\sum_{j=0}^{n}
\lambda_j
e^{-\varepsilon^2(x_*-x_j)^2}.
$$

Unlike cubic spline interpolation, there is no interval or segment to locate. Every Gaussian basis function contributes to the global sum.

A direct evaluation requires $O(n)$ work per query.

### Example

**Inputs:**

$$
(0,0),\qquad(1,0.5),\qquad(2,0),
$$

with Gaussian shape parameter

$$
\varepsilon=1
$$

and query

$$
x_*=0.5.
$$

**Goal:** determine the Gaussian RBF coefficients, verify interpolation at the three nodes, and estimate the value at the query point.

The Gaussian basis is

$$
\phi(r)=e^{-r^2}.
$$

Therefore,

$$
s(x)
=
\lambda_0e^{-x^2}
+
\lambda_1e^{-(x-1)^2}
+
\lambda_2e^{-(x-2)^2}.
$$

### Constructing the Matrix

For $x_0=0$, $x_1=1$, and $x_2=2$,

$$
A_{ij}
=
e^{-(x_i-x_j)^2}.
$$

The required distances give

$$
e^{-1}\approx0.36787944
$$

and

$$
e^{-4}\approx0.01831564.
$$

Thus

$$
A=
\begin{bmatrix}
1 & e^{-1} & e^{-4}\\
e^{-1} & 1 & e^{-1}\\
e^{-4} & e^{-1} & 1
\end{bmatrix}.
$$

Numerically,

$$
A\approx
\begin{bmatrix}
1 & 0.36787944 & 0.01831564\\
0.36787944 & 1 & 0.36787944\\
0.01831564 & 0.36787944 & 1
\end{bmatrix}.
$$

The interpolation equations are therefore

$$
\lambda_0
+
0.36787944\lambda_1
+
0.01831564\lambda_2
=
0,
$$

$$
0.36787944\lambda_0
+
\lambda_1
+
0.36787944\lambda_2
=
0.5,
$$

and

$$
0.01831564\lambda_0
+
0.36787944\lambda_1
+
\lambda_2
=
0.
$$

### Solving for the Coefficients

Because the data are symmetric about $x=1$,

$$
\lambda_0=\lambda_2.
$$

Solving the system gives approximately

$$
\lambda_0=-0.24602546,
$$

$$
\lambda_1=0.68101542,
$$

$$
\lambda_2=-0.24602546.
$$

Hence the Gaussian RBF interpolant is

$$
\boxed{
s(x)
=
-0.24602546e^{-x^2}
+
0.68101542e^{-(x-1)^2}
-
0.24602546e^{-(x-2)^2}
}
$$

### Verification at the Data Points

At $x=0$,

$$
s(0)
=
-0.24602546
+
0.68101542e^{-1}
-
0.24602546e^{-4}.
$$

Numerically,

$$
s(0)\approx0.
$$

At $x=1$,

$$
s(1)
=
-0.24602546e^{-1}
+
0.68101542
-
0.24602546e^{-1},
$$

so

$$
s(1)\approx0.5.
$$

At $x=2$,

$$
s(2)
=
-0.24602546e^{-4}
+
0.68101542e^{-1}
-
0.24602546,
$$

which gives

$$
s(2)\approx0.
$$

Thus the interpolant reproduces all three data values.

| Check  | Value              |
| ------ | ------------------ |
| $s(0)$ | $\approx0=y_0$ ✓   |
| $s(1)$ | $\approx0.5=y_1$ ✓ |
| $s(2)$ | $\approx0=y_2$ ✓   |

Small deviations from the exact values in floating-point calculations come from numerical rounding.

### Evaluating at the Query Point

For

$$
x_*=0.5,
$$

we evaluate the same global expression:

$$
s(0.5)
=
\lambda_0e^{-(0.5)^2}
+
\lambda_1e^{-(0.5-1)^2}
+
\lambda_2e^{-(0.5-2)^2}.
$$

Substituting the coefficients,

$$
s(0.5)
=
-0.24602546e^{-0.25}
+
0.68101542e^{-0.25}
-
0.24602546e^{-2.25}.
$$

Using

$$
e^{-0.25}\approx0.77880078
$$

and

$$
e^{-2.25}\approx0.10539922,
$$

we obtain

$$
s(0.5)\approx0.31284.
$$

Therefore,

$$
\boxed{s(0.5)\approx0.31284}.
$$

This differs from the natural cubic spline value for the same three data points because the two methods impose different mathematical models.

### Derivatives

Since the Gaussian interpolant is smooth, its derivatives can be obtained analytically.

Starting from

$$
s(x)
=
\sum_{j=0}^{n}
\lambda_j e^{-\varepsilon^2(x-x_j)^2},
$$

the first derivative is

$$
s'(x)
=
\sum_{j=0}^{n}
-2\varepsilon^2(x-x_j)
\lambda_j
e^{-\varepsilon^2(x-x_j)^2}.
$$

The second derivative is

$$
s''(x)
=
\sum_{j=0}^{n}
\lambda_j
\left[
4\varepsilon^4(x-x_j)^2
-
2\varepsilon^2
\right]
e^{-\varepsilon^2(x-x_j)^2}.
$$

No separate continuity conditions need to be imposed: these derivatives are automatically continuous everywhere.

### Effect of the Shape Parameter

The shape parameter $\varepsilon$ is an important part of Gaussian RBF interpolation.

For

$$
\phi(r)=e^{-(\varepsilon r)^2},
$$

a **small $\varepsilon$** produces broad, relatively flat Gaussian functions.

A **large $\varepsilon$** produces narrow Gaussian functions concentrated around their centers.

#### Small $\varepsilon$

As

$$
\varepsilon\rightarrow0,
$$

the matrix entries satisfy approximately

$$
A_{ij}\rightarrow1.
$$

Thus the interpolation matrix approaches a matrix whose entries are nearly all equal. The columns become nearly linearly dependent and the system can become extremely ill-conditioned.

This is known as the **flat Gaussian problem**.

Interestingly, a flat Gaussian interpolant can have excellent approximation properties mathematically, even though directly solving for the coefficients may become numerically unstable.

#### Large $\varepsilon$

When $\varepsilon$ is very large,

$$
e^{-\varepsilon^2(x_i-x_j)^2}
\rightarrow0
\qquad
(i\neq j),
$$

so the matrix approaches the identity matrix:

$$
A\rightarrow I.
$$

The basis functions then become very narrow. Although interpolation at the nodes is maintained, the interpolant can vary sharply and may approach zero between separated nodes.

Therefore, selecting $\varepsilon$ involves a tradeoff between the shape of the interpolant and numerical conditioning.

### Advantages

* Gaussian RBF interpolation produces an **infinitely smooth** interpolant.
* It works naturally with **unequally spaced nodes**.
* No endpoint boundary conditions are required.
* The same formulation extends naturally from one dimension to higher dimensions.
* For distinct nodes and a fixed positive $\varepsilon$, the Gaussian interpolation system has a unique solution in exact arithmetic.
* Once the coefficients have been determined, derivatives of any order can be evaluated analytically.
* RBF interpolation is mesh-free: it only requires distances between data points rather than a structured grid.

### Limitations

* The interpolation matrix is generally **dense**, unlike the tridiagonal system arising from cubic splines.
* A standard dense solve requires approximately $O(n^3)$ work and $O(n^2)$ memory.
* Evaluating one query directly requires contributions from all centers and therefore takes $O(n)$ work.
* The result can depend strongly on the choice of shape parameter $\varepsilon$.
* Small values of $\varepsilon$ can make the interpolation matrix severely ill-conditioned.
* Gaussian RBF interpolation does not generally preserve monotonicity, convexity, or positivity.
* Because the interpolant is global, changing one data value generally changes the interpolant throughout the domain.

### Higher-Dimensional Form

One major advantage of radial basis functions is that the same idea extends directly to data in several dimensions.

For points

$$
\mathbf x_0,\mathbf x_1,\ldots,\mathbf x_n
\in\mathbb R^d,
$$

the Gaussian interpolant is

$$
s(\mathbf x)
=
\sum_{j=0}^{n}
\lambda_j
e^{-\varepsilon^2\|\mathbf x-\mathbf x_j\|^2},
$$

where

$$
\|\mathbf x-\mathbf x_j\|
$$

is the Euclidean distance from the query point to the $j$th center.

The interpolation matrix becomes

$$
A_{ij}
=
e^{-\varepsilon^2\|\mathbf x_i-\mathbf x_j\|^2}.
$$

Thus essentially the same algorithm can interpolate scattered data in two, three, or more dimensions without constructing a piecewise mesh.

### Boundary and Numerical Checks

There are no natural or clamped endpoint conditions to verify for a Gaussian RBF interpolant. Instead, useful numerical checks include:

1. Verify that all nodes $x_i$ are distinct.
2. Verify that $\varepsilon>0$.
3. Check the residual

$$
\mathbf r
=
A\boldsymbol{\lambda}-\mathbf y.
$$

For a successful interpolation solve,

$$
\|\mathbf r\|
$$

should be small relative to the scale of the data.

4. Evaluate the interpolant at each node and verify

$$
s(x_i)\approx y_i.
$$

5. Monitor the condition number of $A$ when using small $\varepsilon$ or closely spaced nodes.

It can also be helpful to rescale the input coordinates so that their numerical magnitudes and spacings are reasonably normalized before choosing $\varepsilon$.

For a query point, there is no segment search. Simply evaluate

$$
s(x_*)
=
\sum_{j=0}^{n}
\lambda_j
e^{-\varepsilon^2(x_*-x_j)^2}.
$$

A direct query therefore requires $O(n)$ work.

Queries outside the data range are automatically defined by the same formula, but this should not be confused with reliable extrapolation. Since every Gaussian basis function tends to zero as its distance from its center becomes large,

$$
e^{-\varepsilon^2(x-x_j)^2}\rightarrow0
\quad\text{as}\quad
|x|\rightarrow\infty,
$$

the basic Gaussian RBF interpolant without an added polynomial term satisfies

$$
s(x)\rightarrow0
\quad\text{as}\quad
|x|\rightarrow\infty.
$$

This behavior may be inappropriate for a particular extrapolation problem and should be treated as part of the modeling choice.

For an independent numerical comparison, Gaussian RBF interpolation can be implemented using scientific-computing libraries or directly by constructing the matrix

$$
A_{ij}=e^{-\varepsilon^2(x_i-x_j)^2}
$$

and solving the resulting symmetric positive-definite linear system.
