## Gaussian Elimination

Gaussian elimination is an algorithm employed to solve systems of linear equations. It systematically operationalizes the principle of equation substitution.

## Key Concepts

- The main objective is to transform the augmented matrix — a combination of the coefficient matrix and the constant vector — into its row echelon form. Following this, the system can be resolved using a method known as back substitution.
- The process involves three types of row operations: swapping two rows, multiplying a row by a non-zero scalar, and adding a multiple of one row to another row.

## Mathematical Formulation

Given a system of linear equations, it can be depicted in matrix form as $Ax = b$, where 'A' represents the matrix of coefficients, 'x' is the vector of variables, and 'b' is the constant vector.

The objective of Gaussian elimination is to transform the matrix 'A' into an upper triangular matrix 'U' using a series of row operations. If 'A' is an $n \times n$ matrix, then an upper triangular matrix 'U' is a specific type of matrix where all entries below the main diagonal are zero.

Upon converting 'A' into 'U', the transformed system $Ux = c$ can be solved straightforwardly by back substitution.

## Algorithm Steps

1. Start with the augmented matrix $[A|b]$ of the system $Ax = b$, where A is an n by n coefficient matrix, and b is an n by 1 column vector.

2. For each row from i = 1 to n (the number of rows):

  - Find the maximum value in the current column and the corresponding row, pivotRow. This is called partial pivoting.

  - Swap the pivotRow with the current row i.

  - Normalize the row i by dividing every term by $A[i, i]$ (the pivot element).

  - For every row below i, subtract a multiple of row i such that the value in the current column (column i) becomes zero.

3. At this point, the matrix A should be in row echelon form, which means it should be upper triangular (all entries below the main diagonal are zero).

4. Perform back substitution to solve for x:

  - Initialize x as an empty list (or zero vector).

  - For each row i from n down to 1 (backwards):

  i. Set $x[i] = b[i]$.

  ii. For each column j from i+1 to n, subtract $A[i, j]*x[j]$ from $x[i]$.

  iii. Divide $x[i]$ by $A[i, i]$.

  - Return x as the solution to the system.


## Example

Consider the system of equations: $2x + y - z = 8$, $-3x - y + 2z = -11$, and $-2x + y + 2z = -3$.

1. Represent the system in matrix form and construct the augmented matrix $[A|b]$:

$$
\begin{bmatrix}
2 & 1 & -1 & 8 \\
-3 & -1 & 2 & -11 \\
-2 & 1 & 2 & -3 \\
\end{bmatrix}
$$

2. Apply Gaussian elimination to convert the augmented matrix into its row-echelon form. For instance, you can add the first row to the second to remove the x coefficient in the second row and add twice the first row to the third to remove the x coefficient in the third row:

$$
\begin{bmatrix}
2 & 1 & -1 & 8 \\
0 & 2 & 1 & -3 \\
0 & 3 & 1 & 13 \\
\end{bmatrix}
$$

Then, subtract 1.5 times the second row from the third to eliminate the y coefficient in the third row:

$$
\begin{bmatrix}
2 & 1 & -1 & 8 \\
0 & 2 & 1 & -3 \\
0 & 0 & -0.5 & 6.5 \\
\end{bmatrix}
$$

3. Resolve the system using back substitution. Start with the last equation, $-0.5z = 6.5$, solve for z to get $z = -13$, substitute z into the second equation to find y, then substitute y and z into the first equation to find x. The solution to the system is $x = 1$, $y = -1$, and $z = -13$.

## Advantages

- Gaussian elimination can handle systems with any number of variables.
- The method is beneficial for determining the rank and inverse of a matrix.

## Limitations

- Round-off errors can significantly impact the results, especially for larger systems.
- The method necessitates the division by the pivot element. If the pivot is zero, the method cannot proceed without modifications.
