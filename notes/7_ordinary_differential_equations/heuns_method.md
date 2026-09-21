## Heun's Method

Heun's method improves Euler's method by using information from both ends of each step. It is a second-order explicit Runge--Kutta method and is also known as the **explicit trapezoidal method** or **improved Euler method**.

For the IVP

$$
u'(t)=f(t,u), \qquad u(t_0)=u_0,
$$

Euler uses only the slope at the beginning of a step. Heun first predicts the endpoint, evaluates the slope there, and then advances using the average of the two slopes.

![Heun predictor-corrector geometry](https://github.com/djeada/Numerical-Methods/raw/refs/heads/master/notes/7_ordinary_differential_equations/resources/plots/heun_predictor_corrector.svg)

### Predictor-Corrector Form

Given $(t_n,u_n)$ and step size $h$:

**Predictor**

$$
\widetilde{u}_{n+1}
=
u_n+h f(t_n,u_n).
$$

**Corrector**

$$
u_{n+1}
=
u_n+\frac{h}{2}
\left[
f(t_n,u_n)
+
f(t_n+h,\widetilde{u}_{n+1})
\right].
$$

The predictor is an Euler step. The corrector replaces Euler's single slope by the average of the start and predicted-end slopes.

### Why the Average Helps

The exact solution satisfies

$$
u(t_{n+1})-u(t_n)
=
\int_{t_n}^{t_{n+1}} f(t,u(t))\,dt.
$$

If this integral is approximated by the trapezoidal rule,

$$
u(t_{n+1})
\approx
u(t_n)
+
\frac{h}{2}
\left[
f(t_n,u(t_n))
+
f(t_{n+1},u(t_{n+1}))
\right].
$$

The unknown endpoint $u(t_{n+1})$ would make this implicit. Heun avoids that by replacing it with the Euler prediction $\widetilde{u}_{n+1}$.

The result has:

- **local truncation error:** $O(h^3)$,
- **global error:** $O(h^2)$.

Halving $h$ therefore reduces the global error by roughly a factor of four.

![Heun converges faster than Euler as the step is refined](https://github.com/djeada/Numerical-Methods/raw/refs/heads/master/notes/7_ordinary_differential_equations/resources/plots/heun_error_vs_step.svg)

### Worked Example

Use

$$
u'=u, \qquad u(0)=1,
$$

with $h=0.05$.

For the first step:

$$
k_1=f(0,1)=1,
$$

$$
\widetilde{u}_1
=
1+0.05(1)
=
1.05,
$$

$$
k_2
=
f(0.05,1.05)
=
1.05.
$$

Then

$$
u_1
=
1+\frac{0.05}{2}(1+1.05)
=
1.05125.
$$

For the second step:

$$
\widetilde{u}_2
=
1.05125+0.05(1.05125)
=
1.1038125,
$$

and therefore

$$
u_2
=
1.05125
+
\frac{0.05}{2}
(1.05125+1.1038125)
=
1.1051265625.
$$

The exact value is $e^{0.1}\approx1.105170186$, so Heun is much closer than Euler with the same step size.

### Runge--Kutta Interpretation

Heun can be written as

$$
k_1=f(t_n,u_n),
$$

$$
k_2=f(t_n+h,u_n+h k_1),
$$

$$
u_{n+1}
=
u_n+\frac{h}{2}(k_1+k_2).
$$

This is a two-stage explicit Runge--Kutta method. It uses two evaluations of $f$ per step instead of one.

### Algorithm

```text
t = t0
u = u0

while t < tf:
    k1 = f(t, u)
    predictor = u + h*k1
    k2 = f(t + h, predictor)

    u = u + h*(k1 + k2)/2
    t = t + h
```

### Accuracy Versus Cost

Compared with Euler:

| Method | Function evaluations per step | Global order |
|---|---:|---:|
| Euler | 1 | 1 |
| Heun | 2 | 2 |

A Heun step costs about twice as much if evaluating $f$ dominates the work, but its error decreases much faster under step refinement.

### Stability

Applied to

$$
u'=\lambda u,
$$

Heun produces the amplification factor

$$
R(z)=1+z+\frac{z^2}{2},
\qquad z=h\lambda.
$$

The method is stable for values of $z$ satisfying

$$
|R(z)|\le 1.
$$

Its stability region is larger than Euler's in some directions, but Heun is still explicit and is not a good default for strongly stiff systems.

### Advantages

- Second-order accuracy with a simple formula.
- Easy to understand as a predictor-corrector method.
- More accurate than Euler for a similar conceptual complexity.
- Useful as a building block for more general Runge--Kutta schemes.

### Limitations

- Requires two evaluations of $f$ per step.
- Still uses an explicit stability region.
- Fixed-step implementations do not automatically adapt to difficult portions of a trajectory.
- Stiff systems generally require implicit methods.
