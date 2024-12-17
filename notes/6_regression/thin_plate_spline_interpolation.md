## Introduction

**Thin Plate Spline (TPS) Interpolation** is a non-parametric, spline-based method for interpolating scattered data in two or more dimensions. Originally arising in the context of fitting a smooth surface through a set of points in $\mathbb{R}^2$, thin plate splines can be generalized to higher dimensions. The name "thin plate" comes from the physical analogy of bending a thin sheet of metal so that it passes through given points with minimal bending energy.

While polynomial methods or radial basis functions can also perform interpolation, TPS stands out by providing a minimal "bending energy" solution, leading to a surface that is not only guaranteed to pass through the given points but is also as flat (smooth) as possible away from these points. This makes thin plate splines particularly favored in fields like image warping, geometric modeling, and shape deformation.

## Conceptual Illustration (Not Removing the Plot)

Imagine you have a set of control points $(x_i,y_i,z_i)$ in 3D space, where $(x_i,y_i)$ represent spatial coordinates and $z_i$ is the function value at that location. Thin plate spline interpolation finds a surface $z=f(x,y)$ that exactly passes through all these points. If you imagine the surface as a thin metal sheet pinned at these points, the TPS solution is the shape the sheet would naturally take if it were free to bend but not stretch, minimizing the total bending energy:

```
z 
|          *
|      *       *  known data points
|    *    ~~~~~~~~~~~~~   <-- smooth surface
|  *   
+---------------------------------> x,y
```

The resulting surface is smooth, continuous in its derivatives, and tends to flatten out smoothly between data points.

## Mathematical Formulation

Given a set of $N$ data points $\{(x_i,y_i,z_i)\}_{i=1}^N$, where no two points coincide, we want to find a function:

$$f(x,y) = \alpha_0 + \alpha_1 x + \alpha_2 y + \sum_{i=1}^N w_i \phi(\| (x,y)-(x_i,y_i) \|)$$
that interpolates the given data. Here:

- The $\alpha_0, \alpha_1, \alpha_2$ terms represent a polynomial of degree 1 (a plane) that gives the global trend.
- The function $\phi(r)$ is a radial basis function chosen as:

$$\phi(r) = r^2 \ln(r),$$
which is the fundamental solution associated with the thin plate spline bending energy in 2D.
- The $w_i$ are the coefficients for the radial basis part.

This $f(x,y)$ must satisfy the interpolation conditions:

$$f(x_i,y_i) = z_i, \quad i=1,\ldots,N.$$

Additionally, to ensure a unique solution and remove degeneracies, $f(x,y)$ must satisfy:

$$\sum_{i=1}^N w_i = \sum_{i=1}^N w_i x_i = \sum_{i=1}^N w_i y_i = 0.$$

This leads to a linear system for the unknown parameters $\alpha_0,\alpha_1,\alpha_2,w_1,\ldots,w_N.$

## Derivation

I. **Energy Minimization**:  

Thin plate splines arise from minimizing a bending energy functional:

$$J[f] = \int\int \left(\frac{\partial^2 f}{\partial x^2}\right)^2 + 2\left(\frac{\partial^2 f}{\partial x \partial y}\right)^2 + \left(\frac{\partial^2 f}{\partial y^2}\right)^2 \, dx dy,$$
subject to the interpolation constraints $f(x_i,y_i)=z_i$.

II. **Variational Problem**:  

Solving the Euler-Lagrange equations associated with the energy minimization under the interpolation conditions yields the form of the TPS. The solution can be shown to be a polynomial of degree at most 1 plus a weighted sum of radial basis functions $\phi(r)=r^2\ln(r)$.

III. **Linear System**:

Substitute $f(x,y)$ into the interpolation conditions. This produces a system of $N+3$ linear equations (for $w_i, \alpha_0,\alpha_1,\alpha_2$):

$$\begin{bmatrix}

0 & P^\top \\ P & K

\end{bmatrix}

\begin{bmatrix} \alpha \\ w \end{bmatrix} 

=

\begin{bmatrix} 0 \\ z \end{bmatrix},$$
where:
- $P$ is the $N \times 3$ matrix with rows $[1, x_i, y_i]$.
- $K$ is the $N \times N$ matrix with entries $K_{ij}=\phi(\|(x_i,y_i)-(x_j,y_j)\|)$.
- $z$ is the vector of observed $z_i$.
- $\alpha$ is $[ \alpha_0,\alpha_1,\alpha_2]^\top$ and $w=[w_1,\ldots,w_N]^\top.$

Solving this system yields the TPS coefficients.

## Algorithm Steps

I. **Input**:
- A set of points $(x_i,y_i,z_i)$, $i=1,\ldots,N.$
II. **Form the Matrices**:
- Compute the $N \times N$ kernel matrix $K$ with $K_{ij}= \phi(\sqrt{(x_i - x_j)^2+(y_i-y_j)^2})$ and $\phi(r)=r^2 \ln(r)$.
- Form the $N \times 3$ matrix $P$ with rows $[1, x_i, y_i]$.
- Construct the augmented block matrix and vector as described above.
III. **Solve the Linear System**:
- Solve the linear system for $\alpha$ and $w$.
- This gives all parameters needed for the TPS surface.
IV. **Interpolation**:
- To find $f(x,y)$ at a new point $(x,y)$:

 $$f(x,y) = \alpha_0 + \alpha_1 x + \alpha_2 y + \sum_{i=1}^N w_i \phi(\sqrt{(x - x_i)^2+(y - y_i)^2}).$$

## Example

**Given Data**: Suppose we have 4 points:

$$(0,0,0), (1,0,1), (0,1,1), (1,1,2).$$

I. Compute $K$:

For each pair of points, calculate distance $r$ and then $\phi(r)=r^2\ln(r)$. Handle $r=0$ carefully ($\phi(0)=0$ by definition).

II. Compute $P$:

$$P = \begin{bmatrix}
1 & 0 & 0 \\
1 & 1 & 0 \\
1 & 0 & 1 \\
1 & 1 & 1
\end{bmatrix}$$

III. Form the linear system and solve for $\alpha_0,\alpha_1,\alpha_2,w_i$.

IV. Once solved, you have a TPS surface that passes exactly through these four points. For any $(x,y)$, use the formula to predict $f(x,y)$.

(This is a simplified conceptual example; actual numbers require careful computation.)

## Advantages

- **Smooth and Natural Surfaces**:

TPS yields an infinitely differentiable surface minimizing bending energy, often producing visually pleasing, smooth interpolants.

- **Exact Interpolation**:

The method exactly passes through all given data points.

- **No Grid Required**:

Works with scattered data without needing a regular grid.

- **Extensible**:

Generalizes easily to higher dimensions by changing the form of $\phi(r)$.

## Limitations

- **Computational Cost**:

Requires solving a $(N+3) \times (N+3)$ linear system. For large $N$, this can be expensive.

- **Conditioning Issues**:

The system matrix may become ill-conditioned with many close points. Regularization (TPS smoothing splines) is often needed in practice.

- **Global Method**:

Changing or adding one point affects the entire solution. There is no local control like piecewise methods (unless carefully combined with domain decomposition techniques).
