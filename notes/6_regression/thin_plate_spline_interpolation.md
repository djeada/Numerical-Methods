## Thin Plate Spline Interpolation

Thin Plate Spline (TPS) Interpolation is a versatile method often utilized in image processing, computer graphics, and fields where data approximation and surface fitting are critical.

## Key Concepts

- A Thin Plate Spline denotes a smooth surface traversing through specified points in a 2D or 3D space.
- This method aims to minimize the second derivative of the function, yielding a surface characterized by minimal bending energy.
- TPS interpolation effectively handles both uniform and non-uniform data and can be seamlessly extended to multiple dimensions.

## Mathematical Formulation

A thin plate spline is mathematically formulated as:

$$
f(x, y) = a + bx + cy + \sum_{i=1}^{n} w_i \phi(\| (x, y) - (x_i, y_i) \|) 
$$

In this equation:
- $(x, y)$ denote the coordinates of the points being interpolated,
- $a, b, c$ are constants,
- $(x_i, y_i)$ are the coordinates of the control points,
- $w_i$ are weights associated with each control point,
- $\phi$ represents a radial basis function. 

Typically, for 2D interpolation, the radial basis function $\phi$ is chosen as $\phi(r) = r^2 \log(r^2)$, where $r$ is the Euclidean distance.

## Algorithm Steps

The thin plate spline interpolation algorithm can be broken down into three main steps:

1. **Establish Control Points Matrix**: Begin with a set of control points $(x_i, y_i)$. Compute the matrix of distances between each pair of control points. This distance matrix $R = [r_{ij}]$ is of size $n \times n$, where $n$ is the number of control points and $r_{ij}$ is the Euclidean distance between the $i$th and $j$th control points.

2. **Solve Linear System for Weights**: Solve a linear system to find the weights $w_i$ that minimize the bending energy of the surface. The bending energy of a thin plate spline is defined as the integral of the square of the second derivatives of the function $f$. The linear system that minimizes this energy is often represented as:

$$\begin{bmatrix}R & X \\
X^T & 0 \\
\end{bmatrix}
\begin{bmatrix}
w \\
v \\
\end{bmatrix} = \begin{bmatrix}
z \\
0 \\
\end{bmatrix}$$

Where $R$ is the matrix of radial basis function values between control points, $X$ is a matrix that contains the coordinates of the control points, $z$ are the function values at the control points, $w$ are the weights and $v$ contains the linear coefficients $a$, $b$, and $c$.

3. **Interpolate**: To interpolate a point $(x, y)$, compute the weighted sum of the radial basis functions centered at each control point, plus a linear term:

$$
f(x, y) = a + bx + cy + \sum_{i=1}^{n} w_i \phi(\| (x, y) - (x_i, y_i) \|) 
$$

## Example

Assume we are given a set of control points in 2D, which we denote as $P_1 = \{(x_1, y_1), (x_2, y_2), (x_3, y_3)\}$, specifically let's say $P_1 = \{(1,1), (2,3), (3,7)\}$ and their corresponding points in another set $P_2 = \{(1,1), (3,2), (2,6)\}$. We want to create a thin plate spline interpolant $f(x, y)$ that exactly interpolates these points. 

### Step 1: Compute pairwise distances

First, we need to compute the pairwise distances between the control points in $P_1$. The distance $r_{ij}$ between the points $(x_i, y_i)$ and $(x_j, y_j)$ is given by:

$$ r_{ij} = \sqrt{(x_i - x_j)^2 + (y_i - y_j)^2} $$

We need to create a distance matrix $R$ where each element $R_{ij}$ is the distance between point $i$ and point $j$:

$$ R = \left[ \begin{array}{ccc}
0 & r_{12} & r_{13} \\
r_{21} & 0 & r_{23} \\
r_{31} & r_{32} & 0 \\
\end{array} \right] $$

### Step 2: Construct the radial basis function (RBF) 

For a thin plate spline in 2D, we typically use the radial basis function $φ(r) = r^2 \log(r)$ if $r \neq 0$ and $0$ otherwise. So, we apply this function to every element in our distance matrix $R$:

$$ K = φ(R) = \left[ \begin{array}{ccc}
0 & r_{12}^2 \log(r_{12}) & r_{13}^2 \log(r_{13}) \\
r_{21}^2 \log(r_{21}) & 0 & r_{23}^2 \log(r_{23}) \\
r_{31}^2 \log(r_{31}) & r_{32}^2 \log(r_{32}) & 0 \\
\end{array} \right] $$

### Step 3: Solve for the weights

We need to solve the following system of linear equations for the weights $w = [w_1, w_2, w_3]^T$:

$$\begin{bmatrix}K & P \\
P^T & 0 \\
\end{bmatrix}
\begin{bmatrix}
w \\
a \\
\end{bmatrix} = \begin{bmatrix}
v \\
0 \\
\end{bmatrix}$$

where $K$ is the matrix we computed in Step 2, $P = [[1, x_1, y_1], [1, x_2, y_2], [1, x_3, y_3]]$ is a matrix containing the coordinates of the control points and the value 1, $a$ are the coefficients of the polynomial part of the thin plate spline (which we want to find), and $v = [v_1, v_2, v_3]^T$ are the $y$-coordinates from the $P_2$ control points.

### Step 4: Construct the interpolant function

The thin plate spline interpolant is then given by:

$$ f(x, y) = a_1 + a_2x + a_3y + \sum_{i=1}^{n} w_i φ(||(x, y) - (x_i, y_i)||) $$

Where $a = [a_1, a_2, a_3]^T$ are the coefficients we found in step 3, $(x_i, y_i)$ are the coordinates of the control points, $w_i$ are the weights we also found in step 3, and $φ$ is the radial basis function.

## Advantages

- TPS interpolation can effectively handle both uniform and non-uniform data and can be extended to any number of dimensions.
- It is particularly advantageous for tasks requiring the interpolated surface to pass exactly through the specified points.

## Limitations

- TPS interpolation can be computationally expensive for a large number of control points, as it involves solving an $n \times n$ linear system, where $n$ represents the number of control points.
- The selection of the radial basis function significantly impacts the interpolation result and must be made judiciously.
