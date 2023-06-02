## LU Decomposition

LU Decomposition, also known as LU factorization, refers to the factorization of a square matrix into two matrices – a lower triangular matrix (L) and an upper triangular matrix (U). 

## Key Concepts

- The main idea of LU decomposition is to represent a matrix as the product of a lower triangular matrix and an upper triangular matrix.
- In the decomposition, `A = LU`, where A is the square matrix to be factorized, L is the lower triangular matrix, and U is the upper triangular matrix.

## Mathematical Formulation

The goal is to *decompose* a matrix so that it is computationally cheaper to calculate the solution of the following equation:

$$A\boldsymbol{x}^{n+1} = \boldsymbol{b}(\boldsymbol{x}^n, \ldots)$$

The matrix $A$ get's decomposed into to other matrices $L$ and $U$:

$$ A = LU $$

$L$ is a lower-triangular matrix and $U$ is an upper-triangular matrix. 
These matrices conatin all the infomration needed for the Gaussian elimination.

$$ A\boldsymbol{x} = \boldsymbol{b} \iff (LU)\boldsymbol{x} = \boldsymbol{b} \iff  L(U\boldsymbol{x}) = \boldsymbol{b} $$

We introduce a new notation for the $U$ and $x$ product:

$$\boldsymbol{c}=U\boldsymbol{x}$$

We can then rewrite the previous equation in the following way:

$$ L\boldsymbol{c} = \boldsymbol{b} $$

Since $L$ is in lower-triangular form we can quickly solve the above eqaution.

The last step is this equation:

$$ U\boldsymbol{x} = \boldsymbol{c} $$
## LU Decomposition Algorithm Steps

LU Decomposition is a method that decomposes a square matrix `A` into the product of a lower triangular matrix `L` and an upper triangular matrix `U`. This can be especially useful for solving linear equations, calculating determinants, and facilitating Gaussian elimination. Here are the detailed steps:

1. Start with a given square matrix $A$. The objective is to find matrices $L$ and $U$ such that $A = LU$.

2. Initialize $L$ as an identity matrix of the same size as $A$ and $U$ as a matrix of the same dimensions as $A$ filled with zeros.

3. For each row `i` in $A$, calculate each $u_{ij}$ for all $j \geq i$ and each $l_{ij}$ for all $j < i$.

4. Use the following formulas to compute the elements of $L$ and $U$:
- For $u_{ij}$ use: 

$$u_{ij} = a_{ij} - \sum_{k=1}^{i-1} l_{ik}u_{kj}$$
    
- For $l_{ij}$ use: 
    
$$l_{ij} = \frac{1}{u_{jj}}(a_{ij} - \sum_{k=1}^{j-1} l_{ik}u_{kj})$$

5. Once $L$ and $U$ have been determined, we can solve the system of equations $Ax = b$ through forward and backward substitution.

## Detailed Example

Let's consider the system of linear equations:

$$
\begin{align*}
2x + 3y - 4z &= 1 \\
3x - 3y + 2z &= -2 \\
-2x + 6y - z &= 3
\end{align*}
$$

This system can be represented as a matrix equation $Ax = b$, where $A$ is the matrix of coefficients, $x$ is the vector of variables, and $b$ is the right-hand side. We can use LU Decomposition to solve for $x$.

1. Represent the system in matrix form: 

$$A = \begin{bmatrix} 2 & 3 & -4 \\ 
3 & -3 & 2 \\ 
-2 & 6 & -1\\
\end{bmatrix}$$ 

and 

$$b = \begin{bmatrix} 1 \\ -2 \\ 3 \\
\end{bmatrix}$$

2. Compute the $L$ and $U$ matrices using the LU Decomposition algorithm:

Here we will decompose the matrix A into two matrices - A lower triangular matrix (L) and an upper triangular matrix (U).

Start with the first row:

- For the first element in the first row, we set $u_{11}$ to $a_{11}$ (the first element of A), so $u_{11}=a_{11}=2$. This will be the first element of our upper matrix U.

- Now, for the remaining elements in the first row ($j>1$), we set them equal to the corresponding elements in A, so $u_{1j}=a_{1j}=3,-4$. These are the second and third elements of the first row of U.

- For the first column of the lower triangular matrix L, except for the first element which is always set to 1, we set the remaining elements as $l_{i1}=\frac{a_{i1}}{u_{11}}$. This calculates to $l_{21}=\frac{3}{2}=1.5$ and $l_{31}=\frac{-2}{2}=-1$.

Then proceed to the second row:

- The first step in calculating the second row of U and the second column of L is to calculate the diagonal element of U, $u_{22}$. This is done by subtracting the product of $l_{21}$ and $u_{12}$ from $a_{22}$, i.e., $u_{22}=a_{22}-l_{21}u_{12}=-3-1.5*3=-7.5$.

- For the remaining element in the second row of U ($j>2$), calculate it as $u_{2j}=a_{2j}-l_{21}u_{1j}=2-1.5*(-4)=8$.

- Then, for the remaining element in the second column of L ($i>2$), calculate it as $l_{i2}=\frac{a_{i2}-l_{i1}u_{12}}{u_{22}}$, which results in $l_{32}=\frac{6-(-1)*3}{-7.5}=-2$.

Finally, for the third row:

- The diagonal of U is calculated as $u_{33}=a_{33}-l_{31}u_{13}-l_{32}u

This gives us:

$$
L = \begin{bmatrix} 1 & 0 & 0 \\ 
1.5 & 1 & 0 \\ 
-1 & -2 & 1 \\
\end{bmatrix},
U = \begin{bmatrix} 2 & 3 & -4 \\ 
0 & -7.5 & 8 \\ 
0 & 0 & 1 \\
\end{bmatrix}
$$

3. Use forward substitution to solve $Ly = b$ for $y$. Substituting $L$ and $b$ into the equation, we get $y = [1, -5, 1]$.

4. Finally, use backward substitution to solve $Ux = y$ for $x$. Substituting $U$ and $y$ into the equation, we get $x = [1, -1, 1]$.

Thus, the solution to the system of equations is $x = 1$, $y = -1$, and $z = 1$.

## Advantages

- LU Decomposition is efficient and numerically stable, especially for solving systems of linear equations.
- Can be used for finding the determinant and inverse of a matrix more easily.

## Limitations

- Only applicable for square matrices.
- Not all matrices can be LU decomposed. A is LU decomposable if and only if all its leading principal minors are non-zero.

