## Cubic Spline

Cubic spline interpolation is a refined mathematical tool frequently used within numerical analysis. It's an approximation technique that employs piecewise cubic polynomials, collectively forming a cubic spline. These cubic polynomials are specifically engineered to pass through a defined set of data points, hence striking a balance between overly simple (like linear) and overly intricate (like high-degree polynomial) interpolations.

## Key Elements of Cubic Spline Interpolation

![Screenshot from 2022-09-07 21-24-04](https://user-images.githubusercontent.com/37275728/188960890-781f5947-1d8c-40bc-aba7-91728024eabe.png)

A cubic spline function S(x) is applied in cubic spline interpolation across an interval $[x_i, x_{i+1}]$. The function is represented as:

$$
S_i(x) = a_i + b_i(x - x_i) + c_i(x - x_i)^2 + d_i(x - x_i)^3
$$

Here, the variables $a_i$, $b_i$, $c_i$, and $d_i$ are the coefficients that we need to determine, while $x_i$ and $x_{i+1}$ are the control points.

The goal of cubic spline interpolation is to find these coefficients that make the spline pass smoothly through each point and ensure that the first and second derivatives are continuous across the entire function.

## Derivation of Cubic Spline Interpolation

Cubic spline interpolation involves n+1 data points, denoted as $(x_0, y_0), (x_1, y_1), ..., (x_n, y_n)$, arranged in ascending order of x values.

### Form of the Cubic Spline

The cubic spline S(x) is a piecewise function comprised of n segments, each represented by a cubic polynomial. For the ith interval $[x_i, x_{i+1}]$, the cubic polynomial takes the form:

$$
S_i(x) = a_i + b_i(x - x_i) + c_i(x - x_i)^2 + d_i(x - x_i)^3
$$

Where $a_i$, $b_i$, $c_i$, and $d_i$ are constants to be determined.

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

### Calculating the Coefficients

Given the aforementioned conditions, we can express the coefficients as follows:

1. **The coefficient $a_i$**: From the condition that the polynomial should pass through the data points, we get that $a_i = y_i$.

2. **The coefficient $b_i$**: From the definition of the derivative, we get that $b_i = S^{'}_i(x_i)$.

3. **The coefficient $c_i$**: From the definition of the second derivative, we get that $c_i = S^{''}_i(x_i)/2$.

4. **The coefficient $d_i$**: From the definition of the third derivative, we get that $d_i = S^{'''}_i(x_i)/6$.

With these coefficients, the cubic polynomial becomes:

$$
S_i(x) = y_i + S^{'}_i(x_i)(x - x_i) + S^{''}_i(x_i)/2 (x - x_i)^2 + S^{'''}_i(x_i)/6 (x - x_i)^3
$$

Substituting $x_{i+1}$ into this equation and taking into account that $S_i(x_{i+1}) = y_{i+1}$, we get:

$$
y_{i+1} = y_i + S^{'}_i(x_i)h_i + S^{''}_i(x_i)/2 h_i^2 + S^{'''}_i(x_i)/6 h_i^3
$$

Where $h_i = x_{i+1} - x_i$.

This gives us an expression that links the coefficients of the polynomials on consecutive intervals. To calculate these coefficients, we use the conditions of continuity of the first and second derivatives at the points $x_i$:

$$
S^{'}_{i-1}(x_i) = S^{'}_i(x_i) \quad and \quad S^{''}_{i-1}(x_i) = S^{''}_i(x_i)
$$

These conditions can be transformed into a system of linear equations, which can be solved to find the values of $S^{'}_i(x_i)$ and $S^{''}_i(x_i)$.

Finally, using the boundary conditions for the second derivative, we get:

$$
S^{''}_0(x_0) = S^{''}_{n-1}(x_n) = 0
$$

Which completes the system of equations.

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
