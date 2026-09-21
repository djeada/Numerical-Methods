## Linear Programming

A linear program optimizes a linear objective over linear constraints. A common minimization form is

$$
\min_x c^\top x
$$

subject to

$$
Ax\le b,
\qquad x\ge0.
$$

The feasible region is a polyhedron.

### Why vertices matter

If a linear program has a finite optimum, at least one optimum occurs at an extreme point of the feasible polyhedron. In two dimensions these are polygon vertices.

![Linear-programming geometry and an optimal vertex](https://github.com/djeada/Numerical-Methods/raw/refs/heads/master/notes/8_optimization/resources/plots/linear_programming_geometry.svg)

The objective contours

$$
c^\top x = \gamma
$$

are parallel hyperplanes. Moving them in the improving direction until they last touch the feasible region reveals the optimum geometrically.

### Slack variables

An inequality

$$
a_i^\top x\le b_i
$$

can be rewritten as

$$
a_i^\top x + s_i = b_i,
\qquad s_i\ge0.
$$

Slack variables convert the inequalities into equalities while measuring unused capacity.

### Simplex idea

The simplex method maintains a basis corresponding to a basic feasible solution and moves between adjacent vertices.

For minimization, reduced costs indicate whether introducing a nonbasic variable can improve the objective. If all reduced costs satisfy the optimality sign convention, the current basis is optimal.

A ratio test chooses the leaving variable so that feasibility is preserved.

### Unboundedness and infeasibility

A correct LP solver must distinguish:

- **optimal**: a feasible point achieves the best finite value;
- **unbounded**: feasible points can improve the objective without limit;
- **infeasible**: no point satisfies all constraints.

The educational simplex implementation in this repository assumes a simple initial slack basis and is not a full Phase-I/Phase-II production solver. In particular, general infeasible starts require additional machinery.

### Worked example

Maximize

$$
5x_1 + 4x_2
$$

subject to

$$
2x_1 + x_2\le8,
$$

$$
x_1 + 2x_2\le7,
$$

$$
x_1,x_2\ge0.
$$

The boundary intersection solves

$$
2x_1 + x_2 = 8,
$$

$$
x_1 + 2x_2 = 7,
$$

which gives

$$
(x_1,x_2) = (3,2).
$$

The objective value is

$$
5(3) + 4(2) = 23,
$$

larger than at the other feasible vertices.

### Numerical notes

Degeneracy can produce zero-length pivots and cycling. Real solvers use anti-cycling rules, presolve, scaling, sparse linear algebra, and often dual-simplex or interior-point variants.
