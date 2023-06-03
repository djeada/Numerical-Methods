## Runge-Kutta Method

The Runge-Kutta method is part of a family of iterative methods, both implicit and explicit, which are frequently employed for the numerical integration of ordinary differential equations (ODEs). This family encompasses widely recognized methods like the Euler Method, Heun's method (a.k.a., the 2nd-order Runge-Kutta), and the 4th-order Runge-Kutta method.

## Mathematical Formulation

The first-order ODE that is typically used in the Runge-Kutta methods takes the following form:

$$ \frac{du}{dt} = f(t, u), $$

In this equation, $u$ is the unknown function of time $t$ that we are aiming to solve for, and $f$ is a function of $t$ and $u$.

The general formulation of the 4th order Runge-Kutta method is presented below:

$$k_1 = \Delta t \cdot f(t, u),$$

$$k_2 = \Delta t \cdot f\left(t + \frac{\Delta t}{2}, u + \frac{k_1}{2}\right),$$

$$k_3 = \Delta t \cdot f\left(t + \frac{\Delta t}{2}, u + \frac{k_2}{2}\right),$$

$$k_4 = \Delta t \cdot f(t + \Delta t, u + k_3),$$

$$u(t + \Delta t) = u(t) + \frac{1}{6}(k_1 + 2k_2 + 2k_3 + k_4).$$

## Derivation of Runge-Kutta Method

The derivation of the Runge-Kutta methods, especially the 4th order Runge-Kutta method, begins with an initial condition and attempts to estimate the solution value after a small step $\Delta t$. This is achieved by taking weighted averages of increments at the beginning, middle, and end of the interval. The purpose is to imitate a Taylor series expansion, but without the necessity of computing higher derivatives.

Starting with a Taylor series expansion, we get:

$$u(t+\Delta t) = u(t) + \Delta t u'(t) + \frac{\Delta t^2}{2!} u''(t) + \frac{\Delta t^3}{3!} u'''(t) + \frac{\Delta t^4}{4!} u''''(t) + O(\Delta t^5).$$

The first derivative $u'(t)$ is already provided by the ODE:

$$u'(t) = f(t, u).$$

Higher-order derivatives can also be represented in terms of $f(t, u)$ and its derivatives:

$$u''(t) = \frac{df}{dt} = \frac{\partial f}{\partial t} + \frac{\partial f}{\partial u} \frac{du}{dt} = \frac{\partial f}{\partial t} + \frac{\partial f}{\partial u} f,$$

The Runge-Kutta method is designed to mimic the above Taylor series expansion by taking a suitable weighted average of increments at the start, middle, and end of the interval. It avoids explicitly calculating higher derivatives of $f(t, u)$, instead approximating these increments by evaluating $f(t, u)$ at several points within the interval.

The 4th order Runge-Kutta method is thus given by:

$$k_1 = \Delta t \cdot f(t, u),$$

$$k_2 = \Delta t \cdot f\left(t + \frac{\Delta t}{2}, u + \frac{k_1}{2}\right),$$

$$k_3 = \Delta t \cdot f\left(t + \frac{\Delta t}{2}, u + \frac{k_2}{2}\right),$$

$$k_4 = \Delta t \cdot f(t + \Delta t, u + k_3),$$

$$u(t + \Delta t) = u(t) + \frac{1}{6}(k_1 + 2k_2 + 2k_3 + k_4),$$

In this method, the weights of $k_1, k_2, k_3, k_4$ (1/6, 1/3, 1/3, 1/6) are chosen such that the error term is $O(\Delta t^5)$, indicating that the local truncation error at each step is proportional to the fifth power of the step size, and the global truncation error (after $N$ steps) is proportional to the fourth power of the step size.

## Algorithm Steps

1. Begin with the initial condition $u(t_0) = u_0$.
2. For each step, compute $k_1, k_2, k_3, k_4$ as indicated above.
3. Update $u(t + \Delta t) = u(t) + \frac{1}{6}(k_1 + 2k_2 + 2k_3 + k_4)$.
4. Repeat steps 2 and 3 until a specified number of iterations is reached or the solution approximation is satisfactory.

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

Then, we calculate the next value of $u$:

$$u(0.05) = u(0) + \frac{1}{6}(k_1 + 2k_2 + 2k_3 + k_4)$$

$$u(0.05) = 1 + \frac{1}{6}(0.05 + 2 \cdot 0.05125 + 2 \cdot 0.0515625 + 0.052578125)$$

$$u(0.05) = 1.05104166667.$$

2. Now that we have $u(0.05)$, we move on to $t = 0.1$.

Similarly, we first calculate the four increments:

$$k_1 = \Delta t \cdot f(t, u) = 0.05 \cdot 1.05104166667 = 0.0525520833335,$$

$$k_2 = \Delta t \cdot f\left(t + \frac{\Delta t}{2}, u + \frac{k_1}{2}\right) = 0.05 \cdot (1.05104166667 + 0.0525520833335/2) = 0.0531899049680,$$

$$k_3 = \Delta t \cdot f\left(t + \frac{\Delta t}{2}, u + \frac{k_2}{2}\right) = 0.05 \cdot (1.05104166667 + 0.0531899049680/2) = 0.0533905595735,$$

$$k_4 = \Delta t \cdot f(t + \Delta t, u + k_3) = 0.05 \cdot (1.05104166667 + 0.0533905595735) = 0.0552220602058.$$

Then, we calculate the next value of $u$:

$$u(0.1) = u(0.05) + \frac{1}{6}(k_1 + 2k_2 + 2k_3 + k_4)$$

$$u(0.1) = 1.05104166667 + \frac{1}{6}(0.0525520833335 + 2 \cdot 0.0531899049680 + 2 \cdot 0.0533905595735 + 0.0552220602058)$$

$$u(0.1) = 1.10517087727.$$

## Advantages

- Runge-Kutta methods, especially the 4th order, provide a good compromise between accuracy and computational effort.
- They do not require the computation of higher derivatives of $f(t, u)$, unlike Taylor series methods.

## Limitations

- Runge-Kutta methods can become inefficient for stiff differential equations, which may require an implicit method.
- The error accumulates with each step, hence they may not be suitable for problems requiring high precision.
