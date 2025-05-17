## Thin Plate Spline Interpolation

**Thin Plate Spline (TPS) interpolation** is a non‑parametric, spline‑based technique for fitting a smooth surface through scattered data in two or more spatial dimensions.  In its classical 2‑D form one seeks a function $f\colon\mathbb R^{2}\to\mathbb R$ that passes through specified data points while minimising the *thin‑plate bending energy*—the amount a thin metal sheet would bend if it were pinned at those points.  The construction extends naturally to higher dimensions and higher‑order splines.

While polynomials or other radial‑basis interpolants can achieve the same pointwise accuracy, TPS is unique in that it yields the *minimum possible bending energy* among *all twice‑differentiable functions matching the data*, so the fitted surface stays as flat (i.e. as smooth) as the constraints allow.  This makes TPS a staple in image warping, geometric modelling, and shape deformation tasks.

### Conceptual Illustration

Imagine you have a set of control points $(x\_i,y\_i,z\_i)$ in 3D space, where $(x\_i,y\_i)$ represent spatial coordinates and $z\_i$ is the function value at that location. Thin plate spline interpolation finds a surface $z=f(x,y)$ that exactly passes through all these points. If you imagine the surface as a thin metal sheet pinned at these points, the TPS solution is the shape the sheet would naturally take if it were free to bend but not stretch, minimizing the total bending energy:

