## Local Optimization

Local optimization methods refine a starting point using information about the objective near the current iterate. They are the default tools for smooth numerical optimization because they can converge rapidly with far fewer evaluations than global search.

The tradeoff is fundamental: on a non-convex objective, the answer may depend on the initial point.

### Descent directions

For a differentiable objective, a vector $p_k$ is a descent direction at $x_k$ if

$$
\nabla f(x_k)^\top p_k<0.
$$

An update has the generic form

$$
x_{k+1} = x_k + \alpha_k p_k,
$$

where $\alpha_k>0$ is the step length.

Steepest descent chooses

$$
p_k = -\nabla f(x_k).
$$

Newton's method solves

$$
\nabla^2 f(x_k)p_k = -\nabla f(x_k),
$$

and BFGS uses an approximate inverse Hessian $H_k$:

$$
p_k = -H_k\nabla f(x_k).
$$

### The Rosenbrock valley

The Rosenbrock function

$$
f(x,y) = (1 - x)^2 + 100(y - x^2)^2
$$

has a unique global minimum at $(1,1)$, but its narrow curved valley makes it difficult for methods that do not account for curvature.

![Representative local-optimization paths on the Rosenbrock function](https://github.com/djeada/Numerical-Methods/raw/refs/heads/master/notes/8_optimization/resources/plots/local_rosenbrock_paths.svg)

Gradient descent makes inexpensive iterations but often zig-zags. Newton and quasi-Newton methods spend more work per iteration to learn the valley geometry.

### Convergence rates

Near a sufficiently regular minimizer, common asymptotic rates are:

- gradient descent: **linear** under strong convexity with a suitable step size;
- BFGS: often **superlinear** with a suitable line search;
- Newton: **quadratic** when the Hessian is nonsingular and the iterate is sufficiently close.

If $e_k=\|x_k-x^*\|$, these idealized rates look like

$$
e_{k+1}\le c e_k,
$$

$$
\frac{e_{k+1}}{e_k}\to0,
$$

and

$$
e_{k+1}\le c e_k^2,
$$

respectively.

![Idealized local convergence rates](https://github.com/djeada/Numerical-Methods/raw/refs/heads/master/notes/8_optimization/resources/plots/local_convergence_rates.svg)

### Why plain Newton can fail

The Newton direction is not guaranteed to be a descent direction when the Hessian is indefinite. Far from a minimizer it can point toward a maximum, a saddle, or simply take an enormous step.

Practical Newton-type solvers therefore use one or more safeguards:

- [line search](line_search.md);
- Hessian modification or damping;
- trust regions;
- quasi-Newton positive-definite approximations.

The repository implementation intentionally keeps the algorithms compact: fixed-step gradient descent, plain Newton using `numpy.linalg.solve`, and BFGS with a backtracking Wolfe-style line search.

### BFGS update

Define

$$
s_k = x_{k+1} - x_k,
\qquad y_k = \nabla f(x_{k+1}) - \nabla f(x_k),
$$

and

$$
\rho_k = \frac{1}{y_k^\top s_k}.
$$

The inverse-Hessian BFGS update is

$$
H_{k+1} = (I - \rho_k s_k y_k^\top)H_k(I - \rho_k y_k s_k^\top) + \rho_k s_k s_k^\top.
$$

If $H_k$ is positive definite and $y_k^\top s_k>0$, the update preserves positive definiteness.

See [Newton and quasi-Newton methods](newton_and_quasi_newton.md) for the derivation and numerical interpretation.

### Worked quadratic example

For

$$
f(x,y) = \frac12(8x^2 + 2y^2) - 4x - 2y,
$$

we have

$$
\nabla f=
\begin{bmatrix}
8x-4\\
2y-2
\end{bmatrix},
\qquad
H=
\begin{bmatrix}
8&0\\
0&2
\end{bmatrix}.
$$

The minimizer solves $H x=b$:

$$
(x^*,y^*) = (0.5,1).
$$

Newton reaches it in one exact step from any starting point because the quadratic model is the function itself. Gradient descent generally needs multiple steps and its rate is controlled by the eigenvalue ratio $8/2=4$.

### Practical diagnostics

For a local solver, report more than the final point. Useful diagnostics include:

- gradient norm;
- objective reduction;
- accepted step lengths;
- number of function and gradient evaluations;
- Hessian eigenvalues or quasi-Newton curvature tests;
- sensitivity to the starting point.
