## Runge-Kutta Method

The Runge-Kutta method is one of the most commonly used methods for numerical integration of ordinary differential equations (ODEs). It is a family of implicit and explicit iterative methods, which include the well-known routine called the Euler Method, and the 2nd-order (also known as Heun's method) and 4th-order Runge-Kutta methods.

## Mathematical Formulation

The standard form of the first-order ODE used by the Runge-Kutta methods is:

$$ \frac{du}{dt} = f(t, u), $$

where $u$ is the unknown function of time $t$, and $f$ is a function of $t$ and $u$.

The general form of the 4th order Runge-Kutta method is:

$$k_1 = \Delta t \cdot f(t, u),$$
$$k_2 = \Delta t \cdot f\left(t + \frac{\Delta t}{2}, u + \frac{k_1}{2}\right),$$
$$k_3 = \Delta t \cdot f\left(t + \frac{\Delta t}{2}, u + \frac{k_2}{2}\right),$$
$$k_4 = \Delta t \cdot f(t + \Delta t, u + k_3),$$
$$u(t + \Delta t) = u(t) + \frac{1}{6}(k_1 + 2k_2 + 2k_3 + k_4).$$

## Derivation of Runge-Kutta Method

The Runge-Kutta methods, particularly the 4th order Runge-Kutta method, is derived by taking an initial condition and trying to estimate the value of the solution after a small step $\Delta t$, by taking weighted averages of increments at the beginning, middle, and end of the interval. The method is designed to mimic a Taylor series expansion, but without requiring the computation of higher derivatives. Here's how it's derived.

Let's start with a Taylor series expansion:

$$u(t+\Delta t) = u(t) + \Delta t u'(t) + \frac{\Delta t^2}{2!} u''(t) + \frac{\Delta t^3}{3!} u'''(t) + \frac{\Delta t^4}{4!} u''''(t) + O(\Delta t^5).$$

The first derivative $u'(t)$ is already given by the ODE:

$$u'(t) = f(t, u).$$

The higher-order derivatives can also be expressed in terms of $f(t, u)$ and its derivatives:

$$u''(t) = \frac{df}{dt} = \frac{\partial f}{\partial t} + \frac{\partial f}{\partial u} \frac{du}{dt} = \frac{\partial f}{\partial t} + \frac{\partial f}{\partial u} f,$$

and similarly for $u'''(t)$ and $u''''(t)$.

By taking an appropriate weighted average of increments at the start, middle and end of the interval, the Runge-Kutta method tries to mimic the above Taylor series expansion, but without explicitly calculating the higher derivatives of $f(t, u)$. Instead, it approximates the increments by evaluating $f(t, u)$ at several points within the interval.

Hence we have the 4th order Runge-Kutta method:

$$k_1 = \Delta t \cdot f(t, u),$$
$$k_2 = \Delta t \cdot f\left(t + \frac{\Delta t}{2}, u + \frac{k_1}{2}\right),$$
$$k_3 = \Delta t \cdot f\left(t + \frac{\Delta t}{2}, u + \frac{k_2}{2}\right),$$
$$k_4 = \Delta t \cdot f(t + \Delta t, u + k_3),$$
$$u(t + \Delta t) = u(t) + \frac{1}{6}(k_1 + 2k_2 + 2k_3 + k_4),$$

where the weights of $k_1, k_2, k_3, k_4$ (1/6, 1/3, 1/3, 1/6) are chosen so that the error term is $O(\Delta t^5)$, which means the local truncation error at each step is proportional to the fifth power of the step size, and the global truncation error (after $N$ steps) is proportional to the fourth power of the step size.

## Algorithm Steps

1. Initiate with the initial condition $u(t_0) = u_0$.
2. At each step, calculate $k_1, k_2, k_3, k_4$ as stated above.
3. Update $u(t + \Delta t) = u(t) + \frac{1}{6}(k_1 + 2k_2 + 2k_3 + k_4)$.
4. Repeat steps 2-3 for a specified number of iterations or until the solution approximation becomes satisfactory.

## Example

Consider the differential equation

$$ u'(t)=u(t),$$

with the initial condition $u(0)=1$. We want to estimate the value of $u$ at $t = 0.1$ using the Runge-Kutta method with a step size of $\Delta t = 0.05$.

1. We start at $t=0$ with $u(0) = 1$.

First, we calculate the four increments:

$$k_1 = \Delta t \cdot f(t, u) = 0.05 \cdot 1 = 0.05,$$
$$k_2 = \Delta t \cdot f\left(t + \frac{\Delta t}{2}, u + \frac{k_1}{2}\right) = 0.05 \cdot (1 + 0.05/2) = 0.05125,$$
$$k_3 = \Delta t \cdot f\left(t + \frac{\Delta t}{2}, u + \frac{k_2}{2}\right) = 0.05 \cdot (1 + 0.05125/2) = 0.0515625,$$
$$k_4 = \Delta t \cdot f(t + \Delta t, u + k_3) = 0.05 \cdot (1 + 0.0515625) = 0.052578125.$$

We then calculate the next value of $u$:

$$u(0.05) \approx u(0) + \frac{1}{6}(k_1 + 2k_2 + 2k_3 + k_4)$$
$$u(0.05) \approx 1 + \frac{1}{6}(0.05 + 2 \cdot 0.05125 + 2 \cdot 0.0515625 + 0.052578125)$$
$$u(0.05) \approx 1.053125.$$

2. Now that we have $u(0.05)$, we move on to $t = 0.1$.

Similarly, we first calculate the four increments:

$$k_1 = \Delta t \cdot f(t, u) = 0.05 \cdot 1.053125 = 0.05265625,$$
$$k_2 = \Delta t \cdot f\left(t + \frac{\Delta t}{2}, u + \frac{k_1}{2}\right) = 0.05 \cdot (1.053125 + 0.05265625/2) = 0.0534833984375,$$
$$k_3 = \Delta t \cdot f\left(t + \frac{\Delta t}{2}, u + \frac{k_2}{2}\right) = 0.05 \cdot (1.053125 + 0.0534833984375/2) = 0.05373828125,$$
$$k_4 = \Delta t \cdot f(t + \Delta t, u + k_3) = 0.05 \cdot (1.053125 + 0.05373828125) = 0.055374267578125.$$

Then, we calculate the next value of $u$:

$$u(0.1) \approx u(0.05) + \frac{1}{6}(k_1 + 2k_2 + 2k_3 + k_4)$$
$$u(0.1) \approx 1.053125 + \frac{1

## Advantages

- Runge-Kutta methods, especially the 4th order, provide a good compromise between accuracy and computational effort.
- They do not require the computation of higher derivatives of $f(t, u)$, unlike Taylor series methods.

## Limitations

- Runge-Kutta methods can become inefficient for stiff differential equations, which may require an implicit method.
- The error accumulates with each step, hence they may not be suitable for problems requiring high precision.
