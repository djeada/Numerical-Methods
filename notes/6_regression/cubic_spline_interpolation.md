## Cubic Spline

Cubic spline interpolation is a refined mathematical tool frequently used within numerical analysis. It's an approximation technique that employs piecewise cubic polynomials, collectively forming a cubic spline. These cubic polynomials are specifically engineered to pass through a defined set of data points, hence striking a balance between overly simple (like linear) and overly intricate (like high-degree polynomial) interpolations.

## Mathematical Formulation

![Screenshot from 2022-09-07 21-24-04](https://user-images.githubusercontent.com/37275728/188960890-781f5947-1d8c-40bc-aba7-91728024eabe.png)

A cubic spline function S(x) is applied in cubic spline interpolation across an interval $[x_i, x_{i+1}]$. The function is represented as:

$$
S_i(x) = a_i + b_i(x - x_i) + c_i(x - x_i)^2 + d_i(x - x_i)^3
$$

Here, the variables $a_i$, $b_i$, $c_i$, and $d_i$ are the coefficients that we need to determine, while $x_i$ and $x_{i+1}$ are the control points.

The goal of cubic spline interpolation is to find these coefficients that make the spline pass smoothly through each point and ensure that the first and second derivatives are continuous across the entire function.

### Conditions for Cubic Spline Interpolation

1. Each cubic polynomial $S_i(x)$ should pass through the data points in its interval. That is:

$$
S_i(x_i) = y_i \quad and \quad S_i(x_{i+1}) = y_{i+1}
$$

2. The spline function S(x) should be continuous. This means that the polynomials $S_i(x)$ and $S_{i+1}(x)$ should meet at $x_{i+1}$:

$$
S_i(x_{i+1}) = S_{i+1}(x_{i+1})
$$

3. The first and second derivatives of S(x) should be continuous. This leads to:

$$
S^{'}_i(x_{i+1}) = S^{'}_{i+1}(x_{i+1}) \quad and \quad S^{''}_i(x_{i+1}) = S^{''}_{i+1}(x_{i+1})
$$

4. At the ends, the second derivatives are usually set to zero (natural cubic spline):

$$
S^{''}_0(x_0) = S^{''}_{n-1}(x_n) = 0
$$

With these conditions, we can form a system of equations to find the constants $a_i$, $b_i$, $c_i$, and $d_i$. Solving this system gives us the coefficients of the cubic spline interpolating function.

## Derivation of Cubic Spline Interpolation

We are trying to find a function $S_i(x) = a_i x^3 + b_i x^2 + c_i x + d_i$ going trough both points: $(x_i, y_i)$ and $x_{i+1}, y_{i+1}$.

$$
S_i(x_i) = y_i,\quad i = 1,\ldots,n-1,
$$

$$
S_i(x_{i+1}) = y_{i+1},\quad i = 1,\ldots,n-1,
$$

Smoothness condition:

$$
S'_i(x_{i+1}) = S^{\prime}_{i+1}(x_{i+1}),\quad i = 1,\ldots,n-2,
$$

$$
S''_i(x_{i+1}) = S''_{i+1}(x_{i+1}),\quad i = 1,\ldots,n-2,
$$

Boundary condition: The curve is a “straight line” at the end points:

$$
S''_1(x_1) = 0
$$

$$
S''_{n-1}(x_n) = 0
$$

Let $h_{i}=x_{i}-x_{i-1}$

Let $S_i^{''}(x_i) = S_i^{''}(x_{i+1}) = M_i$

$S_1^{''}(x_1)= M_0 = 0$ and $S_n^{''}(x_n) = M_n = 0$

Other $M_i$ are unknown.

By Lagrange interpolation, we can interpolate each $S_{i}^{''}$ on  $[x_{i-1},x_{i}]$ :

$$S''_{i}(x)=M_{i-1}{\frac {x_{i}-x}{h_{i}}}+M_{i}{\frac {x-x_{i-1}}{h_{i}}} \quad for \quad x\in [x_{i-1},x_{i}]$$

Integrating the above equation twice and using the condition that $C_{i}(x_{i-1})=y_{i-1}$ and $ C_{i}(x_{i})=y_{i}$ to determine the constants of integration, we have.

$$ S_{i}(x)=M_{i-1}{\frac {(x_{i}-x)^{3}}{6h_{i}}}+M_{i}{\frac {(x-x_{i-1})^{3}}{6h_{i}}}+\left(y_{i-1}-{\frac {M_{i-1}h_{i}^{2}}{6}}\right){\frac {x_{i}-x}{h_{i}}}+\left(y_{i}-{\frac {M_{i}h_{i}^{2}}{6}}\right){\frac {x-x_{i-1}}{h_{i}}}$$

$${\text{for}}\quad x\in [x_{i-1},x_{i}] $$

This expression gives us the cubic spline $S(x)$ if $$ M_{i},i=0,1,\cdots ,n$$ can be determined.

$$S'_{i+1}(x)=-M_{i}{\frac {(x_{i+1}-x)^{2}}{2h_{i+1}}}+M_{i+1}{\frac {(x-x_{i})^{2}}{2h_{i+1}}}+{\frac {y_{i+1}-y_{i}}{h_{i+1}}}-{\frac {M_{i+1}-M_{i}}{6}}h_{i+1}$$

$$S'_{i+1}(x_{i})=-M_{i}{\frac {h_{i+1}}{2}}+{\frac {y_{i+1}-y_{i}}{h_{i+1}}}-{\frac {M_{i+1}-M_{i}}{6}}h_{i+1}$$

Similarly, when $x\in [x_{i-1},x_{i}]$, we can shift the index to obtain

$$
S'_{i}(x) =-M_{i-1}{\frac {(x_{i}-x)^{2}}{2h_{i}}}+M_{i}{\frac {(x-x_{i-1})^{2}}{2h_{i}}}+{\frac {y_{i}-y_{i-1}}{h_{i}}}-{\frac {M_{i}-M_{i-1}}{6}}h_{i}
$$

 
$$ S'_{i}(x_{i})=M_{i}{\frac {h_{i}}{2}}+{\frac {y_{i}-y_{i-1}}{h_{i}}}-{\frac {M_{i}-M_{i-1}}{6}}h_{i}$$

Since 

$$ S_{i+1}^{'}(x_{i}) = S_{i}^{'}(x_{i})$$ 

, we can derive:

$$\mu _{i}M_{i-1}+2M_{i}+\lambda _{i}M_{i+1}=d_{i}\quad {\text{for}}\quad i=1,2,\cdots ,n-1,$$
 
$$\mu _{i}={\frac {h_{i}}{h_{i}+h_{i+1}}},\quad \lambda _{i}=1-\mu _{i}={\frac {h_{i+1}}{h_{i}+h_{i+1}}},\quad {\text{and}}\quad d_{i}=6f[x_{i-1},x_{i},x_{i+1}]$$

and $f[x_{i-1},x_{i},x_{i+1}]$ is a divided difference.

According to different boundary conditions, we can solve the system of equations above to obtain the values of $M_{i}$'s.

$$S_{1}^{'}(x_{0})=f_{0}^{'}$$ 

and 

$$S_{n}^{'}(x_{n})=f_{n}^{'}$$

According to equation (7), we can obtain:

$$S'_{1}(x_{0})=-M_{0}{\frac {(x_{1}-x_{0})^{2}}{2h_{1}}}+M_{1}{\frac {(x_{0}-x_{0})^{2}}{2h_{1}}}+{\frac {y_{1}-y_{0}}{h_{1}}}-{\frac {M_{1}-M_{0}}{6}}h_{1}$$

$$\Rightarrow f'_{0}=-M_{0}{\frac {h_{1}}{2}}+f[x_{0},x_{1}]-{\frac {M_{1}-M_{0}}{6}}h_{1}$$

$$\Rightarrow 2M_{0}+M_{1}={\frac {6}{h_{1}}}(f[x_{0},x_{1}]-f'_{0})=6f[x_{0},x_{0},x_{1}]$$

Analogously:

$$ S'_{n}(x_{n})=-M_{n-1}{\frac {(x_{n}-x_{n})^{2}}{2h_{n}}}+M_{n}{\frac {(x_{n}-x_{n-1})^{2}}{2h_{n}}}+{\frac {y_{n}-y_{n-1}}{h_{n}}}-{\frac {M_{n}-M_{n-1}}{6}}h_{n}$$

$$M_{n-1}+2M_{n}={\frac {6}{h_{n}}}(f'_{n}-f[x_{n-1},x_{n}])=6f[x_{n-1},x_{n},x_{n+1}]$$

Let:

$$\lambda _{0}=\mu _{n}=1,$$

$$d_{0}=6f[x_{0},x_{0},x_{1}]$$

$$d_{n}=6f[x_{n-1},x_{n},x_{n}]$$

 
$$
  \begin{bmatrix}
    2 & \lambda_0 \\ 
    \mu_1 & 2 & \lambda_1 \\ 
    & \ddots & \ddots & \ddots \\
    && \ddots & \ddots & \ddots \\
	&&& \ddots & \ddots & \ddots \\
	&&&& \mu_{n-1} & 2 & \lambda_{n-1} \\ 
	&&&&& \mu_{n} & 2 \\ 
  \end{bmatrix}
  \begin{bmatrix}
    M_0 \\
    M_1 \\
    \vdots \\
    \vdots \\
    \vdots \\
    M_{n-1} \\
    M_n \\
  \end{bmatrix}
  	=
  \begin{bmatrix}
    d_0 \\
    d_1 \\
    \vdots \\
    \vdots \\
    \vdots \\
    d_{n-1} \\
    d_n \\
  \end{bmatrix}
$$


## Algorithm Steps

In general, the steps for implementing a cubic spline interpolation algorithm are as follows:

1. **Data Preparation**: 
   - Sort the given set of control points `(x_i, y_i)` in ascending order of `x_i`.
   - Calculate the difference between successive `x_i` values, denoted as `h_i = x_{i+1} - x_i` for `i = 0, ..., n-1`.

2. **Solving for the Second Derivatives**: 
   - Initialize a system of linear equations based on the following formula derived from the conditions of the cubic spline:

     $$h_{i-1}*c_{i-1} + 2*(h_{i-1}+h_i)*c_i + h_i*c_{i+1} = 3*( (y_{i+1}-y_i)/h_i - (y_i-y_{i-1})/h_{i-1} )$$

     This applies for `i = 1, ..., n-1`. Also, initialize the boundary conditions as `c_0 = c_n = 0`.

   - Solve this tridiagonal system of equations (often using techniques like Gaussian elimination or Thomas algorithm) to get the second derivatives `c_i` at each control point `x_i`.

3. **Calculating the Remaining Coefficients**:
   - For each interval `[x_i, x_{i+1}]`, calculate the other coefficients `a_i`, `b_i`, and `d_i` using the formulas:

     
     $$a_i = y_i$$
     
     $$b_i = (y_{i+1} - y_i)/h_i - h_i*(c_{i+1} + 2*c_i)/3$$
     
     $$d_i = (c_{i+1} - c_i)/(3*h_i)$$
     

     These formulas apply for `i = 0, ..., n-1`.

4. **Interpolation**:
   - For a given input `x`, find the interval `[x_i, x_{i+1}]` where it lies.
   - Calculate the cubic polynomial `S_i(x)` using the equation:

     $$S_i(x) = a_i + b_i*(x - x_i) + c_i*(x - x_i)^2 + d_i*(x - x_i)^3$$

This cubic spline interpolation algorithm provides the function `S(x)` that smoothly fits the given control points.

## Example

Given points `(0,0)`, `(1,0.5)`, and `(2,0)`, we aim to calculate the cubic spline that interpolates these points. Following the steps outlined in the algorithm:

1. **Data Preparation**:
   The points are already sorted in ascending order of `x`, and we calculate `h_i`:

$$h_0 = x_1 - x_0 = 1 - 0 = 1$$

$$h_1 = x_2 - x_1 = 2 - 1 = 1$$

2. **Solving for the Second Derivatives**:
   Set up the system of equations. For `i=1`, we have:

$$h_0c_0 + 2(h_0+h_1)*c_1 + h_1c_2 = 3( (y_2-y_1)/h_1 - (y_1-y_0)/h_0 )$$

Substituting the known values:

$$1c_0 + 2(1+1)c_1 + 1c_2 = 3*( (0-0.5)/1 - (0.5-0)/1 )$$

And knowing that `c_0 = c_2 = 0` (boundary conditions), the equation simplifies to:

$$4c_1 = 3(-0.5 - 0.5)$$

Solving for `c_1`, we get `c_1 = -0.75`.

3. **Calculating the Remaining Coefficients**:
We calculate `a_i`, `b_i`, and `d_i`:

For `i=0`:

$$a_0 = y_0 = 0$$

$$b_0 = (y_1 - y_0)/h_0 - h_0*(c_1 + 2*c_0)/3 = (0.5 - 0)/1 - 1*( -0.75 + 2*0 )/3 = 0.5 - (-0.25) = 0.75$$

$$d_0 = (c_1 - c_0)/(3*h_0) = (-0.75 - 0)/(3*1) = -0.25$$

For `i=1`:

$$a_1 = y_1 = 0.5$$

$$b_1 = (y_2 - y_1)/h_1 - h_1*(c_2 + 2*c_1)/3 = (0 - 0.5)/1 - 1*( 0 + 2*(-0.75) )/3 = -0.5 - (-0.5) = 0$$

$$d_1 = (c_2 - c_1)/(3*h_1) = (0 - (-0.75))/(3*1) = 0.25$$

4. **Interpolation**:
The cubic polynomials `S_i(x)` for the intervals are:

For `i=0` (interval `[0, 1]`):

$$S0 = a_0 + b_0(x - x_0) + c_1(x - x_0)^2 + d_0(x - x_0)^3$$

$$= 0 + 0.75(x - 0) - 0.75*(x - 0)^2 - 0.25*(x - 0)^3$$

$$= 0.75x - 0.75x^2 - 0.25*x^3$$

For `i=1` (interval `[1, 2]`):

$$S1 = a_1 + b_1(x - x_1) + c_1(x - x_1)^2 + d_1(x - x_1)^3$$

$$= 0.5 + 0(x - 1) - 0.75*(x - 1)^2 + 0.25*(x - 1)^3$$

$$= 0.5 - 0.75*(x - 1)^2 + 0.25*(x - 1)^3$$

## Advantages 

- Cubic spline interpolation produces smoother and more flexible curves than most other methods.
- It's immune to oscillatory artifacts that high-degree polynomial interpolation may suffer from.

## Limitations

- It can be computationally intense compared to more straightforward methods.
- It requires the resolution of a system of equations, which can become complex with a large number of control points.
