
# Heun's Method

Heun's method is an improved version of Euler's method that increases accuracy by using an average of the slope at the beginning and the predicted slope at the end of the interval.

## Mathematical Formulation

The general form of Heun's method for a first-order differential equation can be written as follows:

Let's assume a first order differential equation:

$$ \frac{dy}{dt} = f(t, y) $$

Given $y(t_0)$ = $y_0$ and step size $h$, Heun's method predicts the solution at time $(t_0 + h)$ as follows:

1. **Euler's step (predictor step)**: Predict the value at $t = t_0 + h$ using Euler's method:

$$ \tilde{y}_{n+1} = y_n + h f(t_n, y_n) $$

2. **Heun's step (corrector step)**: Correct this prediction by taking an average of the slopes at the beginning and end of the interval:

$$ y_{n+1} = y_n + \frac{h}{2} [f(t_n, y_n) + f(t_{n+1}, \tilde{y}_{n+1})] $$

$$ u(t+\Delta t)\approx u(t)+\frac{\Delta t}{2}\big(f(u(t),t)+f(\tilde{u}(t+\Delta t),t+\Delta t)\big)$$

Repeat these steps for each point in the desired interval.

## Derivation

The second order Taylor series expansion around $t$ is given by:

$$ u(t + \Delta t) = u(t) + \Delta t u'(t) + \frac{1}{2}(\Delta t)^2 u''(t) + O(\Delta t^3) $$

We approximate $u''(t)$ by the first difference of $u'(t)$:

$$ u''(t) \approx \frac{u'(t+\Delta t) - u'(t)}{\Delta t} = \frac{f(t + \Delta t, u(t + \Delta t)) - f(t, u(t))}{\Delta t} $$

Substituting this approximation into the Taylor series gives:

$$ u(t + \Delta t) = u(t) + \Delta t u'(t) + \frac{1}{2}(\Delta t)^2 \frac{f(t + \Delta t, u(t + \Delta t)) - f(t, u(t))}{\Delta t} + O(\Delta t^3) $$

We then approximate $u(t + \Delta t)$ by removing the higher order term:

$$ u(t + \Delta t) \approx u(t) + \Delta t u'(t) + \frac{1}{2}(\Delta t) [f(t + \Delta t, u(t + \Delta t)) - f(t, u(t))] $$

Which is the same as:

$$ u(t + \Delta t) \approx u(t) + \frac{\Delta t}{2} [f(t, u(t)) + f(t + \Delta t, u(t + \Delta t))] $$

This is Heun's method, which is a second order method. We make an initial guess for $u(t + \Delta t)$ using Euler's method:

$$ u_{\text{Euler}}(t + \Delta t) = u(t) + \Delta t f(t, u(t)) $$

Then correct this using the average slope:

$$ u(t + \Delta t) \approx u(t) + \frac{\Delta t}{2} [f(t, u(t)) + f(t + \Delta t, u_{\text{Euler}}(t + \Delta t))] $$


## Algorithm Steps

1. Begin with initial conditions $y_0$ and $t_0$.
2. Compute $\tilde{y}_{n+1}$ using the predictor step.
3. Calculate $y_{n+1}$ using the corrector step.
4. Iterate steps 2-3 for all points in the desired interval.

## Example

Consider the differential equation

$$ u'(t)=u(t),$$

with the initial condition $u(0)=1$. We want to estimate the value of $u$ at $t = 0.1$ using Heun's method with a step size of $\Delta t = 0.05$.

1. We start at $t=0$ with $u(0) = 1$.

First, we calculate the Euler's step (predictor):

$$u_e = u(t) + \Delta t \cdot f(t, u(t)) = 1 + 0.05 \cdot 1 = 1.05.$$

Then, we correct this estimation:

$$u(0.05) \approx u(t) + \frac{\Delta t}{2} [f(t, u(t)) + f(t + \Delta t, u_e)]$$
$$u(0.05) \approx 1 + \frac{0.05}{2} [1 + 1.05] = 1.05125.$$

2. Now that we have $u(0.05)$, we move on to $t = 0.1$.

Similarly, we calculate the Euler's step:

$$u_e = u(0.05) + \Delta t \cdot f(t, u(0.05)) = 1.05125 + 0.05 \cdot 1.05125 = 1.1025625.$$

Then, we correct this estimation:

$$u(0.1) \approx u(0.05) + \frac{\Delta t}{2} [f(t, u(0.05)) + f(t + \Delta t, u_e)]$$
$$u(0.1) \approx 1.05125 + \frac{0.05}{2} [1.05125 + 1.1025625] = 1.105158203125.$$

So, the approximate solution to $u(0.1)$ with Heun's method is $1.105158203125$.


## Advantages

- Heun's method is relatively straightforward and easy to understand.
- It generally provides a more accurate approximation than Euler's method.

## Limitations

- Although Heun's method is more accurate than Euler's method, it can still produce substantial error for large step sizes or complicated functions.
- Similar to Euler's method, Heun's method may not provide accurate results for stiff systems or problems with high nonlinearity.
