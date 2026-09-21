## Lagrange Multipliers and KKT Conditions

Lagrange multipliers convert constrained first-order optimality into a system of equations involving the objective and constraint gradients.

### Equality constraint

Consider

$$
\min_x f(x)
$$

subject to

$$
h(x) = 0.
$$

At a regular constrained optimum, the objective gradient is normal to the feasible tangent space, so

$$
\nabla f(x^{\ast}) + \nu\nabla h(x^*) = 0.
$$

![Tangency of an objective contour and an equality constraint](https://github.com/djeada/Numerical-Methods/raw/refs/heads/master/notes/8_optimization/resources/plots/lagrange_tangency.svg)

The Lagrangian is

$$
\mathcal{L}(x,\nu) = f(x) + \nu h(x).
$$

The first-order equations are

$$
\nabla_x\mathcal{L} = 0,
\qquad h(x) = 0.
$$

### Multiple constraints

With equality constraints $h_j(x)=0$ and inequalities $g_i(x)\le0$,

$$
\mathcal{L}(x,\lambda,\nu) = f(x) + \sum_i\lambda_i g_i(x) + \sum_j\nu_j h_j(x).
$$

The Karush-Kuhn-Tucker conditions are:

**Stationarity**

$$
\nabla_x\mathcal{L} = 0.
$$

**Primal feasibility**

$$
g_i(x)\le0,
\qquad h_j(x) = 0.
$$

**Dual feasibility**

$$
\lambda_i\ge0.
$$

**Complementary slackness**

$$
\lambda_i g_i(x) = 0.
$$

### Active constraints

Complementary slackness says that either

$$
g_i(x^*)<0\quad\Rightarrow\quad\lambda_i = 0,
$$

or the constraint is active:

$$
g_i(x^*) = 0.
$$

Only active inequality constraints can exert a first-order force on the optimum.

### Constraint qualifications

KKT conditions are not automatically necessary at every constrained optimum. Regularity assumptions are needed to rule out degenerate constraint geometry. Common examples include LICQ and Slater's condition in convex optimization.

### Sensitivity interpretation

Lagrange multipliers often measure how the optimal value changes when a constraint right-hand side is perturbed. This is the origin of the “shadow price” interpretation in economics and operations research.

The sign depends on how the constraint is parameterized, so sensitivity formulas should be derived from the chosen Lagrangian rather than memorized without context.

### KKT residuals

Numerically, it is useful to monitor a combined residual such as

$$
r=
\begin{bmatrix}
\nabla_x\mathcal{L}\\
h(x)
\end{bmatrix}
$$

for equality-constrained problems. The repository implementation applies a Newton-like step to such a residual using a simple Hessian approximation.
