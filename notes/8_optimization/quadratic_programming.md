## Quadratic Programming

A quadratic program (QP) has a quadratic objective and linear constraints:

$$
\min_x \frac12x^\top Qx+c^\top x
$$

subject to

$$
A_{\text{ub}}x\le b_{\text{ub}},
\qquad
A_{\text{eq}}x=b_{\text{eq}}.
$$

When

$$
Q\succeq0,
$$

the problem is convex.

### Unconstrained solution

If $Q$ is positive definite and there are no constraints, stationarity gives

$$
Qx^*+c=0,
$$

so

$$
Qx^*=-c.
$$

Again, solve this system directly rather than forming $Q^{-1}$.

### Projected gradient idea

For a convex feasible set $C$, projected gradient descent uses

$$
y_k=x_k-\alpha\nabla f(x_k),
$$

then

$$
x_{k+1}=\Pi_C(y_k),
$$

where $\Pi_C$ denotes Euclidean projection.

![Gradient step followed by projection to a feasible set](https://github.com/djeada/Numerical-Methods/raw/refs/heads/master/notes/8_optimization/resources/plots/quadratic_programming_projection.svg)

The repository implementation uses this idea in a simplified form: it takes a gradient step, projects violated half-space inequalities one at a time, and then corrects affine equality residuals.

### Step size for a quadratic

For

$$
f(x)=\frac12x^\top Qx+c^\top x,
$$

the gradient is

$$
\nabla f(x)=Qx+c.
$$

If $Q\succeq0$, the largest eigenvalue is a Lipschitz constant for the gradient. A common conservative fixed step is therefore approximately

$$
\alpha=\frac{1}{\lambda_{\max}(Q)}.
$$

### KKT system for equality-constrained QP

For

$$
Ax=b,
$$

the optimality equations are

$$
Qx+c+A^\top\nu=0,
$$

$$
Ax=b.
$$

Together they form

$$
\begin{bmatrix}
Q&A^\top\\
A&0
\end{bmatrix}
\begin{bmatrix}
x\\
\nu
\end{bmatrix}
=
\begin{bmatrix}
-c\\
b
\end{bmatrix}.
$$

This linear-algebra viewpoint is central to active-set and interior-point methods.

### Numerical caveats

Sequentially projecting violated inequalities is easy to understand but is not the same as computing the exact Euclidean projection onto a general polyhedron. For difficult constraint geometries, a dedicated QP solver is preferable.
