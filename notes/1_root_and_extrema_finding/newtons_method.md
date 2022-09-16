# Newton Method (Newton-Raphson formula)

Netwon method for finding roots of a function uses values of a function $f(x)$ and derivatives $f'(x)$.

The formula comes from the taylor series:

$$ f(x_{i+1}) = f(x_i) + f'(x_i)(x_{i+1}-x_i) + \mathcal{O}(x_{i+1} - x_i)^2 $$

We are looking for roots, so we know that $f(x_{i+1}) = 0$:

$$ 0 = f(x_i) + f'(x_i)(x_{i+1}-x_i) + O(x_{i+1} - x_i)^2 $$

As usual we can drop the higher order terms, because $x_{i}$ is smilar to $x_{i+1}$:

$$ 0 = f(x_i) + f'(x_i)(x_{i+1}-x_i) $$

$$ x_{i+1} = x_i - \frac{f(x_i)}{f'(x_i)} $$
