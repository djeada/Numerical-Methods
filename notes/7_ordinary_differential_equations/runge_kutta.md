# Runge–Kutta Methods

Runge–Kutta methods advance an ODE solution using several carefully chosen slope evaluations inside each step. They achieve higher-order accuracy without requiring derivatives of $f$; only evaluations of $f$ itself are needed.

Consider

$$
u'(t) = f(t,u),
\qquad u(t_0) = u_0.
$$

The best-known member of the family is the classical fourth-order Runge–Kutta method, usually called **RK4**.

## Classical RK4

Given $(t_n,u_n)$ and step size $h$,

$$
k_1 = f(t_n,u_n),
$$

$$
k_2 = f\left(t_n + \frac{h}{2}, u_n + \frac{h}{2}k_1 \right),
$$

$$
k_3 = f\left(t_n + \frac{h}{2}, u_n + \frac{h}{2}k_2 \right),
$$

$$
k_4 = f(t_n + h,u_n + h k_3).
$$

Then

$$
u_{n+1} = u_n + \frac{h}{6} \left(k_1 + 2k_2 + 2k_3 + k_4 \right).
$$

The four stages sample the vector field at the beginning, twice near the middle, and at the end of the step.

![The four RK4 stages sample slopes within one step](https://github.com/djeada/Numerical-Methods/raw/refs/heads/master/notes/7_ordinary_differential_equations/resources/plots/rk4_stages.svg)

## Why RK4 is fourth order

The exact solution has a Taylor expansion containing derivatives such as $u''$, $u'''$, and $u^{(4)}$. Those derivatives can be expressed using derivatives of $f$, but computing them explicitly is inconvenient.

Runge–Kutta methods instead choose stage locations and weights so that the expansion of the numerical update matches the Taylor expansion through a desired order.

For RK4:

- local truncation error is $O(h^5)$,
- global error is $O(h^4)$.

Therefore, halving $h$ reduces the global error by roughly a factor of $16$ in the asymptotic regime.

![RK4 shows fourth-order convergence on a smooth test problem](https://github.com/djeada/Numerical-Methods/raw/refs/heads/master/notes/7_ordinary_differential_equations/resources/plots/rk4_error_vs_step.svg)

### Checking the order conditions

Let $A=(a_{ij})$ denote the strictly lower-triangular stage matrix, let $b$ be the weight vector, and let $c=A\mathbf1$ be the stage-time vector. Expanding each stage in Taylor series and matching the independent derivative terms gives the following conditions through order four. Powers of $c$ in this table are componentwise.

| Order | Conditions |
| --- | --- |
| 1 | $b^\top\mathbf1=1$ |
| 2 | $b^\top c=1/2$ |
| 3 | $b^\top c^2=1/3$, $b^\top Ac=1/6$ |
| 4 | $b^\top c^3=1/4$, $b^\top\operatorname{diag}(c)Ac=1/8$, $b^\top Ac^2=1/12$, $b^\top A^2c=1/24$ |

For example, the first two follow from $k_i=f+hc_i(f_t+f_uf)+O(h^2)$, giving $u_{n+1}=u+h(b^\top\mathbf1)f+h^2(b^\top c)(f_t+f_uf)+O(h^3)$. Matching the exact solution requires coefficients $1$ and $1/2$. The higher conditions account for the additional derivative combinations that appear at orders three and four.

Inserting the RK4 tableau satisfies all eight conditions, establishing fourth order under the required smoothness. On the simpler test equation $u'=\lambda u$, the stages reduce to polynomials in $z=h\lambda$ and the update is

$$
u_{n+1}=\left(1+z+\frac{z^2}{2}+\frac{z^3}{6}+\frac{z^4}{24}\right)u_n.
$$

This matches $e^z$ through degree four and independently checks the stability polynomial. Matching this one test equation alone would not establish order four for every nonlinear ODE; the full conditions explain the additional requirement.

## Worked example

For

$$
u' = u,
\qquad u(0) = 1,
$$

with $h=0.1$:

$$
k_1 = 1,
$$

$$
k_2 = 1 + 0.05k_1 = 1.05,
$$

$$
k_3 = 1 + 0.05k_2 = 1.0525,
$$

$$
k_4 = 1 + 0.1k_3 = 1.10525.
$$

Thus

$$
u_1 = 1 + \frac{0.1}{6} \left(1 + 2(1.05) + 2(1.0525) + 1.10525 \right),
$$

which gives

$$
u_1\approx1.105170833.
$$

The exact solution is

$$
e^{0.1}\approx1.105170918.
$$

The error after a single step is already below $10^{-6}$.

Keeping full precision, the one-step error is about $8.47\times10^{-8}$. The displayed stages are slopes, so the update multiplies their weighted average by $h$ once; some references instead define $k_i$ as increments already containing $h$. Mixing those two conventions changes the method.

## Butcher tableau

A Runge–Kutta method can be summarized by a **Butcher tableau**. For RK4:

$$
\begin{array}{c|cccc}
0 & 0 & 0 & 0 & 0 \\
\frac12 & \frac12 & 0 & 0 & 0 \\
\frac12 & 0 & \frac12 & 0 & 0 \\
1 & 0 & 0 & 1 & 0 \\
\hline
{} & \frac16 & \frac13 & \frac13 & \frac16
\end{array}
$$

The entries specify:

- where each stage is evaluated,
- how previous stages construct the stage state,
- how the final stages are combined.

## General explicit Runge–Kutta form

For an $s$-stage explicit method,

$$
k_i = f\left(t_n + c_i h, u_n + h\sum_{j=1}^{i-1}a_{ij}k_j \right),
$$

and

$$
u_{n+1} = u_n + h\sum_{i=1}^{s}b_i k_i.
$$

Different choices of the coefficients produce different methods and orders.

## Adaptive Runge–Kutta methods

Fixed-step RK4 is simple, but modern solvers often use **embedded pairs**, such as RK45.

An embedded pair computes two approximations of different orders using mostly the same stage evaluations. Their difference estimates the local error.

A controller then changes $h$:

- decrease $h$ when estimated error is too large,
- increase $h$ when the solution is smooth.

This can reduce work dramatically when a problem alternates between easy and difficult regions.

### Estimating RK4 error by step doubling

A fixed RK4 step has no built-in error estimate, but it can be compared with two half steps over the same time interval. Let $u_h$ be the one-step result and $u_{h/2,h/2}$ the two-half-step result, both starting from the same state. For a smooth problem, the accumulated leading error of the half steps is approximately $1/16$ of that of the full step, so

$$
u(t_n+h)-u_{h/2,h/2}\approx\frac{u_{h/2,h/2}-u_h}{15}.
$$

This provides an error estimate and an extrapolated value, at the cost of additional stage evaluations. The difference scales like $h^5$ over this one trial interval, so its basic step-size-controller exponent is $1/5$. Embedded pairs reuse their stages more efficiently, which is one reason they are common in adaptive solvers. Neither estimate is a certified bound when the required smoothness or asymptotic behavior is absent.

## Stability

For

$$
u' = \lambda u,
$$

RK4 has stability polynomial

$$
R(z) = 1 + z + \frac{z^2}{2} + \frac{z^3}{6} + \frac{z^4}{24},
\qquad z = h\lambda.
$$

The method is stable where

$$
|R(z)|\le1.
$$

On the negative real axis this is roughly $-2.78\le z\le 0$. RK4 has a useful explicit stability region but is not A-stable. Strongly stiff systems may still demand impractically small steps.

## RK4 versus Euler and Heun

| Method | Evaluations of $f$ per step | Global order |
| --- | --: | --: |
| Euler | 1 | 1 |
| Heun | 2 | 2 |
| RK4 | 4 | 4 |

Higher order does not automatically mean lower total cost. The best method depends on:

- desired accuracy,
- cost of evaluating $f$,
- smoothness,
- stiffness,
- whether adaptive time stepping is available.

## Systems of ODEs

RK4 applies directly to

$$
\mathbf{u}' = \mathbf{f}(t,\mathbf{u}).
$$

Each $k_i$ becomes a vector. This makes RK methods convenient for mechanics, circuits, chemical kinetics, population models, and other coupled systems.

## Repository implementation

`runge_kutta_4` takes a final time `t_end` and a nominal step `h`. When `(t_end - t0)/h` is not an integer, the last step is shortened so that the returned grid ends exactly at `t_end`; all earlier steps have length `h`. The returned array has shape `(n + 1,)` for a scalar ODE (one component) and `(n + 1, d)` for a system with `d` components.

## Advantages

- High accuracy for smooth non-stiff IVPs.
- No need to compute higher derivatives.
- Straightforward extension to systems.
- Well understood and easy to verify on benchmark problems.

## Limitations

- Four function evaluations per RK4 step.
- Fixed-step RK4 has no built-in error estimator.
- Explicit Runge–Kutta methods can be inefficient on stiff equations.
- Very long integrations may require methods that better preserve invariants or geometric structure.
