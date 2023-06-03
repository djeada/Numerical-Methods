## Euler's Method

Euler's Method is a numerical technique applied in the realm of initial value problems for ordinary differential equations (ODEs). The simplicity of this method makes it a popular choice in cases where the differential equation lacks a closed-form solution. The method might not always provide the most accurate result, but it offers a good trade-off between simplicity and accuracy.

## Mathematical Formulation

Consider an initial value problem (IVP) represented as:

$$y' = f(t, y),$$
$$y(t_0) = y_0.$$

This IVP can be solved by Euler's method, where the method employs the following approximation:

$$y_{n+1} = y_n + h*f(t_n, y_n),$$

where:
- $y_{n+1}$ is the approximate value of $y$ at $t = t_n + h$,
- $y_n$ is the approximate value of $y$ at $t = t_n$,
- $h$ is the step size,
- $f(t_n, y_n)$ is the derivative of $y$ at $t = t_n$.

## Derivation

Let's start with the Taylor series:

$$ u(t+\Delta t)=u(t)+\Delta t u'(t) + O(\Delta t^2) $$

We may alternatively rewrite the above equation as follows:

$$ u(t+\Delta t)=u(t)+ \Delta t f(u(t),t)+ O(\Delta t^2).$$

Which is roughly equivalent to:

$$ u(t+\Delta t)=u(t)+ \Delta t f(u(t),t)$$

## Algorithm Steps

1. Start with initial conditions $t_0$ and $y_0$.
2. Calculate $y_{n+1}$ using the formula: $y_{n+1} = y_n + h*f(t_n, y_n)$.
3. Repeat the above step for a given number of steps or until the final value of $t$ is reached.

## Example

$$ u'(t)=u(t),$$

$$ u(0)=1$$

$$u(0.1)=?$$

Let's choose the step value: $\Delta t = 0.05$

We start at $t=0$:

$$  u(0.05) \approx u(0)+0.05u'(0) $$

$$  u(0.05) \approx1+0.05u(0) $$

$$  u(0.05) \approx1+0.05 \cdot 1 $$

$$  u(0.05) \approx 1.05 $$

Now that we know $u(0.05)$, we can calculate the second step:

$$  u(0.1) \approx u(0.05)+0.05u'(0.05) $$

$$  u(0.1) \approx1.05+0.05u(0.05) $$

$$  u(0.1) \approx1.05+0.05 \cdot 1.05 $$

$$  u(0.1) \approx 1.1025 $$

## Advantages

- Euler's method is straightforward to implement.
- It can provide a reasonable approximation when the step size is small and the function is well-behaved.

## Limitations

- The method is not always accurate and can lead to significant errors if the step size is not chosen appropriately.
- Errors from each step accumulate, leading to larger errors in the final result.
- The method might not be stable for all types of ODEs.
