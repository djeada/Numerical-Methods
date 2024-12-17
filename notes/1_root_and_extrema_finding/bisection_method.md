## Introduction

The bisection method is a classical root-finding technique used extensively in numerical analysis to locate a root of a continuous function $f(x)$ within a specified interval $[a, b]$. It belongs to the family of **bracketing methods**, which use intervals known to contain a root and systematically reduce these intervals until the solution is approximated to a desired level of accuracy. While it is not the fastest method, it is revered for its simplicity, guaranteed convergence (under appropriate conditions), and ease of implementation.

Physically and mathematically, the idea is that if a function $f(x)$ crosses the $x$-axis, then there exists a point $x = \alpha$ such that $f(\alpha) = 0$. If the function is continuous and changes sign over an interval $[a,b]$ (that is, $f(a)f(b) < 0$), then by the Intermediate Value Theorem, there must be at least one root in that interval. The bisection method exploits this fact by repeatedly halving the interval until the resulting interval is sufficiently small to approximate the root.

**Conceptual Illustration (Not Removing the Plot)**:

Below is a conceptual plot (not an actual numerical figure here, but imagine a continuous curve of $f(x)$ intersecting the x-axis):

```
 f(x)
  |
  |         *
  |        / \
  |       /   \
  |      /     \   * root approx.
------+-----x------\-----------> x
  a      c       b
```

In the above conceptual plot, the function $f(x)$ crosses the x-axis somewhere between $a$ and $b$. The bisection step chooses the midpoint $c = \frac{a+b}{2}$ to test the sign of $f(c)$. Depending on the sign, the algorithm halves the interval, guaranteeing that the root remains within the new interval. This halving process is repeated iteratively.

## Mathematical Formulation

Consider a continuous function $f : \mathbb{R} \to \mathbb{R}$. Suppose that we know there is at least one root in the interval $[a, b]$. By the Intermediate Value Theorem, if $f(a)f(b) < 0$, there must exist at least one $\alpha \in (a, b)$ such that $f(\alpha) = 0$.

The bisection method proceeds by evaluating the midpoint:

$$c = \frac{a + b}{2}.$$

We then check the sign of $f(c)$:

- If $f(a)f(c) < 0$, then the root lies between $a$ and $c$.
- If $f(c)f(b) < 0$, then the root lies between $c$ and $b$.

In either case, we have reduced the interval size by a factor of 2. After $n$ steps, the interval size is $\frac{b-a}{2^n}$, guaranteeing that we approximate the root to within a prescribed tolerance.

## Derivation

I. **Assumption**: We start with a continuous function $f(x)$ and an initial bracketing interval $[a_0, b_0]$ such that:

$$f(a_0)f(b_0) < 0.$$

This ensures the existence of at least one root $\alpha$ in $(a_0, b_0)$.

II. **First Iteration**:

Compute the midpoint:

$$c_1 = \frac{a_0 + b_0}{2}.$$
Evaluate $f(c_1)$:
- If $f(a_0)f(c_1) < 0$, set $a_1 = a_0$ and $b_1 = c_1$.
- Else, set $a_1 = c_1$ and $b_1 = b_0$.

In either case, the new interval $[a_1, b_1]$ is half the size of $[a_0, b_0]$, and still contains the root.

III. **Subsequent Iterations**:

At the $k$-th iteration:

$$c_k = \frac{a_{k-1} + b_{k-1}}{2},$$
and based on the sign test:

$$f(a_{k-1})f(c_k) < 0 \implies [a_k, b_k] = [a_{k-1}, c_k],$$
or

$$f(c_k)f(b_{k-1}) < 0 \implies [a_k, b_k] = [c_k, b_{k-1}].$$

As iterations proceed, the length of the interval containing the root is:

$$|b_k - a_k| = \frac{|b_0 - a_0|}{2^k}.$$

IV. **Convergence Criterion**:

The process is repeated until the desired precision $\epsilon$ is reached, i.e., when:

$$|b_k - a_k| < \epsilon,$$
or until the maximum number of iterations $n_{\max}$ is exhausted.

## Algorithm Steps

**Pseudocode for the Bisection Method:**