![output](https://github.com/user-attachments/assets/7eac6046-7538-45a2-8ac2-f9893ae7ffb4)

The resulting surface is smooth, continuous in its derivatives, and tends to flatten out smoothly between data points.

### Mathematical Formulation

Given a set of $N$ data points ${(x\_i,y\_i,z\_i)}\_{i=1}^N$, where no two points coincide, we want to find a function:

$f(x,y) = \alpha_0 + \alpha_1 x + \alpha_2 y + \sum_{i=1}^N w_i \phi(\| (x,y)-(x_i,y_i) \|)$

that interpolates the given data. Here:

* The $\alpha\_0, \alpha\_1, \alpha\_2$ terms represent a polynomial of degree 1 (a plane) that gives the global trend.
* The function $\phi(r)$ is a radial basis function chosen as:

$\phi(r) = r^2 \ln(r)$

which is the fundamental solution associated with the thin plate spline bending energy in 2D.

* The $w\_i$ are the coefficients for the radial basis part.

This $f(x,y)$ must satisfy the interpolation conditions:

$f(x_i,y_i) = z_i, \quad i=1,\ldots,N.$

Additionally, to ensure a unique solution and remove degeneracies, $f(x,y)$ must satisfy:

$\sum_{i=1}^N w_i = \sum_{i=1}^N w_i x_i = \sum_{i=1}^N w_i y_i = 0$

This leads to a linear system for the unknown parameters $\alpha\_0,\alpha\_1,\alpha\_2,w\_1,\ldots,w\_N$

### Derivation

I. **Energy Minimization**:

Thin plate splines arise from minimizing a bending energy functional:

$J[f] = \int\int \left(\frac{\partial^2 f}{\partial x^2}\right)^2 + 2\left(\frac{\partial^2 f}{\partial x \partial y}\right)^2 + \left(\frac{\partial^2 f}{\partial y^2}\right)^2 \, dx dy,$
subject to the interpolation constraints $f(x\_i,y\_i)=z\_i$.

II. **Variational Problem**:

Solving the Euler-Lagrange equations associated with the energy minimization under the interpolation conditions yields the form of the TPS. The solution can be shown to be a polynomial of degree at most 1 plus a weighted sum of radial basis functions $\phi(r)=r^2\ln(r)$.

III. **Linear System**:

Substitute $f(x,y)$ into the interpolation conditions. This produces a system of $N+3$ linear equations (for $w\_i, \alpha\_0,\alpha\_1,\alpha\_2$):

$$$\begin{bmatrix}
0 & P^\top \\ P & K
\end{bmatrix}
\begin{bmatrix} \alpha \\ w \end{bmatrix}
=\begin{bmatrix} 0 \\ z \end{bmatrix}$$

where:

- $P$ is the $N \times 3$ matrix with rows $[1, x_i, y_i]$.
- $K$ is the $N \times N$ matrix with entries $K_{ij}=\phi(\|(x_i,y_i)-(x_j,y_j)\|)$.
- $z$ is the vector of observed $z_i$.
- $\alpha$ is $[ \alpha_0,\alpha_1,\alpha_2]^\top$ and $w=[w_1,\ldots,w_N]^\top.$

Solving this system yields the TPS coefficients.

### Algorithm (matrix form)

I. **Kernel matrix**

$$
K\in\mathbb{R}^{N\times N},
\qquad
K_{ij}=\phi\!\bigl(\lVert\mathbf{x}_i-\mathbf{x}_j\rVert_2\bigr).
$$

II. **Polynomial matrix**

$$
P=\begin{bmatrix}
1 & x_1 & y_1\\
\vdots & \vdots & \vdots\\
1 & x_N & y_N
\end{bmatrix}\in\mathbb{R}^{N\times 3}.
$$

III. **Augmented linear system**

$$
\underbrace{%
  \begin{bmatrix}
    K & P \\ 
    P^{\mathsf T} & 0_{3\times 3}
  \end{bmatrix}%
}_{A\in\mathbb{R}^{(N+3)\times(N+3)}}
\begin{bmatrix}
  \mathbf w \\ 
  \alpha
\end{bmatrix} =
\begin{bmatrix}
  \mathbf z \\ 
  \mathbf 0
\end{bmatrix},
\qquad
\mathbf z = (z_1, \dots, z_N)^{\mathsf T}
$$

* Unknowns: $ \mathbf w=(w_1,\dots ,w_N)^{\!\mathsf T}$ and $\alpha=(a_0,a_1,a_2)^{\!\mathsf T}$.
* $A$ is symmetric and (for distinct points) nonsingular.

IV. **Solve** the linear system once.  Complexity is $O(N^3)$ with dense $K$.

V. **Evaluate** at any $(x,y)$.  Cost per evaluation is $O(N)$.

> **Numerical stability tip**
> Because $\phi(r)\sim r^2\ln r$ is unbounded at infinity, centre and (optionally) scale the $\mathbf{x}_i$ to unit box if $N$ is large or the domain is wide.

### Fully-worked example (four points)

I. Data

$$
\bigl(0,0,0\bigr),
\bigl(1,0,1\bigr),
\bigl(0,1,1\bigr),
\bigl(1,1,2\bigr)
\qquad(N=4)
$$

II. Kernel matrix $K$

Distances $r_{ij}=\lVert\mathbf{x}_i-\mathbf{x}_j\rVert_2$

$$
\begin{array}{c|cccc}
 & 1 & 2 & 3 & 4\\\hline
1 & 0 & 1 & 1 & \sqrt2\\
2 & 1 & 0 & \sqrt2 & 1\\
3 & 1 & \sqrt2 & 0 & 1\\
4 & \sqrt2 & 1 & 1 & 0
\end{array}
$$

Compute $\phi(r)=r^2\ln r$:

* $\phi(0)=0$.
* $\phi(1)=1\cdot\ln 1=0$.
* $\phi(\sqrt2)=2\ln(\sqrt2)=2\cdot0.69314718=0.69314718$.

Thus

$$
K=\begin{bmatrix}
0 & 0 & 0 & 0.69314718\\
0 & 0 & 0.69314718 & 0\\
0 & 0.69314718 & 0 & 0\\
0.69314718 & 0 & 0 & 0
\end{bmatrix}
$$

III. Polynomial matrix $P$

$$
P=\begin{bmatrix}
1 & 0 & 0\\
1 & 1 & 0\\
1 & 0 & 1\\
1 & 1 & 1
\end{bmatrix}
$$

IV. Augmented system

$$
A=\begin{bmatrix}
K & P\\ P^{\!\mathsf T} & 0_{3\times3}
\end{bmatrix},
\qquad
\mathbf b = \begin{bmatrix}
0 \\ 
1 \\ 
1 \\ 
2 \\ 
0 \\ 
0 \\ 
0
\end{bmatrix}
$$

Explicitly,

$$
A = 
\begin{bmatrix}
  0        & 0        & 0        & 0.693147 & 1 & 0 & 0 \\ 
  0        & 0        & 0.693147 & 0        & 1 & 1 & 0 \\ 
  0        & 0.693147 & 0        & 0        & 1 & 0 & 1 \\ 
  0.693147 & 0        & 0        & 0        & 1 & 1 & 1 \\ 
  1 & 1 & 1 & 1 & 0 & 0 & 0 \\ 
  0 & 1 & 0 & 1 & 0 & 0 & 0 \\ 
  0 & 0 & 1 & 1 & 0 & 0 & 0 
\end{bmatrix}
$$

V. Solution

Solving 

$$A\begin{bmatrix}\mathbf w\\ \alpha\end{bmatrix}=\mathbf b$$

gives

$$
\mathbf{w} = \begin{bmatrix}
  0 \\ 
  0 \\ 
  0 \\ 
  0
\end{bmatrix}
$$

$$
\alpha =
\begin{bmatrix}
  a_0 \\ a_1 \\ a_2
\end{bmatrix} =
\begin{bmatrix}
  0 \\ 1 \\ 1
\end{bmatrix}
$$

Interpretation: the four data points lie exactly on the **plane**

$$
f(x,y)=x+y,
$$

so the bending-energy minimiser needs **no** non-linear kernel part ($\mathbf w=0$).

### Remarks and extensions

| Topic                     | Notes                                                                                                                                                               |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Singular cases**        | If the data are exactly coplanar *and* you add any numerical noise, $K$ may become rank-deficient.  Add a small diagonal regulariser $\lambda I$ in $K$ if needed.        |
| **Complexity**            | Solve once in $O(N^3)$; thereafter evaluations are $O(N)$.  For $N\gtrsim2000$ use fast methods (partition of unity, K-D trees, or the O(N) fast-TPS of Beatson & Light). |
| **Higher dimensions**     | In $d$-D the “thin-plate” energy changes and  $\phi(r)$ becomes $r^2\ln r$ only for $d=2$.  In $d=3$ one has $\phi(r)=r$.                                                 |
| **Derivative continuity** | The TPS interpolant is $C^1$ and its second derivatives are square-integrable; ideal for smoothly warping images or terrain surfaces.                                     |

### Advantages

- TPS yields an infinitely differentiable surface, minimizing bending energy, and producing visually pleasing, smooth **interpolants**.
- The method exactly passes through all given data **points**.
- TPS works with scattered data without needing a regular **grid**.
- It generalizes easily to higher dimensions by changing the form of $\phi(r)$, making it **extensible**.

### Limitations

- TPS requires solving a $(N+3) \times (N+3)$ linear system, which can be **expensive** for large $N$.
- The system matrix may become ill-conditioned with many close points, often necessitating regularization like TPS smoothing **splines**.
- Changing or adding one point affects the entire solution, as TPS is a **global** method, lacking local control like piecewise methods unless combined with domain decomposition techniques.
