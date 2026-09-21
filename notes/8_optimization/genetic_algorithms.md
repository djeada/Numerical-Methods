## Genetic Algorithms

A genetic algorithm (GA) searches with a **population** of candidate solutions rather than a single trajectory.

Each generation applies three main operations:

1. selection;
2. crossover;
3. mutation.

### Population and fitness

For minimization, candidates with lower objective values are fitter. The repository implementation uses tournament selection: two individuals are sampled and the better one is copied into the mating pool.

Tournament selection avoids needing a special transformation from objective value to probability.

### Crossover

For two real-valued parents $x^{(1)}$ and $x^{(2)}$, blend crossover can use

$$
y^{(1)} = \alpha\odot x^{(1)} + (1 - \alpha)\odot x^{(2)},
$$

$$
y^{(2)} = (1 - \alpha)\odot x^{(1)} + \alpha\odot x^{(2)},
$$

with componentwise random $\alpha\in[0,1]^n$.

### Mutation

Mutation adds random perturbations to selected genes. It maintains diversity and creates information not already present in the selected parents.

![Population evolution toward a low-objective basin](https://github.com/djeada/Numerical-Methods/raw/refs/heads/master/notes/8_optimization/resources/plots/genetic_algorithm_population.svg)

### Exploration versus selection pressure

Strong selection pressure rapidly concentrates the population, which speeds exploitation but risks premature convergence. Mutation and a sufficiently large population preserve exploration.

The right balance is problem dependent.

### Elitism

Many practical GAs explicitly copy one or more best individuals into the next generation. The compact repository implementation instead tracks the best point found separately; the evolving population itself does not guarantee that the best individual survives.

### Computational cost

If the population size is $P$ and the algorithm runs for $G$ generations, it performs roughly

$$
P(G + 1)
$$

objective evaluations, aside from any reuse or parallelization.

This is often expensive compared with gradient methods, but the evaluations are naturally parallel.

### When genetic algorithms are useful

GAs are most attractive when:

- derivatives are unavailable;
- the search landscape is multimodal;
- variables are mixed or discrete;
- one function evaluation is not prohibitively expensive;
- parallel hardware is available.

For smooth convex problems, they are usually far less efficient than deterministic local methods.