I. **Input**:
- A continuous function $f(x)$.
- Initial interval $[a, b]$ such that $f(a)f(b) < 0$.
- Tolerance $\epsilon > 0$ or maximum iterations $n_{\max}$.
II. **Initialization**:
- Set iteration counter $k = 0$.

III. **Iteration**:

I. Compute the midpoint:

  $$c = \frac{a+b}{2}.$$

II. Evaluate $f(c)$.
III. If $|b-a| < \epsilon$ or $k \geq n_{\max}$:
  - Stop and take $c$ as the approximate root.
IV. Else, determine the sub-interval:
  - If $f(a)f(c) < 0$, set $b = c$.
  - Else, set $a = c$.

V. Increment iteration counter $k = k+1$ and go back to step (3).

IV. **Output**:
- Approximate root $c$.
- Number of iterations performed.

## Example

**Given Function:**

$$f(x) = x^2 - 4.$$

We know $f(0) = -4$ and $f(5) = 25 - 4 = 21$. Thus:

$$f(0)f(5) = (-4)(21) = -84 < 0,$$
so there is at least one root in $[0,5]$.

**Step-by-Step Computation**:

- **Initial Setup:**
- $a_0 = 0$
- $b_0 = 5$
- Interval length: $b_0 - a_0 = 5$
- **Iteration 1**:
- Compute midpoint: 

$$c_1 = \frac{0+5}{2} = 2.5.$$
- Evaluate $f(c_1) = f(2.5) = (2.5)^2 - 4 = 6.25 - 4 = 2.25$.
- Check signs:

$$f(a_0)f(c_1) = f(0)f(2.5) = (-4)(2.25) = -9 < 0.$$
Since this is negative, the root lies in $[0, 2.5]$.
- Update interval:

$$a_1 = 0, \quad b_1 = 2.5.$$

- **Iteration 2**:
- New interval: $[0, 2.5]$
- Midpoint:

$$c_2 = \frac{0+2.5}{2} = 1.25.$$
- Evaluate $f(c_2) = f(1.25) = (1.25)^2 -4 = 1.5625 -4 = -2.4375$.
- Check signs:

$$f(c_2)f(b_1) = (-2.4375)(2.25) < 0.$$
This indicates the root is in $[1.25, 2.5]$.
- Update interval:

$$a_2 = 1.25, \quad b_2 = 2.5.$$

- **Iteration 3**:
- New interval: $[1.25, 2.5]$
- Midpoint:

$$c_3 = \frac{1.25 + 2.5}{2} = 1.875.$$
- Evaluate $f(c_3) = (1.875)^2 -4 = 3.515625 -4 = -0.484375$.
- Check signs:

$$f(c_3)f(b_2) = (-0.484375)(2.25) < 0.$$
So the root is now bracketed in $[1.875, 2.5]$.
- Update interval:

$$a_3 = 1.875, \quad b_3 = 2.5.$$

Continuing this process, as we further narrow down the interval, we find that the root approaches $x=2$. Indeed, $f(2)=0$ exactly, so the root is $x=2$.

## Advantages

I. **Guaranteed Convergence:**  

If $f$ is continuous and the initial interval $[a,b]$ satisfies $f(a)f(b)<0$, the method will converge to a root.

II. **Robustness and Simplicity:**  

The method requires only function evaluations—no derivatives or complicated operations are needed. This makes it easy to understand, implement, and apply to a wide range of problems.

III. **Stable and Predictable Behavior:**  

The number of steps required to achieve a given accuracy can be predicted since the interval size reduces by half each iteration.

## Limitations

I. **Slow Convergence:**  

The bisection method converges linearly, which can be slow compared to other methods like Newton-Raphson or Secant methods, especially for well-behaved functions where derivative information is available.

II. **Requires Initial Bracketing of the Root:**  

You must know two points $[a,b]$ such that $f(a)f(b)<0$. If no such interval is known, it can be hard to apply the method.

III. **Single Root Finding in a Given Interval:**  

The method only finds one root in a given interval. If multiple roots exist, each must be isolated and bracketed separately.

IV. **Not Ideal for Complex or Multiple Roots Situations:**  

The method does not take advantage of any additional information like derivatives or higher-order approximations. Thus, it may not be suitable for more complicated root-finding scenarios where more advanced methods excel.
