## Global Optimization

Global optimization seeks the best feasible point across the entire search region rather than only within the basin of a starting point.

For

$$
\min_{x\in\Omega}f(x),
$$

a global minimizer $x^*$ satisfies

$$
f(x^*)\le f(x)
$$

for every $x\in\Omega$.

The challenge is that a non-convex objective can contain many local minima, flat regions, discontinuities, or noise.

### A multimodal benchmark

The one-dimensional Rastrigin function

$$
f(x) = 10 + x^2 - 10\cos(2\pi x)
$$

contains many local minima but has the global minimum

$$
f(0) = 0.
$$

![Rastrigin landscape with local and global minima](https://github.com/djeada/Numerical-Methods/raw/refs/heads/master/notes/8_optimization/resources/plots/global_rastrigin.svg)

A local descent method started near $x=3$ can settle in a nearby basin instead of finding the origin.

### Three strategies in the repository

The implementation includes:

- **grid search**: deterministic exhaustive sampling on a regular grid;
- **simulated annealing**: a stochastic trajectory that can accept uphill moves;
- **genetic algorithm**: a population-based evolutionary search.

![Representative global-search behavior](https://github.com/djeada/Numerical-Methods/raw/refs/heads/master/notes/8_optimization/resources/plots/global_search_comparison.svg)

Detailed notes:

- [Simulated annealing](simulated_annealing.md)
- [Genetic algorithms](genetic_algorithms.md)

### Grid search and the curse of dimensionality

With $N$ points per coordinate in $n$ dimensions, a full Cartesian grid contains

$$
N^n
$$

points. This makes exhaustive gridding useful for low-dimensional verification but rapidly impractical as $n$ grows.

If a one-dimensional interval has spacing $h$, the nearest grid point is at most $h/2$ away from the true minimizer. In multiple dimensions the geometric discretization error grows with the cell diagonal.

### Exploration versus exploitation

Global methods must balance two goals:

- **exploration**: sample regions not yet understood;
- **exploitation**: improve promising candidates.

Too much exploitation causes premature convergence to a local minimum. Too much exploration wastes evaluations without refining good solutions.

Simulated annealing controls this balance through temperature. Genetic algorithms use selection pressure, crossover, mutation, and population diversity.

### No free finite-time guarantee

For a generic black-box function, a finite number of samples cannot certify a true global optimum without additional assumptions. Strong guarantees require structure such as Lipschitz bounds, interval arithmetic, convexity, or exhaustive combinatorial reasoning.

This is why stochastic global methods usually report the **best point found**, not a mathematical proof of global optimality.

### Hybrid strategies

A powerful practical pattern is:

1. use a global method or multi-start sampling to locate promising basins;
2. refine the best candidates with a fast local solver;
3. compare final objective values and feasibility;
4. repeat with different seeds when stochastic uncertainty matters.

This separates broad exploration from precise local convergence.

### Reproducibility

Stochastic optimization should expose and record random seeds. Report the number of function evaluations, not only iterations, because different algorithms can perform very different amounts of work per iteration.
