## Interpolation

Interpolation constructs a function that matches a finite set of supplied data pairs

$$
\{(x_i,y_i)\}_{i=0}^{n},\qquad x_0< x_1<\dots <x_n,\qquad y_i=f(x_i).
$$

Given a query point $x$ in the closed interval $[x_0,x_n]$, the task is to compute an *interpolant* $\hat f(x)$ such that

$$
\hat f(x_i)=y_i \text{for every }i=0,\dots ,n,
\qquad\text{and}\qquad 
\hat f(x)\approx f(x) \text{for }x\in[x_0,x_n].
$$

Because the nodes $x_i$ are **distinct**, the classical existence-and-uniqueness theorem guarantees that there is a unique algebraic polynomial $P_n$ of degree at most $n$ satisfying the interpolation conditions.

> **Extrapolation** evaluates the same uniquely determined polynomial outside $[x_0,x_n]$. Uniqueness still holds, but it does not guarantee accuracy there—or between the nodes. Infinitely many non-polynomial functions can match the same data.

### Assumptions

* **Data treated as exact constraints.** Measurements may contain noise; interpolation reproduces it. For fitting a trend in noisy observations, see [regression](regression.md).
* **Distinct, ordered abscissas** $x_i\neq x_j$ for $i\neq j$ and $x_0<x_1<\dots <x_n$.
* **Smoothness of the underlying function** Needed only when one wants *error bounds*; e.g. $f\in C^{n+1}[x_0,x_n]$ for polynomial-error formulas.

### Concepts

| Method | Construction | Conditions and behavior |
| --- | --- | --- |
| [Linear](linear_interpolation.md) | Join consecutive nodes with lines | Continuous; slopes may jump. Error on a segment of width $h$ is at most $h^2\max\lvert f''\rvert/8$ for $f\in C^2$. |
| [Lagrange](lagrange_polynomial_interpolation.md) / [Newton](newton_polynomial.md) | One polynomial of degree at most $n$ | Distinct nodes; use the remainder below. Increasing degree does not guarantee convergence. |
| [Gauss](gaussian_interpolation.md) | A central ordering of Newton interpolation | Requires equal spacing; the full polynomial is unchanged by ordering. |
| [Cubic spline](cubic_spline_interpolation.md) | Piecewise cubics with two continuous derivatives | Needs endpoint conditions; can overshoot. Error order depends on smoothness, mesh, and boundary conditions. |
| [Thin plate spline](thin_plate_spline_interpolation.md) | Affine part plus radial kernels in two dimensions | Distinct, non-collinear locations; a global fit for scattered data. |

Choose the method before evaluating the query. Different interpolants can agree at every node and disagree between them. Natural cubic splines, for example, do not automatically achieve a uniform fourth-order error for functions whose endpoint second derivatives are nonzero.

### Mathematical Formulation

I. **Linear interpolation (piecewise)**

For $x\in[x_i,x_{i+1}]$

$$
\hat f(x)=y_i+\frac{y_{i+1}-y_i}{x_{i+1}-x_i}\,(x-x_i).
$$

II. **Polynomial interpolation (global)**

Lagrange form

$$
P_n(x)=\sum_{i=0}^{n} y_i\,\ell_i(x),
\qquad
\ell_i(x)=\prod_{\substack{j=0 \\ j\neq i}}^{n}
\frac{x-x_j}{x_i-x_j}.
$$

**Interpolation remainder** (Lagrange form): if $f\in C^{n+1}$, then for some $\xi(x)\in[x_0,x_n]$

$$
f(x)-P_n(x)=\frac{f^{(n+1)}(\xi(x))}{(n+1)!}\prod_{i=0}^{n}(x-x_i).
$$

III. **Natural cubic spline**

Solve the tridiagonal system

$$
h_{i-1}M_{i-1}+2(h_{i-1}+h_i)M_i+h_iM_{i+1}=6
\left(\frac{y_{i+1}-y_i}{h_i}-\frac{y_i-y_{i-1}}{h_{i-1}}\right),
$$

for $i=1,\ldots,n-1$, with $M_0=M_n=0$, where $h_i=x_{i+1}-x_i$ and $M_i=S''(x_i)$.

Each piece is then

$$
S_i(x)=\frac{M_i(x_{i+1}-x)^3+M_{i+1}(x-x_i)^3}{6h_i}
+\left(\frac{y_{i+1}}{h_i}-\frac{M_{i+1}\,h_i}{6}\right)(x-x_i)
+\left(\frac{y_i}{h_i}-\frac{M_i\,h_i}{6}\right)(x_{i+1}-x).
$$

### Worked Example: Temperature at 10:30

**Inputs:** the time and temperature observations below. **Goal:** estimate the temperature at 10.5 h using a line and a natural cubic spline, then compare the results.

