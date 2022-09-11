Interpolating with Netwon polynomial gives exactly the same results as with Lagrange polynomial.

## Derivation

We have to rewrite the polynomial in the following way:

$$ P_N(x) = a_0 +(x-x_0)a_1 + (x-x_0)(x-x_1)a_2 + \cdots + (x-x_0)(x-x_1)\ldots(x-x_N)a_N,$$

For $N=3$:

$$P_3(x) = a_0 +(x-x_0)a_1 + (x-x_0)(x-x_1)a_2 + (x-x_0)(x-x_1)(x-x_2)a_3$$

$$P_3(x) = a_0 +(x-x_0)[a_1 + (x-x_1)[a_2 + (x-x_2)a_3]]$$

1. Substitute $x=x_0$: We have $P_3(x_0)=a_0$, and we know that our interpolant $P_3(x)$ evaluated at $x_0$ must return $y_0$. Hence we must conclude that 

$$a_0 = y_0.$$


2. Now substitute $x=x_1$: We have $P_3(x_1) = a_0 +(x_1-x_0)a_1 = y_0 +(x_1-x_0)a_1 $, the LHS of this must to  $y_1$, and we know everything on the RHS as we have already calculated that $a_0 = y_0$. We can thus trivially rearrange to yield

$$ a_1 = \frac{(y_1 - y_0)}{(x_1-x_0)}.$$


3. Substituting $x=x_2$ yields 

$$ y_2 = P_3(x_2) = a_0 +(x_2-x_0)[a_1 + (x_2-x_1)a_2] = y_0 + (x_2-x_0)\left[ \frac{(y_1 - y_0)}{(x_1-x_0)} + (x_2-x_1)a_2\right] $$

$$ \implies a_2 = \frac{ \frac{(y_2 - y_0)}{(x_2-x_0)} - \frac{(y_1 - y_0)}{(x_1-x_0)}}{x_2-x_1} $$

To define an algorithm for this method in general let's first introducing the following [*divided difference*](https://en.wikipedia.org/wiki/Divided_differences) notation

$$ \Delta y_i = \frac{y_i-y_0}{x_i-x_0}, \quad i=1,2,\ldots, N $$

$$ \Delta^2 y_i = \frac{\Delta y_i-\Delta y_1}{x_i-x_1}, \quad i=2, 3,\ldots, N $$

$$ \vdots $$

$$ \Delta^N y_N = \frac{\Delta^{N-1} y_N-\Delta^{N-1} y_{N-1}}{x_N-x_{N-1}} $$

With a bit of thought we can hopefully see from the above example that the coefficients of the interpolating polynomial in the general case are given by


$$a_0=y_0, \quad a_1 = \Delta y_1, \quad a_2 = \Delta^2 y_2, \quad \ldots \quad a_N = \Delta^N y_N$$

So an algorithm to evaluate the Newton Polynomial could follow this process:

1. Initialise the unknown array $a$ with the data $y$, so that

$$ a_0 = y_0, \quad a_1 = y_1, \quad a_2 = y_2, ...$$

Based on our derivation above we know that the first of these is correct, i.e. we want to preserve this value for $a_0$ as we move forward.

2. So in this step we don't want to touch $a_0$, but the other $a$ values can be updated. Let's set

$$ a_1 = \frac{(a_1 - a_0)}{(x_1-x_0)}, \quad a_2 = \frac{(a_2 - a_0)}{(x_2-x_0)}, ... $$

but note that due to the values that $a_0$ and $a_1$ take (before $a_1$) is over-written) this has the result of setting

$$ a_1 = \frac{(y_1 - y_0)}{(x_1-x_0)} $$ 

which is what we want, so in the next step we don't want to touch $a_1$ (in addition to not touching $a_0$).

3. So now we set

$$ \quad a_2 = \frac{(a_2 - a_1)}{(x_2-x_1)} $$

but based on the expressions currently stored in $a_1$ and $a_2$ this is equal to

$$ a_2 = \frac{ \frac{(y_2 - y_0)}{(x_2-x_0)} - \frac{(y_1 - y_0)}{(x_1-x_0)}}{x_2-x_1} $$

and so on.
