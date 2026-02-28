## Global Optimization

Global optimization is the branch of mathematical optimization concerned with finding the absolute best solution (the global optimum) of a function that may possess many local optima. Unlike local optimization methods, which converge to the nearest stationary point from a given starting guess, global optimization strategies are designed to explore the entire search space to avoid being trapped in suboptimal valleys. This distinction is critical when dealing with **multimodal functions** — functions that have multiple peaks and valleys — where a local method would return different answers depending on its initialization.

Global optimization appears in engineering design (e.g., shape or topology optimization), computational chemistry (molecular conformation), neural network training, hyperparameter tuning, logistics, and many other domains where the objective landscape is complex and poorly understood. The fundamental challenge is balancing **exploration** (searching broadly across the domain) with **exploitation** (refining the best-known solution), all while keeping computational costs manageable.

**Conceptual Illustration**:

Imagine a rugged mountain range seen from above, with peaks and valleys of varying depths. A local optimizer is like a hiker who always walks downhill — they will end up in the nearest valley regardless of whether a deeper valley exists elsewhere. A global optimizer, by contrast, might fly over the landscape in a helicopter, sample many locations, and then descend into the deepest valley found. Grid search methodically checks every point on a map; simulated annealing occasionally climbs uphill to escape shallow valleys; genetic algorithms evolve a population of candidate solutions to explore multiple regions simultaneously.

### Mathematical Formulation

The general global optimization problem is:

$$\min_{x \in \Omega} f(x)$$

where $f : \mathbb{R}^n \to \mathbb{R}$ may be non-convex, non-smooth, or even black-box, and $\Omega \subseteq \mathbb{R}^n$ is the feasible region (often a box $[l_i, u_i]$ for each coordinate).

A point $x^* \in \Omega$ is a **global minimum** if:

$$f(x^*) \leq f(x) \quad \text{for all } x \in \Omega.$$

In contrast, $x^*$ is only a **local minimum** if this inequality holds in some neighborhood $\|x - x^*\| < \delta$.

**Multimodal Test Function (Rastrigin)**:

A standard benchmark is the Rastrigin function:

$$f(x) = An + \sum_{i=1}^n \left[ x_i^2 - A\cos(2\pi x_i) \right], \quad A = 10.$$

This function has a global minimum of $0$ at the origin but possesses roughly $10^n$ local minima, making it an excellent test for global search strategies.

### Derivation

I. **Brute-Force / Grid Search**:

The simplest global strategy is to evaluate $f$ at every point on a regular grid over $\Omega$. Suppose $\Omega = [a, b]^n$ and we place $N$ equally spaced points along each dimension. The grid consists of $N^n$ points:

$$x_{i_1, \dots, i_n} = \left(a + i_1 \frac{b-a}{N-1}, \dots, a + i_n \frac{b-a}{N-1}\right), \quad i_k = 0, 1, \dots, N-1.$$

The approximate global minimum is:

$$x^* \approx \arg\min_{x \text{ on grid}} f(x).$$

The resolution of the grid is $h = \frac{b-a}{N-1}$. If $f$ is Lipschitz continuous with constant $L$, the error is bounded by $L h \sqrt{n}/2$. However, the total number of evaluations $N^n$ grows exponentially with dimension $n$, a phenomenon known as the **curse of dimensionality**.

II. **Simulated Annealing**:

Inspired by the physical process of cooling a material, simulated annealing explores the search space by accepting not only improvements but also, with some probability, moves that increase the objective value. At iteration $k$ with current point $x_k$ and temperature $T_k$:

- Generate a candidate $y$ from a neighborhood of $x_k$.
- Compute $\Delta f = f(y) - f(x_k)$.
- Accept $y$ with probability:

$$P(\text{accept}) = \begin{cases} 1 & \text{if } \Delta f \leq 0, \\ \exp\left(-\frac{\Delta f}{T_k}\right) & \text{if } \Delta f > 0. \end{cases}$$

The temperature $T_k$ is gradually decreased according to a **cooling schedule** (e.g., $T_k = T_0 \cdot \alpha^k$ for some $\alpha \in (0,1)$). At high temperatures the algorithm explores broadly; as $T_k \to 0$ it behaves like a greedy local search. Under suitable cooling schedules, simulated annealing is guaranteed to converge to the global optimum in probability.

III. **Genetic Algorithms**:

Genetic algorithms maintain a **population** of candidate solutions and evolve them using operators inspired by biological evolution:

- **Selection**: Choose parents from the population with probability proportional to their fitness (lower $f$ = higher fitness).
- **Crossover**: Combine two parents to produce offspring. For real-valued variables, this might be a weighted average or blend of parent coordinates.
- **Mutation**: Randomly perturb offspring to maintain diversity, e.g., $x_i \leftarrow x_i + \sigma \mathcal{N}(0,1)$ for some mutation strength $\sigma$.

The population evolves over generations, and the best individual found across all generations is returned as the approximate global optimum.

### Algorithm Steps

**Simulated Annealing**:

**Input:**

- Objective function $f(x)$.
- Feasible region $\Omega$.
- Initial point $x_0 \in \Omega$.
- Initial temperature $T_0 > 0$.
- Cooling factor $\alpha \in (0,1)$.
- Maximum iterations $n_{\max}$.

**Initialization:**

- Set $x_{\text{best}} = x_0$, $f_{\text{best}} = f(x_0)$, $T = T_0$, $k = 0$.

**Iteration:**

I. Generate a candidate $y$ by perturbing $x_k$:

$$y = x_k + \sigma \cdot \mathcal{N}(0, I_n),$$

projected onto $\Omega$ if necessary.

II. Compute $\Delta f = f(y) - f(x_k)$.

III. If $\Delta f \leq 0$, accept: $x_{k+1} = y$.

IV. If $\Delta f > 0$, accept with probability $\exp(-\Delta f / T)$:

- Draw $u \sim \text{Uniform}(0,1)$.
- If $u < \exp(-\Delta f / T)$, set $x_{k+1} = y$; otherwise $x_{k+1} = x_k$.

V. Update best: if $f(x_{k+1}) < f_{\text{best}}$, set $x_{\text{best}} = x_{k+1}$, $f_{\text{best}} = f(x_{k+1})$.

VI. Cool: $T \leftarrow \alpha T$.

VII. Increment $k$. If $k < n_{\max}$, return to step I.

**Output:**

- Best solution $x_{\text{best}}$.
- Best objective value $f_{\text{best}}$.

### Example

**Multimodal Function:**

Consider the one-dimensional Rastrigin function:

$$f(x) = 10 + x^2 - 10\cos(2\pi x), \quad x \in [-5.12, 5.12].$$

This function has a global minimum of $f(0) = 0$ at $x = 0$ and many local minima at approximately integer values of $x$.

**Grid Search:**

Evaluate $f$ on a grid of $N = 1024$ equally spaced points in $[-5.12, 5.12]$:

$$x_i = -5.12 + i \cdot \frac{10.24}{1023}, \quad i = 0, 1, \dots, 1023.$$

The grid point closest to $x = 0$ is at $x \approx 0.005$, giving $f(0.005) \approx 0.00025 + 10 - 10\cos(0.01\pi) \approx 0.001$. Grid search identifies $x \approx 0$ as the global minimum.

**Simulated Annealing (step-by-step):**

- **Setup**: $x_0 = 3.5$, $T_0 = 10$, $\alpha = 0.9$, $\sigma = 0.5$.
- $f(x_0) = 10 + 12.25 - 10\cos(7\pi) = 10 + 12.25 + 10 = 32.25$.

**Iteration 1** ($T = 10$):

- Candidate: $y = 3.5 + 0.5 \cdot 0.3 = 3.65$.
- $f(3.65) \approx 10 + 13.32 - 10\cos(7.3\pi) \approx 27.28$.
- $\Delta f = 27.28 - 32.25 = -4.97 < 0$. Accept. $x_1 = 3.65$.

**Iteration 2** ($T = 9$):

- Candidate: $y = 3.65 + 0.5 \cdot (-1.2) = 3.05$.
- $f(3.05) \approx 10 + 9.30 - 10\cos(6.1\pi) \approx 18.35$.
- $\Delta f = 18.35 - 27.28 = -8.93 < 0$. Accept. $x_2 = 3.05$.

**Later iterations:**

As the temperature decreases, the algorithm gradually drifts toward regions of lower function values, occasionally accepting uphill moves to escape local traps. After many iterations, simulated annealing converges near $x = 0$, the global minimum.

**Local vs Global Comparison:**

A gradient descent starting from $x_0 = 3.5$ would converge to the nearest local minimum at approximately $x \approx 3$ (with $f(3) \approx 9$), whereas the global methods correctly identify $x = 0$ with $f(0) = 0$.

### Advantages

1. **Ability to escape local optima** distinguishes global methods from local ones, enabling them to find solutions that are globally optimal or near-optimal on multimodal landscapes.
2. **Minimal assumptions on the objective** mean that global methods can handle non-convex, non-smooth, noisy, or black-box functions where gradient information is unavailable.
3. **Parallelizability** of methods such as genetic algorithms and multi-start strategies allows efficient use of modern multi-core and distributed computing resources.
4. **Flexibility** in problem formulation permits handling of mixed-integer variables, combinatorial constraints, and other features that are difficult for classical gradient-based methods.

### Limitations

1. **Computational expense** is often very high, as global methods typically require many more function evaluations than local methods, especially in high-dimensional spaces.
2. **Curse of dimensionality** affects grid-based and exhaustive methods severely, since the number of evaluations required grows exponentially with the problem dimension.
3. **No guarantee of finding the true global optimum** in finite time for most stochastic methods; convergence guarantees are typically asymptotic or probabilistic.
4. **Tuning of algorithm parameters** (temperature schedules, population sizes, mutation rates) can significantly affect performance and often requires problem-specific experimentation.