| Time (h) | 9  | 10 | 11 | 12 | 13 | 14 | 15 |
| -------- | -- | -- | -- | -- | -- | -- | -- |
| Temp (°C)| 20 | 22 | 26 | 28 | 30 | 31 | 31 |

I. **Linear (segment 10 – 11)**

$$
\hat T_{\mathrm{linear}}(10.5)=22+\frac{26-22}{11-10}(10.5-10)=24\text{ °C}.
$$

> If the underlying temperature function has $|T''|\le M$ on this interval, the error bound is $M(1\text{ h})^2/8$. The observations alone supply no bound on $M$, so they do not justify a numerical error claim.

II. **Natural cubic spline (all nodes)**

All spacings are equal ($h_i=1$ for every $i$), so the general tridiagonal equation

$$
h_{i-1}M_{i-1}+2(h_{i-1}+h_i)M_i+h_iM_{i+1}
=6\!\left(\frac{y_{i+1}-y_i}{h_i}-\frac{y_i-y_{i-1}}{h_{i-1}}\right)
$$

simplifies to

$$
M_{i-1}+4M_i+M_{i+1}=6(y_{i+1}-2y_i+y_{i-1}),\qquad i=1,\dots,5.
$$

Computing the right-hand sides from the data:

| $i$ | $y_{i-1}$ | $y_i$ | $y_{i+1}$ | $6(y_{i+1}-2y_i+y_{i-1})$ |
| --- | ---------- | ------ | ---------- | -------------------------- |
| 1   | 20         | 22     | 26         | $6(2)=12$                  |
| 2   | 22         | 26     | 28         | $6(-2)=-12$                |
| 3   | 26         | 28     | 30         | $6(0)=0$                   |
| 4   | 28         | 30     | 31         | $6(-1)=-6$                 |
| 5   | 30         | 31     | 31         | $6(-1)=-6$                 |

Together with the natural boundary conditions $M_0=M_6=0$, the $5\times 5$ tridiagonal system is

$$
\begin{pmatrix}4&1&&&\\ 1&4&1&&\\ &1&4&1&\\ &&1&4&1\\ &&&1&4\end{pmatrix}
\begin{pmatrix}M_1\\ M_2\\ M_3\\ M_4\\ M_5\end{pmatrix}
=\begin{pmatrix}12\\ -12\\ 0\\ -6\\ -6\end{pmatrix}.
$$

For transparency, exploit the unit off-diagonals to eliminate successively. The first four equations give

$$
M_2=12-4M_1,\quad M_3=15M_1-60,\quad
M_4=228-56M_1,\quad M_5=209M_1-858.
$$

The last equation is $M_4+4M_5=-6$. Substitution gives $780M_1-3204=-6$, hence $M_1=3198/780=41/10$. Back-substitution yields

$$
(M_0,\dots,M_6)=\!\left(0,\;\tfrac{41}{10},\;-\tfrac{22}{5},\;\tfrac{3}{2},\;-\tfrac{8}{5},\;-\tfrac{11}{10},\;0\right)
\approx(0,\;4.1,\;{-4.4},\;1.5,\;{-1.6},\;{-1.1},\;0).
$$

For the segment $i=1$ (10–11 h) with $x=10.5$, $x_i=10$, $x_{i+1}=11$, $h_i=1$:

$$
S_1(10.5)
=\frac{M_2(0.5)^3+M_1(0.5)^3}{6}
+\left(y_2-\frac{M_2}{6}\right)(0.5)
+\left(y_1-\frac{M_1}{6}\right)(0.5)
$$

$$
=\frac{(-4.4+4.1)(0.125)}{6}
+\left(26+\frac{4.4}{6}\right)(0.5)
+\left(22-\frac{4.1}{6}\right)(0.5)
= -0.00625+13.366666\ldots+10.658333\ldots
=24.01875\text{ °C}\approx24.02\text{ °C}.
$$

The spline estimate is very close to the linear result here because the curvature contributions from $M_1$ and $M_2$ nearly cancel at the midpoint of this segment.

### Checks and Interpretation

The computed second derivatives satisfy the system: for example, $4(4.1)-4.4=12$ and $-1.6+4(-1.1)=-6$. Each spline piece reproduces its two endpoint temperatures. These checks verify construction, not the unknown temperature at 10.5 h.

The estimates differ by $0.01875$ °C. Neither is established as more accurate without additional measurements or assumptions.

### Advantages

* Exact agreement with supplied values at the nodes.
* A choice of continuity and smoothness appropriate to the task.
* Error bounds when the underlying function satisfies the required derivative bounds.

### Limitations

* **Runge phenomenon** for high-degree global polynomials on equispaced nodes.
* **Error amplification outside $[x_0,x_n]$** (extrapolation).
* **Method sensitivity** Different schemes yield different smoothness, boundary behavior, and error constants; choice must match the application.
