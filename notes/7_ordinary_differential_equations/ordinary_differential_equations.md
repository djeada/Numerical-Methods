## Ordinary Differential Equations

An **ordinary differential equation (ODE)** relates an unknown function of one independent variable to one or more of its derivatives. ODEs are the natural language of dynamical systems: they describe how a state changes when its instantaneous rate of change is known.

A general $n$th-order ODE can be written as

$$
F\left(t, y, y', \ldots, y^{(n)} \right) = 0.
$$

The word *ordinary* means that derivatives are taken with respect to a single independent variable. If several independent variables appear, the corresponding equation is a partial differential equation.

### From a Model to a Trajectory

A common first-order form is

$$
y'(t) = f(t,y(t)),
\qquad y(t_0) = y_0.
$$

At every point $(t,y)$, the function $f$ specifies the slope of a possible solution curve. The initial condition chooses one trajectory from that slope field.

Autonomous problems have the form

$$
y' = f(y),
$$

so the direction of motion depends only on the current state.

![Phase-line behavior of a logistic ODE](https://github.com/djeada/Numerical-Methods/raw/refs/heads/master/notes/7_ordinary_differential_equations/resources/plots/ode_phase_line.svg)

For example, the logistic equation

$$
y' = r y\left(1 - \frac{y}{K}\right)
$$

has equilibria at $y=0$ and $y=K$. When $0<y<K$, the derivative is positive; when $y>K$, it is negative. This qualitative information already reveals the long-term behavior without solving the equation explicitly.

### Initial Value Problems and Boundary Value Problems

An **initial value problem (IVP)** specifies all required conditions at one point. For a second-order ODE,

$$
y'' = g(t,y,y'),
$$

a typical IVP is

$$
y(t_0) = y_0,
\qquad y'(t_0) = v_0.
$$

A **boundary value problem (BVP)** specifies conditions at different locations, for example

$$
y'' + y = 0,
\qquad y(0) = 0,
\qquad y(1) = 1.
$$

IVPs are naturally advanced forward or backward in the independent variable. BVPs usually require different numerical ideas such as shooting or finite differences.

### Classification

#### Order

The order is the highest derivative present.

- $y'=f(t,y)$ is first order.
- $y''+3y'+2y=0$ is second order.
- $y^{(4)}+y=0$ is fourth order.

#### Linear and Nonlinear ODEs

A linear $n$th-order ODE has the form

$$
a_n(t)y^{(n)} + \cdots + a_1(t)y' + a_0(t)y = g(t).
$$

The unknown function and its derivatives appear only linearly.

Examples:

$$
y' + 2y = \sin t
$$

is linear, while

$$
y' = y^2 - t
$$

and

$$
y'' + \sin y = 0
$$

are nonlinear.

#### Homogeneous and Nonhomogeneous Linear Equations

A linear equation is homogeneous when $g(t)=0$. Otherwise it is nonhomogeneous.

### Converting Higher-Order Equations to First-Order Systems

Numerical solvers are usually written for first-order systems. Any higher-order ODE can be rewritten in that form.

For

$$
y'' + c y' + k y = 0,
$$

define

$$
u_1 = y,
\qquad u_2 = y'.
$$

Then

$$
u_1' = u_2,
$$

$$
u_2' = -k u_1 - c u_2.
$$

So the second-order scalar problem becomes

$$
\mathbf{u}' = \mathbf{f}(t,\mathbf{u}).
$$

The same conversion works for arbitrary order.

### Existence and Uniqueness

For

$$
y' = f(t,y),
\qquad y(t_0) = y_0,
$$

a standard local result is the Picard--Lindelof theorem. Roughly, if:

- $f$ is continuous near $(t_0,y_0)$, and
- $f$ is Lipschitz continuous in $y$,

then the IVP has a unique local solution.

A Lipschitz condition in $y$ means there is a constant $L$ such that

$$
|f(t,y_1) - f(t,y_2)| \le L|y_1 - y_2|.
$$

This condition prevents nearby solution curves from splitting unpredictably.

### Analytical Versus Numerical Solutions

Some ODEs have closed-form solutions. Many important nonlinear systems do not.

For example,

$$
y' = ay
$$

has the exact solution

$$
y(t) = y_0e^{a(t-t_0)}.
$$

But once $f$ becomes nonlinear, coupled, discontinuous, or expensive, numerical integration is often the practical route.

Common explicit methods include:

- Euler's method,
- Heun's method,
- Runge--Kutta methods.

Their accuracy can differ dramatically at the same step size.

![Accuracy comparison for several time-stepping methods](https://github.com/djeada/Numerical-Methods/raw/refs/heads/master/notes/7_ordinary_differential_equations/resources/plots/ode_method_accuracy.svg)

### Local and Global Error

A one-step method advances by

$$
u_{n+1} = \Phi_h(t_n,u_n).
$$

Two distinct errors are useful:

- **local truncation error:** the error produced in one step when starting from the exact solution,
- **global error:** the accumulated difference after many steps.

A method of global order $p$ typically satisfies

$$
\max_n |u(t_n) - u_n| = O(h^p)
$$

on a fixed interval as $h\to0$.

Euler has order $1$, Heun order $2$, and classical RK4 order $4$.

### Stability and Stiffness

Accuracy alone does not guarantee a good numerical solution.

For the test equation

$$
y' = \lambda y,
$$

a numerical method produces

$$
y_{n+1} = R(h\lambda)y_n,
$$

where $R$ is the method's stability function. Stability requires the numerical amplification to behave consistently with the exact solution.

A problem is called **stiff** when rapidly decaying modes force explicit methods to use very small steps for stability even though the physically interesting solution evolves on a much slower time scale.

In stiff regimes, implicit methods such as backward Euler, BDF schemes, or implicit Runge--Kutta methods are usually preferred.

### Adaptive Step Sizes

Modern ODE solvers rarely use a single fixed $h$ everywhere. Instead they estimate local error and adapt the step size:

- reduce $h$ when the solution changes rapidly,
- increase $h$ when the solution is smooth.

Embedded Runge--Kutta pairs, such as RK45, obtain two approximations of different orders from related stage evaluations and use their difference as an error estimate.

### Important Model Examples

#### Exponential Growth and Decay

$$
y' = ay.
$$

The sign of $a$ determines growth or decay.

#### Logistic Growth

$$
P' = rP\left(1 - \frac{P}{K}\right).
$$

The parameter $K$ is the carrying capacity.

#### Harmonic Oscillator

$$
x'' + \omega^2x = 0.
$$

As a first-order system:

$$
x' = v,
\qquad v' = -\omega^2x.
$$

#### Damped Oscillator

$$
x'' + 2\zeta\omega x' + \omega^2x = 0.
$$

The damping ratio $\zeta$ controls whether the motion is underdamped, critically damped, or overdamped.

### A Practical Workflow

When solving an ODE numerically:

1. identify whether the problem is an IVP or BVP,
2. rewrite higher-order equations as a first-order system,
3. inspect scales, smoothness, and possible stiffness,
4. choose a suitable method and tolerance,
5. verify convergence by tightening the step or tolerance,
6. compare against invariants, known limits, or exact solutions when available,
7. interpret the numerical result in the context of the model.
