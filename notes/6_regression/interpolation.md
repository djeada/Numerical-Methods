## Interpolation

Interpolation is the problem of reconstructing an **unknown function** from a *finite* set of **exact** data pairs

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

> **Extrapolation** is the computation of $\hat f(x)$ for $x\notin[x_0,x_n]$ and is *not* covered by the uniqueness theorem; error growth can be dramatic.

### Assumptions

* **Exact data** No measurement error: $y_i=f(x_i)$ is taken as ground truth.
* **Distinct, ordered abscissas** $x_i\neq x_j$ for $i\neq j$ and $x_0<x_1<\dots <x_n$.
* **Smoothness of the underlying function** Needed only when one wants *error bounds*; e.g. $f\in C^{n+1}[x_0,x_n]$ for polynomial-error formulas.

### Concepts

| Method                          | Essential idea                                          | Interpolant form                                                                         | Error behavior\*                                                | Typical use-case                       |
| ------------------------------- | ------------------------------------------------------- | ---------------------------------------------------------------------------------------- | --------------------------------------------------------------- | -------------------------------------- |
| **Linear**                      | Join successive points by straight segments             | Piecewise degree-1                                                                       | $O(h^2)$                                                        | Fast previews, computer graphics       |
| **Polynomial**                  | Single poly of degree $n$ through all nodes             | Lagrange, Newton, barycentric, etc.                                                      | $O(h^{n+1})$ but risk of *Runge* oscillations when $n$ is large | Small $n$ on modest intervals          |
| **Spline**                      | Glue low-degree polynomials with continuity constraints | Piecewise degree-$k$ (usually 3)                                                         | $O(h^{k+1})$ plus good shape control                            | Smooth curves, CAD/CAM, statistics     |
| **Radial Basis Function (RBF)** | Weighted radial kernels centered at nodes               | $\displaystyle \hat f(x)=\sum_{i=0}^{n} \lambda_i\,\phi\bigl(\lVert x - x_i\rVert\bigr)$ | Spectral for smooth $\phi$                                      | Scattered data, high-dimensional grids |

Assuming evenly spaced nodes with spacing $h=\max_i (x_{i+1}-x_i)$.

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

**Error bound** (Peano form): if $f\in C^{n+1}$, then for some $\xi(x)\in[x_0,x_n]$

$$
f(x)-P_n(x)=\frac{f^{(n+1)}(\xi(x))}{(n+1)!}\prod_{i=0}^{n}(x-x_i).
$$

III. **Natural cubic spline**

Solve the tridiagonal system

$$
h_{i-1}M_{i-1}+2(h_{i-1}+h_i)M_i+h_iM_{i+1}=6
\left(\frac{y_{i+1}-y_i}{h_i}-\frac{y_i-y_{i-1}}{h_{i-1}}\right),
$$

with $M_0=M_n=0$, where $h_i=x_{i+1}-x_i$.

Each piece is then

$$
S_i(x)=\frac{M_i(x_{i+1}-x)^3+M_{i+1}(x-x_i)^3}{6h_i}
+\left(\frac{y_{i+1}}{h_i}-\frac{M_{i+1}\,h_i}{6}\right)(x-x_i)
+\left(\frac{y_i}{h_i}-\frac{M_i\,h_i}{6}\right)(x_{i+1}-x).
$$

### Example

| Time (h) | 9  | 10 | 11 | 12 | 13 | 14 | 15 |
| -------- | -- | -- | -- | -- | -- | -- | -- |
| Temp (°C)| 20 | 22 | 26 | 28 | 30 | 31 | 31 |

Estimate $T(10.5)$.

I. **Linear (segment 10 – 11)**

$$
T(10.5)=22+\frac{26-22}{11-10}(10.5-10)=24\text{ °C}.
$$

> The linear interpolation error is bounded by $\displaystyle\frac{h^2}{8}\max|f''|$. With $h=1$ and a moderate second derivative, this gives an error on the order of tenths of a degree.

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

Solving via the Thomas algorithm yields

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
\approx 24.02\text{ °C}.
$$

The spline estimate is very close to the linear result here because the curvature contributions from $M_1$ and $M_2$ nearly cancel at the midpoint of this segment.

### Advantages

* **Locality & smoothness control** (splines, RBFs).
* **Provable error bounds** under mild differentiability assumptions.
* **Exactness at data points**—no bias at nodes.

### Limitations

* **Runge phenomenon** for high-degree global polynomials on equispaced nodes.
* **Error amplification outside $[x_0,x_n]$** (extrapolation).
* **Method sensitivity** Different schemes yield different smoothness, boundary behavior, and error constants; choice must match the application.
