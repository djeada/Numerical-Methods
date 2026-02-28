## Convex Optimization

Convex optimization is a subfield of mathematical optimization that deals with minimizing convex functions over convex sets. It occupies a central role in both theory and practice because convex problems have a remarkable property: every local minimum is also a global minimum. This guarantee eliminates the difficulties posed by multiple local minima that plague general nonlinear optimization, and it allows highly efficient algorithms to find globally optimal solutions. Applications span machine learning (e.g., support vector machines, logistic regression), signal processing, control systems, finance (portfolio optimization), and operations research.

The theoretical backbone of convex optimization rests on two pillars: **convex sets** and **convex functions**. Once a problem is recognized as convex, a rich algorithmic toolkit — including interior-point methods, cutting-plane methods, and specialized gradient schemes — becomes available, often solving problems with thousands or millions of variables in polynomial time.

**Conceptual Illustration**:

Picture the graph of a convex function as a smooth bowl sitting on a table. No matter where you place a marble on the inside surface, it will always roll down to the same lowest point at the bottom of the bowl. A non-convex function, by contrast, resembles a landscape of hills and valleys where a marble could settle into many different pockets depending on where it starts.

### Mathematical Formulation

**Convex Sets**:

A set $C \subseteq \mathbb{R}^n$ is **convex** if, for every pair of points $x, y \in C$ and every $\theta \in [0,1]$:

$$\theta x + (1-\theta) y \in C.$$

Geometrically, the line segment connecting any two points in the set lies entirely within the set. Examples include hyperplanes, half-spaces, Euclidean balls, ellipsoids, and polyhedra.

**Convex Functions**:

A function $f : \mathbb{R}^n \to \mathbb{R}$ is **convex** if its domain $\text{dom}(f)$ is a convex set and for all $x, y \in \text{dom}(f)$ and $\theta \in [0,1]$:

$$f(\theta x + (1-\theta) y) \leq \theta f(x) + (1-\theta) f(y).$$

This is the famous **Jensen's inequality** applied pointwise. Intuitively, the function value at any weighted average of two points is at most the weighted average of the function values. Equivalently, the region above the graph of a convex function (the **epigraph**) is a convex set.

**Standard Form of a Convex Optimization Problem**:

$$\min_{x \in \mathbb{R}^n} f(x)$$

subject to:

$$g_i(x) \leq 0, \quad i = 1, \dots, m,$$
$$Ax = b,$$

where $f$ and all $g_i$ are convex functions, and the equality constraints are affine.

**Quadratic Programming (QP)** is a special case in which the objective is a convex quadratic function and the constraints are linear:

$$\min_{x \in \mathbb{R}^n} \frac{1}{2} x^\top Q x + c^\top x$$

subject to:

$$Ax \leq b,$$

where $Q \in \mathbb{R}^{n \times n}$ is symmetric positive semidefinite, ensuring convexity.

### Derivation

I. **Why Local Minima are Global for Convex Problems**:

Suppose $x^*$ is a local minimum of a convex function $f$ over a convex set $C$, and assume for contradiction that there exists $y \in C$ with $f(y) < f(x^*)$. Consider the point:

$$z = \theta y + (1-\theta) x^*, \quad \theta \in (0,1).$$

Since $C$ is convex, $z \in C$. By convexity of $f$:

$$f(z) \leq \theta f(y) + (1-\theta) f(x^*) < \theta f(x^*) + (1-\theta) f(x^*) = f(x^*).$$

For sufficiently small $\theta$, $z$ is arbitrarily close to $x^*$, contradicting the assumption that $x^*$ is a local minimum. Hence every local minimum of a convex function on a convex set is a global minimum.

II. **First-Order Optimality Condition**:

If $f$ is convex and differentiable, then $x^*$ is a global minimizer if and only if:

$$\nabla f(x^*)^\top (y - x^*) \geq 0 \quad \text{for all } y \in C.$$

For unconstrained problems ($C = \mathbb{R}^n$), this simplifies to:

$$\nabla f(x^*) = 0.$$

III. **KKT Conditions for Constrained Convex Problems**:

At an optimal point $x^*$, there exist multipliers $\lambda_i \geq 0$ and $\nu$ such that:

$$\nabla f(x^*) + \sum_{i=1}^m \lambda_i \nabla g_i(x^*) + A^\top \nu = 0,$$
$$\lambda_i g_i(x^*) = 0, \quad i = 1, \dots, m.$$

For convex problems, these Karush–Kuhn–Tucker (KKT) conditions are both necessary and sufficient for optimality (under mild constraint qualifications).

### Algorithm Steps

