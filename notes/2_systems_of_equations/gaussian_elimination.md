## Gaussian elimination

To solve a linear system of equations, the Gaussian elimination approach is just a systematic application of the concept of equation substitution.

The first step is to put a matrix with coeeficients (A) and vector with values into one so called "augmented matrix".

$$
\begin{eqnarray*}
  -x + 5y &=& 12 \\
   x - 7y &=& 35
\end{eqnarray*} 
$$

$$
[A|\boldsymbol{b}] = 
\left[
  \begin{array}{rr|r}
    -1 & 5 & 12 \\
    1 & -7 & 35  \\
  \end{array}
\right]
$$

Now our goal is to convert this matrix to it's upper triangular form. We can achieve that by performing any of the following operations:

* Swap two rows.

* Multiply a row by a scalar that is not zero.

* Subtraction of a (non-zero) multiple of one row by a multiple of another.


## Gaussian Elimination Method

Gaussian elimination is a method for solving matrix equations of the form Ax = b. This method transforms the system's augmented matrix into reduced row-echelon form using a sequence of elementary row operations.

## Key Concepts

- The goal is to transform the augmented matrix to its row echelon form and then solve the system by back substitution.
- The row operations include swapping two rows, multiplying a row by a nonzero scalar, and adding a multiple of one row to another row.

## Mathematical Formulation

Given a system of linear equations, we can write it in matrix form Ax = b, where A is the matrix of coefficients, x is the vector of variables, and b is the constant vector.

The Gaussian elimination aims to convert the matrix A into an upper triangular matrix U by row operations. The transformed system Ux = c can be solved easily by back substitution.

## Algorithm Steps

1. Form the augmented matrix [A|b] of the system Ax = b.
2. Perform row operations to transform the augmented matrix into its row echelon form or reduced row-echelon form.
3. If the system is consistent, solve it by back substitution.

## Example

Consider the system of equations 2x + y - z = 8, -3x - y + 2z = -11, -2x + y + 2z = -3.

1. Write the system in matrix form and form the augmented matrix [A|b].
2. Use Gaussian elimination to transform the augmented matrix into its row-echelon form.
3. Solve the system by back substitution.

## Advantages

- It can handle any number of variables.
- It's useful in finding the rank and inverse of a matrix.

## Limitations

- Round-off errors can significantly affect the results, especially when dealing with large systems.
- The method requires the division by the pivot element. If this is zero, then the method cannot proceed without modification.
