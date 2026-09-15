## Thin Plate Spline Interpolation

A thin plate spline (TPS) fits a surface through scattered observations in two dimensions. Picture a thin sheet constrained to pass through specified heights: the TPS minimizes its mathematical bending energy while meeting those constraints.

The classical solution has an affine part plus radial kernels centered at the input locations. It is continuously differentiable, but its second derivatives can have logarithmic singularities at those locations. The precise energy formulation below uses square-integrable weak second derivatives, rather than requiring a twice continuously differentiable surface.

### Inputs and Goal

**Inputs:** $N\ge3$ finite triples $(x_i,y_i,z_i)$ and a query $(x_*,y_*)$. The coordinates $(x_i,y_i)$ must be distinct and must not all lie on one line. **Goal:** find the classical two-dimensional TPS interpolant and evaluate its height at the query.

Here $x$ and $y$ are spatial coordinates, while $z$ is the response. Non-collinearity concerns the input locations, not whether the triples lie on a plane. Planar response data are valid and should reproduce an affine function exactly.

### Mathematical Formulation

Given a set of $N$ data points $\{(x_i,y_i,z_i)\}_{i=1}^N$, where no two points coincide, we want to find a function:

$f(x,y) = \alpha_0 + \alpha_1 x + \alpha_2 y + \sum_{i=1}^N w_i \phi(\| (x,y)-(x_i,y_i) \|)$

that interpolates the given data. Here:

* The $\alpha_0, \alpha_1, \alpha_2$ terms represent a polynomial of degree 1 (a plane) that gives the global trend.
* The function $\phi(r)$ is a radial basis function chosen as:

$$
\phi(r)=\begin{cases}r^2\ln r,&r>0,\\0,&r=0.\end{cases}
$$

The value at zero is the limit $\lim_{r\to0^+}r^2\ln r=0$; do not evaluate $\ln0$ in code.

Up to a constant absorbed into the weights, this kernel is the fundamental solution of the two-dimensional biharmonic operator.

* The $w_i$ are the coefficients for the radial basis part. They describe the non-affine component.

This $f(x,y)$ must satisfy the interpolation conditions:

$f(x_i,y_i) = z_i, \quad i=1,\ldots,N.$

Additionally, to ensure a unique solution and remove degeneracies, $f(x,y)$ must satisfy:

$\sum_{i=1}^N w_i = \sum_{i=1}^N w_i x_i = \sum_{i=1}^N w_i y_i = 0$

This leads to a linear system for the unknown parameters $\alpha_0,\alpha_1,\alpha_2,w_1,\ldots,w_N$.

### Derivation

I. **Energy Minimization**:

Thin plate splines arise from minimizing a bending energy functional:

$$
J[f]=\int_{\mathbb R^2}\left[(f_{xx})^2+2(f_{xy})^2+(f_{yy})^2\right]\,dx\,dy.
$$

The minimization is subject to the interpolation constraints $f(x_i,y_i)=z_i$.

II. **Variational Problem**:

Solving the Euler-Lagrange equations associated with the energy minimization under the interpolation conditions yields the form of the TPS. The solution can be shown to be a polynomial of degree at most 1 plus a weighted sum of radial basis functions $\phi(r)=r^2\ln(r)$.

III. **Linear System**:

Substitute $f(x,y)$ into the interpolation conditions. This produces a system of $N+3$ linear equations (for $w_i, \alpha_0,\alpha_1,\alpha_2$):

$$
\begin{bmatrix}
K & P \\ P^\top & 0
\end{bmatrix}
\begin{bmatrix} w \\ \alpha \end{bmatrix}
=\begin{bmatrix} z \\ 0 \end{bmatrix}
$$

where:

- $P$ is the $N \times 3$ matrix with rows $[1, x_i, y_i]$.
- $K$ is the $N \times N$ matrix with entries $K_{ij}=\phi(\|(x_i,y_i)-(x_j,y_j)\|)$.
- $z$ is the vector of observed $z_i$.
- $\alpha$ is $[ \alpha_0,\alpha_1,\alpha_2]^\top$ and $w=[w_1,\ldots,w_N]^\top.$

