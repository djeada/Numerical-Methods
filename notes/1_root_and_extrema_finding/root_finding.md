# Root-Finding in Numerical Methods

Root-finding algorithms aim to solve equations of the form

$$
f(x) = 0
$$

for a scalar (or vector) variable $x$. Although linear problems $\,ax + b = 0\,$ admit the straightforward solution $x = -b/a$, many practical applications involve **nonlinear** equations—polynomial or transcendental—where closed-form solutions may be unavailable or difficult to find. Consequently, numerical methods are indispensable for approximating roots.

## Relevance and applications

- **Root-finding** is used in engineering to determine operating points and equilibrium solutions in mechanical, electrical, or chemical systems.
- In **physics**, root-finding helps solve boundary value problems, locate energy eigenstates, or find intersection points in scattering problems.
- In **computer science and machine learning**, root-finding is involved in optimizing objective functions, which can reduce to solving $\nabla f(x) = 0$.
- **Financial applications** include calculating implied volatilities or internal rates of return, often involving transcendental equations that require root-finding.
- Solving **nonlinear systems** in higher dimensions, such as $\mathbf{f}(\mathbf{x}) = \mathbf{0}$, extends 1D root-finding methods (e.g., Newton’s method generalizes to Newton–Raphson for multiple dimensions).

## Basic concepts

### Root

A **root** $r$ of a function $f$ is a solution to

$$
f(r) = 0.
$$

Depending on $f$:

1. **Polynomial functions** $f(x) = a_n x^n + \dots + a_0$ may have multiple real or complex roots.
2. **Transcendental functions** (e.g., $\sin x$, $\exp x$, $\log x$) may have infinitely many roots or require special methods.
3. **Generalized exponents** or radicals ($x^\pi, x^{3/5}, \sqrt{x}, \ldots$) introduce domain constraints or branch cuts.

### Brackets and the intermediate value theorem

A **bracket** $[a,b]$ is an interval such that

$$
f(a)\, f(b) < 0.
$$

Provided $f$ is **continuous** on $[a,b]$, the **Intermediate Value Theorem (IVT)** guarantees there is at least one root in $[a,b]$. This property underpins **bracketing methods**, ensuring that each iteration can reduce the interval size while preserving a sign change that encloses a root.

> **Note**: If $f$ is not continuous, sign changes do not necessarily imply roots in that interval.

### Convergence

An iterative method generates a sequence of approximations $\{x_k\}$. If $x_k \to r$ as $k \to \infty$ (for some root $r$), we say the method **converges** to $r$. The **rate of convergence** is an important property:

- **Linear convergence**: $\lvert x_{k+1} - r\rvert \approx C \,\lvert x_k - r\rvert$ for some $C < 1$.
- **Quadratic convergence**: $\lvert x_{k+1} - r\rvert \approx K \,\lvert x_k - r\rvert^2$.

For example, Bisection typically has **linear convergence**, while Newton’s method can exhibit **quadratic convergence** (under favorable conditions).

### Tolerance

A **tolerance** $\varepsilon$ is chosen so that when

$$
\lvert x_{k+1} - x_k\rvert \,<\, \varepsilon \quad \text{or}\quad \lvert f(x_k)\rvert
\,<\, \delta,
$$
we consider the root sufficiently approximated and stop. The choice of $\varepsilon$ and $\delta$ depends on the application’s precision needs.

### Residual, position error, and conditioning

The **residual** $|f(\widehat r)|$ tells us how well an approximation satisfies the equation; the **position error** $|\widehat r-r|$ tells us how close it is to a particular root. Near a simple root, Taylor expansion gives

$$
f(\widehat r)=f'(r)(\widehat r-r)+O((\widehat r-r)^2),\qquad \widehat r-r\approx\frac{f(\widehat r)}{f'(r)}.
$$

A small derivative can amplify a small residual into a larger position error. For example, $f(x)=10^{-12}(x-1)$ has residual $10^{-12}$ at $x=2$, even though the position error is $1$. Multiplying an equation by a constant changes its residual without changing its roots.

A practical step test combines absolute and relative tolerances,

