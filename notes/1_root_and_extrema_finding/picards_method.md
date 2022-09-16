
## Fixed points

We want to solve a following equation:

$$ x = g(x) $$

If we continue to apply the function $g$ to the output, it will stay the same:

$$x = g(x) = g(g(x)) = g(g(g(x))) = \ldots $$

A fixed point of the function $g$ is a $x$ that fulfills this equation.

## Example

$$ g(x) = x^{2}-3x+4 $$

The above function has the fixed point 2, because:

$$2 = g(2) = g(g(2)) = g(g(g(2))) = \ldots $$

## Algorithm

1. start with an initial guess $x_{k+1}$.
2. set $x_{k}$ to $x_{k+1}$.
3. calculate the value of function $g$ for argument $g(x_k)$ and store it in $x_{k+1}$.
4. repeat steps 2-3 till $x_{k+1}$ is almost the same as $x_k$.

## Root finding

After calculting the fixed point of a function, finding roots becomes trivial.

$$x = g(x) \equiv 0 = g(x) - x$$

