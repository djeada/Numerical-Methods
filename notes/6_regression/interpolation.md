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
S_i(x)=\frac{M_{i+1}(x-x_i)^3+M_i(x_{i+1}-x)^3}{6h_i}
+\frac{y_{i+1}}{h_i}(x-x_i)-\frac{y_i}{h_i}(x_{i+1}-x)
-\frac{h_i}{6}\bigl(M_{i+1}-M_i\bigr)(x-x_i).
$$

### Example

| Time (hh) | Temp (°C) |
| --------- | --------- |
| 9         | 20        |
| 10        | 22        |
| 11        | 26        |
| 12        | 28        |
| 13        | 30        |
| 14        | 31        |
| 15        | 31        |

Estimate $T(10.5)$.

I. **Linear (segment 10 – 11)**

$$
T(10.5)=22+\frac{26-22}{11-10}(10.5-10)=24\text{ °C}.
$$

II. **Natural cubic spline (all nodes)**

Solving the spline system yields second derivatives

$$
(M_0,\dots,M_6)\approx(0,\;2.4,\;3.6,\;0.6,\;-1.2,\;-0.6,\;0).
$$

From the $i=1$ piece (10–11 h) one obtains

$$
T(10.5)\approx 24.77\text{ °C}.
$$

Because the temperature rise slows near noon, the spline—by “seeing” the curvature—predicts a slightly higher value than the straight-line model.

### Advantages

* **Locality & smoothness control** (splines, RBFs).
* **Provable error bounds** under mild differentiability assumptions.
* **Exactness at data points**—no bias at nodes.

### Limitations

* **Runge phenomenon** for high-degree global polynomials on equispaced nodes.
* **Error amplification outside $[x_0,x_n]$** (extrapolation).
* **Method sensitivity** Different schemes yield different smoothness, boundary behavior, and error constants; choice must match the application.