Solving this system yields the TPS coefficients.

### Algorithm and Checks

1. Check finite data, matching lengths, distinct coordinates, and rank three of $P$.
2. Compute pairwise distances and build $K$, using $\phi(0)=0$ on its diagonal.
3. Build $P$ and solve the augmented system for $w$ and $\alpha$ without forming an inverse. The system is symmetric but indefinite; an ordinary positive-definite Cholesky solver is not appropriate.
4. Check both residuals: $Kw+P\alpha-z\approx0$ and $P^\top w\approx0$.
5. Evaluate the affine part and sum $w_i\phi(r_i)$ at the query.

For distinct, non-collinear locations this system is nonsingular. Dense construction and storage take $O(N^2)$, solving takes $O(N^3)$, and each query takes $O(N)$ once coefficients are available. Centering and using a common coordinate scale can help conditioning. Scaling axes differently changes the distance metric and generally changes the fitted surface.

### Fully-worked example (four points)

**Goal:** recover the surface and evaluate it at $(0.5,0.5)$.

I. Input data

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
* $\phi(\sqrt2)=2\ln(\sqrt2)=\ln 2\approx 0.6931$.

Thus

$$
K=\begin{bmatrix}
0 & 0 & 0 & \ln 2\\
0 & 0 & \ln 2 & 0\\
0 & \ln 2 & 0 & 0\\
\ln 2 & 0 & 0 & 0
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
A = \begin{bmatrix}
0        & 0        & 0        & \ln 2 & 1 & 0 & 0 \\ 
0        & 0        & \ln 2   & 0      & 1 & 1 & 0 \\ 
0        & \ln 2   & 0        & 0      & 1 & 0 & 1 \\ 
\ln 2   & 0        & 0        & 0      & 1 & 1 & 1 \\ 
1        & 1        & 1        & 1      & 0 & 0 & 0 \\ 
0        & 1        & 0        & 1      & 0 & 0 & 0 \\ 
0        & 0        & 1        & 1      & 0 & 0 & 0
\end{bmatrix}
$$

V. Solution

Solving 

$$
A\begin{bmatrix}\mathbf w\\ \alpha\end{bmatrix}=\mathbf b
$$

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

so the bending-energy minimizer needs no nonlinear kernel part ($\mathbf w=0$). Substitution gives $Kw+P\alpha=(0,1,1,2)^\top=z$ and $P^\top w=0$. The plane has zero bending energy and gives $f(0.5,0.5)=0.5+0.5=1$.

### Example 2: non-planar data

**Goal:** recover the surface and evaluate it at $(0.5,0.5)$.

I. Input data

$$
\bigl(0,0,1\bigr),
\bigl(1,0,0\bigr),
\bigl(0,1,0\bigr),
\bigl(1,1,1\bigr)
\qquad(N=4)
$$

These four points do **not** lie on a plane: the only candidate is $1 - x - y$, which gives $1-1-1=-1\neq1$ at $(1,1)$.

II. Reuse the Geometry

The locations are unchanged, so reuse the distance matrix, $K$, $P$, and augmented matrix $A$ from Example 1. Only the right-hand side changes to $(1,0,0,1,0,0,0)^\top$.

III. Solve the Constraints and Interpolation Equations

The orthogonality constraint $P^{\!\mathsf T}\mathbf w=\mathbf 0$ gives three equations:

$$
w_1+w_2+w_3+w_4=0,\quad w_2+w_4=0,\quad w_3+w_4=0.
$$

Setting $w_4=w$ we get $w_1=w,\;w_2=-w,\;w_3=-w$.

Write $L=\ln2$. The four interpolation equations become

$$
\begin{aligned}
Lw+\alpha_0&=1,\\
-Lw+\alpha_0+\alpha_1&=0,\\
-Lw+\alpha_0+\alpha_2&=0,\\
Lw+\alpha_0+\alpha_1+\alpha_2&=1.
\end{aligned}
$$

