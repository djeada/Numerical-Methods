## Line Search

A line search chooses the step length $\alpha_k$ after a search direction $p_k$ has been selected:

$$
x_{k+1}=x_k+\alpha_k p_k.
$$

The direction determines **where** to move; the line search determines **how far**.

### One-dimensional reduction

Define

$$
\phi(\alpha)=f(x_k+\alpha p_k).
$$

A line search approximately minimizes $\phi(\alpha)$ for $\alpha>0$ or finds a step that satisfies sufficient-decrease conditions.

Exact minimization is usually unnecessary and can cost more than it saves.

### Armijo sufficient decrease

The Armijo condition requires

$$
f(x_k+\alpha p_k)
\le
f(x_k)+c_1\alpha\nabla f(x_k)^\top p_k,
$$

with a small constant such as $c_1=10^{-4}$.

![Armijo sufficient decrease along a search direction](https://github.com/djeada/Numerical-Methods/raw/refs/heads/master/notes/8_optimization/resources/plots/line_search_armijo.svg)

For a descent direction, the right-hand side lies below $f(x_k)$ for $\alpha>0$.

### Backtracking

A simple backtracking line search is:

1. start from $\alpha=1$;
2. test Armijo;
3. if it fails, replace $\alpha\leftarrow\rho\alpha$ with $0<\rho<1$;
4. repeat until accepted.

This is inexpensive and robust for steepest descent and damped Newton methods.

### Wolfe conditions

Quasi-Newton methods benefit from an additional curvature condition. The weak Wolfe conditions are

$$
f(x_k+\alpha p_k)
\le
f(x_k)+c_1\alpha g_k^\top p_k,
$$

and

$$
\nabla f(x_k+\alpha p_k)^\top p_k
\ge
c_2 g_k^\top p_k,
$$

where

$$
0<c_1<c_2<1.
$$

The second condition prevents an accepted step from being unnecessarily short and helps preserve the curvature condition needed by BFGS.

### Why line search matters

A full Newton step can be excellent near a solution and disastrous far away. Line search provides a **globalization strategy**: it allows a fast local model to be used while demanding actual progress in the nonlinear objective.

### Practical failure modes

- If $p_k$ is not a descent direction, Armijo backtracking may shrink indefinitely.
- Very noisy objectives make sufficient-decrease tests unreliable.
- Poor scaling can force extremely small steps.
- Strict Wolfe checks can increase gradient evaluations.

The BFGS implementation in this repository uses a compact backtracking loop that tests sufficient decrease and a Wolfe-style curvature condition.
