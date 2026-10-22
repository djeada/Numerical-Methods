# Golden Ratio Search

The Golden Ratio Search is a technique employed for locating the extremum (minimum or maximum) of a unimodal function over a given interval. Unlike gradient-based or derivative-requiring methods, this approach uses only function evaluations, making it broadly applicable even when derivatives are difficult or impossible to compute. The method takes its name from the special constant known as the golden ratio $\phi$, which uniquely balances intervals to reduce the problem domain efficiently.

For a unimodal function $f(x)$ defined on an interval $[a,b]$, the Golden Ratio Search progressively narrows down the search interval by evaluating the function at two strategically chosen internal points. By leveraging the intrinsic ratio $\phi$, each iteration reduces the size of the interval while ensuring that no potential minima are prematurely excluded. This process continues until the interval is sufficiently small, providing an approximation to the function’s minimum (or maximum, if desired by adjusting the comparison conditions).

**Conceptual Illustration**:

Imagine the graph of a unimodal function $f(x)$. The goal is to isolate the minimum within a progressively smaller bracket. Initially, we have the interval $[a,b]$:

![Golden-ratio interior points and minimizer brackets](https://github.com/user-attachments/assets/805e7e1d-4f17-457f-88e9-3e26753d5f50)

We pick two points $x_1$ and $x_2$ inside $[a,b]$ using the golden ratio partitioning. Based on the function values at these points, we eliminate a portion of the interval that cannot contain the minimum. This procedure repeats, each time reducing the interval size while maintaining the guarantee of containing the minimum.

## Mathematical Formulation

The golden ratio is defined as:

$$
\phi = \frac{1 + \sqrt{5}}{2} \approx 1.618.
$$

This constant has unique properties, notably:

$$
\frac{1}{\phi} = \phi - 1 \approx 0.618.
$$

To apply the Golden Ratio Search for minimization, we start with an interval $[a,b]$ and choose two internal points $x_1$ and $x_2$ such that:

$$
x_1 = b - \frac{b-a}{\phi}, \quad x_2 = a + \frac{b-a}{\phi}.
$$

It follows from this construction that:

$$
\frac{b - a}{x_2 - a} = \phi.
$$

Because of how $\phi$ partitions the interval, the ratio of the smaller subinterval to the larger subinterval is equal to $1/\phi$, ensuring a consistent and balanced reduction.

## Derivation

I. **Unimodality Assumption:**

Assume $f(x)$ is unimodal on $[a,b]$, meaning it has a single minimum within that interval. Without loss of generality, we focus on minimizing $f(x)$.

II. **Golden Ratio Partition:**

Given the interval $[a,b]$, we introduce points $x_1$ and $x_2$ as described:

$$
x_1 = b - \frac{b-a}{\phi}, \quad x_2 = a + \frac{b-a}{\phi}.
$$

By doing so, we ensure:

$$
x_1 < x_2, \quad a < x_1 < x_2 < b.
$$

III. **Decision Criterion:**

We evaluate $f(x_1)$ and $f(x_2)$:

- If $f(x_1) > f(x_2)$, then the minimum must lie in $[x_1,b]$, because the function is smaller at $x_2$ and the segment $[a,x_1]$ can be safely discarded.
- If $f(x_1) < f(x_2)$, then the minimum must lie in $[a,x_2]$, discarding the segment $[x_2,b]$.

In either case, the length of the interval is reduced by a factor approximately $\frac{1}{\phi}$ each iteration, ensuring rapid convergence.

IV. **Convergence:**

After $n$ iterations, the length of the interval is:

$$
|b - a| \left(\frac{1}{\phi}\right)^n.
$$

Once this length is less than a prescribed tolerance $\epsilon$, we accept that the minimum is approximated by any point within the current interval.

### Where the Golden Ratio Comes From

Write the retained fraction as $\rho=1/\phi$, so the two points lie at $a+(1-\rho)(b-a)$ and $a+\rho(b-a)$. If the left interval $[a,x_2]$ is retained, its length is $\rho(b-a)$. Reusing the old $x_1$ as the new right interior point requires

$$
1-\rho=\rho^2,\qquad \rho^2+\rho-1=0,\qquad \rho=\frac{\sqrt5-1}{2}.
$$

The same condition works when the right interval is retained. This self-similarity, rather than the numerical value alone, saves one function evaluation at each step.

For the standard minimizer-preservation argument, assume $f$ decreases strictly up to its minimizer and increases strictly afterwards. Merely having one local minimum without this monotonic structure is insufficient. Under this strict assumption, an exact tie $f(x_1)=f(x_2)$ places the minimizer in $[x_1,x_2]$, so the mathematical algorithm may retain that interval and continue. The implementation described below instead returns the current midpoint on a tie; that is an early-exit convention and does **not** certify the requested interval tolerance for a general asymmetric function. Broad plateaus and floating point ties need additional care.

With no early exit, after $n$ reductions the width is $L_n=\rho^n L_0$. The final midpoint has position error at most $L_n/2$, so a target $\epsilon_x$ is met when $\rho^n L_0\leq2\epsilon_x$. For maximization, apply the same procedure to $-f$.

## Algorithm Steps

**Input:**

- A continuous unimodal function $f(x)$.
- Initial interval $[a,b]$.
- Tolerance $\epsilon > 0$ or maximum iterations $n_{\max}$.

**Initialization:**

- Define $\phi = \frac{1 + \sqrt{5}}{2}$.
- Set iteration counter $k = 0$.

**Iteration:**

I. Compute (only before the first iteration; later iterations reuse a point, see step III):

$$
x_1 = b - \frac{b-a}{\phi}, \quad x_2 = a + \frac{b-a}{\phi},
$$

and evaluate $f(x_1)$ and $f(x_2)$.

II. If $f(x_1)=f(x_2)$, the implementation stops and returns $\frac{a+b}{2}$. The tie does not choose between the two usual one-sided updates. Under strict unimodality, the mathematical algorithm can instead retain $[x_1,x_2]$ and continue, as explained above; the implementation’s immediate return does not certify the width tolerance.

III. If $f(x_1) > f(x_2)$:

Set $a = x_1$, $x_1 = x_2$, $f(x_1) = f(x_2)$, and compute a new $x_2 = a + \frac{b-a}{\phi}$.

(The minimum is in the interval $[x_1,b]$)

Else ($f(x_1) < f(x_2)$):

Set $b = x_2$, $x_2 = x_1$, $f(x_2) = f(x_1)$, and compute a new $x_1 = b - \frac{b-a}{\phi}$.

(The minimum is in the interval $[a,x_2]$)

Because of the golden ratio, the surviving interior point is exactly one of the two interior points of the smaller interval, so only **one new function evaluation** is needed per iteration.

IV. If $|b-a| < \epsilon$:

Stop and approximate the minimum as $\frac{a+b}{2}$. If $k \geq n_{\max}$ without reaching this, the implementation raises an error.

V. Otherwise evaluate $f$ at the new interior point, increment $k = k+1$ and go back to step II.

**Output:**

- Approximate location of the minimum.
- Number of iterations performed, if tracked as a diagnostic. The repository function `golden_ratio_search` returns only the approximate point, rather than a point-and-count pair.

## Example

**Given Function:**

$$
f(x) = x^2.
$$

We know that $f(x)=x^2$ is unimodal (in fact, strictly convex) on any interval, and it attains its minimum at $x=0$.

**Initial Setup:**

$$
a = -2, \quad b = 2, \quad \phi = \frac{1+\sqrt{5}}{2} \approx 1.618.
$$

**Iteration 1:**

Compute:

$$
x_1 = b - \frac{b-a}{\phi} = 2 - \frac{2 - (-2)}{1.618} = 2 - \frac{4}{1.618} \approx
2 - 2.472 \approx - 0.472.
$$

$$
x_2 = a + \frac{b-a}{\phi} = -2 + \frac{4}{1.618} \approx - 2 + 2.472 = 0.472.
$$

Evaluate:

$$
f(x_1) = (-0.472)^2 \approx 0.2228, \quad f(x_2) = (0.472)^2 \approx 0.2228.
$$

Since $f(x_1)=f(x_2)$, strict unimodality places the minimizer between the two samples. The implementation would stop here and return the current midpoint $0$, which is exact for this symmetric function; that exactness does not extend to every function with tied samples. To illustrate the iteration, let’s instead choose $[a,b] = [-2, x_2] = [-2, 0.472]$. So:

$$
b = 0.472.
$$

**Iteration 2:**

New interval: $[a,b] = [-2,0.472]$

Compute new points:

$$
x_1 = b - \frac{b-a}{\phi} = 0.472 - \frac{0.472 - (-2)}{1.618} = 0.472 -
\frac{2.472}{1.618} \approx 0.472 - 1.528 \approx - 1.056.
$$

$$
x_2 = a + \frac{b-a}{\phi} = -2 + \frac{2.472}{1.618} \approx - 2 + 1.528 = -0.472.
$$

Evaluate:

$$
f(x_1) = (-1.056)^2 \approx 1.115, \quad f(x_2) = (-0.472)^2 \approx 0.223.
$$

Compare:

$$
f(x_1) = 1.115, \quad f(x_2) = 0.223.
$$

Since $f(x_1) > f(x_2)$, the minimum lies in $[x_1,b]$, so we set:

$$
a = x_1 = -1.056
$$

giving $[a,b] = [-1.056, 0.472]$. The old $x_2 = -0.472$ is also an interior point of the new interval (it becomes the new $x_1$), so its value $f(-0.472)$ is reused and only the new $x_2$ has to be evaluated.

**Subsequent Iterations:**

At each iteration, you would similarly compute new $x_1, x_2$, evaluate $f(x_1)$ and $f(x_2)$, and narrow down the interval. Ultimately, as you continue, the interval will shrink around $x=0$, since $f(x) = x^2$ achieves its minimum at $x=0$.

## Advantages

1. **No derivatives required** makes the Golden Ratio Search ideal for problems where derivative information is unavailable or too expensive to compute.
2. **Guaranteed reduction** of the search interval by approximately $\frac{1}{\phi}$ (the Golden Ratio) in each iteration ensures steady progress toward locating the minimum.
3. The method's **robustness** guarantees convergence to a minimum within the provided interval, assuming the function is unimodal.
4. **Simplicity of implementation** makes the algorithm accessible, as it involves straightforward iterative calculations without the need for complex procedures.
5. **One function evaluation per iteration**, since one interior point is reused after each reduction, which matters when $f$ is expensive.

## Limitations

1. **Unimodality required** means the method assumes the function has only one minimum in the interval; multiple minima can lead to convergence to a local minimum or failure to isolate a solution.
2. **Initial bracketing** of the interval $[a, b]$ containing the minimum is essential, and determining this interval can be challenging if the function's behavior is poorly understood.
3. The method is **not the fastest** for all problems, particularly when gradient-based methods like Newton’s method or quasi-Newton methods can be used effectively.
4. **Limited attainable accuracy and ties** arise because the method only compares function values. Near a smooth minimum, changes in the objective are often quadratic in the distance from the minimizer. If a nonzero function-value scale $F$ masks changes smaller than $\epsilon_{\text{mach}}F$, local curvature $f''(x^*)>0$ suggests a resolution scale of order $\sqrt{\epsilon_{\text{mach}}F/f''(x^*)}$. With quantities scaled near one, this is roughly $10^{-8}$ in double precision. The estimate depends on scaling and evaluation error: a function such as $x^2$ with zero minimum need not have that same absolute accuracy limit. Below the distinguishable function-value scale, a smaller requested tolerance may lead to a tie or comparisons dominated by rounding. An exact tie $f(x_1)=f(x_2)$ has the minimizer-bracketing interpretation discussed above only under the strict unimodality assumption; a constant plateau or a rounded equality does not justify returning a uniquely accurate location. The implementation returns the current midpoint on a tie and may therefore stop before the requested width is reached. On iterations that continue, the width decreases by $1/\phi$; the stopping convention and the distinguishability of function values limit the final accuracy.
