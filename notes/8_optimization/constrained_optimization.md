## Constrained Optimization

Constrained optimization addresses the problem of minimizing (or maximizing) an objective function subject to restrictions on the decision variables. These restrictions, or **constraints**, can take the form of equalities, inequalities, or bounds, and they define a **feasible region** — the set of all points that satisfy every constraint simultaneously. The optimal solution must lie within this feasible region while achieving the best possible objective value. Constrained optimization is ubiquitous in practice: engineers allocate limited resources, financial analysts balance risk and return within regulatory limits, and data scientists fit models subject to structural requirements.

Two major problem classes dominate the field. **Linear programming (LP)** deals with a linear objective and linear constraints, and can be solved extremely efficiently by the simplex method or interior-point methods. **Nonlinear constrained optimization** handles more general objectives and constraints, employing techniques such as **Lagrange multipliers**, penalty methods, and sequential quadratic programming (SQP). The unifying theoretical framework is provided by the **Karush–Kuhn–Tucker (KKT) conditions**, which generalize the unconstrained optimality condition $\nabla f = 0$ to account for constraints.

**Conceptual Illustration**:

Imagine a topographic map where the altitude represents the objective function. The feasible region is a fenced area on the map — you are only allowed to stand inside the fence. The constrained optimum is the lowest point of elevation within the fenced area. If the lowest point of the entire landscape happens to lie inside the fence, it is also the constrained optimum. Otherwise, the constrained optimum lies on the boundary of the fence, and Lagrange multipliers tell you how much the optimal value would improve if the fence were moved slightly outward.

### Mathematical Formulation

**General Constrained Optimization Problem:**

$$\min_{x \in \mathbb{R}^n} f(x)$$

subject to:

$$g_i(x) \leq 0, \quad i = 1, \dots, m, \quad \text{(inequality constraints)}$$
$$h_j(x) = 0, \quad j = 1, \dots, p. \quad \text{(equality constraints)}$$

The **feasible set** is:

$$\mathcal{F} = \{x \in \mathbb{R}^n : g_i(x) \leq 0, \; h_j(x) = 0, \; \forall \, i, j\}.$$

**Linear Programming (LP):**

When $f$, $g_i$, and $h_j$ are all affine, the problem is a linear program:

$$\min_{x \in \mathbb{R}^n} c^\top x$$

subject to:

$$Ax \leq b, \quad x \geq 0.$$

**Lagrangian and KKT Conditions:**

The Lagrangian function incorporates the constraints into the objective:

$$\mathcal{L}(x, \lambda, \nu) = f(x) + \sum_{i=1}^m \lambda_i g_i(x) + \sum_{j=1}^p \nu_j h_j(x),$$

where $\lambda_i \geq 0$ are the inequality multipliers and $\nu_j$ are the equality multipliers. The KKT conditions for a local minimum $x^*$ (under constraint qualifications) are:

$$\nabla_x \mathcal{L}(x^*, \lambda^*, \nu^*) = 0, \quad \text{(stationarity)}$$
$$g_i(x^*) \leq 0, \quad h_j(x^*) = 0, \quad \text{(primal feasibility)}$$
$$\lambda_i^* \geq 0, \quad \text{(dual feasibility)}$$
$$\lambda_i^* g_i(x^*) = 0. \quad \text{(complementary slackness)}$$

### Derivation

I. **Lagrange Multipliers for Equality Constraints:**

Consider minimizing $f(x)$ subject to $h(x) = 0$ where $h : \mathbb{R}^n \to \mathbb{R}^p$. At a constrained minimum $x^*$, the gradient of $f$ must be a linear combination of the constraint gradients (otherwise, one could move along the constraint surface and decrease $f$):

$$\nabla f(x^*) = -\sum_{j=1}^p \nu_j \nabla h_j(x^*).$$

This is the stationarity condition of the Lagrangian $\mathcal{L}(x, \nu) = f(x) + \sum_j \nu_j h_j(x)$.

**Geometric Interpretation:** At the optimum, the level curves of $f$ are tangent to the constraint surface $h(x) = 0$. The multiplier $\nu_j$ measures the rate of change of the optimal objective value with respect to a perturbation of the $j$-th constraint: $\frac{df^*}{db_j} = -\nu_j$ for a constraint $h_j(x) = b_j$.

II. **Extension to Inequality Constraints:**

For inequality constraints $g_i(x) \leq 0$, the key insight is that at the optimum, each constraint is either **active** ($g_i(x^*) = 0$) or **inactive** ($g_i(x^*) < 0$). Active constraints behave like equality constraints and contribute to the optimality conditions; inactive constraints do not affect the solution locally. This is captured by the **complementary slackness** condition $\lambda_i g_i(x^*) = 0$: if the constraint is inactive, its multiplier must be zero.

III. **Linear Programming — Simplex Insight:**

For an LP, the feasible region is a **polyhedron** (intersection of half-spaces). A fundamental theorem of linear programming states that if the LP has an optimal solution, then there exists an optimal solution at a **vertex** (extreme point) of the polyhedron. The simplex method exploits this by moving from vertex to adjacent vertex along edges of the polyhedron, always improving the objective, until it reaches an optimal vertex.

### Algorithm Steps

**Solving an LP via the Simplex Method (Tableau Form):**

**Input:**

