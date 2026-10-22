# Secant Method

The secant method approximates a root of $f(x)=0$ using the two most recent points on the graph. Instead of evaluating the derivative in Newton's formula, it uses the slope of the secant line through those points. The next approximation is the zero of that line. This makes the method useful when an analytic derivative is unavailable or inconvenient to evaluate. For a sufficiently smooth function near a simple root, it can converge faster than a linearly convergent bracketing method, although it does not preserve a bracket and need not converge from arbitrary starting values. A function can be evaluated without being differentiable, but the familiar superlinear rate requires the additional local smoothness discussed below.

Conceptually, the secant method constructs a secant line between two points $(x_{n-1}, f(x_{n-1}))$ and $(x_n, f(x_n))$ on the graph of $f(x)$. The root approximation is then taken as the $x$-intercept of this secant line. By iteratively updating these points, the method “zeroes in” on a root.

**Conceptual Illustration**:

Imagine plotting the function $f(x)$:

![Secant-line intercepts approximating a root](https://github.com/user-attachments/assets/5e904eb0-1c4f-499a-9937-39fcdb210fde)

The intersection of the secant line with the x-axis gives the next approximation $x_{n+1}$. Repeating this procedure leads to progressively better approximations of the root, assuming the method converges.

## Mathematical formulation

Consider a continuous function $f(x)$ for which we want to solve $f(x)=0$. The secant method starts with two initial approximations $x_0$ and $x_1$, and then generates a sequence $\{x_n\}$ according to:

$$
x_{n+1} = x_n - f(x_n) \frac{x_n - x_{n-1}}{f(x_n) - f(x_{n-1})}
$$

This formula approximates the derivative $f'(x_n)$ by the finite difference:

$$
f'(x_n) \approx \frac{f(x_n)-f(x_{n-1})}{x_n - x_{n-1}}
$$

By replacing $f'(x_n)$ with the above approximation in the Newton's method formula, we arrive at the secant method formula.

## Derivation

**Step 1: Starting from Newton’s method.**

Newton’s method update rule is:

$$
x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}.
$$

**Step 2: Approximating the derivative.**

If the derivative $f'(x_n)$ is difficult to compute or unknown, we can use a finite difference approximation based on the two most recent points:

$$
f'(x_n) \approx \frac{f(x_n)-f(x_{n-1})}{x_n - x_{n-1}}.
$$

**Step 3: Substitute into Newton’s formula.**

Replacing $f'(x_n)$ with this approximation gives:

$$
x_{n+1} = x_n - \frac{f(x_n)}{\frac{f(x_n)-f(x_{n-1})}{x_n - x_{n-1}}}.
$$

**Step 4: Simplify the expression.**

By rearranging, we get:

$$
x_{n+1} = x_n - f(x_n) \frac{x_n - x_{n-1}}{f(x_n)-f(x_{n-1})}.
$$

This is the secant method iteration formula.

### Why the convergence order is the golden ratio

For a sufficiently smooth function near a simple root $r$, the local errors $e_n=x_n-r$ satisfy, to leading order,