$$
|x_{k+1}-x_k|\leq\epsilon_{\mathrm{abs}}+\epsilon_{\mathrm{rel}}|x_{k+1}|,
$$

and is interpreted alongside a suitably scaled residual or a certified bracket width. A small step alone can mean stagnation. An iteration limit reports failure to meet the requested criterion, rather than establishing that the last iterate is accurate.

A **simple root** satisfies $f'(r)\ne0$. A root of multiplicity $m>1$ has the form $f(x)=(x-r)^m h(x)$ with $h(r)\ne0$. Even multiplicities need not produce a sign change, so scanning for sign changes can miss them. The scalar methods in this chapter should also be distinguished from optimization: solving $f'(x)=0$ finds stationary points, whose classification requires further analysis.

## Common root-finding methods

Root-finding methods can be broadly classified into **bracketing** (guaranteed convergence under certain assumptions) and **open** methods (faster convergence but risk of divergence). Some methods combine both aspects.

### Bracketing methods

#### Bisection method

- Start with an interval $[a_0, b_0]$ where $f(a_0)f(b_0) < 0$ to ensure the presence of a root.
- Calculate the midpoint $m = \frac{a_k + b_k}{2}$ of the current interval.
- If $f(a_k)f(m) < 0$, update the interval to $[a_{k+1}, b_{k+1}] = [a_k, m]$.
- If $f(m)=0$, return $m$ immediately. Otherwise, if $f(a_k)f(m)>0$, update the interval to $[a_{k+1}, b_{k+1}] = [m,b_k]$.
- The method halves the interval length in each iteration, leading to linear convergence with a ratio of 0.5.
- After $n$ steps, the bracket size reduces to $\frac{b_0 - a_0}{2^n}$.

#### False position (regula falsi)

- Select an interval $[a, b]$ such that $f(a)f(b) < 0$, ensuring the presence of a root in the interval.
- Compute the interpolated point $x_{\text{interp}} = \frac{a f(b) - b f(a)}{f(b) - f(a)}$ using linear interpolation between $(a, f(a))$ and $(b, f(b))$.
- Evaluate $f(x_{\text{interp}})$ to check which subinterval contains the root.
- If $f(a)f(x_{\text{interp}}) < 0$, update the interval to $[a, x_{\text{interp}}]$.
- If $f(a)f(x_{\text{interp}}) \geq 0$, update the interval to $[x_{\text{interp}}, b]$.
- Repeat the computation of $x_{\text{interp}}$ and interval updates until the stopping condition is met.
- Stop when $|b - a|$ or $|f(x_{\text{interp}})|$ is smaller than the predefined tolerance.
- The final result is the root approximation $x_{\text{interp}}$ with accuracy determined by the chosen tolerance.

An exact zero at the interpolation point is returned immediately. In classical false position, one endpoint can remain fixed for many steps, so the bracket width may not approach zero even while the interpolated points converge. A residual test, interpreted with conditioning information, or a modified false-position method is useful in this case.

### Open methods

Open methods rely on derivative information or estimates, and do not require an initial bracket. However, they can fail to converge if poorly chosen initial guesses or pathological function behavior occurs.

#### Newton’s method

