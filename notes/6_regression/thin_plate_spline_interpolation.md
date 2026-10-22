# Thin-Plate Spline Interpolation

Thin-plate spline (TPS) interpolation fits a surface through scattered data while controlling bending. This note develops the classical two-dimensional formulation; higher-dimensional polyharmonic spline constructions depend on the dimension and derivative order, so their kernel is not always the same $r^2\log r$.

In two dimensions, suppose we know values

$$
z_i
$$

at locations

$$
\mathbf x_i = (x_i,y_i),
\qquad i = 1,\ldots,N.
$$

A thin-plate spline constructs a surface

$$
s(x,y)
$$

that passes through every data value while minimizing a measure of bending.

The name comes from the physical analogy of a thin elastic plate that is forced through fixed points and settles into the least-bending shape compatible with those constraints.

![Thin-plate spline surface through scattered data](https://github.com/djeada/Numerical-Methods/raw/refs/heads/master/notes/6_regression/resources/plots/thin_plate_spline_surface.svg)

## Radial basis form

In two dimensions, the classical thin-plate spline kernel is

$$
\phi(r) = r^2\log r.
$$

At

$$
r = 0,
$$

the limiting value is defined as

$$
\phi(0) = 0.
$$

The interpolant is

$$
s(\mathbf x) = a_0 + a_1x + a_2y + \sum_{j=1}^{N} w_j
\phi(\|\mathbf x - \mathbf x_j\|_2).
$$

There are two parts:

I. an affine polynomial

$$
a_0 + a_1x + a_2y;
$$

II. a weighted sum of radial basis functions centered at the data sites.

The radial component supplies flexible curvature, while the affine component is required by the mathematical structure of the TPS kernel.

## Interpolation conditions

At every data site,

$$
s(\mathbf x_i) = z_i.
$$

Define

$$
K_{ij} = \phi(\|\mathbf x_i - \mathbf x_j\|_2).
$$

Also define

$$
P =
\begin{bmatrix}
1 & x_1 & y_1\\
1 & x_2 & y_2\\
\vdots & \vdots & \vdots\\
1 & x_N & y_N
\end{bmatrix}.
$$

The TPS coefficients satisfy the block system

$$
\begin{bmatrix}
K & P\\
P^\top & 0
\end{bmatrix}
\begin{bmatrix}
\mathbf w\\
\mathbf a
\end{bmatrix} =
\begin{bmatrix}
\mathbf z\\
0
\end{bmatrix},
$$

where

$$
\mathbf a=
\begin{bmatrix}
a_0\\a_1\\a_2
\end{bmatrix}.
$$

The lower block gives the side constraints

$$
P^\top\mathbf w = 0.
$$

Written componentwise,

$$
\sum_{j=1}^{N}w_j = 0,
$$

$$
\sum_{j=1}^{N}w_jx_j = 0,
$$

and

$$
\sum_{j=1}^{N}w_jy_j = 0.
$$

These constraints make the decomposition between the radial and affine parts unique under the usual geometric conditions.

## Geometric requirements

In two dimensions, the sites must contain enough geometric information for the affine part to be determined. In particular, the points should not all lie on one straight line.

Duplicate data locations are also problematic for exact interpolation unless their values are perfectly consistent and the formulation is modified appropriately.

## Why the surface is global

Every kernel term

$$
\phi(\|\mathbf x - \mathbf x_j\|_2)
$$

depends on the distance from the query to one data site, but the coefficient vector is obtained from one global linear system.

Changing one observed value can therefore alter many or all coefficients and change the surface throughout the domain.

The contour plot makes this global coupling easy to see.

![Contours of a thin-plate spline interpolant](https://github.com/djeada/Numerical-Methods/raw/refs/heads/master/notes/6_regression/resources/plots/thin_plate_spline_contours.svg)

## Bending-energy interpretation

The classical two-dimensional TPS minimizes a bending-energy functional of the form

$$
J[s] = \iint \left[s_{xx}^2 + 2s_{xy}^2 + s_{yy}^2 \right] \, dx\, dy
$$

subject to the interpolation constraints

$$
s(x_i,y_i) = z_i.
$$

The second derivatives measure curvature. Minimizing their squared magnitude favors a surface that bends as little as possible while still passing through the required points.

This variational interpretation explains why thin-plate splines tend to look smooth without specifying a rectangular grid.

### Why the affine part and side constraints are needed

In the classical whole-plane formulation, the bending energy is integrated over $\mathbb R^2$. Every affine function $a_0+a_1x+a_2y$ has zero second derivatives and hence zero bending energy. The energy therefore cannot distinguish an affine addition; this three-dimensional null space is why the representation includes $P\mathbf a$.

The upper block equation is simply $K\mathbf w+P\mathbf a=\mathbf z$, obtained by evaluating the interpolant at all sites. The lower block $P^\top\mathbf w=0$ separates the radial weights from the affine null space. For distinct sites, the TPS kernel is strictly positive on nonzero weight vectors satisfying these side constraints. If a homogeneous block-system solution existed, multiplying its upper equation by $\mathbf w^\top$ would give $\mathbf w^\top K\mathbf w=0$, forcing $\mathbf w=0$. Full column rank of $P$ would then force $\mathbf a=0$. This proves uniqueness under the stated geometry.

The entire block matrix is symmetric **indefinite**, even though the constrained kernel has the positivity property just used. Use a solver that supports this structure or a general pivoted solver; ordinary Cholesky on the full block matrix is inappropriate. The [SciPy RBF reference](https://docs.scipy.org/doc/scipy/reference/generated/scipy.interpolate.RBFInterpolator.html) describes the polynomial rank and distinct-site conditions for these systems.

## Worked example: reproducing a plane

Use the three noncollinear sites $(0,0),(1,0),(0,1)$ with values $1,3,4$. The affine matrix is

$$
P=\begin{bmatrix}1&0&0\\1&1&0\\1&0&1\end{bmatrix}.
$$

It is invertible, so $P^\top\mathbf w=0$ forces $\mathbf w=0$. Solving $P\mathbf a=\mathbf z$ gives $\mathbf a=(1,2,3)^\top$ and $s(x,y)=1+2x+3y$. At $(1/2,1/2)$ the value is $3.5$. The plane matches every data value and has zero bending energy, so no radial curvature is needed. More sites with nonaffine values produce nonzero radial weights.

## Evaluating the interpolant

After solving for $\mathbf w$ and $\mathbf a$, evaluate a new point

$$
\mathbf x = (x,y)
$$

by computing all distances

$$
r_j = \|\mathbf x - \mathbf x_j\|_2
$$

and then

$$
s(\mathbf x) = a_0 + a_1x + a_2y + \sum_{j=1}^{N}w_jr_j^2\log r_j.
$$

For a query that exactly coincides with a data site, use

$$
r^2\log r = 0
$$

at $r=0$ by the limiting definition.

## Algorithm

**Step 1.** Collect distinct scattered data sites $(x_i,y_i,z_i)$;

**Step 2.** Compute every pairwise distance

$$
r_{ij} = \|\mathbf x_i - \mathbf x_j\|_2;
$$

**Step 3.** Build

$$
K_{ij} = \phi(r_{ij});
$$

**Step 4.** Build the affine matrix $P$;

**Step 5.** Assemble the block system;

**Step 6.** Solve for $\mathbf w$ and $\mathbf a$;

**Step 7.** Evaluate queries with the radial sum plus affine term.

## Computational cost

The matrix $K$ is dense.

For $N$ data sites, a straightforward direct implementation uses approximately:

- $O(N^2)$ memory;
- $O(N^3)$ factorization work;
- $O(N)$ work for one new query.

Large datasets may require local approximations, sparse alternatives, iterative methods, or other kernel acceleration techniques.

## Exact interpolation versus smoothing

Exact TPS interpolation treats every observed value as a hard constraint. That can be undesirable for noisy data.

A smoothing thin-plate spline introduces a tradeoff between data fit and bending energy. Conceptually, it solves a problem like

$$
\underset{s}{\mathrm{minimize}} \quad \sum_{i=1}^{N} [z_i - s(x_i,y_i)]^2 + \lambda
J[s],
$$

where

$$
\lambda\ge0
$$

controls smoothness.

For $\lambda>0$, the energy selects a smooth fit while allowing data mismatch. The limit $\lambda\to0^+$ selects the minimum-bending exact interpolant under the geometric assumptions above. Setting $\lambda=0$ in the unrestricted function-space objective removes the bending penalty entirely, so exact fits need not be unique unless a minimum-energy selection is also imposed. Larger $\lambda$ increasingly favors low bending energy, tending toward an affine fit rather than necessarily a constant surface.

## Scaling matters

Distance-based kernels are sensitive to coordinate units.

If one coordinate is measured on a scale of thousands and another on a scale of fractions, Euclidean distance may be dominated by the first coordinate.

Possible remedies include:

- converting variables to comparable physical units;
- nondimensionalizing coordinates;
- standardizing coordinates when scientifically appropriate.

The scaling should reflect the geometry of the actual problem, not just convenience.

## Extrapolation outside the data cloud

TPS interpolation is strongest inside regions supported by nearby data sites.

Outside the convex hull of the observations, the affine term and global radial terms determine the shape with much weaker local constraint. Extrapolated surfaces can therefore be misleading even when the interpolation inside the data cloud looks excellent.

## Relationship to Gaussian RBF interpolation

Both methods use distance-based basis functions, but they differ in important ways.

Gaussian RBF interpolation uses

$$
e^{-(\varepsilon r)^2}
$$

and requires a shape parameter $\varepsilon$.

The classical two-dimensional TPS uses

$$
r^2\log r
$$

plus an affine polynomial and side constraints.

TPS interpolation is especially associated with smooth surface deformation and scattered spatial interpolation.

## Code in this repository

`src/6_regression/thin_plate_spline_interpolation` takes one coordinate pair and one value per data point. It raises `ValueError` for fewer than three points, duplicate sites, or collinear sites (the affine part is then not determined and the block system is singular).
