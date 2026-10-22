# Picard's Iteration Method

Picard iteration turns an initial value problem into a sequence of integral approximations. Each iterate is a function obtained by substituting the previous function into the ODE's integral form. This construction is central to the Picard–Lindelof existence-and-uniqueness theorem and explains how fixed-point arguments enter the analysis of ODE solvers.

Consider

$$
y'(t) = f(t,y(t)),
\qquad y(t_0) = y_0.
$$

Integrating from $t_0$ to $t$ gives the equivalent integral equation

$$
y(t) = y_0 + \int_{t_0}^{t} f(s,y(s))\, ds.
$$

Picard's method replaces the unknown function inside the integral with the previous approximation.

## Picard iteration

Choose an initial function, often

$$
y_0(t) = y_0.
$$

Then define

$$
y_{n+1}(t) = y_0 + \int_{t_0}^{t} f(s,y_n(s))\, ds.
$$

Each iteration produces a new function, not merely a single number.

Here the subscript $n$ counts improvements to the entire function $y_n(t)$; it is not a time-grid index. The starting object $y_0(t)$ is a constant function equal to the prescribed initial value $y_0$. If the integral is discretized, all values of the next function should be formed from the previous function unless a different iteration has deliberately been chosen.

![Successive Picard iterates approaching the exact solution](https://github.com/djeada/Numerical-Methods/raw/refs/heads/master/notes/7_ordinary_differential_equations/resources/plots/picard_iterates.svg)

## Fixed-point interpretation

Define an operator

$$
(Ty)(t) = y_0 + \int_{t_0}^{t} f(s,y(s))\, ds.
$$

A solution of the IVP is exactly a fixed point:

$$
Ty = y.
$$

Picard iteration is therefore the fixed-point iteration

$$
y_{n+1} = Ty_n.
$$

If $T$ is a contraction on a suitable function space, the contraction mapping theorem guarantees convergence to a unique fixed point.

## Why the Lipschitz condition appears

Suppose

$$
|f(t,y) - f(t,z)| \le L|y - z|.
$$

Then on a short interval $|t-t_0|\le a$,

$$
|(Ty)(t) - (Tz)(t)| \le \int_{\min(t,t_0)}^{\max(t,t_0)} L|y(s) - z(s)|\, ds.
$$

Using the supremum norm,

$$
\| Ty - Tz\|_\infty \le La\| y - z\|_\infty.
$$

If

$$
La<1,
$$

then $T$ is a contraction. This is the core idea behind the local Picard--Lindelof theorem.

### Keeping the iterates inside the theorem's domain

The contraction estimate is only part of the argument: $T$ must also map the chosen function space into itself. Suppose $f$ is continuous and bounded by $M$ on the rectangle $|t-t_0|\leq a$, $|y-y_0|\leq b$. Restrict attention to continuous functions in the state band and choose $a$ so that $aM\leq b$. Then

$$
|(Ty)(t)-y_0|\leq aM\leq b,
$$

so $T$ preserves that band. Combining this with $q=La<1$ gives a contraction on a closed set of continuous functions in the supremum norm. The fixed point solves the integral equation and, by differentiation, the original IVP.

The simple contraction condition is sufficient, not necessary. In the linear worked example, $L=1$ and the displayed evaluation point $x=1$ makes $La=1$, so the strict one-step contraction bound does not establish convergence on $[0,1]$. Repeated integration supplies a sharper factorial estimate:

$$
|y_n(x)-y(x)|\leq\frac{x^n}{n!}\|y_0-y\|_{\infty,[0,1]},\qquad 0\leq x\leq1.
$$

It follows by applying $|y_{n+1}(x)-y(x)|\leq\int_0^x|y_n(t)-y(t)|\,dt$ repeatedly. Since $1/n!\to0$, the table at $x=1$ is justified even though the simpler contraction test is inconclusive there.

## Worked example

Consider

$$
y' = x + y,
\qquad y(0) = 1.
$$

The integral form is

$$
y(x) = 1 + \int_0^x(t + y(t))\, dt.
$$

Start with

$$
y_0(x) = 1.
$$

The first iterate is

$$
y_1(x) = 1 + \int_0^x(t + 1)\, dt = 1 + x + \frac{x^2}{2}.
$$

The second iterate is

$$
y_2(x) = 1 + \int_0^x \left(t + 1 + t + \frac{t^2}{2} \right)dt,
$$

so

$$
y_2(x) = 1 + x + x^2 + \frac{x^3}{6}.
$$

The third iterate is

$$
y_3(x) = 1 + x + x^2 + \frac{x^3}{3} + \frac{x^4}{24}.
$$

The exact solution of

$$
y' - y = x
$$

is

$$
y(x) = 2e^x - x - 1.
$$

The iterates approach this solution on intervals where the contraction argument applies.

At $x=1$ the exact value is $2e-2\approx3.4366$, and the iterates give:

| Iterate | $y_n(1)$ | Error at $x=1$ |
| --- | --: | --: |
| $y_0$ | $1$ | $2.4366$ |
| $y_1$ | $2.5$ | $0.9366$ |
| $y_2$ | $3.1667$ | $0.2699$ |
| $y_3$ | $3.375$ | $0.0616$ |

The iterate $y_n$ agrees with the Taylor series of the exact solution through the $x^n$ term, so the error shrinks rapidly on this short interval.

![Picard iteration error decreases with iteration count](https://github.com/djeada/Numerical-Methods/raw/refs/heads/master/notes/7_ordinary_differential_equations/resources/plots/picard_convergence.svg)

## An important distinction

Picard iteration is sometimes described as a numerical method, but a direct implementation can be expensive because every iteration requires a new integral over an entire function.

In practical numerical integration, methods such as Runge–Kutta usually provide better efficiency. Picard iteration remains especially valuable for:

- proving local existence and uniqueness,
- deriving series approximations,
- understanding fixed-point methods,
- motivating iterative schemes for integral and differential equations.

## Numerical implementation

If the integral cannot be evaluated analytically, choose grid points

$$
t_0<t_1<\cdots<t_m
$$

and approximate

$$
\int_{t_0}^{t_j}f(s,y_n(s))\, ds
$$

with a quadrature rule.

This creates two sources of error:

1. iteration error from stopping after finitely many Picard steps,
2. quadrature error from approximating the integral.

The two errors should not be confused.

The repository function `picard_method` in `src/7_ordinary_differential_equations/picard` is **not** Picard iteration on whole functions, despite its name. It is a step-by-step method: on each step it solves the implicit midpoint equation

$$
y_{n+1} = y_n + h f\left(t_n + \frac{h}{2}, \frac{y_n + y_{n+1}}{2}\right)
$$

by fixed-point (Picard-style) substitution. The substitution converges when $hL/2<1$, and the resulting method is second-order accurate. The name refers only to the fixed-point iteration used inside each step.

For an inner iterate $v^{(m)}$, the map is $v\mapsto y_n+hf(t_n+h/2,(y_n+v)/2)$, whose Lipschitz factor is $q=hL/2$. If $q<1$, the remaining inner-solve error after an update is bounded by $q\|v^{(m+1)}-v^{(m)}\|/(1-q)$. The implicit midpoint method is second order when its nonlinear solves are sufficiently accurate; a loose inner tolerance can dominate the time-discretization error. Moreover, an implicit method's stability does not guarantee that this particular fixed-point solver converges for a large step.

When $(t_\text{end}-t_0)/h$ is not an integer, the last step is shortened so that the returned grid ends exactly at $t_\text{end}$. The returned array has shape `(n + 1,)` for a scalar ODE and `(n + 1, d)` for a system with `d` components.

## Convergence caveats

Picard iteration may fail or become inconvenient when:

- $f$ is not Lipschitz in the relevant region,
- the interval is too large for the contraction estimate,
- iterates leave the region where the assumptions hold,
- evaluating the required integrals is difficult,
- the ODE is stiff or highly nonlinear.

A local convergence theorem does not imply that one Picard iteration run converges uniformly over an arbitrarily long interval.