- Start with an initial guess $x_0$ for the root of $f(x) = 0$.
- Compute the next approximation using the formula $x_{k+1} = x_k - \frac{f(x_k)}{f'(x_k)}$.
- At each step, approximate $f(x)$ by the tangent line at $x_k$ and solve for the root of this tangent.
- The method exhibits **quadratic convergence** near simple roots when $f'(r) \neq 0$, as the error reduces quadratically with each iteration.
- The convergence rate satisfies $\lim_{k \to \infty} \frac{|x_{k+1} - r|}{|x_k - r|^2} = \text{constant}$.
- The method requires the derivative $f'(x)$, which must be computed or approximated if unavailable.
- If $f'(x_k) \approx 0$, the method can diverge or produce large, inaccurate jumps.
- Without a guaranteed bracket, the method may fail if the initial guess $x_0$ is too far from the actual root.

#### Secant method

- The **idea** is to approximate $f'(x_k)$ using a finite difference, resulting in the formula $f'(x_k) \approx \frac{f(x_k) - f(x_{k-1})}{x_k - x_{k-1}}$.
- The iterative formula is derived as $x_{k+1} = x_k - f(x_k) \frac{x_k - x_{k-1}}{f(x_k) - f(x_{k-1})}$, replacing the derivative in Newton's method.
- The method typically exhibits **superlinear convergence** with a rate close to $1.618$, which is the golden ratio.
- This approach is **useful** because it avoids the need for an explicit derivative function, relying instead on previous function evaluations.

### Combination methods

- Start with a bracket $[a_0, b_0]$ such that $f(a_0)f(b_0) < 0$, ensuring a root exists within the interval.
- Evaluate $f(a)$ and $f(b)$, and initialize $c = b$ as the last valid root approximation.
- At each iteration, compute an interpolation candidate $x_{\text{interp}}$ using either secant or inverse quadratic interpolation based on the most recent points.
- Check if $x_{\text{interp}}$ falls within the bracket $[a, b]$ and provides sufficient progress toward the root.
- If $x_{\text{interp}}$ is valid and improves the approximation, update the bracket to $[a, x_{\text{interp}}]$ or $[x_{\text{interp}}, b]$ based on the sign of $f(x_{\text{interp}})$.
- If $x_{\text{interp}}$ fails or is outside the bracket, perform a bisection step by setting the midpoint of the bracket as the next approximation.
- Update $c$ to the most recent approximation, ensuring $c$ always represents the last reliable approximation of the root.
- Repeat the process until the stopping condition is met, typically when the interval size or $f(c)$ is below a predefined tolerance.
- The final result is the approximation $c$, which satisfies the convergence criteria.

## Checking the domain before iterating

The numerical problem includes the domain of $f$, not just its formula. For $f(x)=\log x-c$, every iterate must satisfy $x>0$. A secant or Newton step may leave that domain even when its starting points are valid; a bracket wholly inside the domain provides a useful safeguard. Likewise, a sign change across a pole is not a root certificate: $f(x)=1/x$ changes sign across zero, but is discontinuous there and never vanishes. Locate singularities and excluded points before scanning for brackets or interpreting a small step as convergence.

## Choosing a root-finding method

- **Continuity** ensures that a bracketing method can reliably locate a root, as the existence of a sign change guarantees a solution within the interval.
- **Differentiability** allows for use of methods like Newton's, which rely on first derivatives to predict the root. If the derivative is unavailable, alternative methods such as secant or bisection are better options.
- **Multiplicity of roots** poses challenges for Newton’s method; when a root is not simple (e.g., $f(r) = 0$ but $f'(r) = 0$), the method can converge very slowly or fail entirely.
- **Bracketing methods** like bisection are robust because they systematically narrow the interval containing the root, but their linear convergence makes them slower for high-precision needs.
- **Open methods** such as Newton's or secant can converge much faster, often at a superlinear or quadratic rate, but they require good initial guesses to avoid divergence or incorrect results.
- **Computational cost** can escalate when functions or their derivatives are complex to evaluate, making derivative-free methods like secant attractive as they avoid calculating derivatives directly. However, they may require more iterations to achieve the same accuracy.
- **Hybrid approaches** combine reliability and speed by starting with a bracketing method like bisection to secure the root interval, then transitioning to faster methods like Newton's or secant once near the solution.
- **Combination methods** like Brent’s dynamically adapt between bracketing and open techniques, providing both robustness of convergence and faster refinement when conditions are favorable.

### Example flow of decision

- Determine if $f(x)$ has an easily detectable sign change.
- If a sign change is present, use bracketing methods like bisection or false position to isolate the root.
- If no sign change is found, scan the domain or apply domain knowledge to guess a valid interval.
- Assess if $f'(x)$ is analytically or numerically cheap to compute.
- If derivatives are easy to compute, use Newton’s method for faster local convergence.
- If derivatives are not available or are expensive, use derivative-free methods like secant.
- Decide if reliability is a key priority for the solution.
- If reliability is critical, select robust methods like Brent’s, which combine bracketing and open steps.
