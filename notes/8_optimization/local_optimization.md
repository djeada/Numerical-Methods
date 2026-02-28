## Local Optimization

Local optimization methods seek a point in the neighborhood of a starting guess where the objective function attains a (local) minimum. These algorithms are the workhorses of continuous optimization: given a differentiable function and a reasonable initial point, they follow the local geometry of the function — captured by gradients and, optionally, curvature information — to converge efficiently to a nearby stationary point. While they cannot guarantee finding the global minimum of a non-convex function, their speed, well-understood convergence theory, and low per-iteration cost make them indispensable in scientific computing, machine learning, engineering design, and statistics.

The two most prominent families are **gradient descent** (first-order) and **Newton's method** (second-order). Gradient descent uses only the gradient $\nabla f$ to choose a search direction, while Newton's method additionally uses the Hessian $\nabla^2 f$ (or an approximation thereof) to account for curvature. Quasi-Newton methods, such as **BFGS**, strike a practical balance by building an approximate Hessian from gradient information alone, achieving superlinear convergence without the cost of computing or inverting the exact Hessian.

**Conceptual Illustration**:

Imagine standing on a hilly landscape in fog so thick that you can only feel the slope beneath your feet. Gradient descent tells you to walk directly downhill — the steepest descent direction. Newton's method is like having an additional sense for the curvature of the ground: it not only knows the slope but also anticipates how the slope changes, allowing it to take a more informed step that can reach the valley floor in fewer strides. Quasi-Newton methods approximate this curvature sense from the slopes you have already measured at previous locations.

### Mathematical Formulation

Given a twice-differentiable function $f : \mathbb{R}^n \to \mathbb{R}$, the goal is:

$$\min_{x \in \mathbb{R}^n} f(x).$$

**Gradient Descent Update**:

$$x_{k+1} = x_k - \alpha_k \nabla f(x_k),$$

where $\alpha_k > 0$ is the step size (learning rate).

**Newton's Method Update**:

$$x_{k+1} = x_k - [\nabla^2 f(x_k)]^{-1} \nabla f(x_k).$$

This is derived by minimizing the second-order Taylor approximation of $f$ around $x_k$:

$$f(x) \approx f(x_k) + \nabla f(x_k)^\top (x - x_k) + \frac{1}{2} (x - x_k)^\top \nabla^2 f(x_k) (x - x_k).$$

Setting the gradient of this quadratic model to zero gives the Newton step.

**BFGS Update**:

The BFGS (Broyden–Fletcher–Goldfarb–Shanno) method replaces the exact Hessian $\nabla^2 f(x_k)$ with an approximation $B_k$ that is updated at each iteration using gradient differences. The search direction is:

$$d_k = -B_k^{-1} \nabla f(x_k),$$

and after computing $s_k = x_{k+1} - x_k$ and $y_k = \nabla f(x_{k+1}) - \nabla f(x_k)$, the inverse Hessian approximation $H_k = B_k^{-1}$ is updated by:

$$H_{k+1} = \left(I - \rho_k s_k y_k^\top \right) H_k \left(I - \rho_k y_k s_k^\top \right) + \rho_k s_k s_k^\top,$$

where $\rho_k = \frac{1}{y_k^\top s_k}$.

### Derivation

I. **Gradient Descent from Taylor Expansion**:

The first-order Taylor expansion of $f$ at $x_k$ is:

$$f(x_k + d) \approx f(x_k) + \nabla f(x_k)^\top d.$$

To decrease $f$, we choose $d$ so that $\nabla f(x_k)^\top d < 0$. The direction that maximally decreases the linear model per unit step is:

$$d = -\nabla f(x_k).$$

With step size $\alpha_k$, the update becomes $x_{k+1} = x_k - \alpha_k \nabla f(x_k)$.

For a convex quadratic $f(x) = \frac{1}{2} x^\top A x - b^\top x$ with condition number $\kappa = \lambda_{\max}(A)/\lambda_{\min}(A)$, gradient descent with optimal step size converges linearly:

$$f(x_{k+1}) - f(x^*) \leq \left(\frac{\kappa - 1}{\kappa + 1}\right)^2 [f(x_k) - f(x^*)].$$

II. **Newton's Method from Quadratic Model**:

The second-order Taylor expansion at $x_k$ is:

$$m_k(d) = f(x_k) + \nabla f(x_k)^\top d + \frac{1}{2} d^\top \nabla^2 f(x_k) \, d.$$

Setting $\nabla_d m_k = 0$:

$$\nabla f(x_k) + \nabla^2 f(x_k) \, d = 0 \implies d_k^N = -[\nabla^2 f(x_k)]^{-1} \nabla f(x_k).$$

Near a strict local minimum where $\nabla^2 f(x^*) \succ 0$, Newton's method converges quadratically:

$$\|x_{k+1} - x^*\| \leq C \|x_k - x^*\|^2$$

for some constant $C > 0$, provided $x_0$ is sufficiently close to $x^*$.

III. **BFGS as a Quasi-Newton Scheme**:

BFGS maintains the **secant condition**:

$$B_{k+1} s_k = y_k,$$

which ensures the approximate Hessian $B_{k+1}$ correctly models the curvature along the most recent step. The BFGS update is the unique symmetric positive-definite update satisfying this condition that is closest to $B_k$ in a weighted Frobenius norm. In practice, BFGS achieves **superlinear convergence** — faster than gradient descent but not quite quadratic — without requiring explicit Hessian computations.

### Algorithm Steps

**BFGS Algorithm**:

**Input:**

- A twice-differentiable function $f(x)$ and its gradient $\nabla f(x)$.
- A starting point $x_0 \in \mathbb{R}^n$.
- An initial inverse Hessian approximation $H_0 = I$ (the identity matrix).
- Convergence tolerance $\epsilon > 0$ or maximum iterations $n_{\max}$.

**Initialization:**

- Set $k = 0$.
- Compute $g_0 = \nabla f(x_0)$.

**Iteration:**

I. Compute the search direction:

$$d_k = -H_k g_k.$$

II. Perform a line search to find step size $\alpha_k > 0$ satisfying the Wolfe conditions:

$$f(x_k + \alpha_k d_k) \leq f(x_k) + c_1 \alpha_k g_k^\top d_k,$$
$$\nabla f(x_k + \alpha_k d_k)^\top d_k \geq c_2 \, g_k^\top d_k,$$

with $0 < c_1 < c_2 < 1$ (typical values: $c_1 = 10^{-4}$, $c_2 = 0.9$).

III. Update the iterate:

$$x_{k+1} = x_k + \alpha_k d_k.$$

IV. Compute $g_{k+1} = \nabla f(x_{k+1})$.

V. If $\|g_{k+1}\| < \epsilon$ or $k \geq n_{\max}$, stop.

VI. Compute:

$$s_k = x_{k+1} - x_k, \quad y_k = g_{k+1} - g_k, \quad \rho_k = \frac{1}{y_k^\top s_k}.$$

VII. Update the inverse Hessian approximation:

$$H_{k+1} = (I - \rho_k s_k y_k^\top) H_k (I - \rho_k y_k s_k^\top) + \rho_k s_k s_k^\top.$$

VIII. Increment $k$ and return to step I.

**Output:**

- Approximate minimizer $x_{k+1}$.
- Number of iterations performed.

### Example

**Rosenbrock Function:**

$$f(x_1, x_2) = (1 - x_1)^2 + 100(x_2 - x_1^2)^2.$$

The global minimum is at $(x_1, x_2) = (1, 1)$ with $f(1,1) = 0$. The function has a narrow curved valley that makes optimization challenging.

**Gradient:**

$$\nabla f = \begin{pmatrix} -2(1 - x_1) - 400 x_1 (x_2 - x_1^2) \\ 200(x_2 - x_1^2) \end{pmatrix}.$$

**Gradient Descent from $x_0 = (-1, 1)$:**

- **Setup**: $\alpha = 0.001$ (a small learning rate is needed due to the steep valley walls).

**Iteration 1:**

- $\nabla f(-1, 1) = \begin{pmatrix} -2(2) - 400(-1)(1-1) \\ 200(1-1) \end{pmatrix} = \begin{pmatrix} -4 \\ 0 \end{pmatrix}.$
- $x_1 = (-1, 1) - 0.001 \cdot (-4, 0) = (-0.996, 1).$
- $f(-0.996, 1) = (1.996)^2 + 100(1 - 0.992)^2 = 3.984 + 100(0.008)^2 \approx 3.99.$

