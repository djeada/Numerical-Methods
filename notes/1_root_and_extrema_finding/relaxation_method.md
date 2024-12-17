## Introduction

The relaxation method, commonly referred to as the fixed-point iteration method, is an iterative approach used to find solutions (roots) to nonlinear equations of the form $f(x) = 0$. Instead of directly solving for the root, the method involves rewriting the original equation in the form:

$$x = g(x),$$
where $g(x)$ is a suitable function defined such that a fixed point of $g(x)$ corresponds to a root of $f(x)$. That is, if $\alpha$ is a root of $f(x)$, then $g(\alpha) = \alpha$.

This approach transforms a root-finding problem into a fixed-point problem. If the iteration defined by:

$$x_{n+1} = g(x_n)$$
converges, it will do so to the fixed point $\alpha$, which is also the root of the original equation. Relaxation methods can sometimes converge faster than bracket-based methods (like bisection), but they do not come with guaranteed convergence from any starting point. Convergence depends on the properties of the chosen $g(x)$ and the initial guess $x_0$.

**Conceptual Illustration**:

Imagine the line $y = x$ and the curve $y = g(x)$. A fixed point $\alpha$ is a point where the two curves intersect:

![output(17)](https://github.com/user-attachments/assets/6160870c-a9b5-495b-9ba6-ecfa661790b2)

The iteration takes a guess $x_n$, and then maps it to $x_{n+1}=g(x_n)$. If these iterations hone in on the intersection, the sequence converges to the root $\alpha$.

## Mathematical Formulation

**Starting Point:**

Given a nonlinear equation:

$$f(x) = 0,$$
we want to find $\alpha$ such that $f(\alpha)=0$.

**Rewriting the Equation:**

We rearrange the equation into a fixed-point form:

$$x = g(x).$$

There can be infinitely many ways to rewrite $f(x)=0$ as $x=g(x)$. A suitable $g(x)$ must be chosen to ensure convergence.

Once we have:

$$x_{n+1} = g(x_n),$$
if the iteration converges, it must converge to $\alpha$ satisfying $\alpha = g(\alpha)$.

**Convergence Conditions:**

A key sufficient condition for convergence is that:

$$|g'(x)| < 1 \quad \text{in the neighborhood of } \alpha.$$

If the derivative of $g(x)$ in the region around the fixed point is less than 1 in absolute value, the iteration will typically converge.

## Derivation

I. **From Root to Fixed Point Problem:**

Suppose we have $f(x)=0$. We isolate $x$ on one side:

$$x = g(x).$$

If $\alpha$ solves $f(\alpha)=0$, then $g(\alpha)=\alpha$.

II. **Fixed-Point Iteration:**

Define a sequence $\{x_n\}$ by choosing an initial guess $x_0$ and applying:

$$x_{n+1} = g(x_n).$$

III. **Convergence Insight:**

Consider a point $\alpha$ such that $g(\alpha)=\alpha$. If we expand $g$ near $\alpha$:

$$g(\alpha + h) \approx g(\alpha) + g'(\alpha)h = \alpha + g'(\alpha)h.$$

If $|g'(\alpha)|<1$, then iterating this process will reduce the error $|h|$ at each step, leading to convergence of $x_n$ to $\alpha$.

In essence, the choice of $g(x)$ greatly influences the convergence behavior. A poorly chosen $g(x)$ may lead to divergence or very slow convergence.

## Algorithm Steps

**Pseudocode for the Relaxation Method:**

I. **Input:**
- A function $f(x)$ and a corresponding $g(x)$ such that $f(x)=0$ is equivalent to $x=g(x)$.
- An initial guess $x_0$.
- A tolerance $\epsilon >0$ or a maximum number of iterations $n_{\max}$.
II. **Initialization:**
- Set iteration counter $n=0$.

III. **Iteration:**

I. Compute the next approximation:

  $$x_{n+1} = g(x_n).$$
II. Check convergence:
  - If $|x_{n+1}-x_n|< \epsilon$ or $|f(x_{n+1})|< \epsilon$, stop.
  - If $n>n_{\max}$, stop.

III. Otherwise, set $n = n+1$ and repeat from step (3.1).

IV. **Output:**
- Approximate root: $x_{n+1}$.
- Number of iterations performed.

## Example

**Given Equation:**

$$x^2 - 3x + 2 = 0.$$

This equation factors as $(x-1)(x-2)=0$, so the roots are $x=1$ and $x=2$.

**Choose a Fixed-Point Form:**

We can rearrange the equation to:

$$x = \frac{x^2 + 2}{3}.$$

Thus:

$$g(x) = \frac{x^2 + 2}{3}.$$

**Initial Guess:**

Let $x_0=0$.

**Iteration Steps:**

- **Iteration 1:**

$$x_1 = g(x_0) = g(0) = \frac{0^2 + 2}{3} = \frac{2}{3}\approx0.6667.$$

- **Iteration 2:**

$$x_2 = g(x_1) = g(0.6667) = \frac{(0.6667)^2 + 2}{3} = \frac{0.4444 + 2}{3}\approx\frac{2.4444}{3}=0.8148.$$

- **Iteration 3:**

$$x_3 = g(x_2) = g(0.8148)=\frac{(0.8148)^2 +2}{3}=\frac{0.6639+2}{3}\approx\frac{2.6639}{3}=0.8880.$$

Repeating this process, we observe $x_n$ approaching one of the roots (in this case, it will move closer to $x=1$, depending on the behavior of $g(x)$ near that root).

## Advantages

I. **Flexible Formulation:**

The relaxation method is conceptually simple: just rewrite the equation in fixed-point form and iterate.

II. **Potentially Faster Than Bisection:**

For well-chosen $g(x)$, it can converge faster than some bracketing methods such as bisection, especially if the derivative $|g'(x)|<1$ near the root.

III. **Broad Applicability:**

The method does not require derivatives (though good convergence often relates to the derivative of $g$), and can be applied to a variety of nonlinear equations where other methods might be inconvenient.

IV. **Straightforward Implementation:**

Implementing $x_{n+1}=g(x_n)$ is often quite direct once a suitable $g$ is identified.

## Limitations

I. **No Guaranteed Convergence:**

Unlike the bisection method, which is guaranteed to converge if the function satisfies certain conditions, the relaxation method may fail to converge if $|g'(x)| \geq 1$ in the vicinity of the root.

II. **Sensitive to the Choice of $g(x)$:**

There are infinitely many ways to rewrite $f(x)=0$ as $x=g(x)$. Some transformations promote convergence, while others cause divergence.

III. **Initial Guess Importance:**

A poor initial guess may lead to divergence or extremely slow convergence.

IV. **Dependent on Continuity and Differentiability:**

The standard theory and convergence conditions assume that $g(x)$ is continuous and differentiable. Problems violating these conditions may not be suitable for this method.