$$
e_{n+1}\approx C e_n e_{n-1},\qquad C=\frac{f''(r)}{2f'(r)}.
$$

This relation follows by expanding the two function values in the secant formula about $r$: the linear terms cancel, leaving the product of the two previous errors. If the asymptotic order is $p$, so $|e_n|\approx A|e_{n-1}|^p$, then $|e_{n-1}|$ scales like $|e_n|^{1/p}$. The error relation therefore requires

$$
p=1+\frac1p,\qquad p^2-p-1=0,\qquad p=\frac{1+\sqrt5}{2}.
$$

This is a local result for sufficiently close, distinct starting values at a simple root; it is not a guarantee for every continuous function. If the leading constant vanishes, the order can differ.

The denominator must be checked **before** division. Equal function values make the secant horizontal, while nearly equal values can magnify evaluation errors into a very large step. Unlike false position, secant iteration retains the latest two iterates rather than a sign-changing bracket, so the next point may lie outside the previous interval. Caching the surviving function value would require only one new evaluation per iteration after initialization. The compact repository implementation recomputes both function values at each step, so its evaluation count follows that implementation choice.

## Algorithm steps

**Input:**

- A function $f(x)$.
- Two initial points $x_0$ and $x_1$.
- A tolerance $\epsilon > 0$ or a maximum number of iterations $n_{\max}$.

**Initialization:**

Set $n=1$ (since we already have $x_0$ and $x_1$).

**Iteration:**

**Step 1.** Evaluate $f(x_{n})$ and $f(x_{n-1})$.

II. First check that $f(x_n)-f(x_{n-1})$ is nonzero and that the resulting arithmetic is finite. Then compute:

$$
x_{n+1} = x_n - f(x_n) \frac{x_n - x_{n-1}}{f(x_n)-f(x_{n-1})}
$$

**Step 3.** Check for convergence:

- If $|x_{n+1}-x_n|< \epsilon$, stop and return $x_{n+1}$. (The residual $|f(x_{n+1})|$ is not tested.)
- If $n_{\max}$ iterations have been performed without meeting this test, stop with an error (non-convergence).
- If $f(x_n) = f(x_{n-1})$ exactly, the update is undefined (division by zero) and the method stops with an error.

**Step 4.** Update indices: $n = n+1$ and repeat step I.

**Output:**

- Approximate root $x_{n+1}$.
- Number of iterations performed, if tracked as a diagnostic. The repository function `secant_method` returns only the approximate point, rather than a point-and-count pair.

## Example

**Given Function:**

$$
f(x) = x^2 - 4.
$$

We know the roots are $x=\pm 2$. Suppose we do not know the roots in advance and start with:

$$
x_0 = 0, \quad x_1 = 1
$$

**Iteration 1:**

- $f(x_0)=f(0)=0^2-4=-4$.
- $f(x_1)=f(1)=1^2-4=-3$.

Update:

$$
x_2 = x_1 - f(x_1) \frac{x_1 - x_0}{f(x_1)-f(x_0)} = 1 - (-3)
\frac{1-0}{(-3)-(-4)} = 1 - (-3) \frac{1}{-3+4} = 1 - (-3 \times 1) = 1 + 3 = 4.
$$

**Iteration 2:**

Now:

- $x_1=1, x_2=4$.
- $f(1)=-3, f(4)=4^2-4=16-4=12.$

Update:

$$
x_3 = x_2 - f(x_2) \frac{x_2 - x_1}{f(x_2)-f(x_1)} = 4 - 12 \frac{4-1}{12-(-3)} = 4 - 12
\frac{3}{15} = 4 - 12 \times 0.2 = 4 - 2.4 = 1.6.
$$

**Iteration 3:**

Now:

- $x_2=4, x_3=1.6$.
- $f(4)=12, f(1.6)=1.6^2-4=2.56-4=-1.44.$

Update:

$$
x_4 = x_3 - f(x_3) \frac{x_3 - x_2}{f(x_3)-f(x_2)} = 1.6 - (-1.44)
\frac{1.6-4}{-1.44-12}
$$

$$
= 1.6 - (-1.44) \frac{-2.4}{-13.44}
$$

Compute inside:

$$
\frac{-2.4}{-13.44} = 0.1786 \text{(approx)}, \quad (-1.44)\times0.1786 = -0.2571
$$

So:

$$
x_4 = 1.6 - (-0.2571) = 1.6 + 0.2571 = 1.8571
$$

Repeating further will bring the sequence closer to $x=2$.

The first step also shows why the starting values matter: the secant intercept can initially move farther from the desired root, even when later iterates converge. For example, if we start with $x_0=0$ and $x_1=1$, after the first step we got $x_2=4$, which moved us away initially, but subsequent steps pull the approximation toward $x=2$. Adjusting initial guesses (e.g., starting with $x_0=1$ and $x_1=3$) might yield quicker convergence to the root $x=2$.

## Advantages

- The secant method avoids requiring an **analytic derivative**, unlike Newton’s method, which is particularly useful for functions that are difficult or impossible to differentiate analytically.
- Convergence in the secant method is typically **faster than linear convergence**, which is common in the bisection method, though it is not as fast as the quadratic convergence seen in Newton's method.
- The secant method is easy to **implement due to its simple iterative formula**, which relies only on function evaluations and does not require derivative or interval-based calculations.

## Limitations

- Convergence is not **guaranteed**, as poor initial guesses can cause divergence or failure to find a root.
- Functions with **multiple roots** pose challenges because the secant method may converge to an unintended root if the initial guesses are closer to a different zero.
- The method’s **stability and efficiency are highly dependent** on the initial guesses, $x_0$ and $x_1$, which play a critical role in determining whether the method converges and how quickly.
- The secant method does not offer **quadratic convergence** like Newton’s method, resulting in slower convergence rates compared to derivative-based methods when derivatives are available and feasible to compute.
