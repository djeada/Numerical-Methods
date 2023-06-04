## Heun's Method

Heun's method is an improved version of Euler's method that enhances accuracy by using an average of the slope at the beginning and the predicted slope at the end of the interval.

## Mathematical Formulation

Assuming a first order differential equation:

$$ \frac{du}{dt} = f(t, u), $$

given $u(t_0) = u_0$ and a step size $h$, Heun's method predicts the solution at time $(t_0 + h)$ as follows:

1. **Euler's step (predictor step)**: Predict the value at $t = t_0 + h$ using Euler's method:

$$ \tilde{u}_{n+1} = u_n + h f(t_n, u_n), $$

2. **Heun's step (corrector step)**: Correct this prediction by taking an average of the slopes at the beginning and end of the interval:

$$ u_{n+1} = u_n + \frac{h}{2} [f(t_n, u_n) + f(t_{n} + h, \tilde{u}_{n+1})]. $$

This process is repeated for each point in the desired interval.

## Derivation

The second-order Taylor series expansion around $t$ is given by:

$$ u(t + h) = u(t) + h u'(t) + \frac{1}{2}(h)^2 u''(t) + O(h^3), $$

where we approximate $u''(t)$ by the first difference of $u'(t)$:

$$ u''(t) \approx \frac{u'(t+h) - u'(t)}{h} = \frac{f(t + h, u(t + h)) - f(t, u(t))}{h}. $$

Substituting this approximation into the Taylor series, we get:

$$ u(t + h) = u(t) + h u'(t) + \frac{1}{2}(h)^2 \frac{f(t + h, u(t + h)) - f(t, u(t))}{h} + O(h^3), $$

and approximating $u(t + h)$ by removing the higher order term yields Heun's method:

$$ u(t + h) \approx u(t) + \frac{h}{2} [f(t, u(t)) + f(t + h, \tilde{u}_{n+1})]. $$

## Algorithm Steps

1. Begin with initial conditions $u_0$ and $t_0$.
2. Compute $\tilde{u}_{n+1}$ using the predictor step.
3. Calculate $u_{n+1}$ using the corrector step.
4. Repeat steps 2-3 for all points in the desired interval.

## Example

Consider the differential equation

$$ u'(t) = u(t), $$

with the initial condition $u(0) = 1$. We want to estimate the value of $u$ at $t = 0.1$ using Heun's method with a step size of $h = 0.05$.

1. We start at $t = 0$ with $u(0) = 1$.

First, we calculate the Euler's step (predictor):

$$ \tilde{u} = u(0) + h \cdot f(t, u(0)) = 1 + 0.05 \cdot 1 = 1.05. $$

Then, we correct this estimation:

$$ u(0.05) \approx u(0) + \frac{h}{2} [f(t, u(0)) + f(t + h, \tilde{u}_{n+1})] = 1 + \frac{0.05}{2} [1 + 1.05] = 1.05125. $$

2. Now, we have $u(0.05)$, we move on to $t = 0.1$.

Similarly, we calculate the Euler's step:

$$ \tilde{u} = u(0.05) + h \cdot f(t, u(0.05)) = 1.05125 + 0.05 \cdot 1.05125 = 1.1025625. $$

Then, we correct this estimation:

$$ u(0.1) \approx u(0.05) + \frac{h}{2} [f(t, u(0.05)) + f(t + h, \tilde{u}_{n+1})] = 1.05125 + \frac{0.05}{2} [1.05125 + 1.1025625] = 1.105158203125. $$

So, the approximate solution to $u(0.1)$ with Heun's method is $1.105158203125$.

## Advantages

- Heun's method is relatively straightforward and easy to understand.
- It generally provides a more accurate approximation than Euler's method.

## Limitations

- Although Heun's method is more accurate than Euler's method, it can still produce substantial error for large step sizes or complicated functions.
- Similar to Euler's method, Heun's method may not provide accurate results for stiff systems or problems with high nonlinearity.