**Solving a Quadratic Program via Active-Set Method**:

**Input:**

- Symmetric positive semidefinite matrix $Q \in \mathbb{R}^{n \times n}$.
- Cost vector $c \in \mathbb{R}^n$.
- Constraint matrix $A \in \mathbb{R}^{m \times n}$ and vector $b \in \mathbb{R}^m$.
- A feasible starting point $x_0$.

**Initialization:**

- Identify the active set $\mathcal{A}_0 = \{i : A_i x_0 = b_i\}$.
- Set iteration counter $k = 0$.

**Iteration:**

I. Solve the equality-constrained QP restricted to the current active set:

$$\min_d \frac{1}{2} d^\top Q d + (Qx_k + c)^\top d \quad \text{subject to } A_{\mathcal{A}_k} d = 0.$$

II. If $d_k = 0$, compute multipliers $\lambda$ for the active constraints.

- If all $\lambda_i \geq 0$, then $x_k$ is optimal. Stop.
- Otherwise, drop the constraint with the most negative $\lambda_i$ from $\mathcal{A}_k$.

III. If $d_k \neq 0$, compute the step length:

$$\alpha_k = \min\left(1, \min_{i \notin \mathcal{A}_k, A_i d_k > 0} \frac{b_i - A_i x_k}{A_i d_k}\right).$$

IV. Update: $x_{k+1} = x_k + \alpha_k d_k$. If $\alpha_k < 1$, add the blocking constraint to $\mathcal{A}_k$.

V. Increment $k$ and return to step I.

**Output:**

- Optimal solution $x^*$.
- Optimal objective value $\frac{1}{2} (x^*)^\top Q x^* + c^\top x^*$.

### Example

**Quadratic Programming Problem:**

Minimize:

$$f(x_1, x_2) = x_1^2 + x_2^2 - 4x_1 - 6x_2$$

subject to:

$$x_1 + x_2 \leq 6,$$
$$x_1 \leq 4,$$
$$x_1 \geq 0, \quad x_2 \geq 0.$$

**Setup:**

This is a QP with:

$$Q = \begin{pmatrix} 2 & 0 \\ 0 & 2 \end{pmatrix}, \quad c = \begin{pmatrix} -4 \\ -6 \end{pmatrix}.$$

The unconstrained minimum is found by setting $\nabla f = 0$:

$$\nabla f = \begin{pmatrix} 2x_1 - 4 \\ 2x_2 - 6 \end{pmatrix} = 0 \implies x_1 = 2, \; x_2 = 3.$$

**Checking Feasibility:**

- $x_1 + x_2 = 2 + 3 = 5 \leq 6$. ✓
- $x_1 = 2 \leq 4$. ✓
- $x_1 = 2 \geq 0, \; x_2 = 3 \geq 0$. ✓

Since the unconstrained minimizer satisfies all constraints, it is also the constrained optimum.

**Optimal Solution:**

$$x^* = (2, 3), \quad f(x^*) = 4 + 9 - 8 - 18 = -13.$$

**Convex vs Non-Convex Comparison:**

Consider the convex function $f(x) = x^2$ and the non-convex function $g(x) = x^4 - 2x^2 + 1$. The convex function has a single global minimum at $x = 0$, while $g(x) = (x^2 - 1)^2$ has two global minima at $x = \pm 1$ and a local maximum at $x = 0$. A local search starting near $x = 0$ on $g$ may converge to the local maximum rather than a global minimum, illustrating why convexity is such a valuable structural property.

### Advantages

1. **Global optimality guarantee** ensures that any local minimum found is also the global minimum, eliminating the need for multi-start strategies or exhaustive search.
2. **Efficient algorithms** such as interior-point methods solve convex problems in polynomial time, making even large-scale problems tractable.
3. **Strong duality** holds for convex problems under mild conditions, providing certificates of optimality and enabling dual decomposition techniques.
4. **Rich modeling framework** allows a wide variety of practical problems — least-squares, linear programming, semidefinite programming — to be cast as convex optimization problems.

### Limitations

1. **Modeling difficulty** arises because not all optimization problems are naturally convex, and reformulating a non-convex problem into a convex one (if possible) may require significant mathematical insight.
2. **Scalability challenges** remain for very large or structured problems, where even polynomial-time interior-point methods may be impractical without exploiting problem-specific structure.
3. **Sensitivity to problem formulation** means that equivalent-looking formulations can have very different computational properties, requiring expertise to choose the best representation.
4. **Limited expressiveness** compared to general nonlinear optimization means that certain objectives or constraints (e.g., integer variables, non-convex feasible regions) fall outside the convex optimization framework and require different techniques.