- Cost vector $c \in \mathbb{R}^n$.
- Constraint matrix $A \in \mathbb{R}^{m \times n}$ and right-hand side $b \in \mathbb{R}^m$ with $b \geq 0$.
- The LP in standard form: $\min \, c^\top x$ subject to $Ax + s = b$, $x \geq 0$, $s \geq 0$.

**Initialization:**

- Start with the basic feasible solution $x = 0$, $s = b$ (slack variables form the initial basis).
- Construct the initial simplex tableau.

**Iteration:**

I. **Pricing**: Compute the reduced costs $\bar{c}_j = c_j - c_B^\top B^{-1} A_j$ for each non-basic variable $j$.

II. **Optimality test**: If all $\bar{c}_j \geq 0$, the current solution is optimal. Stop.

III. **Pivot column**: Select the entering variable $j^*$ with the most negative $\bar{c}_{j^*}$.

IV. **Ratio test**: For each basic variable $i$ with $(B^{-1}A_{j^*})_i > 0$, compute $\theta_i = \frac{(B^{-1}b)_i}{(B^{-1}A_{j^*})_i}$. The leaving variable is the one with the smallest $\theta_i$.

V. **Pivot**: Update the basis by swapping the entering and leaving variables. Update the tableau.

VI. Return to step I.

**Output:**

- Optimal basic feasible solution $x^*$.
- Optimal objective value $c^\top x^*$.

### Example

**Resource Allocation (Linear Programming):**

A factory produces two products, $P_1$ and $P_2$. Each unit of $P_1$ yields a profit of \$5 and each unit of $P_2$ yields \$4. The factory has constraints on labor and raw materials:

- Labor: each unit of $P_1$ requires 2 hours, each unit of $P_2$ requires 1 hour. Total available: 8 hours.
- Material: each unit of $P_1$ requires 1 kg, each unit of $P_2$ requires 2 kg. Total available: 7 kg.
- Non-negativity: $x_1, x_2 \geq 0$.

**Formulation:**

$$\max_{x_1, x_2} \; 5x_1 + 4x_2$$

subject to:

$$2x_1 + x_2 \leq 8,$$
$$x_1 + 2x_2 \leq 7,$$
$$x_1 \geq 0, \quad x_2 \geq 0.$$

**Finding Vertices of the Feasible Region:**

The constraints define a polygon. The vertices are found by solving pairs of boundary equations:

- $(0, 0)$: intersection of $x_1 = 0$ and $x_2 = 0$. Objective: $0$.
- $(4, 0)$: intersection of $2x_1 + x_2 = 8$ and $x_2 = 0$. Objective: $20$.
- $(0, 3.5)$: intersection of $x_1 = 0$ and $x_1 + 2x_2 = 7$. Objective: $14$.
- $(3, 2)$: intersection of $2x_1 + x_2 = 8$ and $x_1 + 2x_2 = 7$. Objective: $5(3) + 4(2) = 23$.

**Optimal Solution:**

The maximum profit is $\$23$ at $(x_1, x_2) = (3, 2)$: produce 3 units of $P_1$ and 2 units of $P_2$.

**Nonlinear Constrained Example (Lagrange Multipliers):**

Minimize $f(x, y) = x^2 + y^2$ subject to $x + y = 4$.

**Lagrangian:**

$$\mathcal{L}(x, y, \nu) = x^2 + y^2 + \nu(x + y - 4).$$

**Stationarity:**

$$\frac{\partial \mathcal{L}}{\partial x} = 2x + \nu = 0 \implies x = -\nu/2,$$
$$\frac{\partial \mathcal{L}}{\partial y} = 2y + \nu = 0 \implies y = -\nu/2.$$

**Constraint:**

$$x + y = 4 \implies -\nu/2 - \nu/2 = 4 \implies \nu = -4.$$

**Solution:**

$$x = 2, \quad y = 2, \quad f(2,2) = 8.$$

The multiplier $\nu = -4$ indicates that if the constraint were relaxed to $x + y = 4 + \epsilon$, the optimal objective would change by approximately $-4\epsilon$ (i.e., the minimum distance squared increases as the constraint shifts further from the origin).

### Advantages

1. **Rigorous optimality conditions** (KKT conditions) provide a complete characterization of optimal solutions, enabling both theoretical analysis and the design of efficient algorithms.
2. **Mature and highly efficient solvers** for linear programming (e.g., simplex and interior-point methods) and nonlinear programming (e.g., SQP, IPOPT) can handle problems with millions of variables and constraints.
3. **Economic interpretation** of Lagrange multipliers (shadow prices) gives valuable sensitivity information, indicating how much the optimal value would improve if a constraint were relaxed.
4. **Broad applicability** across engineering, economics, logistics, and science makes constrained optimization one of the most widely used mathematical frameworks in practice.

### Limitations

1. **Finding a feasible starting point** can itself be a difficult optimization problem, especially when constraints are complex or the feasible region is small or disconnected.
2. **Non-convex constraints** may lead to multiple local optima within the feasible region, and KKT conditions provide only necessary (not sufficient) conditions for optimality in the non-convex case.
3. **Degeneracy and numerical issues** can arise in linear programming (cycling in simplex) and in nonlinear programming (ill-conditioned KKT systems near constraint boundaries).
4. **Scaling sensitivity** means that constraints and objectives with widely different magnitudes can cause convergence difficulties, often requiring careful problem preprocessing or scaling strategies.