**Iteration 2:**

- $\nabla f(-0.996, 1) \approx \begin{pmatrix} -3.99 - 400(-0.996)(1 - 0.992) \\ 200(1 - 0.992) \end{pmatrix} \approx \begin{pmatrix} -0.80 \\ 1.59 \end{pmatrix}.$
- $x_2 \approx (-0.996, 1) - 0.001 \cdot (-0.80, 1.59) = (-0.9952, 0.9984).$

Gradient descent progresses very slowly along the curved valley, typically requiring thousands of iterations to reach $(1, 1)$.

**Newton's Method from $x_0 = (-1, 1)$:**

The Hessian at $(x_1, x_2)$ is:

$$\nabla^2 f = \begin{pmatrix} 2 + 1200 x_1^2 - 400 x_2 & -400 x_1 \\ -400 x_1 & 200 \end{pmatrix}.$$

At $(-1, 1)$:

$$\nabla^2 f = \begin{pmatrix} 2 + 1200 - 400 & 400 \\ 400 & 200 \end{pmatrix} = \begin{pmatrix} 802 & 400 \\ 400 & 200 \end{pmatrix}.$$

The Newton step is $d = -(\nabla^2 f)^{-1} \nabla f(-1,1) = -\begin{pmatrix} 802 & 400 \\ 400 & 200 \end{pmatrix}^{-1} \begin{pmatrix} -4 \\ 0 \end{pmatrix}$.

Computing the inverse (with determinant $= 802 \cdot 200 - 400^2 = 160400 - 160000 = 400$):

$$(\nabla^2 f)^{-1} = \frac{1}{400}\begin{pmatrix} 200 & -400 \\ -400 & 802 \end{pmatrix} = \begin{pmatrix} 0.5 & -1 \\ -1 & 2.005 \end{pmatrix}.$$

$$d = -\begin{pmatrix} 0.5 & -1 \\ -1 & 2.005 \end{pmatrix} \begin{pmatrix} -4 \\ 0 \end{pmatrix} = \begin{pmatrix} 2 \\ -4 \end{pmatrix}.$$

With a line search, the step would be damped, but the Newton direction points strongly toward the minimum, and Newton's method typically converges to $(1,1)$ in far fewer iterations than gradient descent.

**Effect of Initial Guess:**

Starting from different initial points on the Rosenbrock function:

- From $(-1, 1)$: Both methods converge to $(1, 1)$, but gradient descent takes $\sim 10{,}000+$ iterations while BFGS takes $\sim 30$–$50$ iterations.
- From $(0, 0)$: Convergence is faster since this point is closer to the valley floor.
- From $(-2, 2)$: Gradient descent struggles with the steep gradient outside the valley; BFGS adapts its curvature estimate and converges more efficiently.

### Advantages

1. **Fast convergence** is achieved by Newton's method (quadratic) and BFGS (superlinear), making them highly efficient for smooth, well-conditioned problems near the solution.
2. **Low per-iteration cost** of gradient descent and BFGS (which avoid explicit Hessian computation or inversion) makes them practical for large-scale problems with many variables.
3. **Well-established convergence theory** provides guarantees under standard assumptions (e.g., Lipschitz continuous gradients, strong convexity) and guides the choice of step sizes and stopping criteria.
4. **Broad applicability** to any differentiable objective function, combined with mature software implementations in libraries such as SciPy, PyTorch, and TensorFlow, makes these methods accessible and reliable.

### Limitations

1. **Convergence to local minima** rather than global minima is inherent for non-convex functions, making the result dependent on the choice of initial point.
2. **Sensitivity to step size** in gradient descent means that a poorly chosen learning rate can lead to divergence (too large) or impractically slow progress (too small).
3. **Hessian computation and storage** for Newton's method scales as $O(n^2)$ in memory and $O(n^3)$ per iteration for solving the linear system, which is prohibitive for very high-dimensional problems.
4. **Line search overhead** in quasi-Newton methods adds cost per iteration, and poorly conditioned problems may still require many iterations despite curvature approximations.
