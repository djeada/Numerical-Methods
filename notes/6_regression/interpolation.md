## Introduction

We have to arrays of numbers $X$ and $Y$. Array $X$ contains independent data points. Array $Y$ contains dependent data points $y_i,i=1,…,m$.

We want to find a function $\hat{y}(x)$, which gets the exact same value with given points.\\

## Linear Interpolation

Linear interpolation is achieved by connecting two data points with a straight line.

For $x_i < x < x_{i+1}$:

$$\hat{y}(x) = y_i + \frac{(y_{i+1} - y_{i})(x - x_{i})}{(x_{i+1} - x_{i})}.$$


### Derivation
 
![Screenshot from 2022-09-07 21-23-10](https://user-images.githubusercontent.com/37275728/188960726-ac99ac89-f1b8-4b82-9761-5093cb91d4db.png)


$$\alpha = \frac{y_2 - y_1}{x_2 - x_1}$$

$$h = \alpha \cdot (x - x_1)$$

$$y = y_1 + h$$

$$y = y_1 + (x - x_1) \cdot \frac{y_2 - y_1}{x_2 - x_1}$$

### Example

We are given two points A(-2, 0) and B (2, 2).


![Screenshot from 2022-09-07 21-23-32](https://user-images.githubusercontent.com/37275728/188960814-569c5a91-82b4-415c-9840-f5ebd4cc421d.png)

Let's try to evaluate the value of the function at $x=1$

$$\hat{y}(x) = y_i + \frac{(y_{i+1} - y_{i})(x - x_{i})}{(x_{i+1} - x_{i})} = 0 + \frac{(2 - 0)(1 - (-2))}{(2 - (-2))} = 1.5$$

## Cubic Spline

The interpolating function in cubic spline interpolation is a set of piecewise cubic functions.

For $x_i < x < x_{i+1}$:

We have two points $(x_i, y_i)$ and $(x_{i+1}, y_{i+1})$  joined with a cubic polynomial:

$$S_i(x) = a_i x^3 + b_i x^2 + c_i x + d_i$$

For $n$ points, there are $n-1$ cubic functions to find, and each cubic function requires four coefficients $(a_i, b_i, c_i, d_i)$.

There are $4(n-1)$ unknowns to find.

![Screenshot from 2022-09-07 21-24-04](https://user-images.githubusercontent.com/37275728/188960890-781f5947-1d8c-40bc-aba7-91728024eabe.png)

### Derivation

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

Boundry condition: The curve is a “straight line” at the end points:

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

### Lagrange Polynomial Interpolation

Lagrange polynomial interpolation gives us a single polynomial that connects all of the data points.

That polynomial is denoted as $L(x)$. It is true that $L(x_i) = y_i$ for all points $(x_i, y_i)$ .

$$L(x) = \sum_{i = 1}^n y_i P_i(x).$$

Each polynomial appearing in the sum is called a Lagrange basis polynomials, $P_i(x)$.

$$P_i(x) = \prod_{j = 1, j\ne i}^n\frac{x - x_j}{x_i - x_j},$$

### Example

We are given three points A(-1, 1), B(2, 3) and C(3,5).\\

$$P_1(x) = \frac{(x - x_2)(x - x_3)}{(x_1-x_2)(x_1-x_3)} = \frac{(x - 2)(x - 3)}{(-1-2)(-1-3)} = \frac{1}{12}(x^2 - 5x + 6)$$

$$P_2(x) = \frac{(x - x_1)(x - x_3)}{(x_2-x_1)(x_2-x_3)} = \frac{(x + 1)(x - 3)}{(2 + 1)(2-3)} = -\frac{1}{3}(x^2 - 2x - 3)$$

$$P_3(x) = \frac{(x - x_1)(x - x_2)}{(x_3-x_1)(x_3-x_2)} = \frac{(x + 1)(x - 2)}{(3 + 1)(3-2)} =\frac{1}{4}(x^2 -x - 2)$$

$$ L(x) = 1 \cdot P_1(x) + 3 \cdot P_2(x) + 5 \cdot P_3(x) $$

$$ L(x) = 1 \cdot P_1(x) + 3 \cdot P_2(x) + 5 \cdot P_3(x) $$

$$ L(x) = \frac{1}{3} x^2 + \frac{1}{3} x + 1 $$

![Screenshot from 2022-09-07 21-27-20](https://user-images.githubusercontent.com/37275728/188961030-379f428f-a0c4-403a-a6bd-e4a5393f38e0.png)