Subtracting the first from the fourth gives $\alpha_1+\alpha_2=0$. The middle equations give $\alpha_1=\alpha_2$, so both slopes vanish. Subtracting the second equation from the first then gives $2Lw=1$, and adding them gives $2\alpha_0=1$. Hence

$$
w=\frac{1}{2\ln 2}\approx0.7213,
\qquad
\alpha_0=\tfrac{1}{2},\;\alpha_1=0,\;\alpha_2=0.
$$

Therefore

$$
\mathbf w=\frac{1}{2\ln 2}
\begin{bmatrix}1\\-1\\-1\\1\end{bmatrix},
\qquad
\alpha=\begin{bmatrix}\tfrac12\\0\\0\end{bmatrix}.
$$

Interpretation: the polynomial part is the constant $\frac{1}{2}$, and the non-linear kernel is needed to pull the surface up at corners $(0,0)$ and $(1,1)$ and down at $(1,0)$ and $(0,1)$.

IV. Evaluation at $(0.5,\,0.5)$

All four distances are equal:

$$
r_k = \lVert(0.5,0.5)-\mathbf x_k\rVert = \tfrac{1}{\sqrt2},
\quad k=1,\dots,4.
$$

$$
\phi\!\left(\tfrac{1}{\sqrt2}\right) = \tfrac{1}{2}\ln\tfrac{1}{\sqrt2} = -\tfrac{\ln 2}{4}.
$$

Because $w_1+w_2+w_3+w_4=0$ and all $\phi$ values are identical, the kernel sum vanishes:

$$
\sum_{i=1}^{4}w_i\,\phi(r_i)=(w_1+w_2+w_3+w_4)\!\left(-\tfrac{\ln 2}{4}\right)=0.
$$

Therefore

$$
f(0.5,0.5)=\tfrac{1}{2}+0\cdot0.5+0\cdot0.5+0=\frac{1}{2}.
$$

By symmetry of the data the midpoint value is exactly $\frac{1}{2}$.

### Verification and Interpretation

For the non-planar example, the radial part at the four nodes is $(1/2,-1/2,-1/2,1/2)^\top$. Adding the constant $1/2$ reproduces $(1,0,0,1)^\top$, and the weights satisfy all three side constraints. The midpoint calculation above verifies a new query; an asymmetric query is useful for numerical checks because symmetry alone forces the midpoint value.

### Smoothing, Geometry, and Limitations

- **Smoothness:** TPS is generally $C^1$, with square-integrable weak second derivatives; it is smooth away from the centers, but not infinitely differentiable at them.
- **Singular geometry:** duplicate locations or collinear input coordinates can make the augmented interpolation problem singular. Coplanar response values do not: $K$ depends only on coordinates, not on $z$.
- **Smoothing:** replacing $K$ by $K+\lambda I$, $\lambda>0$, trades exact interpolation for a smoother fit to noisy responses. It does not repair rank deficiency of $P$; if $P\alpha=0$ for a nonzero $\alpha$, the augmented matrix still has a null vector $(0,\alpha)$.
- **Global influence:** changing one response generally affects the entire surface. Dense storage and solution cost limit problem size; local approximations can help but change the construction.
- **Shape:** minimum bending energy does not imply monotonicity, positivity, or reliable predictions outside the observed region.
- **Coordinates and dimensions:** rotations and translations preserve Euclidean distances. Higher-dimensional polyharmonic splines require dimension- and energy-dependent kernels; the classical two-dimensional bending-energy interpretation here should not be transferred unchanged.
- **Kernel convention:** using $r^2\ln(r^2)=2r^2\ln r$ halves the weights for exact interpolation while preserving the surface. With smoothing, the regularization parameter must also be scaled to preserve the same fit.

For an independent comparison, [SciPy's RBFInterpolator](https://docs.scipy.org/doc/scipy/reference/generated/scipy.interpolate.RBFInterpolator.html) supports this construction with `kernel="thin_plate_spline"`, `degree=1`, and `smoothing=0`. Supply an $N\times2$ coordinate array and an $N$-element response vector.
